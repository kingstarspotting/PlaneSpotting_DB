from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QFrame
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QIcon

# Bibliothèque de langue
from Functions.languages import get_text

class Menu(QWidget):
    menu_toggled = pyqtSignal(bool)  # Signal pour notifier le redimensionnement

    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.setStyleSheet("""
            QPushButton {
                background-color: #303030;
                color: #ffffff;
                border: none;
                border-radius: 5px;
                padding: 5px 10px; /* Ajuster le padding */
                margin: 0px;
                font-size: 14px;
                text-align: center;
                height: 40px;  /* Hauteur fixe */
                line-height: 40px; /* Alignement vertical du texte */
            }
            QPushButton:hover {
                background-color: #4d4d4d;
            }
            QFrame {
                background-color: #313131;
            }
        """)

        self.menu = QFrame(self)
        self.menu.setGeometry(0, 0, 160, self.height())  # Toujours visible (largeur 160)
        self.menu.setStyleSheet("background-color: #313131;")
        
        # Layout vertical pour le menu
        self.menu_layout = QVBoxLayout(self.menu)
        self.menu_layout.setAlignment(Qt.AlignTop)  # Aligner les widgets en haut
        self.menu_layout.setContentsMargins(10, 20, 10, 10)  # Marge réduite autour du layout
        
        # Ajouter les boutons au menu
        self.button_home = QPushButton(get_text("menu", "home"), self.menu)
        self.button_spotting = QPushButton(get_text("menu", "spotting"), self.menu)
        self.button_vol = QPushButton(get_text("menu", "flight"), self.menu)
        self.button_stats = QPushButton(get_text("menu", "stats"), self.menu)
        self.button_parametre = QPushButton(get_text("menu", "settings"), self.menu)
        
        # Appliquer le style sans gras pour les boutons du menu
        button_style = """
            QPushButton {
                background-color: #303030;
                color: #ffffff;
                border: none;
                border-radius: 5px;
                padding: 5px 10px;
                margin: 0px;
                font-size: 14px;
                text-align: center;
                height: 40px;
                line-height: 40px;
            }
            QPushButton:hover {
                background-color: #4d4d4d;
            }
        """
        self.button_home.setStyleSheet(button_style)
        self.button_spotting.setStyleSheet(button_style)
        self.button_vol.setStyleSheet(button_style)
        self.button_stats.setStyleSheet(button_style)
        self.button_parametre.setStyleSheet(button_style)
        
        # Ajouter les boutons au layout vertical
        self.menu_layout.addWidget(self.button_home)
        self.menu_layout.addWidget(self.button_spotting)
        self.menu_layout.addWidget(self.button_vol)
        self.menu_layout.addWidget(self.button_stats)
        self.menu_layout.addWidget(self.button_parametre)
        
        # Connecter les signaux clicked des boutons à leurs fonctions respectives
        self.button_home.clicked.connect(lambda: self.open_home())
        self.button_spotting.clicked.connect(lambda: self.open_spotting())
        self.button_vol.clicked.connect(lambda: self.open_flight())
        self.button_stats.clicked.connect(lambda: self.open_stats())
        self.button_parametre.clicked.connect(lambda: self.open_settings())
        
        self.setGeometry(0, 0, 160, parent.height())

    def resizeEvent(self, event):
        super().resizeEvent(event)
        # Redimensionner le menu en fonction de la hauteur de la fenêtre
        self.menu.setGeometry(0, 0, self.menu.width(), self.height())
    
    def open_spotting(self):
        print("Spotting ouvert")
    
    def open_flight(self):
        print("Vols ouvert")
    
    def open_settings(self):
        print("Paramètres ouverts")
    
    def open_stats(self):
        print("Statistiques ouverts")
    
    def open_home(self):
        print("Accueil ouvert")
