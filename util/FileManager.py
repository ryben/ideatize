import os


def load_data_json(filename: str) -> str:
    # Read from file
    return read_file(os.path.join(os.getcwd(), filename))


def read_file(filepath: str) -> str:
    f = open(filepath, "r")
    content = f.read()
    f.close()
    return content


def write_file(filename: str, content: str):
    workspace_folder = os.path.join(os.getcwd(), "workspace")

    if not os.path.exists(workspace_folder):
        os.mkdir(workspace_folder)

    filepath = os.path.join(workspace_folder, f"{filename}.log")

    f = open(filepath, "w")
    f.write(content)
    f.close()
