# CINE-CLUB

This is a simple movie management application, where you can add and remove movie titles to your movie list.

# Prerequisites

Before running this application, make sure you have the following installed:

- Python 3
- PySide6 library (install using pip install PySide6)

  # Code Explanation

movie.py
This script defines a class Movie and a few methods for managing a list of movies stored in a JSON file.

1 - Import necessary modules (os, json, and logging).

2 - Set the data file path for movies.

3 - Define a function get_movies to read and return a list of movies from the JSON data file.

4 - Define a class Movie to represent a movie and its methods to add and remove movies from the list.

5 - Check if this script is the main module and if so, get the list of movies and print them.

app.py

This script is the main application. It uses the PySide6 library to create a GUI for managing movies.

1 - Import necessary modules (PySide6, sys, get_movies, and Movie).
2 - Define a class App for the main application window.
3 - Set up the user interface (UI) with input fields for movie titles and buttons for adding and removing movies.
4 - Set up signal connections for UI components.
5 - Populate the movie list from the data file.
6 - Implement methods for adding and removing movies.
7 - Create a QApplication instance and the main application window.
8 - Show the application window and run the event loop.


# Running the Application

py app.py




