from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QFrame
from PyQt5.QtCore import QRect, QPropertyAnimation, Qt, QEasingCurve, QSize, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap

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
                padding: 10px;
                text-align: center;
                margin: 5px; /* Marge autour des boutons */
                font-size: 14px; /* Taille de la police */
            }
            QPushButton:hover {
                background-color: #4d4d4d;
            }
            QFrame {
                background-color: #313131;
            }
        """)
        
        self.toggle_button = QPushButton(self)
        self.toggle_button.setFixedSize(55, 55)
        self.toggle_button.setIcon(QIcon("media\\img\\menu_sombre.png"))
        self.toggle_button.setIconSize(QSize(25, 25))
        self.toggle_button.setStyleSheet("""
            QPushButton {
                background-color: #303030;
                color: #ffffff;
                border: none;
                border-radius: 5px;
                text-align: center;
                font-size: 20px;  # Taille de la police pour le bouton principal
            }
            QPushButton:hover {
                background-color: #303030;  # Ne pas changer la couleur au survol
            }
            QPushButton:focus {
                border: none;  # Ne pas afficher de bordure au focus
            }
        """)
        
        self.menu = QFrame(self)
        self.menu.setGeometry(0, 0, 0, self.height())  # Initialement caché (largeur 0)
        self.menu.setStyleSheet("background-color: #313131;")
        
        self.animation = QPropertyAnimation(self.menu, b"geometry")
        self.animation.setDuration(200)  # Durée réduite de l'animation
        self.animation.setEasingCurve(QEasingCurve.OutQuad)  # Courbe d'accélération pour une animation fluide
        
        # Layout vertical pour le menu
        self.menu_layout = QVBoxLayout(self.menu)
        self.menu_layout.setAlignment(Qt.AlignTop)  # Aligner les widgets en haut
        self.menu_layout.setContentsMargins(10, 70, 10, 10)  # Marge autour du layout
        
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
                padding: 10px;
                text-align: center;
                margin: 5px;
                font-size: 14px;
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
        
        self.toggle_button.clicked.connect(self.toggle_menu)
        
        self.setGeometry(0, 0, 160, parent.height())

    def resizeEvent(self, event):
        super().resizeEvent(event)
        # Redimensionner le menu en fonction de la hauteur de la fenêtre
        self.menu.setGeometry(0, 0, self.menu.width(), self.height())
    
    def toggle_menu(self):
        if self.menu.width() == 160:
            end_rect_menu = QRect(0, 0, 0, self.height())
            menu_open = False
        else:
            end_rect_menu = QRect(0, 0, 160, self.height())
            menu_open = True
        
        self.animation.setStartValue(self.menu.geometry())
        self.animation.setEndValue(end_rect_menu)
        self.animation.start()

        self.menu_toggled.emit(menu_open)  # Emettre le signal avec l'état du menu
    
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
