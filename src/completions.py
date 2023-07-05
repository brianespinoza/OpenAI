import os
import openai
from completion_options import CompletionOptions
from tiktoken import Tokenizer

class Completions:
    def __init__(self, api_key=None, completion_options=None):
        self.api_key = api_key if api_key else os.getenv("OPENAI_API_KEY")
        if self.api_key is None:
            raise ValueError("OPENAI_API_KEY not found.")
        openai.api_key = self.api_key

        if completion_options is None:
            completion_options = CompletionOptions()
        self.completion_options = completion_options

    def tokenize(self, text):
        """
        Converts a string of text into a sequence of tokens using tiktoken.

        Parameters:
        text (str): The text to tokenize.

        Returns:
        list: The list of tokens.
        """
        tokenizer = Tokenizer()
        tokens = tokenizer.tokenize(text)
        return tokens
    
    def calculateMaxTokens(self, prompt, start_sequence, restart_sequence, max_total_tokens=4096):
        """
        Calculates the maximum number of tokens remaining in a GPT-3 response based on a given
        prompt, start_sequence, and restart_sequence, given a maximum total number of tokens.

        Parameters:
        prompt (str): The initial prompt.
        start_sequence (str): The sequence indicating the start of a response.
        restart_sequence (str): The sequence indicating a restart in the response.

        Returns:
        int: The maximum number of tokens remaining for the response.
        """

        promptTokens = self.tokenize(prompt)
        startTokens = self.tokenize(start_sequence)
        restartTokens = self.tokenize(restart_sequence)

        return max_total_tokens - len(promptTokens) - len(startTokens) - len(restartTokens)


    def create(self, prompt, start_sequence, restart_sequence):
        if(self.completion_options.max_tokens == 0):
            token_total = self.calculateMaxTokens(prompt, start_sequence, restart_sequence)
        else:
            token_total = self.completion_options.max_tokens
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=token_total,
            temperature=self.completion_options.temperature,
            top_p=self.completion_options.top_p,
            frequency_penalty=self.completion_options.frequency_penalty,
            presence_penalty=self.completion_options.presence_penalty
        )
        return response.choices[0].text.strip()