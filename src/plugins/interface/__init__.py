import asyncio
import time

from nonebot.plugin import on_message
from nonebot.rule import to_me
from nonebot.adapters.onebot.v11 import (
    GroupMessageEvent,
    MessageEvent,
    PrivateMessageEvent,
    NoticeEvent,
    PokeNotifyEvent,
    GroupRecallNoticeEvent,
    FriendRecallNoticeEvent,
)

from ...bot.bot import chatbot

chat_bot = chatbot()
on_msg = on_message()

@on_msg.handle()
async def _(event: MessageEvent):
    result = await chat_bot.handle_message(event)
    if result:
        for msg in result:
            await _reply_like_human(msg)
async def  _reply_like_human(msg:str):
    time.sleep(len(msg)//3)
    await on_msg.send(msg)