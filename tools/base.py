from abc import ABC , abstractmethod

class Tool(ABC):
    
    name = "tool"
    description = ""

    @abstractmethod
    def execute(self, query:str):
        pass

        