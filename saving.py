class gameingdata:
    "向内存写入玩家状态"
    states = {}
    ability = {}
    userID = []

    def __AddAbility__(self, ability_name, userID, value):
        input_objectA = ability_name + "@" + userID
        gameingdata.ability[input_objectA] = value

    def __GetAbility__(self, ability_name, userID, ):
        key = ability_name + "@" + userID
        try:
            value = gameingdata.ability[key]
        except KeyError:
            value = "KeyError"
        return value


    def __AddStates__(self, states_name, userID, value):
        input_objectA = states_name + "@" + userID
        gameingdata.states[input_objectA] = value


    def __GetStates__(self, states_name, userID):
        key = states_name + "@" + userID
        try:
            value = gameingdata.states[key]
        except KeyError:
            value = "KeyError"
        return value


    def __AddUserID__(self,userID):
        gameingdata.userID.append(userID)


    def __GetUser__(self):
        ls = gameingdata.userID
        return ls