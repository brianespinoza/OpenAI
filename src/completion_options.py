class CompletionOptions:
    def __init__(self, engine="text-davinci-003", max_tokens=0, temperature=1, top_p=1, frequency_penalty=0, presence_penalty=0):
        """
        CompletionOptions Class for managing options for OpenAI Completions.

        Parameters:
        max_tokens (int): The maximum length of the generated text. If the generated text exceeds this length, it will be cut off. 0 will calculate max available response.
        temperature (float): Determines the randomness of the output. A higher value means the output will be more random, while a lower value makes the output more deterministic.
        top_p (float): A value between 0 and 1. The model will choose from the top tokens whose cumulative probability exceeds the top_p value. This helps add an element of randomness to the output.
        frequency_penalty (float): A value between 0 and 2. The model will be penalized for using tokens that are used frequently or infrequently depending on the value of the frequency_penalty.
        presence_penalty (float): A value between 0 and 2. The model will be penalized for using tokens that are contextually relevant or irrelevant depending on the value of the presence_penalty.
        """
        self.max_tokens = max_tokens
        self.temperature = temperature
        self.top_p = top_p
        self.frequency_penalty = frequency_penalty
        self.presence_penalty = presence_penalty
        self.engine = engine