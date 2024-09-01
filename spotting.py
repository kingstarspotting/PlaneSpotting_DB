import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QHBoxLayout, QLabel
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtCore import Qt
from db_functions.spotting_db import Spotting_db
from ui.menu import Menu

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Spotting Database")
        
        self.table = QTableWidget()
        self.table.setColumnCount(15)
        self.table.setHorizontalHeaderLabels(["Immatriculation", "Modele", "Msn", "Compagnie", "Militaire", "Service", "Livree", "Date", "Aeroport", "Catalogue", "Commentaire", "Achievement", "Nbr_Immat", "Nbr_Msn", "Fav"])
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)  # Disable editing of table cells
        self.table.setSelectionBehavior(QTableWidget.SelectRows)  # Select entire row when a cell is clicked
        self.table.doubleClicked.connect(self.print_immatriculation)  # Connect the doubleClicked signal to the print_immatriculation method

        # Set the background color of the corner widget to match the background color of the table
        corner_widget = QLabel()
        corner_widget.setStyleSheet("background-color: #3c3f41;")
        self.table.setCornerWidget(corner_widget)

        self.db = Spotting_db()
        self.load_data()

        self.menu = Menu()

        layout = QHBoxLayout()
        layout.addWidget(self.menu)
        layout.addWidget(self.table)

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)

        self.setStyleSheet("""
            QMainWindow {
                background-color: #191919;
                color: #ffffff;
            }
            QTableWidget {
                background-color: #3c3f41;
                color: #ddd;
                border: none;
            }
            QTableWidget::item:selected {
                background-color: #4a86cf;
            }
            QHeaderView::section {
                background-color: #3c3f41;
                color: #ddd;
                border: none;
                padding: 5px;
            }
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
            QFrame {
                background-color: #313131;
            }
        """)

    def load_data(self):
        data = self.db.database_display()
        self.table.setRowCount(len(data))
        for i, row in enumerate(data):
            for j, item in enumerate(row):
                self.table.setItem(i, j, QTableWidgetItem(str(item)))

    def print_immatriculation(self):
        row = self.table.currentRow()
        immatriculation = self.table.item(row, 0).text()
        print(immatriculation)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
