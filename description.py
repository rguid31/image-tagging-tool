from openai import OpenAI

client = OpenAI()
from config import openai

def generate_description(tags):
    prompt = f"Write a visually descriptive Unsplash-style description using these tags: {', '.join(tags)}"

    response = client.chat.completions.create(model="gpt-4-turbo",
    messages=[{"role": "system", "content": "You are an expert at writing visually descriptive and engaging image descriptions for stock photography."},
              {"role": "user", "content": prompt}])

    return response.choices[0].message.content