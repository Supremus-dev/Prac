# python -m pip install google-genai

# python -m pip install google-genai
from google import genai

ai = genai.Client(api_key="AQ.Ab8RN6I5h7jCxP8O8yhDZRVSHJkNEo0gVkpKrmvcTtpJs0dawQ")
q = input("Ask: ")

try:
    r = ai.models.generate_content(
        model="gemini-3.8-flash",
        contents=f"Answer clearly with useful details and examples: {q}"
    )
    print(r.text)
except Exception as e:
    print("Error:", e)