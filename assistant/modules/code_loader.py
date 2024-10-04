import os

def load_code(files, project_base_path) -> str:
    """
    Loads files from the project, to help the assistant's understanding of the project,
    and returns them as a string.
    Argument:
    files: a list of file names, including their path from the repository root.
    """

    if not files:
        return ""

    code = """
    I will add relevant code as follows. If you are missing any code, please tell me and I will add it.
    """
    for file in files:
        with open(os.path.join(project_base_path, file), 'r') as f:
            code += f"""
            ```
            {file}
            {f.read()}
            ```
            """
    return code