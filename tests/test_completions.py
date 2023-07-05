# test_completions.py
import sys
import os
import unittest
from dotenv import load_dotenv


# Add src directory to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from completions import Completions
from completion_options import CompletionOptions

class TestCompletions(unittest.TestCase):
    def test_create(self):
        load_dotenv()  # load environment variables from .env file
        api_key = os.getenv("OPENAI_API_KEY")
        if api_key is None:
            raise ValueError("OPENAI_API_KEY not found.")


        start_sequence = "The below text is of a recipe output from an OCR engine. Clean the text and collate the recipe into json format \"title\", \"subtitle\", \"authors note\", \"ingredients\" array, \"preparation steps\" array, and \"servings\" (only populate sections when applicable and use an array where prompted). Respond only with the json."
        restart_sequence = ""
        completion_options = CompletionOptions(max_tokens=0)
        completions = Completions(api_key=api_key, completion_options=completion_options)

        # Open the file and read the prompt
        with open('prompt.txt', 'r') as file:
            prompt = file.read().replace('\n', '')

        result = completions.create(prompt=prompt, start_sequence=start_sequence, restart_sequence=restart_sequence)
        # Very simple test - just checks that some completion was generated
        self.assertTrue(len(result) > 0)

if __name__ == '__main__':
    unittest.main()
