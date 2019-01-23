import flask
from flask import request, jsonify
import urllib 
import datetime
import time

app = flask.Flask(__name__)

#test document (since documents are just text) 
#max length (50 chars) - useful for the post method
#content is stored as values for timestamps (keys)


docs ={'Test 1': 
    	{datetime.datetime(2018, 1, 23, 20, 14, 8): 'oasidn',datetime.datetime(2013, 1, 23, 20, 14, 8): 'ajoj'},
    'Test 2': 
    	{datetime.datetime(2018, 1, 23, 20, 14, 8):'asodn'},
    'Test 3': 
    	{datetime.datetime(2019, 1, 23, 20, 14, 8): 'snoan'}
    }


# not important
@app.route('/', methods=['GET'])
def home():
	return "<h1>Wikipedia</h1>"

#task 1 - get all titles 
@app.route('/documents', methods=['GET'])
def get_titles():
	return jsonify(docs.keys())

#task 2 - get all timestamps for a title
@app.route('/documents/<title>', methods=['GET','POST'])
def get_timestamp(title):
	content = request.json
	title=title.decode('utf8').replace("+"," ") #basic url parsing
	if content:
		if title in docs:
			#adds new timestamp
			docs[title][datetime.datetime.now().replace(microsecond=0)]=content['content']
		else:
			#Creates new doc
			docs[title]={}
			docs[title][datetime.datetime.now().replace(microsecond=0)]=content['content']
		print(docs)
		return ("New content added")
	else:
		if title in docs:
			return jsonify(docs[title].keys())
		else:
			return ("Error doc doesn't exist")

@app.route('/documents/<title>/<timestamp>', methods=['GET'])
def get_content(title,timestamp):

	#without the proper timestamp thing
	title=title.decode('utf8').replace("+"," ") #basic url parsing
	if title in docs:
		doc=docs[title]
		# have to enter actual timestamp - eg. 1516738448
		timestamp=datetime.datetime.fromtimestamp(float(timestamp))
		deltas=[timestamp-time for time in doc.keys() if timestamp>time]

		#to return previous version doc
		return (doc[timestamp-min(deltas)])
	else:
		return ("Error doc doesn't exist")


@app.route('/documents/<title>/latest', methods=['GET','POST'])
def get_latest(title,):
	content = request.json
	title=title.decode('utf8').replace("+"," ") #basic url parsing
	if title in docs:
		doc=docs[title]
		return(doc[max(doc.keys())])
	else:
		return ("Error doc doesn't exist")
app.run()

