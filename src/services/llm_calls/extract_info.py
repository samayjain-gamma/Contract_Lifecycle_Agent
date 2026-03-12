from src.core.llm_call import get_llm
from src.prompts.extract_prompt import extract_prompt

llm = get_llm(temperature=0.0)
file_path = "contract.txt"
with open(file_path, "r") as file:
    data = file.read()

prompt = extract_prompt.format(contract_text=data)
print(prompt)

answer = llm.invoke(prompt=prompt)

print(answer)
