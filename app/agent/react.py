from abc import ABC, abstractmethod
from typing import Optional
from app.agent.base import BaseAgent
from pydantic import Field
from app.schema import Memory, AgentState
from app.llm import LLM

class ReActAgent(BaseAgent, ABC):

    name: str
    description: Optional[str] = None


    system_prompt = Optional[str] = None
    max_step_prompt = Optional[str] = None

    llm: Optional[LLM] = Field(default_factory=LLM)
    memory: Memory = Field(default_factory=Memory)
    state: AgentState = AgentState.IDLE

    max_steps: int = 0
    current_step: int = 0

    @abstractmethod
    async def think(self) -> bool:
        """Process current state and decide next action"""

    @abstractmethod
    async def act(self) -> str:
        """Execute decided actions"""

    async def step(self) -> str:
        should_act = await self.think()
        if not should_act:
            return "Thinking Complete - action needed"

        return await self.act()

