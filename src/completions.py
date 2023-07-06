import os
import openai
from completion_options import CompletionOptions
from tiktoken import encoding_for_model
from openai.error import (
    APIError,
    Timeout,
    RateLimitError,
    APIConnectionError,
    InvalidRequestError,
    AuthenticationError,
    ServiceUnavailableError
)


class Completions:
    def __init__(self, api_key=None, completion_options=None):
        self.api_key = api_key if api_key else os.getenv("OPENAI_API_KEY")
        if self.api_key is None:
            raise ValueError("OPENAI_API_KEY not found.")
        openai.api_key = self.api_key

        if completion_options is None:
            completion_options = CompletionOptions()
        self.completion_options = completion_options
         # Define the encoding
        self.encoding = encoding_for_model(self.completion_options.engine)

    def num_tokens_from_string(self, string):
        """Returns the number of tokens in a text string."""
        num_tokens = len(self.encoding.encode(string))
        return num_tokens

    def calculateMaxTokens(self, prompt, start_sequence, restart_sequence, max_total_tokens=4096):
        """
        Calculates the maximum number of tokens remaining in a GPT response based on a given
        prompt, start_sequence, and restart_sequence, given a maximum total number of tokens.

        Parameters:
        prompt (str): The initial prompt.
        start_sequence (str): The sequence indicating the start of a response.
        restart_sequence (str): The sequence indicating a restart in the response.

        Returns:
        int: The maximum number of tokens remaining for the response.
        """

        promptTokens = self.num_tokens_from_string(prompt)
        startTokens = self.num_tokens_from_string(start_sequence)
        restartTokens = self.num_tokens_from_string(restart_sequence)

        return max_total_tokens - promptTokens - startTokens - restartTokens

    def create(self, prompt, start_sequence, restart_sequence):
        if(self.completion_options.max_tokens == 0):
            token_total = self.calculateMaxTokens(prompt, start_sequence, restart_sequence)
        else:
            token_total = self.completion_options.max_tokens

        prompt = start_sequence + prompt + restart_sequence
        
        print("prompt" + prompt)
        print("tokens: " + str(token_total))

        try:
            response = openai.Completion.create(
                engine=self.completion_options.engine,
                prompt=prompt,
                max_tokens=token_total,
                temperature=self.completion_options.temperature,
                top_p=self.completion_options.top_p,
                frequency_penalty=self.completion_options.frequency_penalty,
                presence_penalty=self.completion_options.presence_penalty
            )
            return response.choices[0].text.strip()
        except openai.api_errors.AuthenticationError as e:
            raise Exception("Invalid API Key") from e
        except openai.api_errors.RateLimitError as e:
            raise Exception("Rate limit exceeded") from e
        except openai.api_errors.InvalidRequestError as e:
            raise Exception("Invalid request") from e
        except openai.api_errors.APIError as e:
            raise Exception("API error occurred") from e
        except openai.api_errors.APIConnectionError as e:
            raise Exception("API connection error occurred") from e
        except Exception as e:
            raise Exception("An unknown error occurred") from e