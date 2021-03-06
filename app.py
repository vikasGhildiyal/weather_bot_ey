#!/usr/bin/env python

import urllib
import json
import os
import requests

from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    res = processRequest(req)
    res = json.dumps(res, indent=4)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r
def processRequest(req):
	res = makeWebhookResult(req)
	return res
def makeWebhookResult(req):
	#result=req.get("result")
	#parameters=result.get("parameters")
	#city=parameters.get("geo-city")
	r=requests.get('http://api.openweathermap.org/data/2.5/weather?q=delhi&appid=fb03265fe100997cf20211361642b414')
	json_object=r.json()
	weather=json_object['weather'][0]['main']
	#speech="The Forecast is "+str(weather)
	speech="PO is approved"
	#for i in range(0,30):
	 #if date in weather[i]['dt']:
	  # condition=weather[i]['weather'][0]['description']
	 #break
	 #speech="The forecast  is "+weather
	#speech="The forecast for"+condition
	return{
        "fulfillmentText": speech,
        #"displayText": speech,
        #"data": {"slack": slack_message, "facebook": facebook_message},
        # "contextOut": [],
        "source": "apiai-weather-webhook-sample"
    }
if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(debug=False, port=port, host='0.0.0.0')
     #app.run(debug=True,port=port,host='127.0.0.1')	
