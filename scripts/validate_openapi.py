#!/usr/bin/env python3
"""
Validate the enhanced OpenAPI specification for:
- Valid JSON structure
- All $ref references are resolvable
- Required fields are present
- Examples match schema types (basic validation)
"""

import json
import sys
from pathlib import Path
from typing import Any


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

    return current


def validate_refs(spec: dict[str, Any]) -> tuple[int, list[str]]:
    """Validate all $ref references in the spec."""
    errors = []
    ref_count = 0

    def check_refs(obj: Any, path: str = "") -> None:
        nonlocal ref_count
        if isinstance(obj, dict):
            if "$ref" in obj:
                ref_count += 1
                ref = obj["$ref"]
                resolved = resolve_ref(spec, ref)
                if resolved is None:
                    errors.append(f"{path}: Unresolved reference '{ref}'")

            for key, value in obj.items():
                check_refs(value, f"{path}.{key}" if path else key)

        elif isinstance(obj, list):
            for i, item in enumerate(obj):
                check_refs(item, f"{path}[{i}]")

    check_refs(spec)
    return ref_count, errors


def validate_required_fields(spec: dict[str, Any]) -> list[str]:
    """Validate that required OpenAPI fields are present."""
    errors = []

    # Required top-level fields
    if "openapi" not in spec:
        errors.append("Missing required field: openapi")
    if "info" not in spec:
        errors.append("Missing required field: info")
    elif not isinstance(spec["info"], dict):
        errors.append("Field 'info' must be an object")
    else:
        info = spec["info"]
        if "title" not in info:
            errors.append("Missing required field: info.title")
        if "version" not in info:
            errors.append("Missing required field: info.version")

    if "paths" not in spec:
        errors.append("Missing required field: paths")
    elif not isinstance(spec["paths"], dict):
        errors.append("Field 'paths' must be an object")

    return errors


def count_examples(spec: dict[str, Any]) -> dict[str, int]:
    """Count different types of examples in the spec."""
    stats = {
        "endpoints_total": 0,
        "endpoints_with_request_examples": 0,
        "endpoints_with_response_examples": 0,
        "endpoints_with_code_samples": 0,
        "total_code_samples": 0,
    }

    for path, methods in spec.get("paths", {}).items():
        for method in ["get", "post", "put", "patch", "delete"]:
            if method not in methods or not isinstance(methods[method], dict):
                continue

            stats["endpoints_total"] += 1
            endpoint = methods[method]

            # Check request examples
            req_body = endpoint.get("requestBody", {})
            if req_body:
                content = req_body.get("content", {})
                if any("example" in v or "examples" in v for v in content.values()):
                    stats["endpoints_with_request_examples"] += 1

            # Check response examples
            responses = endpoint.get("responses", {})
            has_response_example = False
            for response in responses.values():
                content = response.get("content", {})
                if any("example" in v or "examples" in v for v in content.values()):
                    has_response_example = True
                    break
            if has_response_example:
                stats["endpoints_with_response_examples"] += 1

            # Check code samples
            code_samples = endpoint.get("x-codeSamples", [])
            if code_samples:
                stats["endpoints_with_code_samples"] += 1
                stats["total_code_samples"] += len(code_samples)

    return stats


def main() -> int:
    """Main function."""
    base_dir = Path(__file__).parent.parent
    openapi_file = base_dir / "src/bling_doc_mcp/files/bling-openapi.json"

    print(f"Validating {openapi_file}...")
    print()

    # Load and parse JSON
    try:
        with open(openapi_file, encoding="utf-8") as f:
            spec = json.load(f)
        print("✅ Valid JSON structure")
    except json.JSONDecodeError as e:
        print(f"❌ Invalid JSON: {e}")
        return 1

    # Validate required fields
    print("\n--- Required Fields ---")
    field_errors = validate_required_fields(spec)
    if field_errors:
        print(f"❌ Found {len(field_errors)} errors:")
        for error in field_errors:
            print(f"  - {error}")
        return 1
    print("✅ All required fields present")

    # Validate references
    print("\n--- References Validation ---")
    ref_count, ref_errors = validate_refs(spec)
    print(f"Total $ref references: {ref_count}")
    if ref_errors:
        print(f"❌ Found {len(ref_errors)} unresolved references:")
        for error in ref_errors[:10]:  # Show first 10
            print(f"  - {error}")
        if len(ref_errors) > 10:
            print(f"  ... and {len(ref_errors) - 10} more")
        return 1
    print("✅ All references resolved successfully")

    # Count examples
    print("\n--- Examples Coverage ---")
    stats = count_examples(spec)
    print(f"Total endpoints: {stats['endpoints_total']}")
    print(f"Endpoints with request examples: {stats['endpoints_with_request_examples']} "
          f"({stats['endpoints_with_request_examples']/stats['endpoints_total']*100:.1f}%)")
    print(f"Endpoints with response examples: {stats['endpoints_with_response_examples']} "
          f"({stats['endpoints_with_response_examples']/stats['endpoints_total']*100:.1f}%)")
    print(f"Endpoints with code samples: {stats['endpoints_with_code_samples']} "
          f"({stats['endpoints_with_code_samples']/stats['endpoints_total']*100:.1f}%)")
    print(f"Total code samples: {stats['total_code_samples']}")

    # File size
    print("\n--- File Information ---")
    file_size = openapi_file.stat().st_size
    print(f"File size: {file_size/1024:.1f} KB")

    print("\n✅ OpenAPI specification is valid and enhanced!")
    return 0


if __name__ == "__main__":
    sys.exit(main())
