import copy
import cerbos
import emoji


harry = {
    "id": "harry",
    "roles": ["employee"],
    "attr": {"department": "marketing", "geography": "GB", "team": "design"},
}

maggie = {
    "id": "maggie",
    "roles": ["employee", "manager"],
    "attr": {
        "department": "marketing",
        "geography": "GB",
        "managed_geographies": "GB",
        "team": "design",
    },
}

amanda = {
    "id": "amanda",
    "roles": ["employee", "manager"],
    "attr": {
        "department": "marketing",
        "geography": "US",
        "managed_geographies": ["US"],
        "team": "design",
    },
}

pedro = {
    "id": "pedro",
    "roles": ["employee"],
    "attr": {"department": "shipping", "geography": "FR", "team": "Pod 1"},
}

harrys_draft_holiday_request = {
    "kind": "leave_request",
    "attr": {
        "department": "marketing",
        "geography": "GB",
        "id": "XX125",
        "owner": "harry",
        "status": "DRAFT",
        "team": "design",
    },
}

maggies_pending_holiday_request = {
    "kind": "leave_request",
    "attr": {
        "department": "marketing",
        "geography": "GB",
        "id": "XX125",
        "owner": "maggie",
        "status": "PENDING_APPROVAL",
        "team": "design",
    },
}

harrys_pending_holiday_request = copy.deepcopy(harrys_draft_holiday_request)
harrys_pending_holiday_request["attr"]["status"] = "PENDING_APPROVAL"

harrys_approved_holiday_request = copy.deepcopy(harrys_draft_holiday_request)
harrys_approved_holiday_request["attr"]["status"] = "APPROVED"


def questions(principal, action, resource):
    response = None
    icon = None
    if cerbos.check(principal, action, resource):
        response = "_can_"
        icon = emoji.emojize(":thumbs_up:")
    else:
        response = "_cannot_"
        icon = emoji.emojize(":cross_mark:")
    print(
        f"{icon} {principal['id']} {response} {action} {resource['attr']['owner']}'s "
        f"{resource['attr']['status']} holiday request"
    )


# Harry's draft holiday request

for principle, action in [
    (harry, "create"),
    (harry, "view"),
    (pedro, "view"),
    (maggie, "view"),
    (amanda, "view"),
    (maggie, "approve"),
    (amanda, "approve"),
]:
    questions(principle, action, harrys_draft_holiday_request)

print("\nHarry submits his holiday request\n")

# Harry's pending holiday request:
for principle, action in [
    (harry, "approve"),
    (pedro, "view"),
    (amanda, "view"),
    (maggie, "view"),
    (amanda, "approve"),
    (maggie, "approve"),
]:
    questions(principle, action, harrys_pending_holiday_request)

print("\nMaggie approves Harry's holiday request\n")

# Harry's approved holiday request:
for principle, action in [
    (harry, "view"),
    (pedro, "view"),
    (amanda, "view"),
    (maggie, "view"),
]:
    questions(principle, action, harrys_approved_holiday_request)
