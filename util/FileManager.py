import os


def load_data_json(filename: str) -> str:
    # Read from file
    return read_file(os.path.join(os.getcwd(), filename))


def read_file(filepath: str) -> str:
    f = open(filepath, "r")
    content = f.read()
    f.close()
    return content


def read_file_from_workspace(filename: str):
    filepath = os.path.join(get_workspace_folder(), filename)
    return read_file(filepath)


def get_workspace_folder():
    return os.path.join(os.getcwd(), "workspace")


def write_file(filename: str, content: str):
    workspace_folder = get_workspace_folder()

    if not os.path.exists(workspace_folder):
        os.mkdir(workspace_folder)

    filepath = os.path.join(workspace_folder, f"{filename}.log")

    f = open(filepath, "w")
    f.write(content)
    f.close()
