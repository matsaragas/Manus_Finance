from typing import Dict, List, Optional, Union
from app.config import LLMSettings

class LLM:
    _instances: Dict[str, "LLM"] = {}

    def __new__(
            cls, config_name: str = "default", llm_config: Optional[LLMSettings] = None):
        pass