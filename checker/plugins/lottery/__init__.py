from nonebot import get_driver
from nonebot.plugin import on_command
from nonebot.adapters.onebot.v11 import GROUP_ADMIN, GroupMessageEvent,Message,MessageSegment
from nonebot.rule import to_me
from nonebot.params import ArgPlainText
from .config import Config
from .lottery import raffle


global_config = get_driver().config


config = Config.parse_obj(global_config)

number = 0

lottery = on_command("抽奖", aliases={"抽人"}, priority=5, block=True,permission=GROUP_ADMIN,rule=to_me())

@lottery.got("key", prompt="请输入抽奖人数")
async def _(event: GroupMessageEvent, key: str = ArgPlainText()):
    global number
    
    if key.isnumeric():
        number = int(key)
        msg = raffle(number)
        if isinstance(msg, str):
            await lottery.finish(msg)
        else:
            await lottery.finish(Message([MessageSegment.text('所选中的人为'),MessageSegment.text(",".join(msg))]))
    else:
        await lottery.finish("输入错误，请重新输入数字")
    
