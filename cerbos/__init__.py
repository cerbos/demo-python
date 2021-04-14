import uuid
import requests as r
import json

BASE = 'http://localhost:9998/api'
CHECK = BASE + '/check'
def init(url):
    BASE = url

def check(principal, action, resource):
    try:
        request = {}
        request['requestId'] = str(uuid.uuid4())
        request['principal'] = principal
        request['action'] = action
        request['resource'] = resource
        response = r.post(CHECK, data=json.dumps(request))
        j_response = json.loads(response.text)
        if j_response['statusMessage'] == "Allow":
            return True
        else:
            return False
    except Exception as e:
        return None