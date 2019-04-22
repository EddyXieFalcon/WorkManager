# coding=utf8

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog, QInputDialog, QLineEdit, QTableWidgetItem
from PyQt5.QtCore import pyqtSlot
from MainWindow.MainWindow import Ui_MainWindow
from TableWidgetMgr.TableWidgetMgr import TableWidgetMgr
from JsonMgr.JsonMgr import JsonMgr
import os


class MainWindowMgr(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        """构造方法"""

        # 父类方法
        QtWidgets.QWidget.__init__(self, parent)

        # 创建界面
        self.setupUi(self)  # 创建界面

        # 初始化所有成员变量
        self.tabletWidgetSettingMgr = TableWidgetMgr()
        self.tabletWidgetSettingMgr.SetTableWidget(self.tableWidgetSetting)
        self.tabletWidgetUnitMgr = TableWidgetMgr()
        self.tabletWidgetUnitMgr.SetTableWidget(self.tableWidgetUnit)
        self.jsonMgr = JsonMgr()

        # 读取已存在的配置文件
        self.settingMap = self.jsonMgr.Json2Map()

        # 将数据导入界面
        self.LoadMap()

        # 连接所有的按钮与槽函数
        self.btnAddSetting.clicked.connect(self.onBtnAddSettingClickedSlot)
        self.btnDelSetting.clicked.connect(self.onBtnDelSettingClickedSlot)
        self.btnEditSetting.clicked.connect(self.onBtnEditSettingClickedSlot)
        self.btnAddUnit.clicked.connect(self.onBtnAddUnitClickedSlot)
        self.btnDelUnit.clicked.connect(self.onBtnDelUnitClickedSlot)
        self.btnEditUnit.clicked.connect(self.onBtnEditUnitClickedSlot)
        self.btnDo.clicked.connect(self.onBtnDoClickedSlot)
        self.tableWidgetSetting.itemClicked.connect(self.onTableWidgetSettingItemClickedSlot)
        self.tableWidgetUnit.itemChanged.connect(self.onTableWidgetSettingCurrentItemChangedSlot)

    def LoadMap(self):
        """将数据导入界面"""
        # 容错，没有表，无需导入
        if not self.settingMap:
            return

        # 解析map，循环遍历
        lastKey = ""
        for key, value in self.settingMap.items():
            # 添加配置集内容表
            self.tabletWidgetSettingMgr.AddSetting(key)
            lastKey = key

        # 加载配置表（节省效率，只需要加载最后一张）
        self.tabletWidgetUnitMgr.AddUnitMap(self.settingMap[lastKey])

    @pyqtSlot()
    def onBtnAddSettingClickedSlot(self):
        """添加设置主题"""
        # 弹出对话框，要求为配置输入一个名称
        (name, mark) = QInputDialog.getText(self, u"输入一个名称", u"设置集名称：", QLineEdit.Normal, u"")
        if not mark:
            return

        # 判断一下该配置是否存在
        if name in self.settingMap:
            return

        # 先将信息存入Map
        self.settingMap[name] = {}

        # 如果成功获取一个名称，要用接口，保存到界面和配置文件中
        self.tabletWidgetSettingMgr.AddSetting(name)

        # 记录到json文件中
        self.jsonMgr.Map2Json(self.settingMap)

    @pyqtSlot()
    def onBtnDelSettingClickedSlot(self):
        """删除设置主题"""
        # 获取该条数据记录
        name = self.tabletWidgetSettingMgr.GetCurrentSetting()
        if name not in self.settingMap:
            return

        # 先删除map中的数据
        self.settingMap.pop(name)

        # 删除ui中的数据
        self.tabletWidgetSettingMgr.DelSetting()

        # 记录到json文件中
        self.jsonMgr.Map2Json(self.settingMap)

    @pyqtSlot()
    def onBtnEditSettingClickedSlot(self):
        """编辑设置主题"""
        # 先获取要编辑的那条设置集
        oldName = self.tabletWidgetSettingMgr.GetCurrentSetting()
        if oldName not in self.settingMap:
            return

        # 弹出对话框，要求为配置输入一个名称
        (name, mark) = QInputDialog.getText(self, u"输入一个名称", u"设置集名称：", QLineEdit.Normal, oldName)
        if name in self.settingMap:
            return

        # 将map中旧的设置改为新的
        self.settingMap[name] = self.settingMap[oldName]
        self.settingMap.pop(oldName)

        # 将ui中的数据改掉
        self.tabletWidgetSettingMgr.EditSetting(name)

        # 记录到json文件中
        self.jsonMgr.Map2Json(self.settingMap)

    @pyqtSlot()
    def onBtnAddUnitClickedSlot(self):
        """添加设置配置"""
        # 如果没有当前没有选中然和设置集，不予添加
        name = self.tabletWidgetSettingMgr.GetCurrentSetting()
        if name not in self.settingMap:
            return

        # 添加一个设置
        (filePath, fileType) = QFileDialog.getOpenFileName(self, u"打开一个快捷方式", u"C:/ProgramData/Microsoft/Windows/Start Menu/Programs", u"快捷方式(*.lnk)")

        # 解析设置
        fileName = filePath.split("/")[-1].replace(".lnk", "")

        # 判断一下该配置项是否存在
        if fileName in self.settingMap[name]:
            return

        # 将配置的设置放入map中
        self.settingMap[name][fileName] = filePath

        # 将配置的设置访如ui界面中
        self.tabletWidgetUnitMgr.AddUnitMap(self.settingMap[name])

        # 记录到json文件中
        self.jsonMgr.Map2Json(self.settingMap)

    @pyqtSlot()
    def onBtnDelUnitClickedSlot(self):
        """删除设置配置"""
        # 获取该条数据记录
        settingName = self.tabletWidgetSettingMgr.GetCurrentSetting()
        fileName = self.tabletWidgetUnitMgr.GetCurrentSetting()
        if not settingName.strip() and not fileName.strip():
            return

        # 先删除map中的数据
        self.settingMap[settingName].pop(fileName)

        # 删除ui中的数据
        self.tabletWidgetUnitMgr.DelSetting()

        # 记录到json文件中
        self.jsonMgr.Map2Json(self.settingMap)

    @pyqtSlot()
    def onBtnEditUnitClickedSlot(self):
        """编辑设置配置"""
        # 获取该条数据记录
        settingName = self.tabletWidgetSettingMgr.GetCurrentSetting()
        fileName = self.tabletWidgetUnitMgr.GetCurrentSetting()
        if not settingName.strip() and not fileName.strip():
            return

        # 弹出对话框，要求为配置输入一个名称
        (name, mark) = QInputDialog.getText(self, u"输入一个名称", u"快捷方式名称：", QLineEdit.Normal, fileName)
        if not name.strip():
            return

        # 将map中旧的设置改为新的
        self.settingMap[settingName][name] = self.settingMap[settingName][fileName]
        self.settingMap[settingName].pop(fileName)

        # 将ui中的数据改掉
        self.tabletWidgetUnitMgr.AddUnitMap(self.settingMap[settingName])

        # 记录到json文件中
        self.jsonMgr.Map2Json(self.settingMap)

    @pyqtSlot()
    def onBtnDoClickedSlot(self):
        """执行按钮"""
        # 依据当前被选中的配置集，一次打开软件快捷方式
        name = self.tabletWidgetSettingMgr.GetCurrentSetting()
        if name not in self.settingMap:
            return

        # 循环遍历配置集所有的配置，依次使用进程打开程序
        for key, value in self.settingMap[name].items():
            os.startfile(value)

        # 如果勾选了“完成后关闭”，关闭界面
        if self.chbEnableClose.isChecked():
            self.close()

    @pyqtSlot(QTableWidgetItem)
    def onTableWidgetSettingItemClickedSlot(self, item):
        """配置集表切换"""
        # 获取配置集名字
        name = item.text()

        # 判断该配置集是否存在
        if name in self.settingMap:
            # 将配置的设置访如ui界面中
            self.tabletWidgetUnitMgr.AddUnitMap(self.settingMap[name])

    @pyqtSlot(QTableWidgetItem)
    def onTableWidgetSettingCurrentItemChangedSlot(self, currentItem):
        """配置集表单元格被点击"""
        # 容错，当删除最后一个配置集的时候，传来的单元格对象为空
        if currentItem is None:
            self.tabletWidgetUnitMgr.ClearContents()
            return

        # 获取配置集名字
        name = currentItem.text()

        # 判断该配置集是否存在
        if name in self.settingMap:
            # 将配置的设置访如ui界面中
            self.tabletWidgetUnitMgr.AddUnitMap(self.settingMap[name])
