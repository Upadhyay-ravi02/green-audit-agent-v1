from pydantic import BaseModel
from typing import Optional, Dict, List

class BrowserGymObs(BaseModel):
    goal: str
    url: str
    screenshot: Optional[List[float]] = None
    last_action_error: bool = False
    metadata: Dict = {}

class ActionResult(BaseModel):
    observation: BrowserGymObs
    reward: float
    done: bool
    info: Dict = {}