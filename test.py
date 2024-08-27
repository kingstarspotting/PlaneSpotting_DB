import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QStackedWidget

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle('Navigation entre pages')
        
        # Création du QStackedWidget
        self.stacked_widget = QStackedWidget()
        
        # Première page
        self.page1 = QWidget()
        layout1 = QVBoxLayout()
        label1 = QLabel('Page 1')
        layout1.addWidget(label1)
        button1 = QPushButton('Aller à la page 2')
        button1.clicked.connect(self.showPage2)
        layout1.addWidget(button1)
        self.page1.setLayout(layout1)
        
        # Deuxième page
        self.page2 = QWidget()
        layout2 = QVBoxLayout()
        label2 = QLabel('Page 2')
        layout2.addWidget(label2)
        button2 = QPushButton('Retour à la page 1')
        button2.clicked.connect(self.showPage1)
        layout2.addWidget(button2)
        self.page2.setLayout(layout2)
        
        # Ajouter les pages au QStackedWidget
        self.stacked_widget.addWidget(self.page1)
        self.stacked_widget.addWidget(self.page2)
        
        # Layout principal pour la fenêtre
        layout = QVBoxLayout()
        layout.addWidget(self.stacked_widget)
        self.setLayout(layout)
        
    def showPage1(self):
        self.stacked_widget.setCurrentIndex(0)
        
    def showPage2(self):
        self.stacked_widget.setCurrentIndex(1)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
