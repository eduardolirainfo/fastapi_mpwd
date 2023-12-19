import datetime
import pytest
from fastapi.encoders import jsonable_encoder
import json


@pytest.fixture
def data():
    """ datetime object """
    return datetime.datetime.now()


def test_json_dump(data):
    """ json.dumps() raises an exception for datetime objects """
    with pytest.raises(Exception):
        _ = json.dumps(data)


def test_encoder(data):
    """ jsonable_encoder() converts datetime objects to strings """
    out = jsonable_encoder(data)
    assert out
    json_out = json.dumps(out)
    assert json_out
