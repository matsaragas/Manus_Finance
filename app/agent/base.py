from abc import ABC, abstractmethod
from pydantic import BaseModel, Field, model_validator
from typing import List, Optional
from app.llm import LLM
from app.schema import AgentState, ROLE_TYPE, Memory, Message


class BaseAgent(BaseModel, ABC):
    """
    Abstract base class for managing agent state and execution.
    """
    name: str = Field(..., description="Unique name of the agent")
    description: Optional[str] = Field(None, description="Optional Agent Description")

    #Prompts
    system_prompt: Optional[str] = Field(None, description="System-level instruction prompt")
    next_step_prompt: Optional[str] = Field(None, description="Prompt for Determining next action")




    #Dependencies
    llm: LLM = Field(default_factory=LLM, description="Language Model Instance")
    memory: Memory = Field(default_factory=Memory, description="Agent's memory store")

    max_steps: int = Field(default=10, description="Maximum steps before termination")
    current_step: int = Field(default=0, description="Current step in execution")


    @model_validator(mode="after")
    def initialize_agent(self) -> "BaseAgent":
        """Initialize Agent with default settings if not provided"""
        if self.llm is None or not isinstance(self.llm, LLM):
            self.llm = LLM(config_name=self.name.lower())
        if not isinstance(self.memory, Memory):
            self.memory = Memory()
        return self

    async def run(self, request: Optional[str] = None) -> str:
        if self.state != AgentState.IDLE:
            raise RuntimeError(f"Cannot run agent from state: {self.state}")

        if request:
            self.update_memory("user", request)

        async with self.state_context(AgentState.RUNNING):
            while (self.current_step < self.max_steps and self.state != AgentState.FINISHED):
                self.current_step += 1
                logger.info(f"Execution step {self.current_step}/{self.max_steps}")
                step_result = await self.step()






