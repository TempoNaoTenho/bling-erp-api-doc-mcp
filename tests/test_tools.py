from fastmcp import Client

import bling_doc_mcp.server  # noqa: F401 - registra tools/resources/prompts no mcp
from bling_doc_mcp.app import mcp
from bling_doc_mcp.utils.openapi import load_openapi


async def test_mcp_contract_basics() -> None:
    spec = load_openapi()
    assert "paths" in spec
    assert len(spec["paths"]) > 0

    async with Client(mcp) as client:
        tools = await client.list_tools()
        tool_names = {tool.name for tool in tools}
        assert "openapi_list_endpoints" in tool_names
        assert "openapi_get_endpoint_info" in tool_names
        assert "openapi_resolve_ref" in tool_names
        assert "docs_list_sections" in tool_names
        assert "docs_search_content" in tool_names

        resources = await client.list_resources()
        templates = await client.list_resource_templates()
        prompts = await client.list_prompts()

        resource_uris = {str(resource.uri) for resource in resources}
        template_uris = {str(template.uriTemplate) for template in templates}
        prompt_names = {prompt.name for prompt in prompts}

        assert "data://bling-openapi.json" in resource_uris
        assert "data://bling-openapi.json/info" in resource_uris
        assert "data://bling-openapi.json{?offset,limit}" in template_uris
        assert "api_usage_guide" in prompt_names
