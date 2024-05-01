# codingAssistant

This is a very basic and versatile coding assistant, which is able to 
analyse your current code files and help you creating code files
for your project.

The assistant works with ChatGPT. You need to setup a developer account
with openai and define an API key to be able to use your account.

## setup

1. Copy the folder `assistant` to your projects root directory.
2. In lines 14 - 20 use the `system` variable, 
   to give the LLM a general understanding of its role.
3. change the `prompt` string, defined in lines 45 – 47, 
   so that it suits your current problem.
4. store your API key in an environmental variable 
   called `OPENAI_API_KEY`. It will get imported in line 4.
5. Add or remove relevant files in lines 9 - 11.
5. Install python, if it is not installed already.
6. In terminal, navigate to the aassistant directory and type
   `python3 codingAssistant.py` 


If you want the assistant to build up a conversation, you can 
add its responses and your prompts to the corresponding lists in lines 49 to 57.
