from abc import ABC, abstractmethod
from pydantic import BaseModel, Field, model_validator


class BaseAgent(BaseModel, ABC):
    """
    Abstract base class for managing agent state and execution.
    """
    name: str = Field(..., description="Unique name of the agent")
    


