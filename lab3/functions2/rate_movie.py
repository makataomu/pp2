def rate_movie(movie_name, movies):
    for movie in movies:
        if movie['name'] == movie_name:
            return movie['imdb'] > 5.5
    return 'Movie not found'