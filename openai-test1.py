from openai import OpenAI
import os  
from dotenv import load_dotenv
load_dotenv("config.env")                             
from pathlib import Path

#api_key=os.environ.get("OPENAI_API_KEY")

client = OpenAI()

completion = client.chat.completions.create(
    model= "gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
    {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
  ]
)

print(completion.choices[0].message)
