from bling_doc_mcp.app import mcp
from bling_doc_mcp.utils.openapi import (
    load_markdown_sections,
    load_openapi,
)


@mcp.prompt(tags={"documentation", "quickstart"})
def quickstart_guide(resource: str) -> str:
    """Gera um guia rápido de início para um recurso específico da API Bling ERP.

    Retorna uma visão geral do recurso com seus principais endpoints, operações
    disponíveis (CRUD), e um exemplo prático de integração. Ideal para desenvolvedores
    que querem começar rapidamente com um recurso específico.

    Args:
        resource: Nome do recurso da API (ex: "produtos", "contatos", "pedidos",
                  "notas fiscais", "estoque"). Aceita termos em português.

    Retorna um markdown contendo:
        - Visão geral do recurso
        - Lista de endpoints principais (GET, POST, PUT, DELETE)
        - Exemplo de fluxo de integração
        - Links para documentação completa
    """
    # Normalize input
    normalized = resource.strip().lower()
    if not normalized:
        return _invalid_resource_error()

    # Try to find matching section in markdown
    sections = load_markdown_sections()

    # Direct match first
    matched_section = None
    matched_name = None

    for section_name, section_content in sections.items():
        if section_name.lower() == normalized:
            matched_section = section_content
            matched_name = section_name
            break

    # Partial match if no direct match
    if not matched_section:
        for section_name, section_content in sections.items():
            if normalized in section_name.lower():
                matched_section = section_content
                matched_name = section_name
                break

    if matched_section:
        return _build_quickstart_from_section(matched_name, matched_section)

    # Try common aliases
    aliases = {
        "produto": "Produtos",
        "produtos": "Produtos",
        "contato": "Contatos",
        "contatos": "Contatos",
        "cliente": "Contatos",
        "clientes": "Contatos",
        "pedido": "Pedidos - Vendas",
        "pedidos": "Pedidos - Vendas",
        "venda": "Pedidos - Vendas",
        "vendas": "Pedidos - Vendas",
        "compra": "Pedidos - Compras",
        "compras": "Pedidos - Compras",
        "nfe": "Notas fiscais",
        "nf-e": "Notas fiscais",
        "nota fiscal": "Notas fiscais",
        "notas fiscais": "Notas fiscais",
        "estoque": "Estoques",
        "estoques": "Estoques",
    }

    if normalized in aliases:
        section_name = aliases[normalized]
        if section_name in sections:
            return _build_quickstart_from_section(
                section_name, sections[section_name]
            )

    return _resource_not_found_error(resource)


@mcp.prompt(tags={"documentation", "search"})
def find_endpoint_by_action(action: str) -> str:
    """Encontra endpoints relevantes baseado em uma ação ou caso de uso específico.

    Use este prompt quando você souber O QUE quer fazer, mas não souber QUAL endpoint
    usar. Aceita descrições em linguagem natural em português.

    Args:
        action: Descrição da ação desejada em português (ex: "criar produto",
                "atualizar estoque", "listar pedidos pendentes", "buscar cliente por CPF",
                "enviar nota fiscal", "consultar saldo", "adicionar item ao pedido").

    Retorna um markdown contendo:
        - Endpoints recomendados para a ação
        - Método HTTP apropriado (GET, POST, PUT, DELETE)
        - Parâmetros necessários
        - Exemplo de request
        - Dicas de uso

    Exemplos de uso:
        - "criar um novo produto"
        - "atualizar preço de produto"
        - "listar todos os clientes"
        - "buscar pedidos por status"
        - "emitir nota fiscal"
        - "consultar saldo do estoque"
    """
    # Normalize input
    action_lower = action.strip().lower()
    if not action_lower:
        return _invalid_action_error()

    # Load OpenAPI spec for endpoint analysis
    openapi_spec = load_openapi()
    paths = openapi_spec.get("paths", {})

    # Action mapping patterns
    recommendations = []

    # Analyze action intent
    is_create = any(
        word in action_lower
        for word in ["criar", "adicionar", "novo", "nova", "cadastrar", "registrar"]
    )
    is_update = any(
        word in action_lower
        for word in ["atualizar", "modificar", "alterar", "editar", "mudar"]
    )
    is_delete = any(
        word in action_lower
        for word in ["deletar", "remover", "excluir", "apagar"]
    )
    is_list = any(
        word in action_lower
        for word in ["listar", "buscar", "consultar", "obter", "ver", "pesquisar"]
    )

    # Extract resource mentions
    resource_keywords = {
        "produto": ["/produtos"],
        "contato": ["/contatos"],
        "cliente": ["/contatos"],
        "pedido": ["/pedidos"],
        "venda": ["/pedidos/vendas"],
        "compra": ["/pedidos/compras"],
        "nota": ["/nfe", "/nfce", "/nfse"],
        "nfe": ["/nfe"],
        "estoque": ["/estoques", "/depositos"],
        "categoria": ["/categorias"],
        "lote": ["/produtos/lotes"],
        "preço": ["/produtos"],
        "preco": ["/produtos"],
        "fornecedor": ["/contatos"],
        "pagamento": ["/contaspagar", "/contasreceber"],
        "boleto": ["/contasreceber"],
    }

    # Find relevant endpoints
    relevant_paths = []
    for keyword, paths_list in resource_keywords.items():
        if keyword in action_lower:
            for path in paths_list:
                # Find matching paths in OpenAPI
                for api_path, methods in paths.items():
                    if path in api_path:
                        relevant_paths.append((api_path, methods))

    if not relevant_paths:
        # No specific resource found, try to help anyway
        return _action_helper_fallback(action)

    # Build recommendations based on intent
    if is_create:
        recommendations = _find_create_endpoints(relevant_paths)
    elif is_update:
        recommendations = _find_update_endpoints(relevant_paths)
    elif is_delete:
        recommendations = _find_delete_endpoints(relevant_paths)
    elif is_list:
        recommendations = _find_list_endpoints(relevant_paths)
    else:
        # Show all relevant endpoints
        recommendations = _find_all_endpoints(relevant_paths)

    if recommendations:
        return _build_action_guide(action, recommendations)

    return _no_matching_endpoints_error(action)


# Helper functions


def _invalid_resource_error() -> str:
    return (
        "## Erro: Recurso não especificado\n\n"
        "Informe o nome de um recurso da API, por exemplo:\n"
        "- `produtos`\n"
        "- `contatos`\n"
        "- `pedidos`\n"
        "- `notas fiscais`\n"
        "- `estoque`\n\n"
        "**Dica:** Use a ferramenta `docs_list_sections()` para ver todos os recursos disponíveis."
    )


def _resource_not_found_error(resource: str) -> str:
    return (
        f"## Recurso '{resource}' não encontrado\n\n"
        f"O recurso '{resource}' não foi encontrado na documentação.\n\n"
        "### Recursos disponíveis:\n"
        "- **Produtos** - Gestão de produtos e variações\n"
        "- **Contatos** - Clientes, fornecedores e transportadoras\n"
        "- **Pedidos - Vendas** - Pedidos de venda\n"
        "- **Pedidos - Compras** - Pedidos de compra\n"
        "- **Notas fiscais** - NF-e, NFC-e, NFS-e\n"
        "- **Estoques** - Controle de estoque e depósitos\n"
        "- **Categorias** - Categorias de produtos\n"
        "- **Contas a pagar** - Gestão financeira\n"
        "- **Contas a receber** - Gestão financeira\n\n"
        "**Dica:** Use `docs_list_sections()` para ver a lista completa."
    )


def _invalid_action_error() -> str:
    return (
        "## Erro: Ação não especificada\n\n"
        "Descreva o que você quer fazer com a API, por exemplo:\n"
        "- `criar um novo produto`\n"
        "- `atualizar preço de produto`\n"
        "- `listar todos os clientes`\n"
        "- `buscar pedidos por status`\n"
        "- `emitir nota fiscal`\n"
        "- `consultar saldo do estoque`\n\n"
        "**Dica:** Use linguagem natural em português."
    )


def _build_quickstart_from_section(section_name: str, section_content: str) -> str:
    """Build a quickstart guide from a markdown section."""
    lines = section_content.split("\n")

    # Extract endpoints (lines starting with ###)
    endpoints = []
    current_endpoint = None
    current_lines = []

    for line in lines:
        if line.startswith("### ") and "`" in line:
            if current_endpoint:
                endpoints.append((current_endpoint, "\n".join(current_lines[:20])))
            current_endpoint = line
            current_lines = []
        elif current_endpoint:
            current_lines.append(line)

    if current_endpoint:
        endpoints.append((current_endpoint, "\n".join(current_lines[:20])))

    # Build quickstart guide
    guide = f"# 🚀 Guia Rápido: {section_name}\n\n"
    guide += f"## Visão Geral\n\n"
    guide += f"Este guia apresenta os principais endpoints para trabalhar com **{section_name}** na API Bling ERP.\n\n"

    # Organize by HTTP method
    get_endpoints = [e for e in endpoints if "GET" in e[0]]
    post_endpoints = [e for e in endpoints if "POST" in e[0]]
    put_endpoints = [e for e in endpoints if "PUT" in e[0]]
    delete_endpoints = [e for e in endpoints if "DELETE" in e[0]]

    if get_endpoints:
        guide += f"## 📋 Listar e Consultar ({len(get_endpoints)} endpoints)\n\n"
        for endpoint, _ in get_endpoints[:3]:
            guide += f"{endpoint}\n"

    if post_endpoints:
        guide += f"\n## ➕ Criar ({len(post_endpoints)} endpoints)\n\n"
        for endpoint, _ in post_endpoints[:3]:
            guide += f"{endpoint}\n"

    if put_endpoints:
        guide += f"\n## ✏️ Atualizar ({len(put_endpoints)} endpoints)\n\n"
        for endpoint, _ in put_endpoints[:3]:
            guide += f"{endpoint}\n"

    if delete_endpoints:
        guide += f"\n## ❌ Deletar ({len(delete_endpoints)} endpoints)\n\n"
        for endpoint, _ in delete_endpoints[:2]:
            guide += f"{endpoint}\n"

    # Add first endpoint as detailed example
    if endpoints:
        guide += f"\n## 📖 Exemplo Detalhado\n\n"
        example_endpoint, example_content = endpoints[0]
        guide += f"{example_endpoint}\n{example_content[:1000]}\n"
        if len(example_content) > 1000:
            guide += "\n*[Conteúdo truncado - use `docs_search_endpoint()` para ver mais]*\n"

    guide += f"\n## 🔗 Documentação Completa\n\n"
    guide += f"Para ver a documentação completa de **{section_name}**, use:\n"
    guide += f"```python\ndocs_get_section(\"{section_name}\")\n```\n"

    return guide


def _action_helper_fallback(action: str) -> str:
    """Fallback when no specific resource is found."""
    return (
        f"## Buscando endpoints para: '{action}'\n\n"
        f"Não consegui identificar um recurso específico na sua solicitação.\n\n"
        "### Recursos disponíveis na API:\n\n"
        "- **Produtos** - criar, atualizar, listar produtos\n"
        "- **Contatos** - gerenciar clientes, fornecedores\n"
        "- **Pedidos** - criar pedidos de venda/compra\n"
        "- **Notas Fiscais** - emitir e gerenciar NF-e, NFC-e\n"
        "- **Estoque** - consultar e movimentar estoque\n\n"
        "### Dicas:\n\n"
        "1. Seja mais específico sobre o recurso:\n"
        "   - ✅ `criar produto novo`\n"
        "   - ✅ `listar clientes ativos`\n"
        "   - ✅ `atualizar estoque do produto`\n\n"
        "2. Use as ferramentas de busca:\n"
        "   - `docs_search_content('termo')` - busca por palavras-chave\n"
        "   - `docs_list_sections()` - lista todas as categorias\n"
    )


def _find_create_endpoints(paths_list: list) -> list:
    """Find POST endpoints for creation."""
    results = []
    for path, methods in paths_list:
        if "post" in methods:
            results.append(
                {
                    "path": path,
                    "method": "POST",
                    "description": methods["post"].get("summary", "Criar recurso"),
                }
            )
    return results


def _find_update_endpoints(paths_list: list) -> list:
    """Find PUT/PATCH endpoints for updates."""
    results = []
    for path, methods in paths_list:
        for method in ["put", "patch"]:
            if method in methods:
                results.append(
                    {
                        "path": path,
                        "method": method.upper(),
                        "description": methods[method].get(
                            "summary", "Atualizar recurso"
                        ),
                    }
                )
    return results


def _find_delete_endpoints(paths_list: list) -> list:
    """Find DELETE endpoints."""
    results = []
    for path, methods in paths_list:
        if "delete" in methods:
            results.append(
                {
                    "path": path,
                    "method": "DELETE",
                    "description": methods["delete"].get("summary", "Deletar recurso"),
                }
            )
    return results


def _find_list_endpoints(paths_list: list) -> list:
    """Find GET endpoints for listing/querying."""
    results = []
    for path, methods in paths_list:
        if "get" in methods:
            results.append(
                {
                    "path": path,
                    "method": "GET",
                    "description": methods["get"].get("summary", "Obter recurso"),
                }
            )
    return results


def _find_all_endpoints(paths_list: list) -> list:
    """Find all endpoints regardless of method."""
    results = []
    for path, methods in paths_list:
        for method in ["get", "post", "put", "patch", "delete"]:
            if method in methods:
                results.append(
                    {
                        "path": path,
                        "method": method.upper(),
                        "description": methods[method].get("summary", "Operação"),
                    }
                )
    return results


def _build_action_guide(action: str, recommendations: list) -> str:
    """Build guide with recommended endpoints for the action."""
    guide = f"# 🎯 Endpoints para: '{action}'\n\n"

    if not recommendations:
        return _no_matching_endpoints_error(action)

    guide += f"Encontrei **{len(recommendations)}** endpoint(s) relevante(s):\n\n"

    for i, rec in enumerate(recommendations, 1):
        method = rec["method"]
        path = rec["path"]
        description = rec["description"]

        # Method emoji
        emoji = {
            "GET": "📋",
            "POST": "➕",
            "PUT": "✏️",
            "PATCH": "✏️",
            "DELETE": "❌",
        }.get(method, "🔧")

        guide += f"## {i}. {emoji} {method} `{path}`\n\n"
        guide += f"**{description}**\n\n"

        # Add method-specific tips
        if method == "POST":
            guide += "💡 **Dica:** Este endpoint cria um novo recurso. Você precisará fornecer os dados no corpo da requisição (JSON).\n\n"
        elif method in ["PUT", "PATCH"]:
            guide += "💡 **Dica:** Este endpoint atualiza um recurso existente. Identifique o recurso pelo ID no path.\n\n"
        elif method == "DELETE":
            guide += "⚠️ **Atenção:** Esta operação é destrutiva e pode não ser reversível.\n\n"
        elif method == "GET":
            if "{" in path:
                guide += "💡 **Dica:** Este endpoint consulta um recurso específico. Substitua `{id}` pelo ID real.\n\n"
            else:
                guide += "💡 **Dica:** Este endpoint lista recursos. Use parâmetros de query para filtrar (ex: `?pagina=1&limite=50`).\n\n"

    guide += "## 📚 Próximos Passos\n\n"
    guide += "Para ver a documentação completa com exemplos de código:\n\n"

    if recommendations:
        first_path = recommendations[0]["path"]
        # Extract base resource from path
        base = first_path.split("/")[1] if "/" in first_path else first_path
        guide += f"```python\ndocs_search_endpoint('{base}')\n```\n\n"

    guide += "Ou busque por termos específicos:\n"
    guide += f"```python\ndocs_search_content('{action.split()[0]}')\n```\n"

    return guide


def _no_matching_endpoints_error(action: str) -> str:
    """Error when no endpoints match the action."""
    return (
        f"## Nenhum endpoint encontrado para: '{action}'\n\n"
        "Não consegui encontrar endpoints que correspondam à sua ação.\n\n"
        "### Sugestões:\n\n"
        "1. **Reformule sua busca** com palavras-chave diferentes\n"
        "2. **Explore as categorias** disponíveis:\n"
        "   ```python\n"
        "   docs_list_sections()\n"
        "   ```\n"
        "3. **Busque por termo genérico**:\n"
        "   ```python\n"
        "   docs_search_content('sua_palavra_chave')\n"
        "   ```\n\n"
        "### Exemplos de ações válidas:\n"
        "- `criar produto`\n"
        "- `listar pedidos`\n"
        "- `atualizar cliente`\n"
        "- `buscar nota fiscal`\n"
        "- `consultar estoque`\n"
    )

