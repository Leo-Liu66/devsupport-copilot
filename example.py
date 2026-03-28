import os
import openai
import tiktoken
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file

openai.api_key  = os.environ['OPENAI_API_KEY']

client = openai.OpenAI()

response = client.responses.create(
    model="gpt-3.5-turbo",
    input="Write a one-sentence bedtime story about a unicorn."
)

print(response.output_text)