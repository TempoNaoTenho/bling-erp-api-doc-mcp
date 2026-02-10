import hashlib
import json

from bling_doc_mcp.app import mcp
from bling_doc_mcp.utils.openapi import load_openapi_compact_text


class InvalidParameterError(ValueError):
    """Raised when invalid parameters are provided to resource functions."""


@mcp.resource(
    uri="data://bling-openapi.json",
    name="Bling ERP API OpenAPI Full Specification",
    mime_type="application/json",
)
def openapi_bling_doc_file() -> str:
    """Obtain the full OpenAPI specification for the Bling ERP API."""
    # Many MCP hosts/inspectors have practical UI/size limits; this compact
    # serialization keeps the payload smaller than the raw source file.
    return load_openapi_compact_text()


@mcp.resource(
    uri="data://bling-openapi.json/info",
    name="Bling ERP API OpenAPI Info",
    mime_type="application/json",
)
def openapi_bling_doc_info() -> str:
    """Metadata about the OpenAPI resource (size + checksum)."""
    text = load_openapi_compact_text()
    payload = {
        "chars": len(text),
        "bytes_utf8": len(text.encode("utf-8")),
        "sha256_utf8": hashlib.sha256(text.encode("utf-8")).hexdigest(),
    }
    # Some MCP hosts only accept str/bytes (not dict) from resources.
    return json.dumps(payload, ensure_ascii=False, separators=(",", ":"))


@mcp.resource(
    uri="data://bling-openapi.json{?offset,limit}",
    name="Bling ERP API OpenAPI Chunk",
    mime_type="application/json",
)
def openapi_bling_doc_chunk(
    offset: int = 0,
    limit: int = 50_000,
) -> str:
    """Returns a slice of the OpenAPI JSON as text, for clients with size limits.
    Useful if needed to peak at the content in smaller chunks.

    Example:
        data://bling-openapi.json?offset=0&limit=2000
    """
    if offset < 0:
        raise InvalidParameterError
    if limit <= 0:
        raise InvalidParameterError

    text = load_openapi_compact_text()
    total = len(text)
    start = min(offset, total)
    end = min(offset + limit, total)
    payload = {
        "offset": start,
        "limit": limit,
        "total": total,
        "done": end >= total,
        "text": text[start:end],
    }
    return json.dumps(payload, ensure_ascii=False, separators=(",", ":"))
