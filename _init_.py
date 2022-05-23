from nonebot import on_command

__zx_plugin_name__ = "溯洄"
__plugin_usage__ = """
usage:
    处理跑团有关的随机数与记录工作
    指令： 
        创建跑团项目 [项目名] : 创建一个跑团项目,开启游戏
        创建数值 [成员] [类] [默认值] :创建一个数值记录
        创建判定事件 [成员] [键] [值] : 进行一次判定
        投掷骰子 [取值范围] : 取随机数
        记录数值 [成员] [类] [值] :记下一个数值
""".strip()

__plugin_des__ = "听说你喜欢跑团?"

__plugin_cmd__ = ["创建跑团项目?[项目名]",
                  "创建数值?[成员]?[类]?[默认值]",
                  "创建判定事件?[成员]?[键]?[值]",
                  "投掷骰子?[取值范围]",
                  "记录数值?[成员]?[类]?[值]",]

__plugin_settings__ = {"level": 5,
    "default_status": True,
    "limit_superuser": False,
    "cmd": ["OCO"],}

__plugin_version__ = 1.0.0
__plugin_author__ = "young-4"

__plugin_resource__ = {"longtimesaving" : {"value" : 1 ,
                                         "help" : "设置是否存储到本地以长期使用",
                                         "default_value" : 1,},
                     "resultsaving" : {"value" : 1 ,
                                       "help" : "设置是否记录游戏结果(待开发)",
                                       "default_value" : 1,},
}

