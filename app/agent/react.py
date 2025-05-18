from abc import ABC, abstractmethod
from typing import Optional
from app.agent.base import BaseAgent

class ReActAgent(BaseAgent, ABC):

    name: str
    description: Optional[str] = None
