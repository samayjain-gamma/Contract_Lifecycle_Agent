# extract_prompt = """
# Extract the following fields from this contract:

# contract_name
# starting_date
# expiry_date
# contract_status
# description

# deliverables:
# deliverable_name
# delivery_date
# delivery_status
# description

# Return the result strictly as JSON not any other thing

# Contract text:
# {contract_text}
# """

extract_prompt = """
You are an information extraction system.

Extract the following fields from the contract.

Fields:
- contract_name
- starting_date
- expiry_date
- contract_status
- description

Deliverables:
- deliverable_name
- delivery_date
- delivery_status
- description

Output Rules:
1. Return ONLY valid JSON.
2. Do NOT wrap the JSON in markdown or code blocks.
3. Do NOT include ```json or ``` markers.
4. Do NOT include explanations or text outside JSON.
5. The first character must be {{ and the last character must be }}.

Expected JSON structure:

{{
  "contract_name": "",
  "starting_date": "",
  "expiry_date": "",
  "contract_status": "",
  "description": "",
  "deliverables": [
    {{
      "deliverable_name": "",
      "delivery_date": "",
      "delivery_status": "",
      "description": ""
    }}
  ]
}}

Contract text:
{contract_text}
"""
