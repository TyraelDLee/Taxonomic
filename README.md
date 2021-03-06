Table of Contents
=================
  * [Introduction](#introduction)
  * [Project Value](#project-value)
  * [Client Expectation](#client-expectation)
  * [Road Map and System Diagram](#road-map-and-system-diagram)
  * [User Interface Prototype](#user-interface-prototype)
  * [User Story Map](#user-story-map)
  * [Milestones](#milestones)
  * [Schedule](#schedule)
  * [Progress](#progress)
  * [Risk Management](#risk-management)
  * [Team Member Roles](#team-member-roles)
  * [Communiaction Tools](#communication-tools)
  * [Development Environment](#development-environment)
  * [Development Tools](#development-tools)
  * [Decision Make Procedures](#decision-make-procedures)
  * [Testing](#testing)
  * [Meeting Agenda](#meeting-agenda)
  * [Audit Presentation](#audit-presentation)
  * [Other Resources](#other-resources)
## Introduction
Our project aims to automate taxonomic data capture from scientific reports, something which is currently performed manually. This information can then be uploaded to searchable databases where it can be accessed by the public. Automating this process will save our client time, effort and money which can be better spent elsewhere.
# ![Diagram](Resources/concept_diagram.jpg)
## Project Value
Having a comprehensive database of taxa data is useful to those studying biology as they can easily search the database to find relevant materials describing the taxa they are studying. These biological studies can help with sustainable management of biodiversity, conservation/protection of species, biosecurity, management of invasive species and much more. Our project will build an web-based automatic data collection application. Therefore, it can improve the data collection efficiency for Australian Biological Resources Study(ABRS), optimise extraction accuracy, reduce their labor consumption and save a lot of money.  


## Client Expectation
The client expects us to achieve functionality in terms of analysing documents in pdf or xml form and returning taxonomic information in a straightforward format, which the client is then able to check, edit. The program should be intuitive, accurate and time-saving.

## Road Map and System Diagram
# ![Diagram](Resources/roadmap.jpg)
# ![Diagram](Resources/BackEndFlow.png)
## User Interface Prototype
# ![Diagram](Resources/UIPrototype.jpg)
## User Story Map
# ![Diagram](Resources/usm.png)
## Milestones
- Functional webclient interface
- Enable uploading pdfs and viewing them as plain text in sub-window
- Enable customising extractable tags
- Implement automated IBRA7 region calculation
- Successfully use GoldenGate to tag pdfs
- Analyse and maximise the success rate of GoldenGate’s tagging
- Analyse and maximise the success rate of tag extraction
- Propose XML schema which will allow trivial data extraction

## Schedule
Week 6:
- Finalise higher level documentation (schedule, roles, milestones, audit ppt)
- Prepare for audit

Teaching break week 1:
- Thoroughly investigate GoldenGate
- Inquire about getting a web server set up with the ANU
- Create lower level documentation, ie. pseudocode, overall program structure, algorithms and testing plan
- Begin to design UI.

Teaching break week 2: 
- Complete development on basic interface, xml tag extraction and IBRA classification
- Complete basic UI
- Begin working on integrating GoldenGate with the server
- Prepare for audit

Week 7-8:
- Continue Work on implementing GoldenGate interpreting of PDF files server-side (backend)
- Create tools which allow the user to test the validity of output and fix it if necessary (frontend)
- Try to implement audit feedback

Week 9:
- Create project poster
- Meet with client and get feedback regarding program interface
- Work to improve efficiency and accuracy of data classification and extraction

Week 10:
- Overall system testing
- Finalise documentation
- Prepare for audit

Week 11:
- Implement audit feedback
- Prepare handover resources
## Progress
# ![Diagram](Resources/Schedule7.png)

Audit 1:
- Researched relevant biology/taxonomy information
- Indentified risks.
- Created a github project.
- Communicated with clients, find the problem, underlying needs.

Audit 2:
- Created the general structure of the project and the structure of each part (frontend, backend, UI, testing).
- Made statement of work (SOW).
- Allocated tasks and roles according to the SOW.
- Created UI prototype.
- Started research GoldenGate.
- Implemented basic functions to identify new species name and genus name in the abstract of XML formatted article.

Audit3:
- Communicated with clients about the output schema, updating clients’ needs.
-	Designed poster.
-	Finished the research about GoldenGate, started using NLP to process PDF articles.
-	Found other taxonomic information related with new species/genus, agents and reference in XML articles, matching. 
-	Formatted the extracted the extracted data as clients’ needs.
-	Used flask (a micro web framework written in Python) to connect with backend.
-	Wrote unit test.


# Risk Management
As the project is being implemented as part of a secure system, it is important that it does not present any new vulnerabilities to that system. This can be achieved by being considerate of the environment in which our project will be deployed and using appropriate programming techniques.
#### [Risk Register](https://drive.google.com/drive/folders/1VyUxQys5N7-MRKLpOc4DQ5fEEyYf8H6q?usp=sharing)
## Team Member Roles

| Team Member            | Uni ID         | Role                                                                    |
| -----------------------| ---------------| ------------------------------------------------------------------------|
| Jing Li                | u6531952       | Project Manager, Developer(XML extraction)                              |
| Biwei Cao              | u5926643       | Developer(XML extraction), Documentation                                |
| Jiaqi Zhang            | u6089193       | Developer(Testing)                                                      |
| Joshua Trevor          | u6405233       | Developer(PDF extraction), Spokesperson                                 |
| Yanlong LI             | u5890571       | Developer(full stack)                                                   |
| Yuan Yao               | u5945391       | Developer(data interaction), Documentation                              |


## Communication Tools
1. Email
2. Facebook Messenger


## Development Environment
-  Language: 
   - Java installation is necessary for GoldenGate
   - Other languages not determined yet, most likely a combination of python, javascript and php will be used
-  Testing: 
   -  Unit test during development by black/white box
   -  A/B test for the final stage 

## Development Tools
1. PyCharm(Python IDE)
2. Flask(A micro web framework)
3. DreamWeaver(HTML, CSS, JavaScript)

## Decision Make Procedures
# ![Diagram](Resources/decision.jpg)
#### [Decision Making Log](https://drive.google.com/open?id=19k1Fsmo4KuVd94mFDShupvla8UwJ114F)

## Testing
1. #### [Testing Design](https://docs.google.com/document/d/1Ds8spftVot8HpBYaTwZCm5_Jucjr2VzA0EnykC7GGcU/edit)
2. #### [Testing Plan](https://docs.google.com/document/d/1BsLx-H9nUd1ptGQ386oEkVbimc8xFrDpF3hfXgGit60/edit)
3. #### [Testing Methods](https://docs.google.com/document/d/1QbspjZKj_AQi0iJRnJDsckxD-U5ubWqwHPQPurHizXM/edit)
4. Testing Process
# ![Diagram](Resources/Testing_process(draft).png)
5. #### [Testing Results](https://docs.google.com/document/d/1p2bCQ_or1BENsoTOsLfLFjsNcGDdl9NSF6bJGyYsgVE/edit)

## Meeting Agenda
#### [Client Meeting](https://drive.google.com/drive/folders/1mm_xKNJ9t8DZAf-LZkJD0TDQlAKYAVky?usp=sharing)
#### [Group Meeting](https://drive.google.com/drive/folders/1MDCKulVX2guaDb-cfK7kPHIie3Kgz8MA?usp=sharing)

## Audit Presentation
#### [Audit1](https://docs.google.com/presentation/d/14QLdtRtMSZWAxxeWRe2eTX6NPbj8KzNHTZFg8nyr5oM/edit#slide=id.p1)
#### [Audit2](https://docs.google.com/presentation/d/1vWNcryChR0Rqus4ZB2tTV4MMgNu2CFb_9zi9Tp27Gk0/edit#slide=id.p1)
#### [Audit3](https://docs.google.com/presentation/d/1rjIJdBJ7W8cQjsVCMR1VXCtwMlKP513hyzwnLf7jMa8/edit#slide=id.p1)


## Other Resources
#### [Google Drive](https://drive.google.com/open?id=1827uZfi0IwiuHkuLUU6tcL8gX5F0Jx0d)

