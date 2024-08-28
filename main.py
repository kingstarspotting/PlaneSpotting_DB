import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtCore import Qt
from ui.menu import Menu
from Functions.settings_functions import get_settings

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
        self.adjust_title_position()  # Positionner le titre initialement

        self.showMaximized()  # Maximiser la fenêtre dès le lancement
        self.show()
    
    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.adjust_title_position()

    def adjust_title_position(self):
        # Récupérer la taille du menu depuis les paramètres
        menu_size = float(get_settings("settings", "menu_size"))
        menu_width = int(self.width() * menu_size)
        
        # Calculer la largeur disponible après le menu
        available_width = self.width() - menu_width
        
        # Ajuster la position et la taille du label "Bonjour"
        self.title_label.setGeometry(menu_width, 50, available_width, 50)  # Centrer le texte horizontalement dans l'espace restant

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
