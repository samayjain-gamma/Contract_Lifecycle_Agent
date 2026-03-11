def filter_contract_json(raw_json):

    contract_data = {
        "contract_name": raw_json.get("contract_name", "Untitled Contract"),
        "starting_date": raw_json.get("starting_date"),
        "expiry_date": raw_json.get("expiry_date"),
        "contract_status": raw_json.get("contract_status", "Pending"),
        "description": raw_json.get("description", ""),
        "email": raw_json.get("email", None),
    }

    deliverables = []
    for d in raw_json.get("deliverables", []):
        deliverables.append(
            {
                "deliverable_name": d.get("deliverable_name"),
                "delivery_date": d.get("delivery_date"),
                "delivery_status": d.get("delivery_status", "Pending"),
                "description": d.get("description", ""),
            }
        )

    return contract_data, deliverables
