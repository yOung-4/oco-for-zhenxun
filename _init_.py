from nonebot import on_command
from nonebot.adapters.onebot.v11 import GROUP, Bot, GroupMessageEvent, Message
from nonebot.params import CommandArg, Command, ArgStr
import time
import re
import random
import asyncio


create = on_command(
    "创建新项目", aliases={"新建项目", "新项目"}, permission=GROUP, priority=5, block=True)
add_user = on_command(
    "添加用户", aliases={"拉人"}, permission=GROUP, priority=5, block=True
)
add_ability = on_command(
    "新建能力", aliases={"能力"}, permission=GROUP, priority=5, block=True
)

states = 0  # 游戏状态(是否有进行中的游戏)-int-0 : 无状态 / 1 : 新建项目 / 2 : 添加用户 / 3 : 添加能力 / 4 : 添加属性 / 5 : 进行中
userls = []
abilityls = {}

@create.got("project_name", prompt="项目不配拥有姓名吗")
async def _(project_name_input: str = ArgStr("project_name")):
    if states == 1 and 2 and 3 and 4:
        await create.finish("错误,已经有活动中的项目,新建失败", at_sender=True)
    elif states == 5 :
        await create.finish("不要打断(ノへ￣、)", at_sender=True)
    else:
        states = 1
        project_name = project_name_input
        global project_name
    print("log.txt do not exist")
    file = open("log.txt", "a+")
    await create.finish("创建成功", at_sender=True)


@add_user.got("user_input", prompt="一个人都不加那是想干嘛")
async def _(user_input : str = ArgStr("user_input"))
    for object in re.split(r" ", user_input):
        userls.append(object)

@add_ability.got("user_input", prompt="输入能力,格式为'新建能力 用户名 能力名 默认值'")
async  def _(user_input : str = ArgStr("user_input")):
    if re.match(r' ', user_input) :
    ls = re.split(r" ", user_input)
    abilityls[ls[1]] = ls[2]
    await add_ability.finish("创建成功", at_sender=True)
    else:
        await add_ability.finish("错误的输入", at_sender=True)
