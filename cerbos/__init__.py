# Copyright 2021 Zenauth Ltd.

import dataclasses
from dataclasses import dataclass
from enum import Enum
from typing import Any, AbstractSet, Mapping
import requests
import json


class Effect(str, Enum):
    DENY = "EFFECT_DENY"
    ALLOW = "EFFECT_ALLOW"


@dataclass
class Principal:
    id: str
    roles: AbstractSet[str]
    attr: Mapping[str, Any]
    policy_version: str = "default"

    def to_dict(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "policyVersion": self.policy_version,
            "roles": self.roles,
            "attr": self.attr,
        }


@dataclass
class ResourceInstance:
    attr: Mapping[str, Any]


@dataclass
class ResourceSet:
    kind: str
    instances: Mapping[str, ResourceInstance]
    policy_version: str = "default"

    def to_dict(self) -> dict[str, Any]:
        return {
            "kind": self.kind,
            "policyVersion": self.policy_version,
            "instances": self.instances,
        }


@dataclass
class CheckResourceSetRequest:
    request_id: str
    actions: AbstractSet[str]
    principal: Principal
    resource: ResourceSet

    def to_dict(self) -> dict[str, Any]:
        return {
            "requestId": self.request_id,
            "actions": self.actions,
            "principal": self.principal.to_dict(),
            "resource": self.resource.to_dict(),
        }


@dataclass
class ResourceInstanceResult:
    actions: Mapping[str, Effect]


@dataclass
class CheckResourceSetResponse:
    request_id: str
    resource_instances: Mapping[str, ResourceInstanceResult]

    def is_allowed(self, resource_id: str, action: str) -> bool:
        if resource_id in self.resource_instances:
            res = self.resource_instances[resource_id]
            if action in res["actions"]:
                return res["actions"][action] == Effect.ALLOW

        return False


class CheckResourceSetRequestEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, CheckResourceSetRequest):
            return obj.to_dict()

        if dataclasses.is_dataclass(obj):
            return dataclasses.asdict(obj)

        return json.JSONEncoder.default(self, obj)


class ClientException(Exception):
    msg: str

    def __init__(self, msg: str):
        self.msg = msg


class Client:
    host: str

    def __init__(self, host: str):
        self.host = host

    def check_resource_set(
        self, request: CheckResourceSetRequest
    ) -> CheckResourceSetResponse:
        response = requests.post(
            f"{self.host}/api/check",
            data=json.dumps(request, cls=CheckResourceSetRequestEncoder),
        )
        if response.status_code != 200:
            raise ClientException(f"Received status code {response.status_code}")

        obj = response.json()
        return CheckResourceSetResponse(
            request_id=obj["requestId"], resource_instances=obj["resourceInstances"]
        )
