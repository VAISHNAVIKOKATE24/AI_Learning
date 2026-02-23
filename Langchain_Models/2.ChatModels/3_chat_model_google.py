# from langchain_google_genai import ChatGoogleGenerativeAI

# from dotenv import load_dotenv

# load_dotenv()

# model=ChatGoogleGenerativeAI(model="gemini-pro")

# result= model.invoke("What is the captial of india")

# print(result)

from dotenv import load_dotenv
import os
from google import genai

# load env variables
load_dotenv()

# configure client
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

# FREE + STABLE model
model = client.models.generate_content(
    model="models/gemini-1.0-pro",
    contents="Hello"
)

print(model.text)
