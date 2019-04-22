# coding=utf8

from PyQt5.QtWidgets import QTableWidgetItem


class TableWidgetMgr(object):
    def __init__(self):
        """初始化"""
        self.tableWidget = None  # 管理的表格对象

    def SetTableWidget(self, tableWidget):
        """设置本类管理的表格"""
        self.tableWidget = tableWidget

    def AddSetting(self, settingName):
        """添加一条设置集"""
        # 先统计一下总行数
        rowIndex = self.tableWidget.rowCount()
        # 新添加一行
        self.tableWidget.setRowCount(rowIndex + 1)
        # 为新的一行添加文本
        self.tableWidget.setItem(rowIndex, 0, QTableWidgetItem(settingName))
        # 自动将新添加的一行选中
        self.tableWidget.setCurrentCell(rowIndex, 0)

    def DelSetting(self):
        """删除一条设置集"""
        # 必须有一个配置集被选中
        if 0 <= self.tableWidget.currentRow():
            # 删除当前选中的配置集
            self.tableWidget.removeRow(self.tableWidget.currentRow())
            # 默认将最后一行选中
            self.tableWidget.setCurrentCell(self.tableWidget.rowCount() - 1, 0)
            return

        # 如果只有一行，清空表
        if 0 == self.tableWidget.currentRow():
            self.tableWidget.clearContents()
            return

    def EditSetting(self, settingName):
        """重新编辑一条设置集"""
        # 必须有一个配置集被选中
        if 0 <= self.tableWidget.currentRow():
            # 删除当前选中的配置集
            self.tableWidget.item(self.tableWidget.currentRow(), 0).setText(settingName)

        # 默认将最后一行选中
        self.tableWidget.setCurrentCell(self.tableWidget.rowCount() - 1, 0)

    def AddUnitMap(self, unitMap):
        """添加一条设置"""
        # 先清空表格
        self.tableWidget.clearContents()

        # 重新设置表格大小
        self.tableWidget.setRowCount(len(unitMap))

        # 循环遍历map
        row = 0
        for key, value in unitMap.items():
            # 添加内容
            self.tableWidget.setItem(row, 0, QTableWidgetItem(key))
            row = row + 1

        # 默认将最后一行选中
        self.tableWidget.setCurrentCell(self.tableWidget.rowCount() - 1, 0)

    def ClearContents(self):
        """清空表格所有内容"""
        self.tableWidget.claerContents()

    def HasSelectedSetting(self):
        """判断表格中是否有选中项"""
        return 0 <= self.tableWidget.currentRow()

    def GetCurrentSetting(self):
        """获取当前选中的设置的名称"""
        # 如果当前有选中
        if self.HasSelectedSetting():
            # 返回当前选项的文本
            return self.tableWidget.currentItem().text()
        # 如果没有选中
        else:
            # 返回空字符串
            return ""
