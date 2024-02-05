def filter_by_category(category, movies):
    return [movie['name'] for movie in movies if movie['category'] == category]