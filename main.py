#! /usr/bin/env python
# Copyright 2021 Zenauth Ltd.
# SPDX-License-Identifier: Apache-2.0

import copy
import cerbos
import emoji
import uuid

CERBOS_URL="http://localhost:3592"

# Harry is an employee in the UK working in the marketing department's design team
harry = cerbos.Principal(
    id="harry",
    roles=["employee"],
    attr={"department": "marketing", "geography": "GB", "team": "design"},
)

# Maggie is Harry's direct manager
maggie = cerbos.Principal(
    id="maggie",
    roles=["employee", "manager"],
    attr={
        "department": "marketing",
        "geography": "GB",
        "managed_geographies": "GB",
        "team": "design",
    },
)

# Amanda is Maggie's counterpart in the US
amanda = cerbos.Principal(
    id="amanda",
    roles=["employee", "manager"],
    attr={
        "department": "marketing",
        "geography": "US",
        "managed_geographies": ["US"],
        "team": "design",
    },
)

# Pedro is an employee in a different team and geography
pedro = cerbos.Principal(
    id="pedro",
    roles=["employee"],
    attr={"department": "shipping", "geography": "FR", "team": "Pod 1"},
)

# A leave request created by Harry that is still in DRAFT status
harrys_draft_holiday_request = cerbos.ResourceInstance(
    attr={
        "department": "marketing",
        "geography": "GB",
        "id": "XX125",
        "owner": "harry",
        "status": "DRAFT",
        "team": "design",
    }
)

# A leave request created by Maggie that is still in PENDING_APPROVAL status
maggies_pending_holiday_request = cerbos.ResourceInstance(
    attr={
        "department": "marketing",
        "geography": "GB",
        "id": "XX226",
        "owner": "maggie",
        "status": "PENDING_APPROVAL",
        "team": "design",
    }
)

# Harry's leave request that is now in PENDING_APPROVAL state
harrys_pending_holiday_request = copy.deepcopy(harrys_draft_holiday_request)
harrys_pending_holiday_request.attr["status"] = "PENDING_APPROVAL"

# Harry's leave request that is now in APPROVED state
harrys_approved_holiday_request = copy.deepcopy(harrys_draft_holiday_request)
harrys_approved_holiday_request.attr["status"] = "APPROVED"


# Check whether the principal is allowed to perform a specific action on the given resource
def check(
    client: cerbos.Client,
    principal: cerbos.Principal,
    action: str,
    resource: cerbos.ResourceInstance,
):
    # Build the Cerbos request
    request = cerbos.CheckResourceSetRequest(
        request_id=str(uuid.uuid4()),
        actions=[action],
        principal=principal,
        resource=cerbos.ResourceSet(
            kind="leave_request", instances={resource.attr["id"]: resource}
        ),
    )

    try:
        # Make a Cerbos request
        response = client.check_resource_set(request)

        effect = "_cannot_"
        icon = emoji.emojize(":cross_mark:")

        # Check whether the Cerbos response indicates that this action is allowed
        if response.is_allowed(resource.attr["id"], action):
            effect = "_can_"
            icon = emoji.emojize(":thumbs_up:")

        print(
            f"{icon} {principal.id} {effect} {action} {resource.attr['owner']}'s "
            f"{resource.attr['status']} holiday request"
        )
    except cerbos.ClientException as e:
        print(f"Request failed: {e.msg}")


if __name__ == "__main__":
    # Initialise the Cerbos client
    client = cerbos.Client(host=CERBOS_URL)

    # Check access to Harry's draft holiday request
    for principal, action in [
        (harry, "create"),
        (harry, "view"),
        (pedro, "view"),
        (maggie, "view"),
        (amanda, "view"),
        (maggie, "approve"),
        (amanda, "approve"),
        (harry, "submit"),
    ]:
        check(client, principal, action, harrys_draft_holiday_request)

    # Check access to Harry's pending holiday request
    print("\nHarry submits his holiday request\n")

    for principal, action in [
        (harry, "view"),
        (harry, "approve"),
        (pedro, "view"),
        (amanda, "view"),
        (maggie, "view"),
        (amanda, "approve"),
        (maggie, "approve"),
    ]:
        check(client, principal, action, harrys_pending_holiday_request)

    # Check access to Harry's approved holiday request
    print("\nMaggie approves Harry's holiday request\n")

    for principal, action in [
        (harry, "view"),
        (pedro, "view"),
        (amanda, "view"),
        (maggie, "view"),
    ]:
        check(client, principal, action, harrys_approved_holiday_request)
