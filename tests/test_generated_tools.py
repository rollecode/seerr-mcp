"""Call real generated tools and check the requests they build.

The coverage tests read tools.py as text and the runtime tests exercise call()
directly, so without this nothing proves a generated function actually
produces the request its docstring claims.
"""

import json

import httpx
import pytest

from seerr_mcp import runtime, tools


@pytest.fixture(autouse=True)
def transport(monkeypatch):
    monkeypatch.setenv("SEERR_API_KEY", "k")
    monkeypatch.setenv("SEERR_URL", "http://seerr.test")
    runtime._http = None
    seen: dict = {}

    def handler(request: httpx.Request) -> httpx.Response:
        seen["method"] = request.method
        seen["path"] = request.url.path
        seen["query"] = dict(request.url.params)
        seen["body"] = json.loads(request.content) if request.content else None
        return httpx.Response(200, json={"ok": True})

    runtime._http = httpx.Client(
        base_url="http://seerr.test",
        headers={"X-Api-Key": "k"},
        transport=httpx.MockTransport(handler),
    )
    yield seen
    runtime._http = None


def test_a_collection_read_hits_the_collection(transport):
    result = json.loads(tools.list_request())
    assert result["status"] == "success"
    assert transport["method"] == "GET"
    assert transport["path"] == "/api/v1/request"


def test_a_path_parameter_lands_in_the_url(transport):
    tools.get_request_by_request_id(42)
    assert transport["path"] == "/api/v1/request/42"


def test_a_write_sends_its_payload(transport):
    tools.create_request({"mediaType": "movie", "mediaId": 1})
    assert transport["path"] == "/api/v1/request"
    assert transport["body"] == {"mediaType": "movie", "mediaId": 1}



def test_a_delete_reaches_the_right_path(transport):
    tools.delete_request_by_request_id(7)
    assert transport["method"] == "DELETE"
    assert transport["path"] == "/api/v1/request/7"


def test_a_failure_comes_back_as_a_structured_error():
    runtime._http = httpx.Client(
        base_url="http://seerr.test",
        transport=httpx.MockTransport(lambda request: httpx.Response(404)),
    )
    result = json.loads(tools.list_request())
    assert result["status"] == "error"


def test_annotations_match_what_each_tool_does():
    import asyncio

    registered = {t.name: t for t in asyncio.run(runtime.mcp.list_tools())}
    assert registered["list_request"].annotations.readOnlyHint is True
    assert registered["delete_request_by_request_id"].annotations.destructiveHint is True
    assert registered["create_request"].annotations.readOnlyHint is False
