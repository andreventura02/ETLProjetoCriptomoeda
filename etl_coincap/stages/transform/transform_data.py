from etl_coincap.stages.contracts.transform_contract import TransformContract
from etl_coincap.stages.contracts.extract_contract import ExtractContract

from typing import List, Dict

class TransformData:
    
    def transform_data_contract(self,extract_contract: ExtractContract) -> TransformContract:
        clean_data = self.__clear_and_transform_data(extract_contract)
        return TransformContract(transformed_data=clean_data)
    
    def __clear_and_transform_data(self, extract_contract: ExtractContract) -> List[Dict]:
        lista_dados = []
        for data in extract_contract:
            for data_dict in data['data']:
                if data_dict['rank'] != None:
                    data_dict['rank'] = int(data_dict['rank'])
                    
                if data_dict['supply'] != None:
                    data_dict['supply'] = round(float(data_dict['supply']),2)
                    
                if data_dict['maxSupply'] != None:
                    data_dict['maxSupply'] = round(float(data_dict['maxSupply']),2)
                    
                if data_dict['marketCapUsd'] != None:
                    data_dict['marketCapUsd'] = round(float(data_dict['marketCapUsd']),2)
                    
                if data_dict['volumeUsd24Hr'] != None:
                    data_dict['volumeUsd24Hr'] = round(float(data_dict['volumeUsd24Hr']),2)
                    
                if data_dict['priceUsd'] != None:   
                    data_dict['priceUsd'] = float(data_dict['priceUsd'])
                    
                if data_dict['changePercent24Hr'] != None:
                    data_dict['changePercent24Hr'] = float(data_dict['changePercent24Hr'])
                    
                if data_dict['vwap24Hr'] != None:
                    data_dict['vwap24Hr'] = float(data_dict['vwap24Hr'])
                    
                if data_dict['explorer'] != None:
                    for i in ['https://','http://']:
                        data_dict['explorer'] = data_dict['explorer'].replace(i,'')
                        
                data_dict['timestamp'] = data['timestamp']
                lista_dados.append(data_dict)
        return lista_dados