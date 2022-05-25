from saving import gameingdata
import random

class GamingStateChanging :
    "常规(不好用的)游戏流程逻辑(修改属性)"
    RollResult = 0
    funa = 0 # funa : 触发修改的规则 =0 大于触发
    funb = 0 # funb : 修改方向 =0 减去
    StratValue = 0 # startvalue : 起始值
    EndValve = 0 # endvalue : 终止值
    changing = 0 # changing修改的量
    state = "" # state : 要修改的状态
    ability = "" # 要判断的能力

    def __RollProject__(self, funa, funb, StratValue, EndValve, state, ability):
        GamingStateChanging.funa = funa
        GamingStateChanging.funb = funb
        GamingStateChanging.StratValue = StratValue
        GamingStateChanging.EndValve = EndValve
        GamingStateChanging.state = state
        GamingStateChanging.ability = ability


    def __Roll__(self, userID, changing):
        GamingStateChanging.changing = changing
        GamingStateChanging.RollResult = random.randint(GamingStateChanging.StratValue, GamingStateChanging.EndValve)
        standard = gameingdata.__GetAbility__(ability_name=GamingStateChanging.ability, userID=userID)
        if GamingStateChanging.funa == 0:
            if GamingStateChanging.RollResult >= standard :
                GamingStateChanging.__stateschang__()
            else:
                if GamingStateChanging.RollResult <= standard :
                    GamingStateChanging.__stateschang__()


    def __stateschang__(self) :
        if GamingStateChanging.funb == 0:
            result = (float(gameingdata.__GetStates__(states_name=GamingStateChanging.state, userID=GamingStateChanging.userID)) - float(
                GamingStateChanging.changing))
            gameingdata.__AddStates__(states_name=GamingStateChanging.state, userID=GamingStateChanging.userID, value=result)
            return "触发"
        if GamingStateChanging.funb == 1:
            result = (float(gameingdata.__GetStates__(states_name=GamingStateChanging.state, userID=GamingStateChanging.userID)) + float(
                GamingStateChanging.changing))
            gameingdata.__AddStates__(states_name=GamingStateChanging.state, userID=GamingStateChanging.userID, value=result)
            return "触发"


class Gaming:
    "判断"
    RollResult = 0
    funa = 0 # funa : 触发修改的规则 =0 大于触发
    StratValue = 0 # startvalue : 起始值
    EndValve = 0 # endvalue : 终止值
    ability = "" # 要判断的能力

    def __RollProject__(self, funa, StratValue, EndValve, ability):
        Gaming.funa = funa
        Gaming.StratValue = StratValue
        Gaming.EndValve = EndValve
        Gaming.ability = ability


    def __Roll__(self, userID):
        Gaming.RollResult = random.randint(Gaming.StratValue, Gaming.EndValve)
        standard = gameingdata.__GetAbility__(ability_name=Gaming.ability, userID=userID)
        if Gaming.funa == 0:
            if Gaming.RollResult >= standard :
                return "触发"
            else:
                if Gaming.RollResult <= standard :
                    return "触发"