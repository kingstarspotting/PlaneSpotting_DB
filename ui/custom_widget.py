import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QFrame
from PyQt5.QtCore import Qt, QPropertyAnimation, QRect

class menu:
    def __init__(self) -> None:
        # Créer et positionner le bouton en haut à gauche
        self.toggle_button = QPushButton("☰", self.central_widget)
        self.toggle_button.setFixedSize(50, 50)
        self.toggle_button.move(10, 10)  # Ajuster la position
        self.toggle_button.setStyleSheet("""
            QPushButton {
                background-color: #303030;
                color: #ffffff;
                border: none;
                border-radius: 5px;
                padding: 10px;
                text-align: center;
            }
            QPushButton:hover {
                background-color: #4d4d4d;
            }
        """)
        self.toggle_button.clicked.connect(self.toggle_menu)
        
        self.menu = QFrame(self.central_widget)
        self.menu.setGeometry(0, 0, 0, self.height())  # Initialement caché (largeur 0)
        self.menu.setStyleSheet("background-color: #313131;")
        
        self.animation = QPropertyAnimation(self.menu, b"geometry")
        self.animation.setDuration(200)  # Durée réduite de l'animation
        
        # Layout vertical pour le menu
        self.menu_layout = QVBoxLayout(self.menu)
        self.menu_layout.setAlignment(Qt.AlignTop)  # Aligner les widgets en haut
        self.menu_layout.setContentsMargins(10, 70, 10, 10)  # Marge autour du layout
        
        # Ajouter les boutons au menu
        self.button1 = QPushButton("Option 1", self.menu)
        self.button2 = QPushButton("Option 2", self.menu)
        self.button3 = QPushButton("Option 3", self.menu)
        
        # Appliquer le style aux boutons
        self.button1.setStyleSheet("""
            QPushButton {
                background-color: #303030;
                color: #ffffff;
                border: none;
                border-radius: 5px;
                padding: 10px;
                text-align: center;
                font-size: 14px; /* Augmenter la taille de la police */
            }
            QPushButton:hover {
                background-color: #4d4d4d;
            }
        """)
        self.button2.setStyleSheet("""
            QPushButton {
                background-color: #303030;
                color: #ffffff;
                border: none;
                border-radius: 5px;
                padding: 10px;
                text-align: center;
                font-size: 14px; /* Augmenter la taille de la police */
            }
            QPushButton:hover {
                background-color: #4d4d4d;
            }
        """)
        self.button3.setStyleSheet("""
            QPushButton {
                background-color: #303030;
                color: #ffffff;
                border: none;
                border-radius: 5px;
                padding: 10px;
                text-align: center;
                font-size: 14px; /* Augmenter la taille de la police */
            }
            QPushButton:hover {
                background-color: #4d4d4d;
            }
        """)
        
        # Ajouter les boutons au layout vertical
        self.menu_layout.addWidget(self.button1)
        self.menu_layout.addWidget(self.button2)
        self.menu_layout.addWidget(self.button3)
        
        # Connecter les signaux clicked des boutons à leurs fonctions respectives
        self.button1.clicked.connect(lambda: self.on_button_clicked("Option 1"))
        self.button2.clicked.connect(lambda: self.on_button_clicked("Option 2"))
        self.button3.clicked.connect(lambda: self.on_button_clicked("Option 3"))
        
        self.show()

    def resizeEvent(self, event):
        super().resizeEvent(event)
        # Repositionner le bouton lorsque la fenêtre est redimensionnée
        self.toggle_button.raise_()
        self.toggle_button.move(10, 10)
        # Redimensionner le menu en fonction de la hauteur de la fenêtre
        self.menu.setGeometry(0, 0, self.menu.width(), self.height())
    
    def toggle_menu(self):
        if self.menu.width() == 200:
            end_rect_menu = QRect(0, 0, 0, self.height())
            end_rect_button = QRect(10, 10, 50, 50)
        else:
            end_rect_menu = QRect(0, 0, 200, self.height())
            end_rect_button = QRect(210, 10, 50, 50)
        
        self.animation.setStartValue(self.menu.geometry())
        self.animation.setEndValue(end_rect_menu)
        self.animation.start()
        
        if self.menu.width() == 200:
            self.animation.finished.connect(lambda: self.menu.setVisible(False))
            self.toggle_button.setGeometry(end_rect_button)
        else:
            self.animation.finished.connect(lambda: self.menu.setVisible(True))
    
    def on_button_clicked(self, option):
        print(f"Option '{option}' clicked!")
