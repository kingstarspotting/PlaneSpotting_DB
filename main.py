import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import Qt
from ui.menu import Menu

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Menu dépliable latéral")
        
        # Appliquer un style sombre à l'application
        self.setStyleSheet("""
            QMainWindow {
                background-color: #191919;
                color: #ffffff;
            }
        """)
        
        self.central_widget = Menu(self)
        self.setCentralWidget(self.central_widget)
        
        self.showMaximized()  # Maximiser la fenêtre dès le lancement
        self.show()

    def resizeEvent(self, event):
        super().resizeEvent(event)
        # Repositionner le bouton lorsque la fenêtre est redimensionnée
        self.central_widget.toggle_button.raise_()
        self.central_widget.toggle_button.move(10, 10)
        # Redimensionner le menu en fonction de la hauteur de la fenêtre
        self.central_widget.menu.setGeometry(0, 0, self.central_widget.menu.width(), self.height())
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
