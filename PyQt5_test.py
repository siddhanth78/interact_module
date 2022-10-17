import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from pyQt5_testUI import Ui_MainWindow

class window(QMainWindow):

    def __init__(self, parent = None):
    
        super(window, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.pushButton.clicked.connect(self.changeLabel)
        
        
    def changeLabel(self):
        self.ui.label.setText("NUT")
        
def main():
    app = QApplication(sys.argv)
    ex = window()
    ex.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
        main()