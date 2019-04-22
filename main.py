# coding=utf8

import sys
from PyQt5.QtWidgets import QApplication
from MainWindow.MainWindowMgr import MainWindowMgr


def main():
    app = QApplication(sys.argv)
    window = MainWindowMgr()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
