from etl_coincap.utils.interfaces.request_api import HttpRequestInterface
from etl_coincap.stages.contracts.extract_contract import ExtractContract

class ExtractData:
    
    def __init__(self, request_api: HttpRequestInterface) -> None:
        self.__request_api = request_api
        
    def extract_raw_data(self) -> ExtractContract:
        raw_data = self.__request_api.request_asset()
        return ExtractContract(raw_data=raw_data)