# import asyncio
from langflow.load import run_flow_from_json
from dotenv import load_dotenv
import requests
from typing import Optional
import json
import os
# import nest_asyncio


# # Apply nest_asyncio patch to allow nested loops
# nest_asyncio.apply()

# Load environment variables
load_dotenv()

BASE_API_URL = "https://api.langflow.astra.datastax.com"
LANGFLOW_ID = "32d6adb8-f324-415d-9ad3-21d9729c1098"
APPLICATION_TOKEN = os.getenv("LANGFLOW_TOKEN")





# from astrapy import DataAPIClient

# # Initialize the client
# client = DataAPIClient("ASTRA_DBTOKEN")
# db = client.get_database_by_api_endpoint(
#   "https://4cab54ff-3f23-4408-9714-a8c432bd71dc-us-east-2.apps.astra.datastax.com"
# )

# print(f"Connected to Astra DB: {db.list_collection_names()}")

def ask_ai(profile, question):
    TWEAKS = {
        "TextInput-xYAYV": {
            "input_value": question
        },
        "TextInput-12Lm7": {
            "input_value": profile
        },
        "AstraVectorStoreComponent": {
            "user_id": "divineintelligence3.0@gmail.com",
        },
    }


    result = run_flow_from_json(flow="AskAIV2.json",
                                input_value="message",
                                fallback_to_env_vars=True,
                                tweaks=TWEAKS)

    return result[0].outputs[0].results["text"].data["text"]


def get_macros(profile, goals):
    TWEAKS = {
        "TextInput-9EERK": {
            "input_value": goals
        },
        "TextInput-4kiqO": {
            "input_value": profile
        },
    }
    return run_flow("", tweaks=TWEAKS, application_token=APPLICATION_TOKEN)



def run_flow(message: str,
  output_type: str = "chat",
  input_type: str = "chat",
  tweaks: Optional[dict] = None,
  application_token: Optional[str] = None) -> dict:
    api_url = f"{BASE_API_URL}/lf/{LANGFLOW_ID}/api/v1/run/macros"

    payload = {
        "input_value": message,
        "output_type": output_type,
        "input_type": input_type,
    }
    headers = None
    if tweaks:
        payload["tweaks"] = tweaks
    if application_token:
        headers = {"Authorization": "Bearer " + application_token, "Content-Type": "application/json"}
    response = requests.post(api_url, json=payload, headers=headers)
    return response.json()["outputs"][0]["outputs"][0]["results"]["text"]["data"]["text"]