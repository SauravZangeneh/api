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
    	{datetime.datetime(2018, 1, 23, 20, 14, 8, 603536): 'oasidn',datetime.datetime(2013, 1, 23, 20, 14, 8, 603536): 'ajoj'},
    'Test 2': 
    	{datetime.datetime(2018, 1, 23, 20, 14, 8, 603536):'asodn'},
    'Test 3': 
    	{datetime.datetime(2019, 1, 23, 20, 14, 8, 603536): 'snoan'}
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
		docs[title][datetime.datetime.now()]=content['content']
		print(docs)
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
		timestamp=datetime.fromtimestamp(timestamp)
		print(timestamp)
		if timestamp in doc:
			return doc[timestamp]
	else:
		return ("Error doc doesn't exist")

app.run()

