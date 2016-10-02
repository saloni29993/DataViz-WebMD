import json
import pickle
from pprint import pprint

data_answers = []
data_questions = []

with open('webmd-answer.json') as data_file:    
    data_answers = json.load(data_file)

with open('webmd-question.json') as data_file:
	data_questions = json.load(data_file)


#iterating through questions
for q in data_questions:
	#getting answers based on question id
	
	answer_blocks = filter(lambda x: x['questionId'] == q['questionId'], data_answers)
	pprint(answer_blocks)
	# count = len(answer_blocks);
	# if count != 1:
	# 	print "\n**** New Question *****"
	# 	print count 

