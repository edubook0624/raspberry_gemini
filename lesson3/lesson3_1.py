"""
title: Example Filter
author: open-webui
author_url: https://github.com/open-webui
funding_url: https://github.com/open-webui
version: 0.1
"""

from pydantic import BaseModel, Field
from typing import Optional


class Filter:
    class Valves(BaseModel):
        priority: int = Field(
            default=0, description="Priority level for the filter operations."
        )
        max_turns: int = Field(
            default=8, description="Maximum allowable conversation turns for a user."
        )
        pass

    class UserValves(BaseModel):
        max_turns: int = Field(
            default=4, description="Maximum allowable conversation turns for a user."
        )
        pass

    def __init__(self):
        # Indicates custom file handling logic. This flag helps disengage default routines in favor of custom
        # implementations, informing the WebUI to defer file-related operations to designated methods within this class.
        # Alternatively, you can remove the files directly from the body in from the inlet hook
        # self.file_handler = True

        # Initialize 'valves' with specific configurations. Using 'Valves' instance helps encapsulate settings,
        # which ensures settings are managed cohesively and not confused with operational flags like 'file_handler'.
        self.valves = self.Valves()
        pass

    def inlet(self, body: dict, __user__: Optional[dict] = None) -> dict:
        # print("使用者輸入:")
        # print(body.get("messages", [])[-1].get("content", "") if body.get("messages") else "")
        
        return body

    def outlet(self, body: dict, __user__: Optional[dict] = None) -> dict:
        # print last user message
        # messages = body.get("messages", [])
        # user_messages = [m for m in messages if m.get("role") == "user"]
        # if user_messages:
        #     print(user_messages[-1].get("content", ""))

        # # force assistant reply to Hello World
        # for message in body.get("messages", []):
        #     if message.get("role") == "assistant":
        #         message["content"] = "Hello 徐老師!!:D:D"
        for message in body.get("messages", []):
            if message.get("role") == "assistant":
                message["content"] = message.get("content", "") + "\n你的餘額不足囉~~~"

        return body