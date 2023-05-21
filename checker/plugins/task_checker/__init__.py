from nonebot import get_driver
from .config import Config
from .get_member import get_member
from nonebot import on_command
from nonebot.permission import SuperUser
from os import walk
from os.path import join
from nonebot.params import ArgPlainText
from nonebot.rule import to_me
from nonebot.adapters.onebot.v11 import MessageSegment, Message


global_config = get_driver().config
config = Config.parse_obj(global_config)

path = r'C:\Users\zy\OneDrive - tzenay\作业收集'
content = []
for root, dirs, files in walk(path):
    if len(files) != 0:
        content.append(root)
content = [i[35:] for i in content]
content = list(map(lambda x: (content.index(x)+1).__str__()+':'+x, content))
content_message = '\n'.join(content)

temp = 0


task_checker = on_command('task_checker', aliases={'查看作业', '作业检查'}, priority=5, block=True,permission=SuperUser,rule=to_me())

@task_checker.got('content_message', prompt=content_message)
async def _(content_message:str = ArgPlainText()):
    global temp
    temp = int(content_message)
    await task_checker.send(f'正在查询{content_message}号文件夹')

@task_checker.handle()
async def _():
    global temp
    asked_path = join(path, content[temp-1][2:])
    uncommiteedID, wrong_ID = get_member(asked_path)
    if uncommiteedID == '所有人都提交了':
        await task_checker.finish('所有人都提交了')
    elif len(wrong_ID)!=0:
        message = Message([MessageSegment.text('未提交的人有：')])
        for i in uncommiteedID:
            message.append(MessageSegment.at(i))
        message.append(MessageSegment.text('\n以下学号填写错误：'))
        for i in wrong_ID:
            message.append(MessageSegment.text(str(i)+','))
        await task_checker.finish(message)
    else:
        message = Message([MessageSegment.text('未提交的人有：')])
        for i in uncommiteedID:
            message.append(MessageSegment.at(i))
        await task_checker.finish(message)

