import json
from collections import Counter

with open('webmd-topics.json') as data_file:    
    topic_data = json.load(data_file)
    
with open("webmd-question.json") as data_file:
    question_data = json.load(data_file)

topicId = set()
question = []
finalQuestion = []




for i in range(0, len(topic_data)):
    topicId.add(topic_data[i]["topicId"])
  
for i in range(0, len(question_data)):
    if len(question_data[i]["questionTopicId"]) != 0:
        question.insert(len(question), question_data[i]["questionTopicId"]) 


for i in range(0, len(question)):
    for j in range(0, len(question[i].split(","))):
        if(len(question[i].split(",")[j]) != 0):
            finalQuestion.insert(len(finalQuestion), str(question[i].split(",")[j].strip().replace("-questions","")))
 
cnt = Counter(finalQuestion)

print cnt