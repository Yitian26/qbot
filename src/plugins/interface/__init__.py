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
on_msg = on_message(rule=to_me())

@on_msg.handle()
async def _(event: MessageEvent):
    result = await chat_bot.handle_message(event)
    print(result)
    if result:
        await on_msg.finish(result)