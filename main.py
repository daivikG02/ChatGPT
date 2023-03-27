import openai
import prompt_toolkit

# Set up OpenAI API credentials
openai.api_key = "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"


# Define the prompt to use for the GPT-3.5 model
def get_prompt(user_input):
  return f"User: {user_input}\nAI: "


# Define a function to generate a response using the GPT-3.5 model
def generate_response(prompt):
  response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
  )
  message = response.choices[0].text.strip()
  return message


# Define a function to run the chatbot
def run_chatbot():
  while True:
    user_input = prompt_toolkit.prompt("User: ")
    print("")
    prompt = get_prompt(user_input)
    message = generate_response(prompt)
    print(f"AI:  {message}")
    print("")


# Run the chatbot
if __name__ == "__main__":
  run_chatbot()
