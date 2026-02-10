# bling-doc-mcp

Servidor MCP que conecta seu assistente de IA (Claude) à documentação completa da **API Bling ERP v3** — com exemplos de código, parâmetros detalhados e busca inteligente.

## O que é isso?

MCP (Model Context Protocol) é uma forma de dar ao Claude acesso a ferramentas externas durante a conversa. Com este servidor instalado, você pode perguntar ao Claude diretamente sobre a API Bling sem precisar abrir a documentação oficial.

**Exemplos de perguntas que você poderá fazer:**

- _"Quais endpoints existem para gerenciar produtos no Bling?"_
- _"Como criar um pedido de venda via API? Me dá um exemplo em Python."_
- _"Quais parâmetros o endpoint GET /contatos aceita?"_
- _"Me mostra como emitir uma nota fiscal eletrônica pelo Bling."_

## Requisitos

- **Python 3.11+** — [python.org/downloads](https://www.python.org/downloads/)
- **uv** — gerenciador de pacotes Python moderno

Para instalar o `uv`:

```bash
# macOS / Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows (PowerShell)
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

## Instalação

```bash
# 1. Clone o repositório
git clone https://github.com/seu-usuario/bling-doc-mcp.git
cd bling-doc-mcp

# 2. Instale as dependências
uv sync
```

## Integração com o Claude

### Claude Desktop

Edite o arquivo de configuração do Claude Desktop:

- **macOS:** `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows:** `%APPDATA%\Claude\claude_desktop_config.json`

Adicione a entrada abaixo (ajuste o caminho para onde você clonou o projeto):

```json
{
  "mcpServers": {
    "bling-doc": {
      "command": "uv",
      "args": [
        "run",
        "--project",
        "/caminho/para/bling-doc-mcp",
        "fastmcp",
        "run",
        "src/bling_doc_mcp/server.py"
      ]
    }
  }
}
```

Reinicie o Claude Desktop. O servidor estará disponível automaticamente.

### Claude Code (CLI)

```bash
claude mcp add bling-doc -- uv run --project /caminho/para/bling-doc-mcp fastmcp run src/bling_doc_mcp/server.py
```

### Instalação via fastmcp

Também é possível instalar diretamente com o `fastmcp`:

```bash
uv run fastmcp install fastmcp.json --name "Bling API Docs"
```

## Ferramentas disponíveis

Após a integração, o Claude terá acesso às seguintes ferramentas:

### Navegação OpenAPI (estrutura JSON)

| Ferramenta | O que faz |
|------------|-----------|
| `openapi_list_endpoints()` | Lista todos os endpoints da API (159 no total) |
| `openapi_get_endpoint_info(endpoint)` | Retorna método, descrição e parâmetros de um endpoint |
| `openapi_get_parameter_info(parameter)` | Busca informações sobre um parâmetro específico |
| `openapi_resolve_ref(ref)` | Resolve schemas `$ref` do OpenAPI recursivamente |

### Documentação Markdown (exemplos e descrições)

| Ferramenta | O que faz |
|------------|-----------|
| `docs_list_sections()` | Lista todas as categorias de recursos (Produtos, Contatos, etc.) |
| `docs_get_section(section)` | Retorna documentação completa de uma categoria |
| `docs_search_endpoint(endpoint)` | Busca documentação de um endpoint com exemplos de código |
| `docs_search_content(query)` | Busca por termos em toda a documentação |

### Prompts inteligentes

| Prompt | O que faz |
|--------|-----------|
| `quickstart_guide(resource)` | Gera guia rápido para um recurso ("produtos", "pedidos", etc.) |
| `find_endpoint_by_action(action)` | Encontra endpoints por ação em linguagem natural ("criar produto") |

### Resources

| Resource | O que fornece |
|----------|---------------|
| `openapi://spec` | Especificação OpenAPI completa em JSON |
| `openapi://metadata` | Metadados do arquivo (tamanho, checksum) |
| `openapi://chunk/{n}` | Leitura em partes para clientes com limite de payload |

## Recursos da API Bling cobertos

- **Produtos** — cadastro, variações, estruturas, lotes, preços
- **Contatos** — clientes, fornecedores, transportadoras
- **Pedidos de Venda** — criação, consulta, atualização, situação
- **Pedidos de Compra** — recebimento, consulta
- **Notas Fiscais** — NF-e, NFC-e, NFS-e (emissão e consulta)
- **Estoques e Depósitos** — saldos, movimentações, transferências
- **Contas a Pagar / Receber** — lançamentos e baixas
- **Categorias, Campos customizados, Etiquetas** e muito mais

## Para desenvolvedores

### Verificações de qualidade

```bash
uv run ruff check .       # lint
uv run basedpyright       # type check
uv run pytest -q          # testes
```

### Executar servidor manualmente

```bash
uv run fastmcp run src/bling_doc_mcp/server.py
```

### Estrutura do projeto

```text
src/bling_doc_mcp/
  app.py                  # Instância FastMCP
  server.py               # Entrypoint — registra tools/resources/prompts
  tools/api_info.py       # 8 ferramentas de consulta OpenAPI/Markdown
  resources/docs.py       # Resources para dados do OpenAPI
  prompts/small_prompts.py # Prompts quickstart_guide e find_endpoint_by_action
  utils/openapi.py        # Loaders com cache e parser de markdown
  utils/ref_resolver.py   # Resolução recursiva de $ref
  files/
    bling-openapi.json          # Especificação OpenAPI v3 completa (1MB)
    bling-openapi-reference.md  # Referência markdown com exemplos (321KB)
```

## Licença

Apache-2.0 — veja [LICENSE](LICENSE).
