from filter_category import filter_by_category
from average_imdb import compute_average_imdb

def compute_average_imdb_category(category, movies):
    list_of_movies = filter_by_category(category, movies)
    return compute_average_imdb(list_of_movies, movies)  