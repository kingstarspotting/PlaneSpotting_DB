from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QStyleFactory, QWidget, QVBoxLayout
from settings_functions import get_color

colors = get_color()

class bouton_test:
    def __init__(self, ct_widget):
        layout = QVBoxLayout(ct_widget)
        # Crée un bouton avec la couleur colors[1]
        self.button = QPushButton("Cliquez-moi", self)
        self.button.setStyleSheet(f"background-color: {colors[2]}; color: {colors[3]};")

        
        # Ajoute le bouton au layout
        layout.addWidget(self.button)