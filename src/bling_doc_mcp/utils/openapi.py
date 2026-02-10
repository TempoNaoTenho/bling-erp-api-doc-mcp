# src/bling_doc_mcp/utils/openapi.py
import json
from functools import lru_cache
from importlib.resources import files
from typing import Any


@lru_cache(maxsize=1)
def load_openapi() -> dict[str, Any]:
    text: str = (files("bling_doc_mcp.files") / "bling-openapi.json").read_text(
        encoding="utf-8"
    )
    return json.loads(text)


@lru_cache(maxsize=1)
def load_openapi_compact_text() -> str:
    return json.dumps(load_openapi(), ensure_ascii=False, separators=(",", ":"))


@lru_cache(maxsize=1)
def load_markdown_reference() -> str:
    """Load the markdown reference file with caching."""
    text: str = (
        files("bling_doc_mcp.files") / "bling-openapi-reference.md"
    ).read_text(encoding="utf-8")
    return text


def parse_markdown_sections(content: str) -> dict[str, str]:
    """Parse markdown content into sections by headers."""
    sections = {}
    current_section = "header"
    current_content = []

    for line in content.split("\n"):
        # Main section header (## Header)
        if line.startswith("## ") and not line.startswith("### "):
            # Save previous section
            if current_content:
                sections[current_section] = "\n".join(current_content)
            # Start new section
            current_section = line[3:].strip()
            current_content = [line]
        else:
            current_content.append(line)

    # Save last section
    if current_content:
        sections[current_section] = "\n".join(current_content)

    return sections


@lru_cache(maxsize=1)
def load_markdown_sections() -> dict[str, str]:
    """Load and parse markdown sections with caching."""
    content = load_markdown_reference()
    return parse_markdown_sections(content)


def extract_markdown_endpoint(content: str, endpoint: str) -> list[str]:
    """Extract documentation for a specific endpoint from markdown.

    Args:
        content: Full markdown content
        endpoint: Endpoint search term (partial matching supported)

    Returns:
        List of endpoint documentation sections matching the search term
    """
    results = []
    lines = content.split("\n")

    i = 0
    while i < len(lines):
        line = lines[i]
        # Look for endpoint headers like "### GET `/produtos`"
        # Changed to support partial matching (endpoint in line)
        if line.startswith("### ") and endpoint in line:
            # Extract until next endpoint (### with `) or section (##)
            endpoint_lines = [line]
            i += 1
            while i < len(lines):
                next_line = lines[i]
                # Stop at next endpoint or section
                if (next_line.startswith("### ") and "`" in next_line) or (
                    next_line.startswith("## ") and not next_line.startswith("### ")
                ):
                    break
                endpoint_lines.append(next_line)
                i += 1
            results.append("\n".join(endpoint_lines))
        else:
            i += 1

    return results


@lru_cache(maxsize=1)
def build_markdown_header_index() -> dict[int, str]:
    """Build line number -> endpoint header mapping for fast lookups.

    Returns:
        Dictionary mapping line numbers to their containing endpoint headers
    """
    content = load_markdown_reference()
    lines = content.split("\n")
    index = {}
    current_header = None

    for i, line in enumerate(lines):
        if line.startswith("### ") and "`" in line:
            current_header = line
        if current_header:
            index[i] = current_header

    return index
