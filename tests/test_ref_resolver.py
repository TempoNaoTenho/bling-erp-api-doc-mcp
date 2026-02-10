import pytest

from bling_doc_mcp.utils.openapi import load_openapi
from bling_doc_mcp.utils.ref_resolver import RefResolutionError, resolve_openapi_ref


def test_resolve_openapi_ref_expands_nested_refs():
    openapi = load_openapi()
    resolved = resolve_openapi_ref(openapi, "#/components/schemas/ErrorResponse")

    assert isinstance(resolved, dict)
    assert resolved
    assert "type" in resolved or "properties" in resolved


def test_resolve_openapi_ref_invalid_ref_raises():
    openapi = load_openapi()
    with pytest.raises(RefResolutionError, match="Unsupported ref"):
        resolve_openapi_ref(openapi, "/components/schemas/ErrorResponse")
