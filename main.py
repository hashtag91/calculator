from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QToolButton, QVBoxLayout, 
                             QHBoxLayout, QGridLayout, QSizePolicy, QPushButton)
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt
import sys

class Main_Interface(QWidget):
    def __init__(self):
        super().__init__()
        

        self.main_layout = QVBoxLayout()
        self.setupUi()
        self.setLayout(self.main_layout)
        
    def setupUi(self):
        self.one = Btn("1")
        self.one.clicked.connect(lambda: self.button_function("1"))
        self.two = Btn("2")
        self.two.clicked.connect(lambda: self.button_function("2"))
        self.three = Btn("3")
        self.three.clicked.connect(lambda: self.button_function("3"))
        self.four = Btn("4")
        self.four.clicked.connect(lambda: self.button_function("4"))
        self.five = Btn("5")
        self.five.clicked.connect(lambda: self.button_function("5"))
        self.six = Btn("6")
        self.six.clicked.connect(lambda: self.button_function("6"))
        self.seven = Btn("7")
        self.seven.clicked.connect(lambda: self.button_function("7"))
        self.eight = Btn("8")
        self.eight.clicked.connect(lambda: self.button_function("8"))
        self.nine = Btn("9")
        self.nine.clicked.connect(lambda: self.button_function("9"))
        self.zero = Btn("0")
        self.zero.clicked.connect(lambda: self.button_function("0"))
        self.addition = Btn("+")
        self.addition.clicked.connect(lambda: self.operator_function("+"))
        self.substraction = Btn("-")
        self.substraction.clicked.connect(lambda: self.operator_function("-"))
        self.division = Btn("/")
        self.division.clicked.connect(lambda: self.operator_function("/"))
        self.multiply = Btn("*")
        self.multiply.clicked.connect(lambda: self.operator_function("*"))
        self.egal = Btn("=")
        self.egal.clicked.connect(self.egal_function)
        self.clear = Btn("C")
        self.clear.clicked.connect(self.clear_function)
        self.comma = Btn(",")
        self.comma.clicked.connect(lambda: self.button_function("."))
        btn_layout = QGridLayout()
        btn_layout.addWidget(self.clear,0,2)
        btn_layout.addWidget(self.division,0,3)
        btn_layout.addWidget(self.one,1,0)
        btn_layout.addWidget(self.two,1,1)
        btn_layout.addWidget(self.three,1,2)
        btn_layout.addWidget(self.multiply,1,3)
        btn_layout.addWidget(self.four,2,0)
        btn_layout.addWidget(self.five,2,1)
        btn_layout.addWidget(self.six,2,2)
        btn_layout.addWidget(self.substraction,2,3)
        btn_layout.addWidget(self.seven,3,0)
        btn_layout.addWidget(self.eight,3,1)
        btn_layout.addWidget(self.nine,3,2)
        btn_layout.addWidget(self.addition,3,3)
        btn_layout.addWidget(self.zero,4,0,1,2)
        btn_layout.addWidget(self.comma,4,2)
        btn_layout.addWidget(self.egal,4,3)
        self.result_label = QLineEdit()
        self.result_label.setText("0")
        self.result_label.setReadOnly(True)
        self.result_label.setMinimumHeight(80)
        self.result_label.setObjectName("result_label")
        self.result_label.setFont(QFont("Arial Black",18,QFont.Bold))
        self.result_label.setAlignment(Qt.AlignmentFlag.AlignVCenter)
        self.result_label.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.result_label.textChanged.connect(self.result_function)

        self.main_layout.addWidget(self.result_label)
        self.main_layout.addLayout(btn_layout)
    def button_function(self,value):
        if self.result_label.text() != "0":
            self.result_label.setText(self.result_label.text()+value)
        else:
            self.result_label.setText(value)
    def operator_function(self, value):
        if value == "/":
            self.result_label.setText(self.result_label.text()+" "+value+" ")
            self.multiply.setDisabled(True)
            self.substraction.setDisabled(True)
            self.addition.setDisabled(True)
        elif value == "*":
            self.result_label.setText(self.result_label.text()+" "+value+" ")
            self.division.setDisabled(True)
            self.substraction.setDisabled(True)
            self.addition.setDisabled(True)
        elif value == "+":
            self.result_label.setText(self.result_label.text()+" "+value+" ")
            self.multiply.setDisabled(True)
            self.substraction.setDisabled(True)
            self.division.setDisabled(True)
        elif value == "-":
            self.result_label.setText(self.result_label.text()+" "+value+" ")
            self.multiply.setDisabled(True)
            self.division.setDisabled(True)
            self.addition.setDisabled(True)
    def clear_function(self):
        self.result_label.setText("0")
        self.multiply.setDisabled(False)
        self.division.setDisabled(False)
        self.addition.setDisabled(False)
        self.substraction.setDisabled(False)
    def result_function(self):
        if len(self.result_label.text()) >= 2:
            if self.result_label.text()[-2] in ["/","+","-","*"]:
                self.comma.setDisabled(True)
            else:
                self.comma.setDisabled(False)
    def egal_function(self):
        elements = self.result_label.text().split(" ")
        if len(elements) == 3:
            if "." in elements[0] or "." in elements[2]:
                elements[0] = float(elements[0])
                elements[2] = float(elements[2])
            else:
                elements[0] = int(elements[0])
                elements[2] = int(elements[2])
            if elements[1] == "+":
                result = elements[0] + elements[2]
                self.result_label.setText(str(result))
            elif elements[1] == "-":
                result = elements[0] - elements[2]
                self.result_label.setText(str(result))
            elif elements[1] == "*":
                result = elements[0] * elements[2]
                self.result_label.setText(str(result))
            elif elements[1] == "/":
                if elements[2] <= 0:
                    self.result_label.setText("0")
                else:
                    result = elements[0] / elements[2]
                    self.result_label.setText(str(result))
            self.multiply.setDisabled(False)
            self.division.setDisabled(False)
            self.addition.setDisabled(False)
            self.substraction.setDisabled(False)
        else: 
            pass
        
class Btn(QPushButton):
     def __init__(self,texte:str):
        super().__init__()
        self.texte = texte
        self.setText(self.texte)
        self.setFont(QFont("Arial Black",10,QFont.Bold))
        self.setStyleSheet("""
                        QPushButton{
                             background-color: #5c5c5c;
                             border-radius: 15%;
                             color: rgb(255,255,255);
                             }
                        QPushButton:hover{
                             background-color: #6d6e6d;
                             border-radius: 15px;
                             }
                             """)
        self.setMinimumSize(100,100)
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setMaximumWidth(500)
    win.setMaximumHeight(700)
    win.setCentralWidget(Main_Interface())
    with open("style.css") as style:
            win.setStyleSheet(style.read())
            style.close()
    win.show()
    sys.exit(app.exec())