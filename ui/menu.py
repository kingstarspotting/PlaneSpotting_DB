from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QFrame
from PyQt5.QtCore import QRect, QPropertyAnimation, Qt, QEasingCurve, QSize
from PyQt5.QtGui import QIcon, QPixmap

class Menu(QWidget):
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
        self.toggle_button.setIcon(QIcon("media\\img\\Home_sombre.png"))
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
        self.button1 = QPushButton("Option 1", self.menu)
        self.button2 = QPushButton("Option 2", self.menu)
        self.button3 = QPushButton("Option 3", self.menu)
        
        # Appliquer le style sans gras pour les boutons du menu
        button_style = """
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
        """
        self.button1.setStyleSheet(button_style)
        self.button2.setStyleSheet(button_style)
        self.button3.setStyleSheet(button_style)
        
        # Ajouter les boutons au layout vertical
        self.menu_layout.addWidget(self.button1)
        self.menu_layout.addWidget(self.button2)
        self.menu_layout.addWidget(self.button3)
        
        # Connecter les signaux clicked des boutons à leurs fonctions respectives
        self.button1.clicked.connect(lambda: self.on_button_clicked("Option 1"))
        self.button2.clicked.connect(lambda: self.on_button_clicked("Option 2"))
        self.button3.clicked.connect(lambda: self.on_button_clicked("Option 3"))
        
        self.toggle_button.clicked.connect(self.toggle_menu)
        
        self.setGeometry(0, 0, 160, parent.height())

    def resizeEvent(self, event):
        super().resizeEvent(event)
        # Redimensionner le menu en fonction de la hauteur de la fenêtre
        self.menu.setGeometry(0, 0, self.menu.width(), self.height())
    
    def toggle_menu(self):
        if self.menu.width() == 160:
            end_rect_menu = QRect(0, 0, 0, self.height())
        else:
            end_rect_menu = QRect(0, 0, 160, self.height())
        
        self.animation.setStartValue(self.menu.geometry())
        self.animation.setEndValue(end_rect_menu)
        self.animation.start()
    
    def on_button_clicked(self, option):
        print(f"Option '{option}' clicked!")
