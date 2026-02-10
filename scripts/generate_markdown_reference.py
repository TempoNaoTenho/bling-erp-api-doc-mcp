#!/usr/bin/env python3
"""
Generate enhanced markdown reference from OpenAPI spec with examples and code samples.
"""

import json
import sys
from pathlib import Path
from typing import Any


def format_param_type(param: dict[str, Any]) -> str:
    """Format parameter type information."""
    schema = param.get("schema", {})
    param_type = schema.get("type", "any")
    if "enum" in schema:
        return f"{param_type} (enum)"
    if param_type == "array":
        items_type = schema.get("items", {}).get("type", "any")
        return f"array&lt;{items_type}&gt;"
    return param_type


def resolve_ref(spec: dict[str, Any], ref: str) -> dict[str, Any] | None:
    """Resolve a $ref in the spec."""
    if not ref.startswith("#/"):
        return None

    parts = ref[2:].split("/")
    current = spec

    for part in parts:
        if not isinstance(current, dict) or part not in current:
            return None
        current = current[part]

    return current if isinstance(current, dict) else None


def format_parameters_table(parameters: list[dict[str, Any]], spec: dict[str, Any]) -> str:
    """Format parameters as markdown table."""
    if not parameters:
        return ""

    lines = [
        "| Name | In | Required | Type | Description |",
        "|------|----|----------|------|-------------|"
    ]

    for param in parameters:
        # Resolve $ref if present
        if "$ref" in param:
            resolved = resolve_ref(spec, param["$ref"])
            if resolved:
                param = resolved

        # Skip parameters without name (invalid/unresolved refs)
        name = param.get("name", "")
        if not name:
            continue

        location = param.get("in", "")
        required = "**Yes**" if param.get("required") else "No"
        param_type = format_param_type(param)
        description = param.get("description", "").replace("\n", "<br>")

        lines.append(f"| {name} | {location} | {required} | {param_type} | {description} |")

    # If only headers, return empty (no valid parameters)
    if len(lines) == 2:
        return ""

    return "\n".join(lines)


def format_code_sample(sample: dict[str, Any]) -> str:
    """Format a code sample."""
    lang = sample.get("lang", "")
    label = sample.get("label", "")
    source = sample.get("source", "")

    # Map language names to markdown code fence languages
    lang_map = {
        "Shell": "bash",
        "Python": "python",
        "JavaScript": "javascript",
    }

    fence_lang = lang_map.get(lang, lang.lower())

    return f"**{label}**\n\n```{fence_lang}\n{source}\n```"


def format_example(example: dict[str, Any], title: str) -> str:
    """Format a JSON example."""
    json_str = json.dumps(example, ensure_ascii=False, indent=2)
    return f"**{title}**\n\n```json\n{json_str}\n```"


def generate_endpoint_section(
    path: str,
    method: str,
    endpoint: dict[str, Any],
    spec: dict[str, Any]
) -> str:
    """Generate markdown section for a single endpoint."""
    lines = []

    # Header
    summary = endpoint.get("summary", "")
    description = endpoint.get("description", "")

    lines.append(f"### {method.upper()} `{path}`")
    lines.append("")
    if summary:
        lines.append(f"**{summary}**")
        lines.append("")
    if description and description != summary:
        lines.append(description)
        lines.append("")

    # Parameters
    parameters = endpoint.get("parameters", [])
    if parameters:
        param_table = format_parameters_table(parameters, spec)
        if param_table:  # Only add section if there are valid parameters
            lines.append("#### Parameters")
            lines.append("")
            lines.append(param_table)
            lines.append("")

    # Request Body
    request_body = endpoint.get("requestBody", {})
    if request_body:
        lines.append("#### Request Body")
        lines.append("")
        content = request_body.get("content", {})

        for media_type, media_spec in content.items():
            lines.append(f"**Content-Type:** `{media_type}`")
            lines.append("")

            # Add example if present
            if "example" in media_spec:
                lines.append(format_example(media_spec["example"], "Example Request"))
                lines.append("")

    # Responses
    responses = endpoint.get("responses", {})
    if responses:
        lines.append("#### Responses")
        lines.append("")

        for status_code, response in sorted(responses.items()):
            desc = response.get("description", "")
            lines.append(f"**{status_code}** - {desc}")
            lines.append("")

            content = response.get("content", {})
            for media_type, media_spec in content.items():
                if "example" in media_spec:
                    lines.append(format_example(
                        media_spec["example"],
                        f"Example Response ({status_code})"
                    ))
                    lines.append("")

    # Code Samples
    code_samples = endpoint.get("x-codeSamples", [])
    if code_samples:
        lines.append("#### Code Examples")
        lines.append("")

        for sample in code_samples:
            lines.append(format_code_sample(sample))
            lines.append("")

    lines.append("---")
    lines.append("")

    return "\n".join(lines)


def generate_markdown_reference(spec: dict[str, Any]) -> str:
    """Generate complete markdown reference from OpenAPI spec."""
    lines = []

    # Header
    info = spec.get("info", {})
    lines.append(f"# {info.get('title', 'API Documentation')}")
    lines.append("")
    lines.append(f"**Version:** {info.get('version', '1.0.0')}")
    lines.append("")
    if "description" in info:
        lines.append(info["description"])
        lines.append("")

    # Authentication Section
    lines.append("## Authentication")
    lines.append("")
    lines.append("The Bling API uses OAuth 2.0 for authentication. You need to obtain an access token to make API calls.")
    lines.append("")
    lines.append("### Getting Your Access Token")
    lines.append("")
    lines.append("1. Register your application at https://developer.bling.com.br/")
    lines.append("2. Obtain your Client ID and Client Secret")
    lines.append("3. Follow the OAuth 2.0 authorization code flow to get an access token")
    lines.append("")
    lines.append("### Using the Access Token")
    lines.append("")
    lines.append("Include the access token in the `Authorization` header of all API requests:")
    lines.append("")
    lines.append("```")
    lines.append("Authorization: Bearer YOUR_ACCESS_TOKEN")
    lines.append("```")
    lines.append("")

    # Base URLs
    servers = spec.get("servers", [])
    if servers:
        lines.append("## Base URLs")
        for server in servers:
            url = server.get("url", "")
            desc = server.get("description", "")
            lines.append(f"- `{url}`: {desc}")
        lines.append("")

    # Group endpoints by tag
    paths = spec.get("paths", {})
    endpoints_by_tag: dict[str, list[tuple[str, str, dict[str, Any]]]] = {}

    for path, methods in paths.items():
        for method in ["get", "post", "put", "patch", "delete"]:
            if method in methods and isinstance(methods[method], dict):
                endpoint = methods[method]
                tags = endpoint.get("tags", ["Other"])
                tag = tags[0]

                if tag not in endpoints_by_tag:
                    endpoints_by_tag[tag] = []

                endpoints_by_tag[tag].append((path, method, endpoint))

    # Generate sections for each tag
    for tag in sorted(endpoints_by_tag.keys()):
        lines.append(f"## {tag}")
        lines.append("")

        for path, method, endpoint in endpoints_by_tag[tag]:
            lines.append(generate_endpoint_section(path, method, endpoint, spec))

    return "\n".join(lines)


def main() -> int:
    """Main function."""
    base_dir = Path(__file__).parent.parent
    input_file = base_dir / "src/bling_doc_mcp/files/bling-openapi.json"
    output_file = base_dir / "src/bling_doc_mcp/files/bling-openapi-reference.md"
    backup_file = base_dir / "src/bling_doc_mcp/files/bling-openapi-reference.md.backup"

    print(f"Loading OpenAPI spec from {input_file}...")
    with open(input_file, encoding="utf-8") as f:
        spec = json.load(f)

    print("Generating markdown reference...")
    markdown = generate_markdown_reference(spec)

    # Backup existing file
    if output_file.exists():
        print(f"Backing up existing file to {backup_file}...")
        output_file.rename(backup_file)

    print(f"Writing markdown reference to {output_file}...")
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(markdown)

    # Stats
    lines_count = len(markdown.split("\n"))
    size_kb = len(markdown.encode("utf-8")) / 1024

    print("\n✅ Markdown reference generated successfully!")
    print(f"  Lines: {lines_count:,}")
    print(f"  Size: {size_kb:.1f} KB")

    return 0


if __name__ == "__main__":
    sys.exit(main())
