import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")
scriptPath = os.path.dirname(os.path.abspath(__file__))

supabaseBasePath = scriptPath + '/../'

files = [
    'assistant/codingAssistant.py',
    ]

def get_completion(prompt, user_messages=[], assistant_messages=[], model="gpt-4-turbo-preview"):
    system = """
    you are a helpful assistant, supporting a software developer in creating an coding assistant script 
    based on the OpenAI API.:
    

    Your task is to generate python code.
    """
    
    messages = [
        {"role": "system", "content": system}
        ]
    
    if user_messages:
        for message in user_messages:
            messages.append({"role": "user", "content": message})
    
    if prompt:
        messages.append({"role": "user", "content": prompt})

    if assistant_messages:
        for message in assistant_messages:
            messages.append({"role": "assistant", "content": message})
    
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]


prompt = """
I'm looking for advice on becoming a better Python developer.
"""

user_messages = [
    "How can I improve my Python skills?",
    "What are some advanced Python topics I should learn?"
]

assistant_messages = [
    "Practice coding daily and work on projects.",
    "Consider learning about asynchronous programming, metaprogramming, and system design."
]

def load_code_files(files) -> str:
    
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

prompt += load_code_files(files)

print(prompt)

print('----------------\n--- response ---\n----------------\n\n\n')

get_completion(prompt)

print(get_completion(prompt))
