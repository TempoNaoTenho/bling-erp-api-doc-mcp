from __future__ import annotations

from typing import Any


class RefResolutionError(ValueError):
    """Raised when a $ref cannot be resolved safely."""


def _decode_json_pointer_token(token: str) -> str:
    return token.replace("~1", "/").replace("~0", "~")


def _resolve_json_pointer(document: dict[str, Any], ref: str) -> Any:
    if not ref.startswith("#/"):
        raise RefResolutionError(
            f"Unsupported ref '{ref}'. Only local refs like '#/components/...' are supported."
        )

    current: Any = document
    tokens = ref[2:].split("/")
    for raw_token in tokens:
        token = _decode_json_pointer_token(raw_token)
        if isinstance(current, dict):
            if token not in current:
                raise RefResolutionError(f"Ref '{ref}' points to missing key '{token}'.")
            current = current[token]
            continue

        if isinstance(current, list):
            if not token.isdigit():
                raise RefResolutionError(
                    f"Ref '{ref}' points to list but token '{token}' is not an index."
                )
            index = int(token)
            if index >= len(current):
                raise RefResolutionError(
                    f"Ref '{ref}' points to index '{index}' outside list bounds."
                )
            current = current[index]
            continue

        raise RefResolutionError(
            f"Ref '{ref}' cannot be traversed at token '{token}' ({type(current).__name__})."
        )

    return current


def _resolve_nested_refs(
    value: Any,
    openapi: dict[str, Any],
    seen_refs: set[str],
    *,
    depth: int,
    max_depth: int,
) -> Any:
    if depth > max_depth:
        raise RefResolutionError(
            f"Max ref depth reached ({max_depth}). Possible circular chain: {sorted(seen_refs)}"
        )

    if isinstance(value, dict):
        if "$ref" in value:
            ref = value["$ref"]
            if not isinstance(ref, str):
                raise RefResolutionError("Invalid '$ref': expected string.")
            if ref in seen_refs:
                raise RefResolutionError(f"Circular ref detected: {ref}")

            target = _resolve_json_pointer(openapi, ref)
            resolved_target = _resolve_nested_refs(
                target, openapi, seen_refs | {ref}, depth=depth + 1, max_depth=max_depth
            )
            siblings = {k: v for k, v in value.items() if k != "$ref"}
            if siblings and isinstance(resolved_target, dict):
                resolved_siblings = _resolve_nested_refs(
                    siblings, openapi, seen_refs, depth=depth + 1, max_depth=max_depth
                )
                return {**resolved_target, **resolved_siblings}
            return resolved_target

        return {
            key: _resolve_nested_refs(
                nested, openapi, seen_refs, depth=depth + 1, max_depth=max_depth
            )
            for key, nested in value.items()
        }

    if isinstance(value, list):
        return [
            _resolve_nested_refs(item, openapi, seen_refs, depth=depth + 1, max_depth=max_depth)
            for item in value
        ]

    return value


def resolve_openapi_ref(
    openapi: dict[str, Any], ref: str, *, max_depth: int = 25
) -> Any:
    """Resolve one OpenAPI local reference recursively."""
    if max_depth < 1:
        raise RefResolutionError("max_depth must be >= 1.")

    target = _resolve_json_pointer(openapi, ref)
    return _resolve_nested_refs(target, openapi, {ref}, depth=0, max_depth=max_depth)
