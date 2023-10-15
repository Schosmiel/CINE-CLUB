# Import the 'os' module for working with the operating system.
import os
# Import the 'json' module for JSON data handling.
import json
# Import the 'logging' module for logging messages and warnings.
import logging

# Get the current directory of the script file.
CUR_DIR = os.path.dirname(__file__)
# Create the path to the 'movie.json' data file within the 'data' directory.
DATA_FILE = os.path.join(CUR_DIR, "data", "movie.json")

# Define a function to get a list of movies from the JSON data file.
def get_movies():
    # Open the data file for reading.
    with open(DATA_FILE, "r") as f:
        # Load the movie titles from the JSON file.
        movies_title = json.load(f)
    # Create a list of Movie objects from the titles.
    movies = [Movie(movie_title) for movie_title in movies_title]
    # Return the list of Movie objects.
    return movies

# Define a class 'Movie' to represent a movie.
class Movie:
    # Initialize a Movie object with a title.
    def __init__(self, title):
        # Store the movie title, capitalized.
        self.title = title.title()

    # Define a string representation for the Movie object.
    def __str__(self):
        return self.title
    
    # Define a method to get the list of movies from the JSON data file.
    def _get_movies(self):
        # Open the data file for reading.
        with open(DATA_FILE, "r") as f:
            return json.load(f)

    # Define a method to write a list of movies to the JSON data file.
    def _write_movies(self, movies):
        # Open the data file for writing.
        with open(DATA_FILE, "w") as f:
            # Write the movies to the JSON file with indentation.
            json.dump(movies, f, indent=4) 

    # Define a method to add the movie to the list of movies.
    def add_to_movies(self):
        # Get the list of movies from the data file.
        movies = self._get_movies()
        # Check if the movie is not already in the list.
        if self.title not in movies:
            # If not, add the movie to the list and write it back to the file.
            movies.append(self.title)
            self._write_movies(movies)
            return True
        else: 
            # Log a warning if the movie is already in the list.
            logging.warning(f"The movie {self.title} is already registered.")  
            return False     
        
    # Define a method to remove the movie from the list of movies.
    def remove_from_movie(self):
        # Get the list of movies from the data file.
        movies = self._get_movies()
        # Check if the movie is in the list.
        if self.title in movies:
            # If it is, remove the movie from the list and write it back to the file.
            movies.remove(self.title)
            self._write_movies(movies)

# Check if this script is the main module.
if __name__ == "__main__":
    # Get the list of movies using the 'get_movies' function.
    movies = get_movies()
    # Print the list of Movie objects.
    print(movies)
