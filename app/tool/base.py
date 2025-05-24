from pydantic import BaseModel, Field
from abc import ABC


class BaseTool(ABC, BaseModel):
    name: str
    description: str
    parameters: str

