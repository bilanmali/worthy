import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def get_verdict(name, days_since_last_used):
    # ask the AI whether this subscription seems worth keeping
    prompt = f"A subscription called {name} hasn't been used in {days_since_last_used} days. In one short sentence, say whether it seems worth keeping or worth reconsidering, and briefly why."

    response = client.chat.completions.create(
    model="openai/gpt-oss-20b",
    messages=[{"role": "user", "content": prompt}]
)

    return response.choices[0].message.content