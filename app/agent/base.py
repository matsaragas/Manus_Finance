from abc import ABC, abstractmethod
from pydantic import BaseModel, Field, model_validator
from typing import List, Optional
from app.llm import LLM

class BaseAgent(BaseModel, ABC):
    """
    Abstract base class for managing agent state and execution.
    """
    name: str = Field(..., description="Unique name of the agent")
    description: Optional[str] = Field(None, description="Optional Agent Description")
    system_prompt: Optional[str] = Field(None, description="System-level instruction prompt")

    #Dependencies
    self.llm: LLM = Field(default_factory=LLM, description="Language Model Instance")



    @model_validator(mode="after")
    def initialize_agent(self) -> "BaseAgent":
        """Initialize Agent with default settings if not provided"""
        if self.llm is None or not isinstance(self.llm, LLM):
            self.llm = LLM(config_name=self.name.lower())



