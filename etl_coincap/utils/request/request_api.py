from etl_coincap.utils.interfaces.request_api import HttpRequestInterface
from typing import Dict 
import requests
import json

class HttpRequest(HttpRequestInterface):
    
    def __init__(self) -> None:
        self.__url = "https://api.coincap.io/v2/assets/"
        
    def request_asset(self) -> Dict:
        response = requests.get(self.__url)
        return json.loads(response.text)
        