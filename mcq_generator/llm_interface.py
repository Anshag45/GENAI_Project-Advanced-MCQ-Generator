import openai
import os

# Load API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_questions(model: str, prompt: str, temperature: float = 0.95, top_p: float = 0.95, max_tokens: int = 1000):
    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=[
                {"role": "system", "content": "You write pedagogically sound Multiple Choice Questions precisely according to user inputs."},
                {"role": "user", "content": prompt}
            ],
            temperature=temperature,
            top_p=top_p,
            max_tokens=max_tokens
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {e}"
