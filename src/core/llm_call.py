import os

import ollama
from dotenv import load_dotenv
from groq import Groq

load_dotenv()


class GroqLLM:

    def __init__(self, temperature=0.0, model="llama-3.1-8b-instant"):
        self.temperature = temperature
        self.model = model
        key = os.getenv("GROQ_API_KEY")
        self.client = Groq(api_key=key)

    def invoke(self, prompt: str):

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "system",
                    "content": "You extract structured information from contracts.",
                },
                {"role": "user", "content": prompt},
            ],
            temperature=self.temperature,
        )
        return response


class OllamaLLM:

    def __init__(self, temperature=0.0, model="phi"):
        self.temperature = temperature
        self.model = model

    def invoke(self, prompt: str):

        response = ollama.chat(
            model=self.model,
            messages=[
                {
                    "role": "system",
                    "content": "You extract structured information from contracts.",
                },
                {"role": "user", "content": prompt},
            ],
            options={"temperature": self.temperature},
        )

        return response["message"]["content"]


def get_llm(temperature=0.0):

    return OllamaLLM(temperature=temperature)

    # return GroqLLM(temperature=temperature)
