def load_data(filename: str):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return file.readlines()
    except FileNotFoundError:
        return "File not found"
