import sys
from settings_functions import get_color
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QStyleFactory, QWidget, QVBoxLayout
from PyQt5.QtGui import QColor, QPalette
from ui.custom_widget import bouton_test

colors = get_color()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.showMaximized()
        
        # Thème de couleur
        QApplication.setStyle(QStyleFactory.create('Fusion'))
        app.setPalette(QPalette(QColor(colors[1]), QColor(colors[0])))

        # Crée un widget central et un layout
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        
        test = bouton_test


        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())