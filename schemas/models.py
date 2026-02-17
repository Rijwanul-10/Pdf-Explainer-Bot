from pydantic import BaseModel
from typing import List

class RetrievedChunk(BaseModel):
    content: str

class LLMResponse(BaseModel):
    answer: str
