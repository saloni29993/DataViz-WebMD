import json  
from collections import Counter  
    
    
jquestiondata = json.loads(open ('dataset/webmd-question.json').read())
janswerdata = json.loads(open('dataset/webmd-answer.json').read())


topicdata = list()

for i in range(len(jquestiondata)):
    for j in range(len(jquestiondata[i]['questionTopicId'].split(","))):
        if(len(str(jquestiondata[i]['questionTopicId'].split(",")[j])) != 0 and len(jquestiondata[i]['questionPostDate'].split("-")[0]) != 0):
            string = str(jquestiondata[i]['questionTopicId'].split(",")[j]) + "," + str(jquestiondata[i]['questionPostDate'].split("-")[0]) + "-" + str(jquestiondata[i]['questionPostDate'].split("-")[1])
            topicdata.append(string.strip(" "))


answerids = list()
for i in range(len(janswerdata)):
    answerids.append(str(janswerdata[i]['questionId']))
   
for k in range(len(answerids)):
    for i in range(len(jquestiondata)):
        if answerids[k] == jquestiondata[i]['questionId']:
            for j in range(len(jquestiondata[i]['questionTopicId'].split(","))):
                if(len(str(jquestiondata[i]['questionTopicId'].split(",")[j])) != 0 and len(jquestiondata[i]['questionPostDate'].split("-")[0]) != 0):
                    string = str(jquestiondata[i]['questionTopicId'].split(",")[j]) + "," + str(jquestiondata[i]['questionPostDate'].split("-")[0]) + "-" + str(jquestiondata[i]['questionPostDate'].split("-")[1])
                    topicdata.append(string.strip(" "))
        

topiccounter = Counter(topicdata)

print topiccounter