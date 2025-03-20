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
from .message_buffer import MessageManager
from .llmapi import llmApi
from .config import global_config

class chatbot:
    def __init__(self):
        self.prompt_builder =promptBuilder(global_config.enabled_prompts)
        self.llm_api = llmApi(global_config.gpt_settings)
        self.message_manager = MessageManager()
    async def handle_message(self, message:MessageEvent) -> list[str]:
        """
        消息处理函数
        Args:
            message (MessageEvent): 消息事件
        """
        if isinstance(message,GroupMessageEvent):
            self.message_manager.push_message(message.group_id,False,message)
            if message.is_tome():
                chat_history = self.message_manager.get_all_messages(message.group_id,False)
                prompt = self.prompt_builder.build_prompt(message,chat_history)
                raw_resp = self.llm_api.send_request_text(prompt) 
                resp = raw_resp.split("。")
                return [part for part in resp if part]
            else:
                return []
