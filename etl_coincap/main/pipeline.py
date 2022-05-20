from etl_coincap.utils.request.request_api import HttpRequest
from etl_coincap.stages.extract.extract_data import ExtractData
from etl_coincap.stages.transform.transform_data import TransformData
from etl_coincap.utils.connector.postgre_connector import PostgreConnector
from etl_coincap.utils.connector.assets_sql import assets_sql
import psycopg2.extras as p

class Pipeline:
    def __init__(self) -> None:
        self.__extract_data = ExtractData(HttpRequest())
        self.__transform_data = TransformData()
        self.__load_data = PostgreConnector('postgres','password','host','database')
    
    def run_pipeline(self) -> None:
        contract_extract_data = self.__extract_data.extract_raw_data()
        contract_transformed_data = self.__transform_data.transform_data_contract(contract_extract_data)
        with self.__load_data.cursor_manager() as curr:
            p.execute_batch(curr,assets_sql(),contract_transformed_data[0])