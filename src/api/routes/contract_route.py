import json

from fastapi import APIRouter, File, HTTPException, UploadFile

from src.core.logger import logger
from src.queries.view import view_database_route
from src.services.contract_extractor import extract_contract
from src.services.database_services.contract import insert_contract
from src.services.database_services.deliverables import (
    insert_deliverables,
    modify_deliverable_status,
)
from src.services.json_filter import filter_contract_json

router = APIRouter(prefix="/contracts", tags=["Contracts"])


@router.post("/upload")
async def upload_contract(file: UploadFile = File(...)):

    content = await file.read()
    contract_text = content.decode("utf-8")

    logger.info("LLm call will be initiated")
    llm_response = extract_contract(contract_text)

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


@router.get("/database/view")
def get_database_view():

    data = view_database_route()

    return {"status": "success", "data": data}


@router.patch("/deliverables/{deliverable_id}/toggle")
def toggle_status(deliverable_id: int):

    deliverable = modify_deliverable_status(deliverable_id)

    if not deliverable:
        raise HTTPException(status_code=404, detail="Deliverable not found")

    return {
        "deliverable_id": deliverable.deliverable_id,
        "new_status": deliverable.delivery_status,
    }
