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

        # Connecter le signal menu_toggled à une méthode pour redimensionner la fenêtre
        self.central_widget.menu_toggled.connect(self.resize_window)

    def resize_window(self, menu_open):
        if menu_open:
            self.resize(self.width() + 160, self.height())
        else:
            self.resize(self.width() - 160, self.height())

    def resizeEvent(self, event):
        super().resizeEvent(event)
        # Repositionner le bouton lorsque la fenêtre est redimensionnée
        self.central_widget.toggle_button.raise_()
        self.central_widget.toggle_button.move(10, 10)
        # Redimensionner le menu en fonction de la hauteur de la fenêtre
        self.central_widget.menu.setGeometry(0, 0, self.central_widget.menu.width(), self.height())
        # Repositionner le titre lorsque la fenêtre est redimensionnée
        self.title_label.setGeometry(0, 50, self.width(), 50)

    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
