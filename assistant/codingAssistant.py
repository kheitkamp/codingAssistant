# assistant/codingAssistant.py
from openai import OpenAI
from modules.code_loader import load_code
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
scriptPath = os.path.dirname(os.path.abspath(__file__))
projectBasePath = scriptPath + '/../'

# Default model
# model_quick_change = "gpt-4o" # for the gpt-4o model
model_quick_change = "gpt-4o-mini" # for the gpt-4o-mini model
# model_quick_change = "o1-preview" # for the o1-preview model
# model_quick_change = "o1-mini" # for the o1-mini model
# model_quick_change = "gpt-4" # for the gpt-4 model
# model_quick_change = "gpt-4-turbo" # for the gpt-4-turbo model
# model_quick_change = "gpt-3.5-turbo" # for the gpt-3.5-turbo model

project_files = [
    'assistant/codingAssistant.py',
    'assistant/modules/code_loader.py'
]


def get_completion(prompt, model=model_quick_change, user_messages=None, assistant_messages=None):
    """Get completion from OpenAI API based on the provided prompt and messages."""
    if assistant_messages is None:
        assistant_messages = []
    if user_messages is None:
        user_messages = []

    system = """
    you are a helpful assistant, supporting a software developer in creating an coding assistant script
    based on the OpenAI API.:
    Your task is to improve given python code and to generate new python code.
    """

    messages = [{"role": "system", "content": system}]

    if user_messages:
        for user_message in user_messages:
            messages.append({"role": "user", "content": user_message})

    if prompt:
        messages.append({"role": "user", "content": prompt})

    if assistant_messages:
        for message in assistant_messages:
            messages.append({"role": "assistant", "content": message})

    try:
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            temperature = 0
            # change settings for o1-mini and o1-preview models
            if model == "o1-mini" or model == "o1-preview":
                # remove system message
                messages.pop(0)
                # set temperature to 1
                temperature = 1
                
            temperature=temperature,  # this is the degree of randomness of the model's output
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"An error occurred: {str(e)}"


def main():
    """Main function to run the coding assistant."""
    my_prompt = "I would like to become a better python developer.\n"

    user_msgs = [
        "How can I improve my Python skills?",
        "What are some advanced Python topics I should learn?"
    ]

    assistant_msgs = [
        "Practice coding daily and work on projects.",
        "Consider learning about asynchronous programming, metaprogramming, and system design."
    ]

    my_prompt += load_code(project_files, projectBasePath)

    print(my_prompt)

    print('----------------\n--- response ---\n----------------\n\n\n')

    response = get_completion(my_prompt, model=model_quick_change, user_messages=user_msgs,
                              assistant_messages=assistant_msgs)
    print(response)


if __name__ == "__main__":
    main()
