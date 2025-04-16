import httpx

from retell import Retell

async def create_retell_agent(data: dict):
    

    client = Retell(
        api_key="key_21bd448971c49ff3c6432212f2c4",
    )
    agent_response = client.agent.create(
        response_engine={
            "llm_id": "llm_234sdertfsdsfsdf",
            "type": "retell-llm",
        },
        voice_id="11labs-Adrian",
    )
    print(agent_response.agent_id)
    