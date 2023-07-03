import os
import openai
import CompletionOptions

class ChatGPT:
    def __init__(self, api_key=None, completion_options=None):
        self.api_key = api_key if api_key else os.getenv("OPENAI_API_KEY")
        if self.api_key is None:
            raise ValueError("OPENAI_API_KEY not found.")
        openai.api_key = self.api_key

        if completion_options is None:
            completion_options = CompletionOptions()
        self.completion_options = completion_options

    def create(self, prompt):
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=self.completion_options.max_tokens,
            temperature=self.completion_options.temperature,
            top_p=self.completion_options.top_p,
            frequency_penalty=self.completion_options.frequency_penalty,
            presence_penalty=self.completion_options.presence_penalty
        )
        return response.choices[0].text.strip()