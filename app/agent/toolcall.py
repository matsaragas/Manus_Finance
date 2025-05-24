from app.agent.react import ReActAgent
from app.prompt.toolcall import SYSTEM_PROMPT, NEXT_STEP_PROMPT
from app.tool import CreateChatCompletion, Terminate, ToolColletion

class ToolCallAgent(ReActAgent):

    name: str = "toolcall"
    description: str = "an agent that can execute tool calls"

    system_prompt: str = SYSTEM_PROMPT
    next_step_prompt: str = NEXT_STEP_PROMPT

    available_tools = ToolCollection = ToolColletion(
        CreateChatCompletion(), Terminate()

    )


