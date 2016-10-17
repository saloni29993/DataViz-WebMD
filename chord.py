import difflib as dl
import json
from pprint import pprint

topic = "pain-questions"


#loading questions 
with open('dataset/webmd-question.json') as data_file:
 	data_question = json.load(data_file)


#loading answers
with open('dataset/webmd-answer.json') as data_file:
 	data_answer = json.load(data_file)


#print data_question

#get list of questions based on topics
question = list(filter(lambda x: topic in x['questionTopicId'] or topic in x['questionContent'], data_question))

#get list of question ids
questionids = set(map(lambda x: x['questionId'] , question))

#get disease list
diseases = [line.split('(')[0].strip('\n\t\r') for line in open("ScrapedData/diseases.txt")]

#get answers from question id
answer = map(lambda y: str(y['answerContent']),list(filter(lambda x: x['questionId'] in questionids, data_answer)))

#extract disease from questions
for q in question:
	med = dl.get_close_matches(q['questionTitle'],diseases,10,0.8)
	if len(med) != 0:
		print "q:",q['questionTitle']
		print med,"\n"


#extract disease from answers
for a in answer:
	med = dl.get_close_matches(a,diseases,10,0.8)
	if len(med) != 0:
		print "a:",a
		print med,"\n"

