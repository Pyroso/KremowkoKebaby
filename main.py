import sys
from itertools import count

from PyQt6.QtWidgets import QDialog, QApplication

from layout import Ui_Dialog

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.kremowkaSum.setReadOnly(True)
        self.ui.kebabSum.setReadOnly(True)
        self.ui.kremowkaPrice.textChanged.connect(self.kremowki_sum)
        self.ui.kremowka.valueChanged.connect(self.kremowki_sum)
        self.ui.kebabPrice.textChanged.connect(self.kebab_sum)
        self.ui.kebabSpin.valueChanged.connect(self.kebab_sum)

        self.show()



    def kremowki_sum(self):
        count = self.ui.kremowka.value()
        price = self.ui.kremowkaPrice.text()
        try:
            price = float(price)
        except ValueError:
            price = 0
        self.ui.kremowkaSum.setText(f'{price * count : .2f} zł')

    def kebab_sum(self):
        count = self.ui.kebabSpin.value()
        price = self.ui.kebabPrice.text()
        try:
            price = float(price)
        except ValueError:
            price = 0
        self.ui.kebabSum.setText(f'{price * count : .2f} zł')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyForm()
    sys.exit(app.exec())