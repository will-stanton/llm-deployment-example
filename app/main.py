from chatbot import Chatbot

from contextlib import asynccontextmanager
from fastapi import FastAPI
from pydantic import BaseModel, Field


pokemon_chatbot = Chatbot()


class Prompt(BaseModel):
    """Define the required schema for request data in the POST request"""

    text: str = Field(default="", title="Text input from user", max_length=100)


app = FastAPI()


@app.post("/chat/")
async def get_completion(prompt: Prompt):
    """Get the response from the LLM as part of a POST request"""

    llm_response = pokemon_chatbot.query_chain(prompt.text)
    results = {"completion": llm_response}
    return results
