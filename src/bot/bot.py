import logging

from nonebot.adapters.onebot.v11 import (
    Bot,
    GroupMessageEvent,
    MessageEvent,
    PrivateMessageEvent,
    NoticeEvent,
    PokeNotifyEvent,
    GroupRecallNoticeEvent,
    FriendRecallNoticeEvent,
)

from .prompt_builder import promptBuilder
from .gptapi import gptApi

enabled_prompts = [
    "time", 
    "personal_information", 
    "current_msg", 
    "basic",
]

gpt_settings = {
    "api_key": "sk-phlbcwawejllfeldnbgxonvrpokfwoeahkdtfzzbjgekrafv",
    "base_url": "https://api.siliconflow.cn/v1",
    "model": "deepseek-ai/DeepSeek-V3",
}

class chatbot:
    def __init__(self):
        self.prompt_builder =promptBuilder(enabled_prompts)
        self.gptApi = gptApi(**gpt_settings)

    async def handle_message(self, message:MessageEvent) -> str:
        prompt = self.prompt_builder.build_prompt(message,[message])
        resp = self.gptApi.send_request(prompt)
        return resp
