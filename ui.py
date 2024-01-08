import gradio as gr
import os
import requests

APPRUNNER_URL = os.environ["APPRUNNER_URL"]


def query_api(prompt: str):
    """Queries the AppRunner service to get a response from the LLM"""

    response = requests.post(f"{APPRUNNER_URL}/chat/", json={"text": prompt})

    response_json = response.json()

    return response_json["completion"]


gr.Interface(fn=query_api, inputs="text", outputs="text").launch()

demo.launch()
