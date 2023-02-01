import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, \
    QGridLayout, QLineEdit, QSizePolicy

class Calculadora(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Calculadora") 
        self.setFixedSize(400, 400)
        
        self.cw = QWidget()
        self.grid = QGridLayout(self.cw)

        self.display = QLineEdit()
        self.grid.addWidget(self.display, 0, 0, 1, 5)
        self.display.setDisabled(True)
        self.display.setStyleSheet('*{background-color: #fff; color: #000; font-size: 30px;}')

        self.display.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)

        self.add_btn(QPushButton('7'), 1, 0, 1, 1)
        self.add_btn(QPushButton('8'), 1, 1, 1, 1)
        self.add_btn(QPushButton('9'), 1, 2, 1, 1)
        self.add_btn(QPushButton('+'), 1, 3, 1, 1)
        self.add_btn(QPushButton('c'), 1, 4, 1, 1, 
                        lambda: self.display.setText(""),
                        "background: #D93654; color: #FFF; font-weight: 700;"
                    )

        self.add_btn(QPushButton('4'), 2, 0, 1, 1)
        self.add_btn(QPushButton('5'), 2, 1, 1, 1)
        self.add_btn(QPushButton('6'), 2, 2, 1, 1)
        self.add_btn(QPushButton('-'), 2, 3, 1, 1)
        self.add_btn(QPushButton('<-'), 2, 4, 1, 1, 
                        lambda: self.display.setText(self.display.text()[:-1]),
                        "background: #F26B8F; color: #FFF; font-weight: 700;"
                    )

        self.add_btn(QPushButton('1'), 3, 0, 1, 1)
        self.add_btn(QPushButton('2'), 3, 1, 1, 1)
        self.add_btn(QPushButton('3'), 3, 2, 1, 1)
        self.add_btn(QPushButton('/'), 3, 3, 1, 1)
        # self.add_btn(QPushButton(''), 3, 4, 1, 1)

        self.add_btn(QPushButton('.'), 4, 0, 1, 1)
        self.add_btn(QPushButton('0'), 4, 1, 1, 1)
        self.add_btn(QPushButton(''), 4, 2, 1, 1)
        self.add_btn(QPushButton('*'), 4, 3, 1, 1)
        self.add_btn(QPushButton('='), 3, 4, 2, 1,
                        self.eval_igual,
                        "background: #6B98BF; color: #FFF; font-weight: 700;"
                    )

        self.setCentralWidget(self.cw)

    def eval_igual(self):
        try:
            self.display.setText(str(eval(self.display.text())))
        except Exception as e:
            self.display.setText("Conta Inválida")

    def add_btn(self, btn: QPushButton, l, c, rp, cp, func=None, style=None):
        self.grid.addWidget(btn, l, c, rp, cp)

        if not func:
            btn.clicked.connect(lambda: self.display.setText(self.display.text() + btn.text()))
        else:
            btn.clicked.connect(func)

        if style:
            btn.setStyleSheet(style)
            
        btn.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)


if __name__ == "__main__":
    qt = QApplication(sys.argv);
    app = Calculadora()
    app.show()
    qt.exec()