import PyPDF2
import os
import requests
from nltk.corpus import words


common_ending_words = ["in", "sp", "type", "and", "are", "figs"]
common_preceding_words = ["as", "australia", "holo", "iso", "perth", "canb", "species", "and"]
pre_buffer = 15
post_buffer = 15


def create_pdf_reader(path):
    pdf_file_obj = open(path, 'rb')
    return PyPDF2.PdfFileReader(pdf_file_obj)


def read_all_pages(pdf_reader):
    page_index = 0
    result = ""
    while page_index < pdf_reader.getNumPages():
        page = (pdf_reader.getPage(page_index).extractText())
        page = normalise_spacing(page)
        result = result + page
        page_index = page_index + 1
    return result


def read_page(page_num, pdf_reader):
    page = (pdf_reader.getPage(page_num).extractText())
    page = normalise_spacing(page)
    return page


def normalise_spacing(page):
    page = page.replace("\n", " ")
    page = page.replace("  ", " ")
    return page


def remove_punctuation(str):
    result_str = str.replace(",", "")
    result_str = result_str.replace(".", "")
    result_str = result_str.replace(" ", "")
    result_str = result_str.replace("&", "")
    result_str = result_str.replace(":", "")
    result_str = result_str.replace("(", "")
    result_str = result_str.replace(")", "")
    return result_str


def process_string(doc_string):
    find_new_names(doc_string)
    reference_index = find_references(doc_string)
    find_document_data(doc_string, reference_index)


#currently does not return anything, just prints out relevant information #
# If a document mentions a name with sp. n. twice first is usually in abstract while second is description
#Later be amended to return the location of the string within the document.
def find_new_names(doc_string):
    working_index = 0
    word_list = doc_string.split(" ")
    for word in word_list:
        if word == "sp.":
            name = word_list[working_index-pre_buffer: working_index+post_buffer]
            #print(name)
            request_str = ""
            debugstr=""
            index = 0
            for name_component in name:
                if index > pre_buffer and remove_punctuation(name_component.lower()) in common_ending_words:
                    break

                elif index < pre_buffer and remove_punctuation(name_component.lower()) in common_preceding_words:
                    request_str = ""
                    debugstr = ""
                    index += 1
                    continue

                if len(remove_punctuation(name_component)) > 0:
                    request_str = request_str + ("+" + name_component)
                    debugstr += (name_component + " ")
                index += 1
            print(debugstr)
            #print(request_str[1:])
            #r = requests.get('http://parser.globalnames.org/api?q=' + (request_str[1:])) #print(r.json())
        working_index = working_index + 1


def get_example_path(pdf_name):
    abs_file_path = os.path.abspath(__file__)
    parent_dir = os.path.dirname(abs_file_path)
    parent_dir = os.path.dirname(parent_dir)
    result = os.path.join(parent_dir, "Examples/PDFs/{}".format(pdf_name))
    return result.replace("\\", "/")


def get_config_path():
    abs_file_path = os.path.abspath(__file__)
    parent_dir = os.path.dirname(abs_file_path)
    parent_dir = os.path.dirname(parent_dir)
    return os.path.join(parent_dir, "Configuration")


def get_configurations():
    get_key_words(get_config_path())


def get_key_words(config_path):
    index = 0
    key_word_files = ["CommonPrecedingWords.txt", "CommonEndingWords.txt"]
    common_ending_words.clear()
    common_preceding_words.clear()
    while index < 2:
        file = open(os.path.join(config_path, key_word_files[index]))
        lines = file.read().split("\n")
        for line in lines:
            if line.startswith("#"):
                continue

            if key_word_files[index].__contains__("Preceding"):
                common_preceding_words.append(line)

            else:
                common_ending_words.append(line)
        index +=1



#currently uses naiive approach: finding the last usage of the word references, should work 99% of the time but can still be improved
def find_references(doc_string):
    references = ""
    word_list = doc_string.split(" ")
    index = 0
    reference_index = 0
    for word in word_list:
        if word.lower() == "references":
            references = word_list[index:]
            reference_index = index
        index += 1
    print("References begin at word number " + str(reference_index))
    return reference_index


#Finds high level information about the pdf like author, data published, zoobank id etc. Does not look in the references section.
#Todo: fix issue where two words on different lines are merged during conversion
def find_document_data(doc_string, reference_index):
    word_list = doc_string.split(" ")
    url_list = []
    for word in word_list[:reference_index]:
        if word.__contains__("http"):
            word = word[word.index("http"):]
            url_list.append(word)

    for url in url_list:
        if url.__contains__("zootaxa") or url.__contains__("zoobank"):
            print("Self referencing information: " + url)


#Todo: extract coordinate information
def find_coordinates():
    return None

#Todo: Given a string index, find the nearby name which that information is most likely to belong to.
def associate_info_with_name():
    return None

get_configurations()
process_string(read_all_pages(create_pdf_reader(get_example_path("kurina_2019_zootaxa4555_3 Diptera Mycetophilidae manota new sp (1).pdf"))))
