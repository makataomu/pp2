def compute_average_imdb(list_of_movies, movies):
    ratings = [movie['imdb'] for movie in movies if movie['name'] in list_of_movies]
    sum = 0
    for r in ratings:
        sum += r
    return sum / len(ratings)