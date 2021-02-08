import requests

from hypothesis import given, settings, HealthCheck
from hypothesis_jsonschema import from_schema

from tokenlists import TokenList

TOKENLISTS_SCHEMA = "https://uniswap.org/tokenlist.schema.json"


@given(token_list=from_schema(requests.get(TOKENLISTS_SCHEMA).json()))
@settings(suppress_health_check=(HealthCheck.too_slow,))
def test_schema(token_list):
    assert TokenList.from_dict(token_list).to_dict() == token_list
