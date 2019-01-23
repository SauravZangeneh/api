import flask
from flask import request, jsonify
import urllib 
app = flask.Flask(__name__)

#test document (since documents are just text) 
#max length (50 chars) - useful for the post method
#content is stored as values for timestamps (keys)
docs ={'Test 1': 
    	{'1pm': 'oasidn','3pm': 'ajoj'},
    'Test 2': 
    	{'4pm': 'abd','5pm': 'anlo'},
    'Test 3': 
    	{'12am': 'snoan','6pm': 'ando'}
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
@app.route('/documents/<title>', methods=['GET'])
def get_timestamp(title):
	title=title.decode('utf8').replace("+"," ") #basic url parsing
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
		if timestamp in doc:
			return doc[timestamp]
	else:
		return ("Error doc doesn't exist")
app.run()

