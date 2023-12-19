import os


def load_data_json(filename: str) -> str:
    # Read from file
    return read_file(os.path.join(os.getcwd(), filename))


def read_file(filepath: str) -> str:
    f = open(filepath, "r")
    content = f.read()
    f.close()
    return content
