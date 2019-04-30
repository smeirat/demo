#!/usr/bin/env python

import urllib
import json
import os

from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def abot_slotfill():
  #  print(request)

    req = request.json
    print(req)
    if len(req) > 0 and 'action' in req['queryResult'].keys():
        print(req)
        action = req['queryResult']['action']
        print(action)
        if action != '' and action != 'cancel' and action != 'bye' and action != 'exit':
            res = 'working'
            if res == '':
                return Response(status=200)
            else:

                response = json.dumps({
                    'fulfillmentText': 'Your working time starts from 08:30 AM to 05:00 PM'
                })
                return response
        else:
            return Response(status=200)
    else:
        return Response(status=200)


#print(json.dumps(res))



if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print ("Starting app on port %d" %(port))

    app.run(debug=True, port=port, host='127.0.0.1')


