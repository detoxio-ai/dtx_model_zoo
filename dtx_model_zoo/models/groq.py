import logging
from retry import retry
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from .exceptions import InvalidInputException, NoneResultException
from .utils import escape_special_characters
from .base import BaseModel

class GroqModel(BaseModel):
    """
    Model that talk to groq service to interact with models
    """
    _logger = logging.getLogger(__name__)
    _MODELS = {
        "llama3-8b": "llama3-8b-8192",
        "llama3-70b": "llama3-70b-8192",
        "mixtral-7b": "mixtral-8x7b-32768",
        "gemma-7b": "gemma-7b-it",
        "whisper-large-v3": "whisper-large-v3",
    }
    
    DEFAULT_MODEL_PARAMS = {
        "temperature": 0.7,
        # "top_p": 1.0,
        # "frequency_penalty": 0.0,
        # "presence_penalty": 0.0,
    }
    
    def __init__(self, model_name="llama3-8b"):
        """
        Initialize the GroqModel with the given model.
        
        Args:
            model_name (str): The name of the model to use.
        """
        super().__init__()
        model_id = self._name2model_id(model_name)
        self.model = ChatGroq(model=model_id, **self.DEFAULT_MODEL_PARAMS)
        self.parser = StrOutputParser()

    def _name2model_id(self, model_name):
        """
        Convert a model name to its corresponding model ID.
        
        Args:
            model_name (str): The name of the model.
        
        Returns:
            str: The corresponding model ID.
        
        Raises:
            InvalidInputException: If the model name is not supported.
        """
        model_id = self._MODELS.get(model_name)
        if model_id is None:
            self._logger.debug("Model %s not found. Options: %s", model_name, self._MODELS.keys())
            raise InvalidInputException(f"Model {model_name} is not supported")
        return model_id
            
    def run(self, prompt: str, system: str=None):
        """
        Run the prompt analysis.
        
        Args:
            prompt (str): The prompt to analyze.
        
        Returns:
            Any: The result of the prompt analysis.
        """
        message = []
        if system:
            message.append(("system", system))
        
        escaped_prompt = escape_special_characters(prompt)
        message.append(("human", escaped_prompt))
        prompt = ChatPromptTemplate.from_messages(message)

        chain = prompt | self.model | self.parser
        result = chain.invoke({})
        return result
