from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont # проверка типов вводимых значений
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QLabel, QLineEdit
from instr import*
from second_win import*

class MainWin(QWidget):
    def __init__(self):
        ''' окно, в котором располагается приветствие '''
        super().__init__()
        self.set_appear() #устанавливает, как будет выглядеть окно(надпись, размер, место)
        self.setStyleSheet("QWidget"
                            "{"
                            "background-color: rgb(242, 195, 167)" 
                            "}")
        self.initUI() #создаём и  настраиваем графические элементы
        self.connects() #устанавливаем связь между элементами
        self.show() #старт
    def initUI(self):
        ''' создаёт графические элементы '''
        self.btn_next = QPushButton(txt_next)
        self.btn_next.setStyleSheet("QPushButton" 
                                    "{"
                                    "background-color: rgb(171, 235, 203);"
                                    "border-width: 2px;"
                                    "border-radius: 10px;"
                                    "border-color: beige;"
                                    "font: bold 14px;"
                                    "min-width: 10em;"
                                    "padding: 6px;"
                                    "}")
        self.hello_text = QLabel(txt_hello)
        self.hello_text.setStyleSheet("QLabel" 
                                    "{"
                                    "background-color: rgb(171, 235, 203);"
                                    "font: bold 14px;"
                                    "}")
        self.instruction = QLabel(txt_instruction)
        self.instruction.setStyleSheet("QLabel" 
                                    "{"
                                    "font: bold 12px;"
                                    "}")
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.hello_text, alignment = Qt.AlignCenter) 
        self.layout.addWidget(self.instruction, alignment = Qt.AlignCenter)
        self.layout.addWidget(self.btn_next, alignment = Qt.AlignCenter)
        self.setLayout(self.layout)

    def next_click(self):
        self.tw = TestWin()
        self.hide()

    def connects(self):
        self.btn_next.clicked.connect(self.next_click)

    ''' устанавливает, как будет выглядеть окно (надпись, размер, место) '''
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

app = QApplication([])
mw = MainWin()
app.exec_()