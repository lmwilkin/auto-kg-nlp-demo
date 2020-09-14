from typing import Dict, List, Optional, AnyStr
from pydantic import BaseModel, Schema


class RecordRequest(BaseModel):
    text: str

class RecordDataResponse(BaseModel):
    resolved_text: str

class Message(BaseModel):
    message: str

class RecordResponse(BaseModel):
    data: RecordDataResponse
    errors: Optional[List[Message]]
    warnings: Optional[List[Message]]



