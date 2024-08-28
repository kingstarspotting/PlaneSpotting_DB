from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Taille de la Fenêtre")
        self.setGeometry(100, 100, 800, 600)  # Position (x, y) et taille (largeur, hauteur)
        
        # Label pour afficher la taille
        self.size_label = QLabel(self)
        self.size_label.setGeometry(50, 50, 300, 50)  # Position et taille du label
        self.update_size_label()  # Mettre à jour le texte du label
        
        self.show()
        
    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.update_size_label()  # Mettre à jour la taille affichée lors du redimensionnement

    def update_size_label(self):
        # Obtenir la taille de la fenêtre
        width = self.width()
        height = self.height()
        
        # Afficher la taille dans le label
        self.size_label.setText(f"Largeur : {width}, Hauteur : {height}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
