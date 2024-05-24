# SAS Project

_Members:_

| Name | Matriculation |
| ------ | ------ |
| Parth Navadiya | 22202538 |
| Nemish kyada | 22212034 |

**Project Title: **

GIT LINK : https://mygit.th-deg.de/kickers-as/my-project

WIKI LINK : https://mygit.th-deg.de/kickers-as/my-project/-/wikis/home

# Project Description
Our project offers a comprehensive language learning system, featuring diverse courses, elective classes, a tandem programme, and a Rasa chatbot for interactive support. 
Designed for real-world linguistic competence, it prepares learners for global communication and cultural immersion.

# Prerequisites
To run this project on your computer you need to have to have software such as:
1. Python 3.8
2. Rasa 3.1

# Installation
## Setup and Usage
In order to use this chatbot offline on your personal system, follow the below steps:
- Download or clone this repository using following command:
```
git clone https://mygit.th-deg.de/kickers-as/my-project
```
- Go to the cloned directory and install virtualenv package (if you don't have it already)
```
cd {file name}
pip install virtualenv
```
- Create a new virtual environment in current directory with specified version of Python and activate it
```
python -m venv env

.\env\Scripts\activate.bat
```
`Note: Python3.8 is the recommanded Python version for this project. Install and add it to PATH incase there are any errors.`
- Next step is to install Rasa and train the model
```
pip install Rasa
rasa train
```
- To connect port, open another terminal, activate virtual environment and run following command
```
rasa run actions
```
- Open previous terminal and enter following command to start interacting with chatbot
```
rasa shell
```

## Contributions

Nemish Kyada:
1. Worked on domain, nlu and stories.
2. Created dialogs and converted it into a flow
3. Created critical use case and documented it.
4. Implemented classes in actions for chatbot to reply accordingly.
5. Created a system and 2 user personas.
6. Worked on actions.py file.

Parth Navadiya:
1. Worked on domain, nlu and stories.
2. Created dialogs and converted it into a flow.
3. Created rules for chatbot.
4. Implemented classes in actions for chatbot to reply accordingly.
5. Created 1 user personas.
6. Worked on test stories.
