import os
import cohere
from dotenv import load_dotenv

load_dotenv()

client = cohere.Client(os.getenv("COHERE_API_KEY"))

def query_cohere(prompt):
    """Query Cohere model with a prompt"""
    try:
        response = client.chat(
            model="command-r-plus-08-2024",
            message=prompt,
            temperature=0.7
        )
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"


if __name__ == "__main__":
    user_prompt = input("Enter your prompt: ")
    print("Querying Cohere...")
    result = query_cohere(user_prompt)
    print("\nResponse:")
    print(result)