from typing import Any, List, Optional, Type, Union

from pydantic import BaseModel, Field
from app.tool import BaseTool

class CreateChatCompletion(BaseTool):

    name: str = "create_chat_completion"
    description: str = (
        "Creates a structured completion with specified output formatting."
    )
