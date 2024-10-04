import os

def load_code(files, project_base_path) -> str:
    """
    Loads files from the project, to help the assistant's understanding of the project,
    and returns them as a string.
    Argument:
    files: a list of file names, including their path from the repository root.
    """

    code_snippets = ""
    for file in files:
        file_path = os.path.join(project_base_path, file)
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                code_snippets += f.read() + "\n\n"
        else:
            code_snippets += f"File {file} not found.\n\n"
    return code_snippets