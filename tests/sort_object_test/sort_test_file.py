import pytest
from code_challenges.sort.sort_object.sort_object_file import Movie,sort_by_title,sort_by_year,sorted_by_title,sorted_by_year
# Tests for sort_by_year function
def test_sort_by_year():
    movies = [
        Movie("The Dark Knight", 2008, ["Action", "Crime", "Drama"]),
        Movie("An Inception", 2010, ["Action", "Adventure", "Sci-Fi"]),
        Movie("A Beautiful Mind", 2001, ["Biography", "Drama"]),
        Movie("Avengers: Endgame", 2019, ["Action", "Adventure", "Drama"]),
        Movie("Joker", 2019, ["Crime", "Drama", "Thriller"]),
    ]

    sorted_movies = sort_by_year(movies)
    assert sorted_movies[0].title == "Joker"
    assert sorted_movies[1].title == "Avengers: Endgame"
    assert sorted_movies[2].title == "An Inception"
    assert sorted_movies[3].title == "The Dark Knight"
    assert sorted_movies[4].title == "A Beautiful Mind"


# Tests for sort_by_title function
def test_sort_by_title():
    movies = [
        Movie("The Dark Knight", 2008, ["Action", "Crime", "Drama"]),
        Movie("An Inception", 2010, ["Action", "Adventure", "Sci-Fi"]),
        Movie("A Beautiful Mind", 2001, ["Biography", "Drama"]),
        Movie("Avengers: Endgame", 2019, ["Action", "Adventure", "Drama"]),
        Movie("Joker", 2019, ["Crime", "Drama", "Thriller"]),
    ]

    sorted_movies = sort_by_title(movies)
    assert sorted_movies[0].title == "Avengers: Endgame"
    assert sorted_movies[1].title == "An Inception"
    assert sorted_movies[2].title == "A Beautiful Mind"
    assert sorted_movies[3].title == "The Dark Knight"
    assert sorted_movies[4].title == "Joker"


# Pytest test functions
def test_sort_by_year():
    movies = [
        Movie("The Dark Knight", 2008, ["Action", "Crime", "Drama"]),
        Movie("An Inception", 2010, ["Action", "Adventure", "Sci-Fi"]),
        Movie("A Beautiful Mind", 2001, ["Biography", "Drama"]),
        Movie("Avengers: Endgame", 2019, ["Action", "Adventure", "Drama"]),
        Movie("Joker", 2019, ["Crime", "Drama", "Thriller"]),
    ]

    sorted_movies = sort_by_year(movies)
    assert sorted_movies[0].title == "Joker"
    assert sorted_movies[1].title == "Avengers: Endgame"
