from etl_coincap.stages.contracts.transform_contract import TransformContract
from etl_coincap.utils.request.request_api import HttpRequest
from etl_coincap.stages.extract.extract_data import ExtractData
from etl_coincap.stages.transform.transform_data import TransformData
from etl_coincap.utils.connector.postgre_connector import PostgreConnector
from etl_coincap.utils.connector.get_credentials import get_credentials
from etl_coincap.utils.connector.assets_sql import assets_sql
import psycopg2.extras as p

def test_transform_data():
    http = HttpRequest()
    extract_data = ExtractData(http)
    raw_data = extract_data.extract_raw_data()
    transform_data = TransformData()
    transform_contract = transform_data.transform_data_contract(raw_data)
    
    with PostgreConnector('postgres','1234','localhost','cripto').cursor_manager() as curr:
            data = list(transform_contract.transformed_data)
            print(data)
            p.execute_batch(curr,assets_sql(),data)