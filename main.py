import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtCore import Qt
from ui.menu import Menu
from Functions.languages import get_text

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Aero Database")
        
        # Appliquer un style sombre à l'application
        self.setStyleSheet("""
            QMainWindow {
                background-color: #191919;
                color: #ffffff;
            }
            QLabel {
                font-size: 36px;
                font-weight: bold;
                color: #ffffff;
            }
        """)
        
        self.central_widget = Menu(self)
        self.setCentralWidget(self.central_widget)
        
        # Ajouter le titre "Bonjour"
        self.title_label = QLabel("Bonjour", self)
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.setGeometry(0, 50, self.width(), 50)  # Ajustez la position et la taille selon vos besoins

        self.showMaximized()  # Maximiser la fenêtre dès le lancement
        self.show()

    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
