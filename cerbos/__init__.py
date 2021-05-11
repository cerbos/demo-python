import uuid
import requests as r
import json

BASE = "http://localhost:9998/api"
CHECK = BASE + "/check"


def init(url):
    BASE = url


def check(principal, action, resource):
    try:
        resource_id = resource["attr"]["id"]

        request = {}
        request["requestId"] = str(uuid.uuid4())
        request["principal"] = principal
        request["actions"] = [action]
        request["resource"] = {
            "kind": resource["kind"],
            "instances": {resource_id: {"attr": resource["attr"]}},
        }

        response = r.post(CHECK, data=json.dumps(request))
        j_response = json.loads(response.text)

        return (
            j_response["resourceInstances"][resource_id]["actions"][action]
            == "EFFECT_ALLOW"
        )
    except Exception as e:
        return None
