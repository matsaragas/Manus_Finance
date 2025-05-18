from pydantic import BaseModel

class LLMSettings(BaseModel):
    model: str = Field(..., description="Model Name")
