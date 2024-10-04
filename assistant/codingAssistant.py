from openai import OpenAI
import os

client = OpenAI(api_key = os.getenv("OPENAI_API_KEY"))
scriptPath = os.path.dirname(os.path.abspath(__file__))
model_quick_change = "01-mini"

supabaseBasePath = scriptPath + '/../'

project_files = [
    'assistant/codingAssistant.py',
    ]

def get_completion(prompt, user_messages=None, assistant_messages=None, model="01-mini"):
    if assistant_messages is None:
        assistant_messages = []
    if user_messages is None:
        user_messages = []
    system = """
    you are a helpful assistant, supporting a software developer in creating an coding assistant script 
    based on the OpenAI API.:
    

    Your task is to generate python code.
    """

    messages: list[dict[str, str]] = [
        {"role": "system", "content": system}
    ]
    
    if user_messages:
        for user_message in user_messages:
            messages.append({"role": "user", "content": user_message})
    
    if prompt:
        messages.append({"role": "user", "content": prompt})

    if assistant_messages:
        for message in assistant_messages:
            messages.append({"role": "assistant", "content": message})
    
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message.content


my_prompt = """
I would like to become a better python developer.

"""

user_msgs = [
    "How can I improve my Python skills?",
    "What are some advanced Python topics I should learn?"
]

assistant_msgs = [
    "Practice coding daily and work on projects.",
    "Consider learning about asynchronous programming, metaprogramming, and system design."
]

def load_code_files(files) -> str:
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
        with open(supabaseBasePath + '/' + file, 'r') as f:
            code += f"""
            ```
            {file}
            {f.read()}
            ```
            """
    return code

my_prompt += load_code_files(project_files)

print(my_prompt)

print('----------------\n--- response ---\n----------------\n\n\n')

get_completion(my_prompt)

print(get_completion(my_prompt))
