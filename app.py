#!/usr/bin/env python

import urllib
from urllib.request import urlopen, Request
from urllib.error import HTTPError
import json
import os

 
from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)

    print("Request:")
    print(json.dumps(req, indent=4))

    res = makeWebhookResult(req)

    res = json.dumps(res, indent=4)
    print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

def makeWebhookResult(req):
    action= req.get("result").get("action")
    
    result = req.get("result")
    parameters = result.get("parameters")
    c=result.get("fulfillment")
    d=c.get('messages')
    x=d[0]
    z=x.get('speech')
    statev = parameters.get("state")
    if(action=="light"):
        if(statev=="on"):
            y="http://zoimate.com/update1.php?field=%23A&id=8V8BC7CA2R9VSOY8QL13"
        elif(statev=="off"):
            y="http://zoimate.com/update1.php?field=%23a&id=8V8BC7CA2R9VSOY8QL13"
   
    result1=urlopen(y).read()
    speech =str(result1)
    if(speech=="b'0'"):
        speech1="I missed that whatever you say,Try again"
    elif(speech!="b'0'"):
        speech1="OK! I have done."


    return {
        "speech": z,
        "displayText": z,
        "source": "kk bhai"
            }


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    #print "Starting app on port %d" % port

    app.run(debug=True, port=port, host='0.0.0.0')
