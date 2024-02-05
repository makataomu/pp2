def filter_high_rated(movies, min_rating=5.5):
    return [movie['name'] for movie in movies if movie['imdb'] > min_rating]