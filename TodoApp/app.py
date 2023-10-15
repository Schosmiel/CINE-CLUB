# Import necessary modules from PySide6 and sys
from PySide6 import QtWidgets, QtCore
import sys
# Import functions and classes from the 'movie' module
from movie import get_movies
from movie import Movie

# Define a class for the main application window
class App(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ciné Club")
        self.setup_ui()
        self.setup_connections()
        self.populate_movies()  

    # Set up the user interface (UI) for the application
    def setup_ui(self):
        self.main_layout = QtWidgets.QVBoxLayout(self)

        # Create a QLineEdit widget for entering movie titles
        self.le_moviesTitle = QtWidgets.QLineEdit()
        # Create a QPushButton widget for adding movies
        self.btn_addMovie = QtWidgets.QPushButton("Add a Movie")
        # Create a QListWidget for displaying the list of movies
        self.lw_movies = QtWidgets.QListWidget()
        # Set the selection mode for the QListWidget
        self.lw_movies.setSelectionMode(QtWidgets.QListWidget.ExtendedSelection)
        # Create a QPushButton widget for removing selected movies
        self.btn_removeMovie = QtWidgets.QPushButton("Remove Selected Movie(s)")

        # Add the widgets to the main layout
        self.main_layout.addWidget(self.le_moviesTitle)
        self.main_layout.addWidget(self.btn_addMovie)
        self.main_layout.addWidget(self.lw_movies)
        self.main_layout.addWidget(self.btn_removeMovie)

    # Set up signal connections for the UI components
    def setup_connections(self):
        # Connect the "Add a Movie" button click event to the 'add_movie' method
        self.btn_addMovie.clicked.connect(self.add_movie) 
        # Connect the "Remove Selected Movie(s)" button click event to the 'remove_movie' method
        self.btn_removeMovie.clicked.connect(self.remove_movie)
        # Connect the return key press event in the QLineEdit to the 'add_movie' method
        self.le_moviesTitle.returnPressed.connect(self.add_movie)

    # Populate the QListWidget with movies from the 'movie' module
    def populate_movies(self):
        movies = get_movies()
        for movie in movies:
            lw_item = QtWidgets.QListWidgetItem(movie.title)
            lw_item.setData(QtCore.Qt.UserRole, movie)
            self.lw_movies.addItem(lw_item)

    # Method for adding a movie
    def add_movie(self):
        # Get the movie title from the QLineEdit
        movie_title = self.le_moviesTitle.text()
        if not movie_title:
            return False
        # Create a Movie object with the entered title
        movie = Movie(title=movie_title)
        # Add the movie to the movie list and get the result
        result = movie.add_to_movies()
        if result:
            lw_item = QtWidgets.QListWidgetItem(movie.title)
            lw_item.setData(QtCore.Qt.UserRole, movie)
            self.lw_movies.addItem(lw_item)
        # Clear the text in the QLineEdit
        self.le_moviesTitle.setText("")

    # Method for removing selected movies
    def remove_movie(self):
        for selected_items in self.lw_movies.selectedItems():
            movie = selected_items.data(QtCore.Qt.UserRole)
            movie.remove_from_movie()
            self.lw_movies.takeItem(self.lw_movies.row(selected_items))

# Create a QApplication instance
app = QtWidgets.QApplication([])

# Create an instance of the App class
win = App()

# Show the application window
win.show()

# Run the application event loop
sys.exit(app.exec())
