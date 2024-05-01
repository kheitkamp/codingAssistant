import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")
scriptPath = os.path.dirname(os.path.abspath(__file__))

supabaseBasePath = scriptPath + '/../src/app/'

files = [
    'app.component.html',
    'app.component.scss',
    'app.component.ts',
    'app.module.ts'
    ]

def get_completion(prompt, model="gpt-4-turbo-preview"):
    system = """
    you are a helpful assistant, supporting a software developer in creating an app using the following tools:
    - Angular
    - rxjs
    - angular material
    - ngrx for state management
    - ngx-translate for internationalization

    The app is {{add your description here}}.

    Your task is to generate typescript, html and scss code.
    """
    
    messages = [
        {"role": "system", "content": system},
        {"role": "user", "content": prompt},
        # {"role": "assistant", "content": firstAssistanPrompt}
        ]
    
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]


prompt = """
I need a login page. Please start with an HTML template first and explain to me how I add it to the existing Angular framework.

I will add relevant code as follows. If you are missing any code, please tell me and I will add it.

"""

def load_code_files(files) -> str:
    code = ''
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
