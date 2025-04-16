from pydantic import BaseModel
from typing import Optional

class AgentRequest(BaseModel):
    platform: str  # 'vapi' or 'retell'

    name: Optional [str] = "ABC"
    lang: Optional[str] = "en"
