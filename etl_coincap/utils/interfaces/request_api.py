from abc import ABC, abstractmethod
from typing import Dict

class HttpRequestInterface(ABC):
    
    @abstractmethod
    def request_asset(self) -> Dict:
        pass
        