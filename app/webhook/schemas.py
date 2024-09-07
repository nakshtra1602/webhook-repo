from pydantic import BaseModel
from enum import Enum
from datetime import datetime

class Action(str, Enum):
    PUSH = "push"
    PULL_REQUEST = "pull_request"
    MERGE = "merge"

class GitHubEvent(BaseModel):
    request_id: str
    author: str
    from_branch: str
    to_branch: str
    timestamp: str(datetime.utcnow())
    action: Action
