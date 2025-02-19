import openai
import os
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_post(topic, tone="enthusiastic"):
    prompt = f"Generate an engaging and {tone} social media post about {topic}."
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a creative social media expert."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=100
    )
    return response["choices"][0]["message"]["content"]

if __name__ == "__main__":
    topic = input("Enter a topic for the social media post: ")
    tone = input("Enter the desired tone (e.g., enthusiastic, humorous, professional): ")
    post = generate_post(topic, tone)
    print("Generated Social Media Post:\n", post)
