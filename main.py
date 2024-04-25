import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QStyleFactory
from PyQt5.QtGui import QColor, QPalette

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set the window to be maximized
        self.showMaximized()

        # Set the dark theme
        QApplication.setStyle(QStyleFactory.create('Fusion'))
        app.setPalette(QPalette(QColor(53, 53, 53), QColor(85, 85, 85)))
        app.setStyleSheet('QToolTip { color: #ffffff; background-color: #2a82da; border: 1px solid white; }')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())