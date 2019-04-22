# coding=utf8

import json


class JsonMgr(object):
    def __init__(self):
        pass

    def Json2Map(self):
        """将Jason文件转换为内存映射的设置表"""

        settingMap = {}

        # 尝试打开json文件
        try:
            with open("setting.json", 'r') as jsonFile:
                settingMap = json.load(jsonFile)
        except:
            fp = open("setting.json", "w")
            fp.close()

        return settingMap

    def Map2Json(self, settingMap):
        """将内存中的设置表保存成json文件"""

        with open("setting.json", "w") as jsonFile:
            try:
                json.dump(settingMap, jsonFile)
            except:
                pass


if __name__ == '__main__':
    JsonMgrObj = JsonMgr()
    JsonMgrObj.Json2Map()
