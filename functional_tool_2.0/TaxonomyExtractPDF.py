import PyPDF2
import os
import requests
import pandas as pd
from nltk.corpus import words


common_ending_words = ["in", "sp", "type", "and", "are", "figs"]
common_preceding_words = ["as", "australia", "holo", "iso", "perth", "canb", "species", "and"]
pre_buffer = 15
post_buffer = 20



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
    combined_request_str = ""
    post_buffer = 20
    for word in word_list:
        if word == "sp.":
            confidence = 0
            name = word_list[working_index-pre_buffer: working_index+post_buffer]
            # Abstract this to include variations of sp. nov. later and ensure they are close together as well
            if name.__contains__("sp.") and name.__contains__("nov."):
                name = name[:pre_buffer]
                confidence += 1

            request_str = ""
            debugstr=""
            index = 0
            for name_component in name:
                if index > pre_buffer and remove_punctuation(name_component.lower()) in common_ending_words and not remove_punctuation(name_component.lower()) == "":
                    confidence += 1
                    break

                elif index < pre_buffer and remove_punctuation(name_component.lower()) in common_preceding_words and not remove_punctuation(name_component.lower()) == "":
                    request_str = ""
                    debugstr = ""
                    confidence = 1
                    index += 1
                    continue

                name_component = name_component.replace("&", "%26")
                if len(remove_punctuation(name_component)) > 0:
                    request_str = request_str + ("+" + name_component)
                    debugstr += (name_component + " ")
                index += 1
            # print("Confidence: {} for name: {}".format(confidence, debugstr))

            combined_request_str = combined_request_str + request_str + "|"
        working_index = working_index + 1

    # print(combined_request_str)
    r = requests.get('http://parser.globalnames.org/api?q=' + (combined_request_str[1:-1]))
    # print(r.json())
    return r.json()


#Abstract out the identical part of these two functions soonTM
def get_example_path(pdf_name):
    # abs_file_path = os.path.abspath(__file__)
    # parent_dir = os.path.dirname(abs_file_path)
    # parent_dir = os.path.dirname(parent_dir)
    # result = os.path.join(parent_dir, "functional_tool_2.0/Examples/PDFs/{}".format(pdf_name))
    # # result = os.path.join(parent_dir, "{}".format(pdf_name))
    # print(result.replace("\\", "/"))
    # print(os.path.exists('uploaded_folder/853.pdf'))
    # result = 'uploaded_folder/853.pdf'
    return pdf_name

def get_output_path(name):
    abs_file_path = os.path.abspath(__file__)
    parent_dir = os.path.dirname(abs_file_path)
    parent_dir = os.path.dirname(parent_dir)
    name = name.split('/')[-1]
    result = os.path.join(parent_dir, "functional_tool_2.0/xls_folder/{}.xls".format(name))
    return result.replace("\\", "/")


def get_config_path():
    abs_file_path = os.path.abspath(__file__)
    parent_dir = os.path.dirname(abs_file_path)
    parent_dir = os.path.dirname(parent_dir)
    return os.path.join(parent_dir, "functional_tool_2.0/Configuration")


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

    if(reference_index == 0):
        print("No reference section was detected")
        return reference_index
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


#Later replace try and except statements with a method which dynamically works out which tags exist in the json
#check to use later: if any(tag['key'] == 'ecs_scaling' for tag in data['Tags']):
#(https://stackoverflow.com/questions/45964144/pythonic-way-to-determine-if-json-object-contains-a-certain-value)
def parse_json_list(json_string):
    df = pd.DataFrame(columns=['Verbatim', 'Genus', 'Species', 'Authorship'])
    for item in json_string:
        # print(item)
        try:
            if item['parsed'] == True:
                df.loc[0] = [item['verbatim'], item['details'][0]['genus']['value'], item['details'][0]['specificEpithet']['value'],
                           item['details'][0]['specificEpithet']['authorship']['value']]
        except:
            print("The parser was given a name which did not contain a genus/species/author. Currently the program only deals with names containing these components")
    return df



#Todo: Attempt to fix situations where spaces/tabs/newlines are not registered by PyPDF which often interferes with parsing.
def correct_unintentional_joining():
    return None


#Todo: Create temporary function which stores output in an XML file to be interpreted by frontend
def get_excel_output(path):
    df = parse_json_list(find_new_names(read_all_pages(
        create_pdf_reader(get_example_path(path)))))
    df.to_excel(get_output_path(path[:-4]))


#get_configurations()
#(process_string(read_all_pages(
#    create_pdf_reader(get_example_path("853.pdf")))))


