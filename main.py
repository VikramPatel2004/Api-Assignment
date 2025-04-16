from fastapi import FastAPI, HTTPException
from schemas import AgentRequest
from services.vapi import create_vapi_agent
from services.retell import create_retell_agent

app = FastAPI()

@app.post("/create-agent")
async def create_agent(request: AgentRequest):
    platform = request.platform.lower()
    data = request.dict()

    try:
        if platform == "vapi":
            return await create_vapi_agent(data)
        elif platform == "retell":
            return await create_retell_agent(data)
        else:
            raise HTTPException(status_code=400, detail="Invalid platform: must be 'vapi' or 'retell'")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    