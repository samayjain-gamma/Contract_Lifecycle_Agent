from src.core.llm_call import get_llm
from src.core.logger import logger
from src.prompts.extract_prompt import extract_prompt

llm = get_llm()

# def extract_contract(file_path):
#     print(file_path)
#     with open(file_path, "r", encoding="utf-8") as f:
#         data = f.read()

#     prompt = extract_prompt.format(contract_text=data)

#     answer = llm.invoke(prompt)

#     return answer


def extract_contract(contract_text: str):

    prompt = extract_prompt.format(contract_text=contract_text)
    logger.info(prompt)
    logger.info("Entered in to extract contract, llm call will be initializexs")
    answer = llm.invoke(prompt)
    logger.info(answer)
    return answer
