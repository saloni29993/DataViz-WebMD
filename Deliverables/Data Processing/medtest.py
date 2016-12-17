import difflib as dl
import json
from pprint import pprint


######################### loading DAta from files #############################
#loading questions 
with open('dataset/webmd-question.json') as data_file:
 	data_question = json.load(data_file)

#loading topic
with open('dataset/webmd-topics.json') as data_file:
 	data_topics = json.load(data_file)

tests = [line.split('(')[0].strip('\n\t\r').strip(' ') for line in open("ScrapedData/medicaltests.txt")]

questions = filter(lambda x: " test " in x['questionTitle'] or " test " in x['questionContent'] or " tests " in x['questionContent'] or " tests " in x['questionTitle'], data_question)


#pprint(questions)

medtest = {}

for t in data_topics:
	topic = t['topicId']
	med_diseases = []
	question = filter(lambda x: topic in x['questionTopicId'], questions)
	for q in question:
		disease_question = dl.get_close_matches(q['questionTitle'],tests,10,0.5)
		disease_content = dl.get_close_matches(q['questionContent'],tests,10,0.5)
		med_diseases = med_diseases + disease_question + disease_content

	topic_tests = list(set(med_diseases))
	print topic
	medtest[topic] = topic_tests

with open('med_test.json', 'w') as outfile:
	json.dump(medtest, outfile)


        

