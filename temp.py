import json

with open("tp.json") as data_file:
    data = json.load(data_file)


for key,value in data.iteritems():
	print '{"name":"' +key +'", "size":',value,'}'