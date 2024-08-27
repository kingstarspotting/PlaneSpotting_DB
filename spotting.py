import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QTableWidget, QTableWidgetItem, QHeaderView
from PyQt5.QtCore import Qt
from ui.menu import Menu
from Functions.languages import get_text
from Functions.settings_functions import get_settings, get_database

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle(get_settings("settings", "title"))

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
            QTableWidget {
                background-color: #2e2e2e;
                color: #ffffff;
                gridline-color: #404040;
                selection-background-color: #404040;
                selection-color: #ffffff;
            }
            QTableWidget::item {
                border: 1px solid #404040;
                padding: 5px;
            }
            QHeaderView::section {
                background-color: #2e2e2e;
                color: #ffffff;
                padding: 5px;
                border: 1px solid #404040;
            }
            QTableCornerButton::section {
                background-color: #2e2e2e;
                border: 1px solid #404040;
            }
        """)

        self.central_widget = Menu(self)
        self.setCentralWidget(self.central_widget)

        # Ajouter le titre "Aerolog"
        self.title_label = QLabel("Aerolog", self)
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.setGeometry(0, 50, self.width(), 50)  # Ajustez la position et la taille selon vos besoins

        # Ajouter le QTableWidget
        self.table_widget = QTableWidget(self)
        self.table_widget.setGeometry(50, 150, self.width() - 100, self.height() - 200)  # Ajuster la taille et la position selon vos besoins

        self.load_data()  # Charger les données de la base de données

        self.showMaximized()  # Maximiser la fenêtre dès le lancement
        self.show()

        # Connecter le signal menu_toggled à une méthode pour redimensionner la fenêtre
        self.central_widget.menu_toggled.connect(self.resize_window)

    def load_data(self):
        # Obtenir le chemin de la base de données en utilisant get_database
        database_path = get_database()  # Appel de get_database sans paramètres
        connection = sqlite3.connect(database_path)
        cursor = connection.cursor()

        # Requête pour récupérer les données
        cursor.execute("SELECT * FROM Spotting")  # Utiliser le nom correct de la table
        rows = cursor.fetchall()

        # Définir le nombre de colonnes
        self.table_widget.setColumnCount(len(rows[0]) if rows else 0)
        self.table_widget.setRowCount(len(rows))

        # Définir les en-têtes de colonnes
        self.table_widget.setHorizontalHeaderLabels([
            'Id_spott', 'Immatriculation', 'Modele', 'Msn', 'Compagnie',
            'Militaire', 'Service', 'Livree', 'Date', 'Aeroport', 
            'Catalogue', 'Commentaire', 'Achievement', 'Image', 
            'Nbr_Immat', 'Nbr_Msn', 'Fav'
        ])

        # Remplir le QTableWidget avec les données
        for row_num, row_data in enumerate(rows):
            for col_num, data in enumerate(row_data):
                item = QTableWidgetItem(str(data))
                item.setFlags(item.flags() & ~Qt.ItemIsEditable)  # Rendre la cellule non éditable
                self.table_widget.setItem(row_num, col_num, item)

        # Ajuster la taille des colonnes
        self.adjust_column_sizes()
        # Ajuster la taille des lignes
        self.adjust_row_heights()

        # Fermer la connexion
        connection.close()

    def adjust_column_sizes(self):
        # Redimensionner les colonnes pour occuper uniformément l'espace disponible
        total_width = self.table_widget.width()
        num_columns = self.table_widget.columnCount()
        if num_columns > 0:
            column_width = total_width // num_columns
            for col in range(num_columns):
                self.table_widget.setColumnWidth(col, column_width)
        # Ajuster la largeur des colonnes pour le contenu restant
        self.table_widget.resizeColumnsToContents()

    def adjust_row_heights(self):
        # Ajuster la hauteur des lignes pour utiliser tout l'espace vertical disponible
        total_height = self.table_widget.height()
        num_rows = self.table_widget.rowCount()
        if num_rows > 0:
            row_height = total_height // num_rows
            self.table_widget.setRowHeight(0, row_height)  # Appliquer la hauteur aux lignes
            for row in range(num_rows):
                self.table_widget.setRowHeight(row, row_height)
        # Ajuster la hauteur des lignes en fonction du contenu
        self.table_widget.resizeRowsToContents()

    def resize_window(self, menu_open):
        if menu_open:
            # Ajouter de l'espace pour le menu sur le côté gauche
            self.resize(self.width() + 160, self.height())
        else:
            # Réduire l'espace pour le menu
            self.resize(self.width() - 160, self.height())

    def resizeEvent(self, event):
        super().resizeEvent(event)
        # Repositionner le bouton lorsque la fenêtre est redimensionnée
        self.central_widget.toggle_button.raise_()
        self.central_widget.toggle_button.move(10, 10)
        # Redimensionner le menu en fonction de la hauteur de la fenêtre
        self.central_widget.menu.setGeometry(0, 0, self.central_widget.menu.width(), self.height())
        # Repositionner le titre lorsque la fenêtre est redimensionnée
        self.title_label.setGeometry(0, 50, self.width(), 50)
        # Redimensionner le QTableWidget
        self.table_widget.setGeometry(50, 150, self.width() - 100, self.height() - 200)
        # Ajuster la taille des colonnes après le redimensionnement de la fenêtre
        self.adjust_column_sizes()
        # Ajuster la taille des lignes après le redimensionnement de la fenêtre
        self.adjust_row_heights()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
