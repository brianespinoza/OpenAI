class CompletionOptions:
    def __init__(self, max_tokens=100, temperature=0.5, top_p=1, frequency_penalty=0, presence_penalty=0):
        self.max_tokens = max_tokens
        self.temperature = temperature
        self.top_p = top_p
        self.frequency_penalty = frequency_penalty
        self.presence_penalty = presence_penalty