import importlib

import pytest

MODULES = [
    "common_pb2",
    "data_pb2",
    "debug_pb2",
    "error_pb2",
    "query_pb2",
    "raw_pb2",
    "sc2api_pb2",
    "score_pb2",
    "spatial_pb2",
    "ui_pb2",
]


@pytest.mark.parametrize("name", MODULES)
def test_import(name):
    mod = importlib.import_module(f"s2clientprotocol.{name}")
    assert hasattr(mod, "DESCRIPTOR")


def test_create_message():
    from s2clientprotocol import common_pb2

    point = common_pb2.Point2D(x=1.0, y=2.0)
    assert point.x == 1.0
    assert point.y == 2.0


def test_request_response_exist():
    from s2clientprotocol import sc2api_pb2

    assert "Request" in sc2api_pb2.DESCRIPTOR.message_types_by_name
    assert "Response" in sc2api_pb2.DESCRIPTOR.message_types_by_name


def test_enum_race():
    from s2clientprotocol import common_pb2

    assert common_pb2.Terran == 1
    assert common_pb2.Zerg == 2
    assert common_pb2.Protoss == 3


def test_serialization_roundtrip():
    from s2clientprotocol import common_pb2

    original = common_pb2.Point(x=1.0, y=2.0, z=3.0)
    data = original.SerializeToString()
    restored = common_pb2.Point()
    restored.ParseFromString(data)
    assert restored == original
