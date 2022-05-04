# Copyright 2021-2022 Zenauth Ltd.
# SPDX-License-Identifier: Apache-2.0

import dataclasses
import os

import emoji
from cerbos.sdk.client import CerbosClient
from cerbos.sdk.container import CerbosContainer
from cerbos.sdk.model import *

# Define the principals and resources we are going to use in the demo.

# Harry is an employee in the UK working in the marketing department's design team
harry = Principal(
    id="harry",
    roles={"employee"},
    attr={"department": "marketing", "geography": "GB", "team": "design"},
)

# Maggie is Harry's direct manager
maggie = Principal(
    id="maggie",
    roles={"employee", "manager"},
    attr={
        "department": "marketing",
        "geography": "GB",
        "managed_geographies": "GB",
        "team": "design",
    },
)

# Amanda is Maggie's counterpart in the US
amanda = Principal(
    id="amanda",
    roles={"employee", "manager"},
    attr={
        "department": "marketing",
        "geography": "US",
        "managed_geographies": ["US"],
        "team": "design",
    },
)

# Pedro is an employee in a different team and geography
pedro = Principal(
    id="pedro",
    roles={"employee"},
    attr={"department": "shipping", "geography": "FR", "team": "Pod 1"},
)

# A leave request created by Harry that is still in DRAFT status
harrys_draft_holiday_request = Resource(
    id="XX125",
    kind="leave_request",
    attr={
        "department": "marketing",
        "geography": "GB",
        "id": "XX125",
        "owner": "harry",
        "status": "DRAFT",
        "team": "design",
    },
)

# A leave request created by Maggie that is still in PENDING_APPROVAL status
maggies_pending_holiday_request = Resource(
    id="XX226",
    kind="leave_request",
    attr={
        "department": "marketing",
        "geography": "GB",
        "id": "XX226",
        "owner": "maggie",
        "status": "PENDING_APPROVAL",
        "team": "design",
    },
)

# Harry's leave request that is now in PENDING_APPROVAL state
harrys_pending_holiday_request = Resource(
    **dataclasses.asdict(harrys_draft_holiday_request)
)
harrys_pending_holiday_request.attr["status"] = "PENDING_APPROVAL"

# Harry's leave request that is now in APPROVED state
harrys_approved_holiday_request = Resource(
    **dataclasses.asdict(harrys_draft_holiday_request)
)
harrys_approved_holiday_request.attr["status"] = "APPROVED"


# Check whether the principal is allowed to perform a specific action on the given resource
def check(
    client: CerbosClient,
    principal: Principal,
    action: str,
    resource: Resource,
):
    try:
        effect = "_cannot_"
        icon = emoji.emojize(":cross_mark:")

        if client.is_allowed(action=action, principal=principal, resource=resource):
            effect = "_can_"
            icon = emoji.emojize(":thumbs_up:")

        print(
            f"{icon} {principal.id} {effect} {action} {resource.attr['owner']}'s "
            f"{resource.attr['status']} holiday request"
        )
    except Exception as e:
        print(f"Request failed: {e}")


if __name__ == "__main__":
    # Use the Cerbos TestContainer to start Cerbos automatically. This is for demonstration purposes only.
    # In production scenarios Cerbos would be deployed as a separate service.
    container = CerbosContainer()
    policy_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "policies")
    container.with_volume_mapping(policy_dir, "/policies")

    with container:
        container.wait_until_ready()
        host = container.http_host()

        # Create a Cerbos client
        with CerbosClient(host) as client:
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
