__author__ = 'twi'

import interface04_ui
from PyQt4 import QtGui
import sys

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = interface04_ui.Ui_MainWindow()
    ex.show()
    sys.exit(app.exec_())


