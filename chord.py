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
diseases = [line.split('(')[0].strip('\n\t\r').strip(' ') for line in open("ScrapedData/diseases.txt")]

#get symptom list
symptoms = [line.split('(')[0].strip('\n\t\r').strip(' ') for line in open("ScrapedData/symptoms.txt")]

#get answers from question id
answer = map(lambda y: str(y['answerContent']),list(filter(lambda x: x['questionId'] in questionids, data_answer)))

chord_dict = {}



#extract disease from questions
for q in question:
	#extract disease
	disease_question = dl.get_close_matches(q['questionTitle'],diseases,10,0.7)
	disease_content = dl.get_close_matches(q['questionContent'],diseases,10,0.7)
	med_diseases = disease_question + disease_content

	#extract symptom
	symptom_question = dl.get_close_matches(q['questionTitle'],symptoms,10,0.7)
	symptom_content = dl.get_close_matches(q['questionContent'],symptoms,10,0.7)
	med_symptoms = symptom_question + symptom_content

	for d in med_diseases:
		if d not in chord_dict.keys():
			chord_dict[d] = set()
		for s in med_symptoms:
			chord_dict[d].add(s)

			if s not in chord_dict.keys():
				chord_dict[s] = set()

			chord_dict[s].add(d)

#extract disease from answers
for a in answer:
	#extract disease
	med_diseases = dl.get_close_matches(a,diseases,10,0.7)

	#extract symptom
	med_symptoms = dl.get_close_matches(a,symptoms,10,0.7)

	for d in med_diseases:
		if d not in chord_dict.keys():
			chord_dict[d] = set()
		for s in med_symptoms:
			chord_dict[d].add(s)

			if s not in chord_dict.keys():
				chord_dict[s] = set()

			chord_dict[s].add(d)
	

# pprint(chord_dict)

final = '['

for c in chord_dict.keys():
	if len(chord_dict[c]):
		final+='{"name":"' +c +'","size":1,"imports":' +str(list(chord_dict[c])) +'},'

final += ']'

pprint(final)