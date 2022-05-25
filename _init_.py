from gamingstatechanging import GamingStateChanging, Gaming
from saving import gameingdata
from nonebot import on_command
from nonebot.params import ArgStr
from nonebot.adapters.onebot.v11 import GROUP
import re


create_project = on_command( "创建项目", aliases={"新建项目"}, permission=GROUP, priority=5, block=True)
add_states = on_command( "添加状态", aliases={"新建状态", "创建状态"}, permission=GROUP, priority=5, block=True)
add_ability = on_command( "添加能力", aliases={"新建能力", "创建能力"}, permission=GROUP, priority=5, block=True)
roll = on_command( "roll", aliases={"Roll", "ROLL"}, permission=GROUP, priority=5, block=True)
add_roll = on_command( "添加修改roll", aliases={"新建修改Roll", "创建修改roll"}, permission=GROUP, priority=5, block=True)
add_roll2 = on_command("添加roll", aliases={"新建Roll", "创建roll"}, permission=GROUP, priority=5, block=True)
GamingStates = 0

@create_project.handle()
async def GamingStatesChang():
    global GamingStates
    GamingStates = 1 # 以后用的
    await create_project.finish("@猫屋敷你比较可爱,你来写吧") # 创建项目成功


@add_states.got("state_input", prompt="@猫屋敷你比较可爱,你来写吧") # 用户发了关键词,没写后面的参数(虚空命令)
# 格式: 属性名 用户名 默认值
async def new(states_input: str = ArgStr("state_input")):
    ReResult = []
    ReResult = re.split(r" ", states_input)
    state_name =ReResult[0]
    userID = ReResult[1]
    value = Result[2]
    await gameingdata.__AddStates__(states_name=state_name, userID=userID, value=value)
    await add_states.finish("@猫屋敷你比较可爱,你来写吧") # 添加成功


@add_ability.got("ability_input", prompt="@猫屋敷你比较可爱,你来写吧") # 用户发了关键词,没写后面的参数(虚空命令)
# 格式: 属性名 用户名 默认值
async def new(ability_input: str = ArgStr("ability_input")):
    ReResult = []
    ReResult = re.split(r" ", ability_input)
    ability_name =ReResult[0]
    userID = ReResult[1]
    value = Result[2]
    await gameingdata.__AddAbility__(ability_name=ability_name, userID=userID, value=value)
    await add_states.finish("@猫屋敷你比较可爱,你来写吧") # 添加成功


@add_roll.got("InputObject", prompt="@猫屋敷你比较可爱,你来写吧") # 用户发了关键词,没写后面的参数(虚空命令)
async def new(InputObject: str = ArgStr("InputObject")):
    global GamingStates
    ReResult = []
    ReResult = re.split(r" ", InputObject)
    funa = ReResult[0]
    funb = ReResult[1]
    StartValue = Result[2]
    EndValue = ReResult[3]
    ability = ReResult[4]
    await GamingStateChanging.__RollProject__(funa=funa, funb=funb, StratValue=StartValue, EndValve=EndValue, ability=ability)
    await add_states.finish("@猫屋敷你比较可爱,你来写吧")  # 添加成功
    GamingStates = 2.1



@add_roll2.got("InputObject", prompt="@猫屋敷你比较可爱,你来写吧") # 用户发了关键词,没写后面的参数(虚空命令)
async  def new(InputObject: str = ArgStr("InputObject")):
    global GamingStates
    ReResult = re.split(r" ", InputObject)
    funa = ReResult[0]
    StartValue = ReResult[1]
    EndValue = ReResult[2]
    ability = ReResult[3]
    await Gaming.__RollProject__(funa=funa, StratValue=StartValue, EndValve=EndValue, ability=ability)
    await  add_roll2.finish("猫屋敷你比较可爱,你来写吧")
    GamingStates = 2.2



@roll.got("userID", prompt="猫屋敷你比较可爱,你来写吧")
async def new(userID: str = ArgStr("userID")):
    if GamingStates == 2.1 :
        GamingStateChanging.__Roll__(userID=userID)
    elif GamingStates == 2.2 :
        Gaming.__Roll__(userID=userID)

