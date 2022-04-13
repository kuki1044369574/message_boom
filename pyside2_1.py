from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton,  QPlainTextEdit,QMessageBox
from pynput.mouse import Button , Controller as mouse_c
from pynput.keyboard import Key, Controller as key_c


class app():
    def __init__(self):
        #主窗口
        self.main_window=QMainWindow()
        self.main_window.resize(300,150)
        self.main_window.move(400,300)
        self.main_window.setWindowTitle('消息轰炸')
        #轰炸内容
        self.enter_text=QPlainTextEdit(self.main_window)
        self.enter_text.resize(200,120)
        self.enter_text.move(0,30)


        self.enter_text.setPlaceholderText("请输入轰炸内容：")
        #轰炸次数
        self.time=QPlainTextEdit(self.main_window)
        self.time.resize(200,30)
        self.time.move(0,0)
        self.time.setPlaceholderText('请输入轰炸次数')
        #反应按钮
        self.button=QPushButton('开始轰炸',self.main_window)
        self.button.move(200,55)
        self.button.clicked.connect(self.hongzha)
    def hongzha(self):
        times=int(self.time.toPlainText())
        text=str(self.enter_text.toPlainText())
        mouse = mouse_c()
        mouse.press(Button.left)
        mouse.release(Button.left)
        for i in range(times):
            keyboard = key_c()
            keyboard.type(text)
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)




App=QApplication()
app=app()
app.main_window.show()
App.exec_()

