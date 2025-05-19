from google import genai
from google.genai import types
import os

class LectureSummarizerGensim:
    def __init__(self):
        api_key = self.get_gemini_api_key()
        self.client = genai.Client(api_key=api_key)

    def get_gemini_api_key(self):
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY environment variable not set.")
        return api_key

    def summarize(self, text):
        response = self.client.models.generate_content(
            model="gemini-2.0-flash",
            config=types.GenerateContentConfig(
                system_instruction=(
                    "You are a lecture summarizer. You will be given a lecture transcript and "
                    "will be asked to generate a summary. It is best not to skip important detail. "
                    "Using bullets or a list can also be helpful."
                ),
                temperature=0.0,
            ),
            contents=text
        )
        # The Gemini client response might have a slightly different structure
        # Adjust as necessary (e.g., response.candidates[0].content)
        return response.candidates[0].content
