
import requests

async def create_vapi_agent(data: dict):
    response = requests.post(
    "https://api.vapi.ai/assistant",headers={"Authorization": "Bearer "},json={},)

    print(response.json())





    