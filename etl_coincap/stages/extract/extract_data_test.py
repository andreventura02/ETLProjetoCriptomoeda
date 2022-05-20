from etl_coincap.utils.request.request_api import HttpRequest
from etl_coincap.stages.extract.extract_data import ExtractData
from etl_coincap.stages.contracts.extract_contract import ExtractContract

def test_extract_raw_data():
    http = HttpRequest()
    extract_data = ExtractData(http)
    raw_data = extract_data.extract_raw_data()
    
    assert isinstance(raw_data, ExtractContract)