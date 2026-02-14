import files_utilities

def get_cats_info(path):
    cats_data = files_utilities.load_data(path)

    return get_data(cats_data)

def get_data(data):
    cats_data = []
    print(data)
    for cat in data:
        cat_info = [param.strip() for param in cat.split(',') if param.strip()]
        cats_data.append({'id': cat_info[0], 'name': cat_info[1], 'age': cat_info[2]})

    return cats_data
