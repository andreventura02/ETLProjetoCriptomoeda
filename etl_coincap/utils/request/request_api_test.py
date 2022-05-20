from .request_api import HttpRequest

def test_request_asset():
    http =  HttpRequest()
    request_response_ = http.request_asset()
    lista_elementos = ['explorer','id','rank','symbol','name','supply','maxSupply','marketCapUsd','volumeUsd24Hr','priceUsd','changePercent24Hr','vwap24Hr']
    request_response = request_response_.get('data')
    
    
    assert type(request_response[0]) == dict
    assert {'data','timestamp'} == set([x for x in request_response_.keys()])
    assert set(lista_elementos) == set([x for x in request_response[0].keys()])
    