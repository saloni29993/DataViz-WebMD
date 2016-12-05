import json

jquestiondata = json.loads(open ('dataset/webmd-question.json').read())

topicdata = list()

for i in range(len(jquestiondata)):
    for j in range(len(jquestiondata[i]['questionTopicId'].split(","))):
        if(len(str(jquestiondata[i]['questionTopicId'].split(",")[j])) != 0 and len(jquestiondata[i]['questionPostDate'].split("-")[0]) != 0):
            string = str(jquestiondata[i]['questionTopicId'].split(",")[j])
            topicdata.append(string.strip(" "))
            
questionmap = dict()

for topic in topicdata:
    count = 0
    questionlist = list()
    for i in range(len(jquestiondata)):
        questiontitlemap = dict()
        if topic in jquestiondata[i]['questionTopicId']:
            if count == 3:
                break
            questiontitlemap['q'] = jquestiondata[i]['questionTitle']
            questiontitlemap['qurl'] = jquestiondata[i]['questionURL']
            count = count + 1
            questionlist.append(questiontitlemap)
        questionmap[topic] = questionlist

jsonmap = json.dumps(questionmap)

print jsonmap
    
