extract_prompt = """
Extract the following fields from this contract:

contract_name
starting_date
expiry_date
contract_status
description

deliverables:
deliverable_name
delivery_date
delivery_status
description

Return the result strictly as JSON not any other thing

Contract text:
{contract_text}
"""
