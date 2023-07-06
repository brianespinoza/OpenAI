# OpenAI GPT Model Completions

This project provides a Python script that uses the OpenAI API to generate text completions based on user-provided prompts. The prompts, as well as several optional parameters for the completion task, can be configured in a Python dictionary. 

## Setup

### Requirements

- Python 3.7+
- OpenAI Python library
- tiktoken library

### Installation

1. Clone this repository to your local machine.
2. Navigate into the project directory and install the required Python libraries with:

```sh
pip install -r requirements.txt
```

## Usage

The main class in this project is `Completions`, which is used to create completions using the OpenAI GPT models.

### Initialising `Completions`

You can initialise a `Completions` instance with an API key and a `CompletionOptions` instance. If you don't provide an API key, the constructor will attempt to use the `OPENAI_API_KEY` environment variable.

```python
completions = Completions(api_key="my-api-key")
```

### Generating Completions

Use the `create` method to generate a completion. This method requires a prompt, start_sequence, and restart_sequence:

```python
prompt = "Translate the following English text to French: '{}'"
start_sequence = "[English to French]: "
restart_sequence = "\n[English to French]: "
result = completions.create(prompt, start_sequence, restart_sequence)
print(result)
```

### Error Handling

The `create` method contains robust error handling, and will raise descriptive exceptions in the event of an API error.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)