#!/usr/bin/env python3
"""
Script to enhance the Bling API OpenAPI specification with:
- Request body examples
- Response body examples
- Code samples (curl, Python, JavaScript)
- Better descriptions and authentication docs
"""

import json
import sys
from copy import deepcopy
from pathlib import Path
from typing import Any


def add_auth_example(spec: dict[str, Any]) -> None:
    """Add authentication example to security schemes."""
    if "components" not in spec:
        spec["components"] = {}
    if "securitySchemes" not in spec["components"]:
        spec["components"]["securitySchemes"] = {}

    # Add OAuth2 bearer token scheme if not present
    if "OAuth2" not in spec["components"]["securitySchemes"]:
        spec["components"]["securitySchemes"]["OAuth2"] = {
            "type": "oauth2",
            "description": (
                "Autenticação OAuth2. Obtenha seu token em "
                "https://developer.bling.com.br/"
            ),
            "flows": {
                "authorizationCode": {
                    "authorizationUrl": "https://www.bling.com.br/Api/v3/oauth/authorize",
                    "tokenUrl": "https://www.bling.com.br/Api/v3/oauth/token",
                    "scopes": {}
                }
            }
        }


def create_code_samples(
    method: str,
    path: str,
    has_request_body: bool = False,
    request_example: dict[str, Any] | None = None,
) -> list[dict[str, str]]:
    """Create code samples for curl, Python, and JavaScript."""
    samples = []

    # Curl example
    curl_cmd = f'curl -X {method.upper()} "https://api.bling.com.br/Api/v3{path}" \\\n'
    curl_cmd += '  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \\\n'
    curl_cmd += '  -H "Content-Type: application/json"'

    if has_request_body and request_example:
        body_json = json.dumps(request_example, ensure_ascii=False, indent=2)
        curl_cmd += f" \\\n  -d '{body_json}'"

    samples.append({
        "lang": "Shell",
        "label": "cURL",
        "source": curl_cmd
    })

    # Python example
    python_code = "import requests\n\n"
    python_code += f'url = "https://api.bling.com.br/Api/v3{path}"\n'
    python_code += "headers = {\n"
    python_code += '    "Authorization": "Bearer YOUR_ACCESS_TOKEN",\n'
    python_code += '    "Content-Type": "application/json"\n'
    python_code += "}\n"

    if has_request_body and request_example:
        python_code += f"\ndata = {json.dumps(request_example, ensure_ascii=False, indent=4)}\n"
        python_code += f"\nresponse = requests.{method}(url, headers=headers, json=data)\n"
    else:
        python_code += f"\nresponse = requests.{method}(url, headers=headers)\n"

    python_code += "print(response.json())"

    samples.append({
        "lang": "Python",
        "label": "Python (requests)",
        "source": python_code
    })

    # JavaScript example
    js_code = f'const url = "https://api.bling.com.br/Api/v3{path}";\n'
    js_code += "const headers = {\n"
    js_code += '  "Authorization": "Bearer YOUR_ACCESS_TOKEN",\n'
    js_code += '  "Content-Type": "application/json"\n'
    js_code += "};\n"

    if has_request_body and request_example:
        js_code += f"\nconst data = {json.dumps(request_example, ensure_ascii=False, indent=2)};\n"
        js_code += f'\nfetch(url, {{\n  method: "{method.upper()}",\n'
        js_code += "  headers: headers,\n"
        js_code += "  body: JSON.stringify(data)\n"
        js_code += "})"
    else:
        js_code += f'\nfetch(url, {{\n  method: "{method.upper()}",\n'
        js_code += "  headers: headers\n"
        js_code += "})"

    js_code += "\n  .then(response => response.json())\n"
    js_code += "  .then(data => console.log(data))\n"
    js_code += '  .catch(error => console.error("Error:", error));'

    samples.append({
        "lang": "JavaScript",
        "label": "JavaScript (fetch)",
        "source": js_code
    })

    return samples


# Realistic examples for common Bling ERP entities
EXAMPLES = {
    "Produtos": {
        "request": {
            "nome": "Camiseta Básica Preta",
            "codigo": "CAM-BAS-PTA-M",
            "preco": 49.90,
            "tipo": "P",
            "situacao": "A",
            "formato": "S",
            "descricaoCurta": "Camiseta básica 100% algodão",
            "descricaoComplementar": "Camiseta básica preta, tamanho M, 100% algodão",
            "unidade": "UN",
            "pesoLiquido": 0.200,
            "pesoBruto": 0.250,
            "gtin": "7891234567890",
            "gtinEmbalagem": "17891234567897",
            "dimensoes": {
                "largura": 30,
                "altura": 40,
                "profundidade": 2,
                "unidadeMedida": 7
            }
        },
        "response_list": {
            "data": [
                {
                    "id": 12345678,
                    "nome": "Camiseta Básica Preta",
                    "codigo": "CAM-BAS-PTA-M",
                    "preco": 49.90,
                    "tipo": "P",
                    "situacao": "A",
                    "formato": "S"
                },
                {
                    "id": 12345679,
                    "nome": "Camiseta Básica Branca",
                    "codigo": "CAM-BAS-BCA-M",
                    "preco": 49.90,
                    "tipo": "P",
                    "situacao": "A",
                    "formato": "S"
                }
            ]
        },
        "response_single": {
            "data": {
                "id": 12345678,
                "nome": "Camiseta Básica Preta",
                "codigo": "CAM-BAS-PTA-M",
                "preco": 49.90,
                "tipo": "P",
                "situacao": "A",
                "formato": "S",
                "descricaoCurta": "Camiseta básica 100% algodão",
                "unidade": "UN",
                "pesoLiquido": 0.200,
                "pesoBruto": 0.250
            }
        }
    },
    "Contatos": {
        "request": {
            "nome": "João Silva",
            "codigo": "CLI-001",
            "situacao": "A",
            "numeroDocumento": "12345678901",
            "telefone": "11987654321",
            "celular": "11987654321",
            "email": "joao.silva@email.com",
            "endereco": {
                "geral": {
                    "endereco": "Rua das Flores",
                    "numero": "123",
                    "complemento": "Apto 45",
                    "bairro": "Centro",
                    "cep": "01234-567",
                    "municipio": "São Paulo",
                    "uf": "SP",
                    "pais": "Brasil"
                }
            },
            "tipo": {
                "tipoContato": "cliente"
            }
        },
        "response_single": {
            "data": {
                "id": 12345678,
                "nome": "João Silva",
                "codigo": "CLI-001",
                "situacao": "A",
                "numeroDocumento": "12345678901",
                "email": "joao.silva@email.com"
            }
        }
    },
    "Pedidos": {
        "request": {
            "numero": "PED-2024-001",
            "data": "2024-01-15",
            "observacoes": "Pedido de teste - entregar pela manhã",
            "observacoesInternas": "Cliente preferencial",
            "contato": {
                "id": 12345678
            },
            "itens": [
                {
                    "produto": {
                        "id": 12345678
                    },
                    "quantidade": 2,
                    "valor": 49.90,
                    "descricao": "Camiseta Básica Preta"
                }
            ],
            "parcelas": [
                {
                    "data": "2024-01-15",
                    "valor": 99.80,
                    "observacoes": "Pagamento à vista",
                    "formaPagamento": {
                        "id": 12345678
                    }
                }
            ],
            "transporte": {
                "transportador": {
                    "nome": "Transportadora XYZ"
                },
                "fretePorConta": 0,
                "valorFrete": 15.00
            }
        },
        "response_single": {
            "data": {
                "id": 12345678,
                "numero": "PED-2024-001",
                "data": "2024-01-15",
                "situacao": {
                    "id": 1,
                    "valor": "Em aberto"
                },
                "contato": {
                    "id": 12345678,
                    "nome": "João Silva"
                },
                "total": 114.80
            }
        }
    },
    "NotasFiscais": {
        "request": {
            "tipo": 1,
            "situacao": 1,
            "numero": "12345",
            "serie": "1",
            "data": "2024-01-15",
            "dataEmissao": "2024-01-15T10:30:00-03:00",
            "naturezaOperacao": {
                "id": 12345678
            },
            "contato": {
                "id": 12345678
            },
            "itens": [
                {
                    "produto": {
                        "id": 12345678
                    },
                    "quantidade": 2,
                    "valor": 49.90,
                    "descricao": "Camiseta Básica Preta"
                }
            ],
            "transporte": {
                "fretePorConta": 0,
                "transportador": {
                    "nome": "Transportadora XYZ"
                }
            }
        },
        "response_single": {
            "data": {
                "id": 12345678,
                "numero": "12345",
                "serie": "1",
                "situacao": {
                    "valor": 1,
                    "descricao": "Aguardando processamento"
                },
                "chaveAcesso": "12345678901234567890123456789012345678901234",
                "xml": "PHhtbCB2ZXJzaW9uPSIxLjAiPz4=..."
            }
        }
    }
}


def get_example_for_tag(tag: str, example_type: str) -> dict[str, Any] | None:
    """Get example data for a specific tag."""
    # Map tag names to example keys
    tag_mapping = {
        "Produtos": "Produtos",
        "Contatos": "Contatos",
        "Pedidos - Vendas": "Pedidos",
        "Pedidos - Compras": "Pedidos",
        "Notas Fiscais Eletrônicas": "NotasFiscais",
        "Notas Fiscais de Consumidor Eletrônicas": "NotasFiscais",
        "Notas Fiscais de Serviço Eletrônicas": "NotasFiscais",
    }

    example_key = tag_mapping.get(tag)
    if not example_key or example_key not in EXAMPLES:
        return None

    return EXAMPLES[example_key].get(example_type)


def enhance_endpoint(
    path: str,
    method: str,
    endpoint: dict[str, Any]
) -> dict[str, Any]:
    """Enhance a single endpoint with examples and code samples."""
    enhanced = deepcopy(endpoint)
    tags = enhanced.get("tags", [])
    tag = tags[0] if tags else ""

    # Add request body examples for POST/PUT/PATCH
    if method in ["post", "put", "patch"]:
        request_body = enhanced.get("requestBody", {})
        if request_body and "content" in request_body:
            example_data = get_example_for_tag(tag, "request")
            if example_data:
                for media_type in request_body["content"].values():
                    if "example" not in media_type and "examples" not in media_type:
                        media_type["example"] = example_data

    # Add response examples
    responses = enhanced.get("responses", {})
    for status_code, response in responses.items():
        if "content" in response:
            for media_type in response["content"].values():
                if "example" not in media_type and "examples" not in media_type:
                    # Determine which example type to use
                    if status_code == "200":
                        if method == "get" and "{" not in path:
                            # List endpoint
                            example_data = get_example_for_tag(tag, "response_list")
                        else:
                            # Single resource endpoint
                            example_data = get_example_for_tag(tag, "response_single")
                    elif status_code in ["201", "202"]:
                        example_data = get_example_for_tag(tag, "response_single")
                    elif status_code == "400":
                        example_data = {
                            "error": {
                                "type": "validation_error",
                                "message": "Dados inválidos fornecidos",
                                "fields": {
                                    "nome": ["O campo nome é obrigatório"]
                                }
                            }
                        }
                    elif status_code == "401":
                        example_data = {
                            "error": {
                                "type": "authentication_error",
                                "message": "Token de autenticação inválido ou expirado"
                            }
                        }
                    elif status_code == "404":
                        example_data = {
                            "error": {
                                "type": "not_found",
                                "message": "Recurso não encontrado"
                            }
                        }
                    else:
                        example_data = None

                    if example_data:
                        media_type["example"] = example_data

    # Add code samples for important endpoints
    priority_tags = [
        "Produtos", "Contatos", "Pedidos - Vendas", "Pedidos - Compras",
        "Notas Fiscais Eletrônicas", "Notas Fiscais de Consumidor Eletrônicas"
    ]

    if tag in priority_tags:
        has_request = method in ["post", "put", "patch"]
        request_example = None
        if has_request:
            request_example = get_example_for_tag(tag, "request")

        code_samples = create_code_samples(method, path, has_request, request_example)
        enhanced["x-codeSamples"] = code_samples

    return enhanced


def enhance_openapi_spec(spec: dict[str, Any]) -> dict[str, Any]:
    """Enhance the entire OpenAPI specification."""
    enhanced_spec = deepcopy(spec)

    # Add authentication documentation
    add_auth_example(enhanced_spec)

    # Enhance each endpoint
    paths = enhanced_spec.get("paths", {})
    for path, methods in paths.items():
        for method in ["get", "post", "put", "patch", "delete"]:
            if method in methods and isinstance(methods[method], dict):
                methods[method] = enhance_endpoint(path, method, methods[method])

    return enhanced_spec


def main() -> int:
    """Main function."""
    base_dir = Path(__file__).parent.parent
    input_file = base_dir / "src/bling_doc_mcp/files/bling-openapi.json"
    output_file = base_dir / "src/bling_doc_mcp/files/bling-openapi-enhanced.json"

    print(f"Loading OpenAPI spec from {input_file}...")
    with open(input_file, encoding="utf-8") as f:
        spec = json.load(f)

    print("Enhancing OpenAPI spec...")
    enhanced_spec = enhance_openapi_spec(spec)

    print(f"Writing enhanced spec to {output_file}...")
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(enhanced_spec, f, ensure_ascii=False, indent=2)

    # Calculate stats
    total_endpoints = 0
    endpoints_with_examples = 0
    endpoints_with_code_samples = 0

    for path, methods in enhanced_spec.get("paths", {}).items():
        for method in ["get", "post", "put", "patch", "delete"]:
            if method in methods:
                total_endpoints += 1
                endpoint = methods[method]

                # Check for examples
                has_example = False
                if "requestBody" in endpoint:
                    content = endpoint["requestBody"].get("content", {})
                    if any("example" in v or "examples" in v for v in content.values()):
                        has_example = True

                responses = endpoint.get("responses", {})
                for response in responses.values():
                    content = response.get("content", {})
                    if any("example" in v or "examples" in v for v in content.values()):
                        has_example = True
                        break

                if has_example:
                    endpoints_with_examples += 1

                if "x-codeSamples" in endpoint:
                    endpoints_with_code_samples += 1

    print("\nEnhancement Summary:")
    print(f"  Total endpoints: {total_endpoints}")
    print(f"  Endpoints with examples: {endpoints_with_examples} ({endpoints_with_examples/total_endpoints*100:.1f}%)")
    print(f"  Endpoints with code samples: {endpoints_with_code_samples} ({endpoints_with_code_samples/total_endpoints*100:.1f}%)")

    print(f"\n✅ Enhanced OpenAPI spec saved to {output_file}")
    print("\nTo use the enhanced version, replace the original file:")
    print(f"  mv {output_file} {input_file}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
