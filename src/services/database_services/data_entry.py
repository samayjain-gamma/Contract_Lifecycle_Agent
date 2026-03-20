from src.services.database_services.contract import insert_contract
from src.services.database_services.deliverables import insert_deliverables
from src.services.json_filter import filter_contract_json

raw_json = {
    "contract_name": "Website Development Agreement",
    "starting_date": "2026-03-01",
    "expiry_date": "2026-03-15",
    "contract_status": "Active",
    "description": "This agreement outlines the terms under which Orion Digital Solutions will design and develop a corporate website for the client. The contract includes planning, design, backend development, and deployment of the website.",
    "email": "samay.jain@gammaedge.io",
    "deliverables": [
        {
            "deliverable_name": "UI/UX Design Prototype",
            "delivery_date": "2026-03-12",
            "deliverable_status": "Pending",
            "description": "Creation of initial wireframes and high-fidelity design prototypes for the website's homepage and main navigation pages.",
        },
        {
            "deliverable_name": "Backend API Development",
            "delivery_date": "2026-03-11",
            "deliverable_status": "Pending",
            "description": "Development of backend APIs required for user authentication, content management, and data retrieval for the website.",
        },
        {
            "deliverable_name": "Final Website Deployment",
            "delivery_date": "2026-06-15",
            "deliverable_status": "Pending",
            "description": "Deployment of the fully developed website to the production server, including testing, bug fixes, and final performance checks.",
        },
    ],
}


contract_data, deliverables = filter_contract_json(raw_json)

print("CONTRACT INFORMATION : \n", contract_data)
print("DELIVERABLE INFORMAITON : \n", deliverables)


contract_id = insert_contract(contract_data)
insert_deliverables(contract_id, deliverables)
