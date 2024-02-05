from movies import movies

from rate_movie import rate_movie
from filter_rating import filter_high_rated
from filter_category import filter_by_category
from average_imdb import compute_average_imdb
from average_imdb_category import compute_average_imdb_category


print(rate_movie('MF DOOM', movies))
print(rate_movie('Dark Knight', movies))

print(filter_high_rated(movies, min_rating=5.5))

print(filter_by_category(category='Romance', movies=movies))

print(compute_average_imdb(  list_of_movies=['Hitman', 'Dark Knight']
                           , movies=movies))

print(compute_average_imdb_category(category='Romance', movies=movies))
