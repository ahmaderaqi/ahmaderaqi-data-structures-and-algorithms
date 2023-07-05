class Movie:
    def __init__(self, title, year, genres):
        self.title = title
        self.year = year
        self.genres = genres


def sort_by_year(movies):
    sort = sorted(movies, key=lambda movie: movie.year, reverse=True)
    return sort


def sort_by_title(movies):
    def sort_key(movie):
        title = movie.title
        if title.startswith("A "):
            title = title[2:]
        elif title.startswith("An "):
            title = title[3:]
        elif title.startswith("The "):
            title = title[4:]
        return title

    sorted_movies = sorted(movies, key=sort_key)
    return sorted_movies


movies = [
    Movie("The Dark Knight", 2008, ["Action", "Crime", "Drama"]),
    Movie("An Inception", 2010, ["Action", "Adventure", "Sci-Fi"]),
    Movie("A Beautiful Mind", 2001, ["Biography", "Drama"]),
    Movie("Avengers: Endgame", 2019, ["Action", "Adventure", "Drama"]),
    Movie("Joker", 2019, ["Crime", "Drama", "Thriller"]),
]

sorted_by_year = sort_by_year(movies)
print("Sorted by year:")
for movie in sorted_by_year:
    print(f"{movie.title} ({movie.year})")
    
sorted_by_title = sort_by_title(movies)
print("\nSorted by title:")
for movie in sorted_by_title:
    print(movie.title)
