import json
import pickle
from pprint import pprint
import difflib as dl

data_answers = []
data_questions = []
drugs = []
symptoms = []
medicaltests = []

# with open('dataset/webmd-answer.json') as data_file:    
#     data_answers = json.load(data_file)

with open('dataset/webmd-question.json') as data_file:
 	data_questions = json.load(data_file)

#loading drugs
drugs = set([line.strip('\n\t\r').replace(' oral','') for line in open('ScrapedData/drugs.txt')])

#loading symptoms
symptoms = set([line.strip('\n\t\r') for line in open('ScrapedData/symptoms.txt')])

#loading medicaltests
medicaltests = set([line.strip('\n\t\r') for line in open('ScrapedData/medicaltests.txt')])


# #iterating through questions
# for q in data_questions:
# 	#getting answers based on question id
# 	answer_blocks = filter(lambda x: x['questionId'] == q['questionId'], data_answers)
# 	pprint(answer_blocks)

print dl.get_close_matches("ammoxcilin",drugs,10,0.8)