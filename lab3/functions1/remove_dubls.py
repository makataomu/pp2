def remove_duplicates(array):

    unique_elements = []
    for item in array:
        if item not in unique_elements:
            unique_elements.append(item)

    return unique_elements