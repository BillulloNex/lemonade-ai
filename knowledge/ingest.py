def read_txt(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()