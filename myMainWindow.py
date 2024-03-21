from PyQt5.QtWidgets import QMainWindow
from Ui_MainWindow import Ui_MainWindow
import sys


class QmyMainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # 让python中的print语句和错误输出到textBrowser,因为print等价于sys.stdout.write
        # 所以把self赋值给sys.stdout和sys.stderr,并且提供一个write方法
        # In python, print() == sys.stdout.write()
        # so we can let sys.stdout point to a UI object who have write().
        self.sys_stdout_bak = sys.stdout
        self.sys_stderr_bak = sys.stderr
        sys.stdout = self
        sys.stderr = self

    # 这个write方法是给sys.stdout的调用的。
    # This write() can be called by sys.stdout.
    def write(self, text):
        self.ui.textBrowser.insertPlainText(text)
        self.ui.textBrowser.moveCursor(self.ui.textBrowser.textCursor().End)

    # 退出主窗口前把sys.stdout和sys.stderr还原，否则系统退出时报错，120退出代码
    # When close, restore sys.stdout and sys.stderr, to avoid python return error exit code 120.
    def closeEvent(self, event):
        sys.stdout = self.sys_stdout_bak
        sys.stderr = self.sys_stderr_bak






