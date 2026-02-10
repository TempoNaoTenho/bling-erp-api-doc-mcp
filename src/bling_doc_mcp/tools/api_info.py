from typing import Any

from bling_doc_mcp.app import mcp
from bling_doc_mcp.utils.openapi import (
    build_markdown_header_index,
    extract_markdown_endpoint,
    load_markdown_reference,
    load_markdown_sections,
    load_openapi,
)
from bling_doc_mcp.utils.ref_resolver import (
    RefResolutionError,
    resolve_openapi_ref,
)


@mcp.tool(tags={"catalog"})
def openapi_list_endpoints() -> dict[str, Any]:
    """Lists all available endpoints in the Bling ERP API from the OpenAPI JSON structure.
    Use this to navigate the raw OpenAPI specification paths."""
    openapi = load_openapi()
    # Loads each endpoint inside the key "paths" of the JSON file
    endpoints: list[str] = list(openapi["paths"].keys())
    return {"endpoints": endpoints}


@mcp.tool(tags={"search"})
def openapi_get_endpoint_info(endpoint: str) -> dict[str, Any]:
    """Returns concise information about a specific endpoint from the OpenAPI JSON structure.
    Use it when you need a fast overview of an endpoint's raw specification data.
    You can search for a term that matches the endpoint name or part of it.

    Args:
        endpoint: Endpoint name (ex: "/produtos",
                                "/produtos/lotes",
                                "/produtos/lotes/{idLote}/status").

    Returns:
        A dictionary with the endpoint name and the concise information about
        the endpoint. The dictionary has the following structure:
        {
            "endpoints": {
                "endpoint_name": {
                    "path": "path",
                    "method": "method",
                    "description": "description",
                    "params": "params"
                }
            }
        }
    """
    openapi = load_openapi()
    request: dict[str, Any] = {}

    for path, methods_dict in openapi.get("paths", {}).items():
        if endpoint in path:
            for method, endpoint_info in methods_dict.items():
                # Only consider actual HTTP methods
                if method.lower() in {"get", "put", "patch", "delete", "post"}:
                    description = endpoint_info.get("description", "")
                    params: list[str | Any] = []

                    for param in endpoint_info.get("parameters", []):
                        # If it's a reference, just include the ref
                        if "$ref" in param:
                            param_info = param["$ref"]
                            param_name: str | Any = param_info
                        else:
                            name_value: str | None = param.get("name")
                            param_name = param if name_value is None else name_value
                        params.append(param_name)

                    if path not in request:
                        request[path] = {}
                    request[path][method.upper()] = {
                        "path": path,
                        "method": method.upper(),
                        "description": description,
                        "params": params,
                    }
    return {"endpoints": request}


@mcp.tool(tags={"search"})
def openapi_get_parameter_info(parameter: str) -> dict[str, Any]:
    """Returns information about a specific parameter from the OpenAPI JSON structure.
    Use it when you need to know the raw parameter specification.
    You can search for a term that matches the parameter name or part of it.

    Args:
        parameter: Parameter name (ex: "id", "nome", "descricao").

    Returns:
        A dictionary with the parameter name and the information about the parameter.
        The dictionary has the following structure:
        {
            "parameters": {
                "parameter_name": {
                    "name": "name",
                    "in": "in",
                    "description": "description",
                    "required": "required",
                    "schema": "schema"
                }
            }
        }
    """
    openapi = load_openapi()
    request: dict[str, Any] = {}

    for path, methods_dict in openapi.get("paths", {}).items():
        for method, endpoint_info in methods_dict.items():
            # Only consider actual HTTP methods
            if method.lower() in {"get", "put", "patch", "delete", "post"}:
                parameters = endpoint_info.get("parameters", [])
                for param in parameters:
                    if parameter in param.get("name", ""):
                        if path not in request:
                            request[path] = {}
                        request[path][method.upper()] = {
                            "name": param.get("name", ""),
                            "in": param.get("in", ""),
                            "description": param.get("description", ""),
                            "required": param.get("required", False),
                            "schema": param.get("schema", {}),
                        }
    return {"parameters": request}


@mcp.tool(tags={"schema", "search"})
def openapi_resolve_ref(ref: str, max_depth: int = 25) -> dict[str, Any]:
    """Resolves an OpenAPI $ref recursively from the JSON structure for documentation lookup.

    Args:
        ref: Local OpenAPI reference (ex: "#/components/schemas/ErrorResponse").
        max_depth: Maximum recursion depth to avoid infinite loops.

    Returns:
        A dictionary with the original ref and its recursively expanded content.
    """
    openapi = load_openapi()
    try:
        resolved = resolve_openapi_ref(openapi, ref, max_depth=max_depth)
    except RefResolutionError as exc:
        raise ValueError(str(exc)) from exc
    return {"ref": ref, "resolved": resolved}


@mcp.tool(tags={"documentation", "search"})
def docs_search_endpoint(endpoint: str) -> dict[str, Any]:
    """Search for documentation of a specific endpoint in the markdown reference.
    Returns complete documentation including parameters, examples, and code samples.
    Use this when you need detailed human-readable documentation with examples.

    Args:
        endpoint: Endpoint path to search for (ex: "/produtos", "/contatos", "/nfe").
                 Can be partial (ex: "produtos" will match "/produtos" and "/produtos/lotes").

    Returns:
        A dictionary with matching endpoint documentation sections.
        Each section includes method, path, description, parameters, examples, and code samples.
    """
    content = load_markdown_reference()
    matches = extract_markdown_endpoint(content, endpoint)

    if not matches:
        return {
            "found": False,
            "message": f"No documentation found for endpoint containing '{endpoint}'",
            "hint": "Try a shorter or different search term, like 'produtos' or 'contatos'"
        }

    return {
        "found": True,
        "endpoint_search": endpoint,
        "matches_count": len(matches),
        "documentation": matches
    }


@mcp.tool(tags={"documentation", "catalog"})
def docs_list_sections() -> dict[str, Any]:
    """List all main documentation sections (API resource categories) from the markdown docs.
    Use this to discover available API resources and their organization.

    Returns:
        A dictionary with all section names (categories like Produtos, Contatos, etc.)
        and their line counts for size estimation.
    """
    sections = load_markdown_sections()

    # Remove header and create summary
    sections_info = {}
    for name, section_content in sections.items():
        if name != "header":
            line_count = len(section_content.split("\n"))
            sections_info[name] = {
                "lines": line_count,
                "size_category": "large" if line_count > 1000 else "medium" if line_count > 300 else "small"
            }

    return {
        "total_sections": len(sections_info),
        "sections": sections_info
    }


@mcp.tool(tags={"documentation", "search"})
def docs_get_section(section_name: str) -> dict[str, Any]:
    """Get complete documentation for a specific API resource section/category from markdown.
    Use this to retrieve all endpoints and documentation within a category.
    WARNING: Large sections (like Produtos, Contatos) can be 1000+ lines.

    Args:
        section_name: Section name to retrieve (ex: "Produtos", "Contatos", "Notas fiscais").
                     Use docs_list_sections() to see all available sections.

    Returns:
        A dictionary with the complete section content including all endpoints,
        parameters, examples, and code samples for that category.
    """
    sections = load_markdown_sections()

    # Try exact match first
    if section_name in sections:
        section_content = sections[section_name]
        line_count = len(section_content.split("\n"))
        return {
            "found": True,
            "section_name": section_name,
            "lines": line_count,
            "content": section_content
        }

    # Try case-insensitive partial match
    section_lower = section_name.lower()
    matches = {name: content for name, content in sections.items()
               if section_lower in name.lower() and name != "header"}

    if matches:
        # Return first match if multiple
        matched_name = next(iter(matches.keys()))
        section_content = matches[matched_name]
        line_count = len(section_content.split("\n"))
        return {
            "found": True,
            "section_name": matched_name,
            "lines": line_count,
            "content": section_content,
            "note": f"Matched '{matched_name}' from search '{section_name}'"
        }

    return {
        "found": False,
        "message": f"No section found matching '{section_name}'",
        "hint": "Use list_documentation_sections() to see all available sections"
    }


@mcp.tool(tags={"documentation", "search"})
def docs_search_content(query: str, max_results: int = 5) -> dict[str, Any]:
    """Search for specific text/terms in the markdown documentation content.
    Use this to find endpoints or information by keywords, descriptions, or examples.
    Returns relevant sections containing the search term.

    Args:
        query: Text to search for (ex: "situacao", "status", "OAuth", "JSON").
               Search is case-insensitive.
        max_results: Maximum number of endpoint sections to return (default 5).

    Returns:
        A dictionary with matching documentation sections that contain the query term.
        Each match includes context showing where the term appears.
    """
    content = load_markdown_reference()
    header_index = build_markdown_header_index()
    query_lower = query.lower()
    matches = []
    seen_headers = set()  # O(1) deduplication instead of O(n²)

    lines = content.split("\n")
    i = 0

    while i < len(lines) and len(matches) < max_results:
        line = lines[i]

        # When we find a line containing the query
        if query_lower in line.lower():
            # Use header index for O(1) lookup instead of O(n) backtracking
            endpoint_header = header_index.get(i, "")

            # If we found an endpoint header and haven't seen it yet
            if endpoint_header and endpoint_header not in seen_headers:
                seen_headers.add(endpoint_header)

                # Find the section start
                section_start = i
                while section_start > 0 and lines[section_start] != endpoint_header:
                    section_start -= 1

                # Extract endpoint section
                section_lines = [lines[section_start]]
                j = section_start + 1
                while j < len(lines):
                    next_line = lines[j]
                    if (next_line.startswith("### ") and "`" in next_line) or (
                        next_line.startswith("## ")
                        and not next_line.startswith("### ")
                    ):
                        break
                    section_lines.append(next_line)
                    j += 1

                section_content = "\n".join(section_lines)

                matches.append(
                    {
                        "endpoint_header": endpoint_header,
                        "match_context": line.strip(),
                        "content": section_content,
                    }
                )

                # Skip past this section
                i = j
            else:
                i += 1
        else:
            i += 1

    return {
        "found": len(matches) > 0,
        "query": query,
        "matches_count": len(matches),
        "matches": matches,
    }
