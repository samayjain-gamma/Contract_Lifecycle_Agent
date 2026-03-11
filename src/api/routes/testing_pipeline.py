import json

from src.core.logger import logger
from src.services.contract_extractor import extract_contract
from src.services.database_services.contract import insert_contract
from src.services.database_services.deliverables import insert_deliverables
from src.services.json_filter import filter_contract_json

llm_response = """
{
  "contract_name": "Website Development Agreement",
  "starting_date": "2026-03-01",
  "expiry_date": "2026-06-30",
  "contract_status": "Active",
  "description": "This agreement outlines the terms under which Orion Digital Solutions will design and develop a corporate website for the client. The contract includes planning, design, backend development, and deployment of the website.",
  "deliverables": [
    {
      "deliverable_name": "UI/UX Design Prototype",
      "delivery_date": "2026-03-25",
      "deliverable_status": "Pending",
      "description": "Creation of initial wireframes and high-fidelity design prototypes for the website’s homepage and main navigation pages."
    },
    {
      "deliverable_name": "Backend API Development",
      "delivery_date": "2026-04-30",
      "deliverable_status": "Pending",
      "description": "Development of backend APIs required for user authentication, content management, and data retrieval for the website."
    },
    {
      "deliverable_name": "Final Website Deployment",
      "delivery_date": "2026-06-15",
      "deliverable_status": "Pending",
      "description": "Deployment of the fully developed website to the production server, including testing, bug fixes, and final performance checks."
    }
  ]
}

"""


def test_pipeline(llm_response):

    logger.info(
        "LLM call occured, now move to the next process, which is filter_contract_json..."
    )
    # convert to dict
    extracted_json = json.loads(llm_response)
    logger.info(f"extracted_json : {extracted_json}")
    # filter for database
    contract_data, deliverables = filter_contract_json(extracted_json)
    logger.info(f"contract_data : {contract_data}")
    logger.info(f"deliverables : {deliverables}")
    # contract_data, deliverables = filter_contract_json(llm_response)

    contract_id = insert_contract(contract_data)

    insert_deliverables(contract_id, deliverables)

    return {"message": "Contract stored successfully", "contract_id": contract_id}


if __name__ == "__main__":
    test_pipeline(llm_response)
