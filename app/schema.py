from pydantic import BaseModel, Field
from enum import Enum
from typing import Optional, List


class Role(str, Enum):
    """Message Role Options"""
    SYSTEM = "system"
    USER = "user"
    ASSISTANT = "assistant"
    TOOL = "tool"

class Function(BaseModel):
    name: str
    arguments: str

class ToolCall(BaseModel):
    id: str
    type: str = "function"
    function: Function


ROLE_VALUES = tuple(role.value for role in Role)
# only ROLE_VALUES are acceptable in ROLE_TYPE
ROLE_TYPE = Literal[ROLE_VALUES]

class Message(BaseModel):
    """
    Represent a chat message in the conversation
    """
    role: ROLE_TYPE = Field(...)
    content: Optional[str] = Field(default=None)
    tool_calls: Optional[List[ToolCall]] = Field(default=None)
    name: Optional[str] = Field(default=None)
    tool_call_id: Optional[str] = Field(default=None)
    base64_image: Optional[str] = Field(default=None)

    def __add__(self, other) -> List["Message"]:
        if isinstance(other, list):
            return [self] + other
        elif isinstance(other, Message):
            return [self, other]
        else:
            raise TypeError(
                f"unsupported operand type(s) for +: '{type(self).__name__}' and '{type(other).__name__}'"
            )

    def __radd__(self, other) -> List["Message"]:
        pass

    def to_dict(self) -> dict:
        """TODO"""
        message = {"role": self.role}
        if self.content is not None:
            message["content"] = self.content

        return message


