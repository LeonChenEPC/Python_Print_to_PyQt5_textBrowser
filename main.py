from PyQt5.QtWidgets import QApplication
from myMainWindow import QmyMainWindow


app = QApplication([])
mainWindow = QmyMainWindow()
mainWindow.show()

print("hello world")
print("test")
print("test1")
print("test2")

app.exec_()
