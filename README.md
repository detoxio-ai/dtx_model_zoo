# Model Zoo

A collection of services to interact with various language models, including Groq, Gemini, and OpenAI. Each service maintains a list of models and provides methods to analyze prompts and return responses.

## Project Structure

- `groq_model.py`: Interacts with Groq models.
- `gemini_model.py`: Interacts with Gemini models.
- `openai_model.py`: Interacts with OpenAI models.
- `exceptions.py`: Custom exceptions used across the services.

## Installation

This project uses [Poetry](https://python-poetry.org/) for dependency management. Follow the instructions below to set up the project.

### Prerequisites

- Python 3.7 or higher
- Poetry

### Steps

1. Clone the repository:

    ```sh
    git clone https://github.com/your-username/model-zoo.git
    cd model-zoo
    ```

2. Install Poetry:

    ```sh
    curl -sSL https://install.python-poetry.org | python3 -
    ```

    Or follow the instructions from the [Poetry documentation](https://python-poetry.org/docs/#installation).

3. Install dependencies:

    ```sh
    poetry install
    ```

4. Activate the virtual environment:

    ```sh
    poetry shell
    ```

## Usage

### Example Script

Here's an example of how to use the `GroqModel` class to analyze a prompt:

```python
from groq_model import GroqModel

service = GroqModel(model_name="llama3-8b")
response = service.run(prompt="Analyze this case for me.")
print(response)

