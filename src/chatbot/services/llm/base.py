from abc import ABC, abstractmethod


class LLMProvider(ABC):
    @abstractmethod
    def text_output():
        pass