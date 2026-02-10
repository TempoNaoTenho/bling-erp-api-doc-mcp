# Bling API

**Version:** 3.0

A sessão abaixo contém a documentação das API's que o Bling disponibiliza.

## Authentication

The Bling API uses OAuth 2.0 for authentication. You need to obtain an access token to make API calls.

### Getting Your Access Token

1. Register your application at https://developer.bling.com.br/
2. Obtain your Client ID and Client Secret
3. Follow the OAuth 2.0 authorization code flow to get an access token

### Using the Access Token

Include the access token in the `Authorization` header of all API requests:

```
Authorization: Bearer YOUR_ACCESS_TOKEN
```

## Base URLs
- `https://api.bling.com.br/Api/v3`: Ambiente de produção
- `https://developer.bling.com.br/api/bling`: Ambiente de teste da documentação

## Anúncios

### GET `/anuncios`

**Obtém anúncios**

Obtém anúncios paginados.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| pagina | query | No | integer | N° da página da listagem |
| limite | query | No | integer | Quantidade de registros que devem ser exibidos por página |
| situacao | query | No | integer (enum) | Situação do anúncio <br> `1` Publicado <br> `2` Rascunho <br> `3` Com problema <br> `4` Pausado |
| idProduto | query | No | integer | ID do produto |
| tipoIntegracao | query | **Yes** | string | Tipo de integração |
| idLoja | query | **Yes** | integer | ID da loja |

#### Responses

**200** - 

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

---

### POST `/anuncios`

**Cria um anúncio**

Cria um anúncio.

#### Request Body

**Content-Type:** `application/json`

#### Responses

**201** - 

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

---

### GET `/anuncios/{idAnuncio}`

**Obtém um anúncio**

Obtém os detalhes de um anúncio específico pelo seu ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idAnuncio | path | **Yes** | integer | ID do anúncio |
| tipoIntegracao | query | **Yes** | string | Tipo de integração |
| idLoja | query | **Yes** | integer | ID da loja |

#### Responses

**200** - 

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

---

### PUT `/anuncios/{idAnuncio}`

**Altera um anúncio**

Altera um anúncio pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idAnuncio | path | **Yes** | integer | ID do anúncio |

#### Request Body

**Content-Type:** `application/json`

#### Responses

**204** - No content.

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

---

### DELETE `/anuncios/{idAnuncio}`

**Remove um anúncio**

Remove um anúncio pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idAnuncio | path | **Yes** | integer | ID do anúncio |
| tipoIntegracao | query | **Yes** | string | Tipo de integração |
| idLoja | query | **Yes** | integer | ID da loja |

#### Responses

**204** - No content.

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

---

### POST `/anuncios/{idAnuncio}/publicar`

**Publica um anúncio**

Altera o status do anúncio para publicado.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idAnuncio | path | **Yes** | integer | ID do anúncio |
| tipoIntegracao | query | **Yes** | string | Tipo de integração |
| idLoja | query | **Yes** | integer | ID da loja |

#### Responses

**204** - No content.

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

---

### POST `/anuncios/{idAnuncio}/pausar`

**Pausa um anúncio**

Altera o status do anúncio para pausado.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idAnuncio | path | **Yes** | integer | ID do anúncio |
| tipoIntegracao | query | **Yes** | string | Tipo de integração |
| idLoja | query | **Yes** | integer | ID da loja |

#### Responses

**204** - No content.

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

---

## Anúncios - Categorias

### GET `/anuncios/categorias`

**Obtém categorias de anúncios**

Obtém categorias de anúncios.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| tipoIntegracao | query | **Yes** | string | Tipo de integração |
| idLoja | query | **Yes** | integer | ID da loja |
| idCategoria | query | No | integer | ID da categoria |
| tipoProduto | query | No | string | Tipo do produto |

#### Responses

**200** - 

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

---

### GET `/anuncios/categorias/{idCategoria}`

**Obtém uma categoria de anúncio**

Obtém uma categoria de anúncio pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idCategoria | path | **Yes** | integer | ID da categoria de receita e despesa |
| tipoIntegracao | query | **Yes** | string | Tipo de integração |
| idLoja | query | **Yes** | integer | ID da loja |

#### Responses

**200** - 

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

---

## Borderôs

### GET `/borderos/{idBordero}`

**Obtém um borderô**

Obtém um borderô pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idBordero | path | **Yes** | integer | ID do bordero |

#### Responses

**200** - 

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

---

### DELETE `/borderos/{idBordero}`

**Remove um borderô**

Remove um borderô pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idBordero | path | **Yes** | integer | ID do bordero |

#### Responses

**204** - No content.

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

---

## Caixas e Bancos

### GET `/caixas`

**Obtém lista de lançamentos de caixas e bancos.**

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| pagina | query | No | integer | N° da página da listagem |
| dataInicial | query | No | string | Data inicial de consulta de movimentações, só serão retornados os lançamento a partir dessa data. Caso não informado, o padrão será o primeiro dia do mês atual. |
| dataFinal | query | No | string | Data final de consulta de movimentações, só serão retornados os lançamento até essa data. Caso não informado, o padrão será o último dia do mês atual. |
| idsCategorias | query | No | array&lt;integer&gt; | IDs das categorias de movimentações. |
| idContaFinanceira | query | No | integer | ID da conta financeira. |
| pesquisa | query | No | string | Pesquisa por descrição do lançamento. |
| valor | query | No | number | Valor do lançamento. |
| situacaoConciliacao | query | No | integer (enum) | Situação da conciliação do lançamento <br> `1` Registros conciliados <br> `2` Registros não conciliados <br> `3` Todos os registros |
| situacao | query | No | string (enum) | Situação do lançamento.<br>'R' para registros<br>'E' para excluídos |

#### Responses

**200** - 

**400** - Valor de filtro inválido.

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

---

### POST `/caixas`

**Cria um novo lançamento de caixa e banco.**

Cria um novo lançamento de caixa e banco com os dados fornecidos.

#### Request Body

**Content-Type:** `application/json`

#### Responses

**201** - Lançamento criado com sucesso

**400** - Dados inválidos ou campos obrigatórios não informados

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

---

### GET `/caixas/{idCaixa}`

**Obtém um lançamento de caixa e banco.**

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idCaixa | path | **Yes** | integer | ID do lançamento de caixas e bancos |

#### Responses

**200** - 

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

---

### PUT `/caixas/{idCaixa}`

**Atualiza um lançamento de caixa e banco.**

Atualiza um lançamento de caixa e banco existente com os dados fornecidos.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idCaixa | path | **Yes** | integer | ID do lançamento de caixas e bancos |

#### Request Body

**Content-Type:** `application/json`

#### Responses

**200** - Lançamento atualizado com sucesso

**400** - Dados inválidos ou campos obrigatórios não informados

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

**404** - Lançamento não encontrado

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

---

### DELETE `/caixas/{idCaixa}`

**Remove um lançamento de caixa e banco**

Remove um lançamento de caixa e banco pelo ID. O registro não é excluído permanentemente, apenas marcado como excluído (exclusão lógica).

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idCaixa | path | **Yes** | integer | ID do lançamento de caixa e banco a ser excluído. |

#### Responses

**204** - No content. O lançamento foi excluído com sucesso.

**400** - Erro de validação.

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

**404** - Lançamento não encontrado.

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

---

## Campos Customizados

### GET `/campos-customizados/modulos`

**Obtém módulos que possuem campos customizados**

Obtém módulos que possuem campos customizados.

#### Responses

**200** - 

---

### GET `/campos-customizados/tipos`

**Obtém tipos de campos customizados**

Obtém tipos de campos customizados.

#### Responses

**200** - 

---

### GET `/campos-customizados/modulos/{idModulo}`

**Obtém campos customizados por módulo**

Obtém campos customizados por módulo paginados.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idModulo | path | **Yes** | integer |  |
| pagina | query | No | integer | N° da página da listagem |
| limite | query | No | integer | Quantidade de registros que devem ser exibidos por página |

#### Responses

**200** - 

---

### GET `/campos-customizados/{idCampoCustomizado}`

**Obtém um campo customizado**

Obtém um campo customizado pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idCampoCustomizado | path | **Yes** | integer | ID do campo customizado |

#### Responses

**200** - 

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

---

### PUT `/campos-customizados/{idCampoCustomizado}`

**Altera um campo customizado**

Altera um campo customizado pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idCampoCustomizado | path | **Yes** | integer | ID do campo customizado |

#### Request Body

**Content-Type:** `application/json`

#### Responses

**200** - 

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

---

### DELETE `/campos-customizados/{idCampoCustomizado}`

**Remove um campo customizado**

Remove um campo customizado pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idCampoCustomizado | path | **Yes** | integer | ID do campo customizado |

#### Responses

**204** - No content.

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

---

### POST `/campos-customizados`

**Cria um campo customizado**

Cria um campo customizado.

#### Request Body

**Content-Type:** `application/json`

#### Responses

**201** - 

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

---

### PATCH `/campos-customizados/{idCampoCustomizado}/situacoes`

**Altera a situação de um campo customizado**

Altera a situação de um campo customizado pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idCampoCustomizado | path | **Yes** | integer | ID do campo customizado |

#### Request Body

**Content-Type:** `application/json`

#### Responses

**204** - No content.

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

---

## Canais de Venda

### GET `/canais-venda`

**Obtém canais de venda**

Obtém canais de venda paginados.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| pagina | query | No | integer | N° da página da listagem |
| limite | query | No | integer | Quantidade de registros que devem ser exibidos por página |
| tipos[] | query | No | array&lt;string&gt; | Parâmetro para filtrar os registros através de uma lista de tipos de canal de venda. |
| situacao | query | No | integer (enum) | Parâmetro para filtrar os registros através da situação<br> `1` Habilitado<br> `2` Desabilitado |
| agrupador | query | No | integer (enum) | Agrupador do canal de venda<br> `1` Loja virtual<br> `2` Hub<br> `3` Marketplace<br> `4` API |

#### Responses

**200** - 

---

### GET `/canais-venda/{idCanalVenda}`

**Obtém um canal de venda**

Obtém uma canal de venda pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idCanalVenda | path | **Yes** | integer | ID do canal de venda |

#### Responses

**200** - 

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

---

### GET `/canais-venda/tipos`

**Obtém os tipos de canais de venda**

Obtém os tipos de canais de venda paginados.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| agrupador | query | No | integer (enum) | Agrupador do canal de venda<br> `1` Loja virtual<br> `2` Hub<br> `3` Marketplace<br> `4` API |

#### Responses

**200** - 

---

## Categorias - Lojas

### GET `/categorias/lojas`

**Obtém categorias de lojas virtuais vinculadas a de produtos**

Obtém categorias de lojas virtuais vinculadas a de produtos paginadas.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| pagina | query | No | integer | N° da página da listagem |
| limite | query | No | integer | Quantidade de registros que devem ser exibidos por página |
| idLoja | query | No | integer | ID da loja |
| idCategoriaProduto | query | No | integer | ID da categoria do produto |
| idCategoriaProdutoPai | query | No | integer | ID da categoria do produto pai |

#### Responses

**200** - 

---

### POST `/categorias/lojas`

**Cria o vínculo de uma categoria da loja com a de produto**

Cria o vínculo de uma categoria da loja com a de produto.

#### Request Body

**Content-Type:** `application/json`

#### Responses

**201** - 

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

---

### GET `/categorias/lojas/{idCategoriaLoja}`

**Obtém uma categoria da loja vinculada a de produto**

Obtém uma categoria da loja vinculada a de produto pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idCategoriaLoja | path | **Yes** | integer | ID do vínculo da categoria de produto com a da loja |

#### Responses

**200** - 

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

---

### PUT `/categorias/lojas/{idCategoriaLoja}`

**Altera o vínculo de uma categoria da loja com a de produto**

Altera o vínculo de uma categoria da loja com a de produto pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idCategoriaLoja | path | **Yes** | integer | ID do vínculo da categoria de produto com a da loja |

#### Request Body

**Content-Type:** `application/json`

#### Responses

**204** - No content.

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

---

### DELETE `/categorias/lojas/{idCategoriaLoja}`

**Remove o vínculo de uma categoria da loja com a de produto**

Remove o vínculo de uma categoria da loja com a de produto pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idCategoriaLoja | path | **Yes** | integer | ID do vínculo da categoria de produto com a da loja |

#### Responses

**204** - No content.

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

---

## Categorias - Produtos

### GET `/categorias/produtos`

**Obtém categorias de produtos**

Obtém categorias de produtos paginadas.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| pagina | query | No | integer | N° da página da listagem |
| limite | query | No | integer | Quantidade de registros que devem ser exibidos por página |

#### Responses

**200** - 

---

### POST `/categorias/produtos`

**Cria uma categoria de produto**

Cria uma categoria de produto.

#### Request Body

**Content-Type:** `application/json`

#### Responses

**201** - 

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

---

### GET `/categorias/produtos/{idCategoriaProduto}`

**Obtém uma categoria de produto**

Obtém uma categoria de produto pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idCategoriaProduto | path | **Yes** | integer | ID da categoria de produto |

#### Responses

**200** - 

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

---

### PUT `/categorias/produtos/{idCategoriaProduto}`

**Altera uma categoria de produto**

Altera uma categoria de produto pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idCategoriaProduto | path | **Yes** | integer | ID da categoria de produto |

#### Request Body

**Content-Type:** `application/json`

#### Responses

**204** - No content.

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

---

### DELETE `/categorias/produtos/{idCategoriaProduto}`

**Remove uma categoria de produto**

Remove uma categoria de produto pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idCategoriaProduto | path | **Yes** | integer | ID da categoria de produto |

#### Responses

**204** - No content.

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

---

## Categorias - Receitas e Despesas

### GET `/categorias/receitas-despesas`

**Obtém categorias de receitas e despesas**

Obtém categorias de receitas e despesas paginadas.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| pagina | query | No | integer | N° da página da listagem |
| limite | query | No | integer | Quantidade de registros que devem ser exibidos por página |
| tipo | query | No | integer (enum) | `0` Todas<br>`1` Despesa<br>`2` Receita<br>`3` Receita e despesa |
| situacao | query | No | integer (enum) | `0` Ativas e Inativas<br>`1` Ativas<br>`2` Inativas |

#### Responses

**200** - 

---

### POST `/categorias/receitas-despesas`

**Cria uma categoria de receita e despesa**

Cria uma categoria de receita e despesa.

#### Request Body

**Content-Type:** `application/json`

#### Responses

**201** - 

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

---

### DELETE `/categorias/receitas-despesas`

**Remove múltiplas categorias de receita e despesa**

Remove múltiplas categorias de receita e despesa a partir de uma lista de IDs.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idsCategorias[] | query | **Yes** | array&lt;integer&gt; | IDs das categorias a serem removidas |

#### Responses

**200** - 

**204** - No content.

---

### GET `/categorias/receitas-despesas/{idCategoria}`

**Obtém uma categoria de receita e despesa**

Obtém uma categoria de receita e despesa pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idCategoria | path | **Yes** | integer | ID da categoria de receita e despesa |

#### Responses

**200** - 

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

---

### PUT `/categorias/receitas-despesas/{idCategoria}`

**Atualiza uma categoria de receita e despesa**

Atualiza uma categoria de receita e despesa a partir do ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idCategoria | path | **Yes** | integer | ID da categoria de receita e despesa |

#### Request Body

**Content-Type:** `application/json`

#### Responses

**200** - 

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

---

### DELETE `/categorias/receitas-despesas/{idCategoria}`

**Remove uma categoria de receita e despesa**

Remove uma categoria de receita e despesa pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idCategoria | path | **Yes** | integer | ID da categoria de receita e despesa |

#### Responses

**204** - No content.

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

---

## Contas Financeiras

### GET `/contas-contabeis`

**Obtém contas financeiras**

Obtém contas financeiras paginadas.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| pagina | query | No | integer | N° da página da listagem |
| limite | query | No | integer | Quantidade de registros que devem ser exibidos por página |
| ocultarInvisiveis | query | No | boolean | Oculta contas financeiras invisíveis |
| ocultarTipoContaBancaria | query | No | boolean | Oculta contas financeiras do tipo conta bancária |
| situacoes | query | No | array&lt;integer&gt; | Situação da conta financeira<br> `1` Ativo<br> `2` Inativo<br> `3` Pendente<br> `4` Cancelada |
| aliasIntegracao | query | No | string | Alias da integração |
| aliasIntegracao | path | No | string | Alias da integração |
| ordenacao | query | No | string (enum) | Ordenação da obtenção pelos campos: <br> `descricao` |

#### Responses

**200** - 

---

### GET `/contas-contabeis/{idContaContabil}`

**Obtém uma conta financeira**

Obtém uma conta financeira pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idContaContabil | path | **Yes** | integer | ID da conta financeira |

#### Responses

**200** - 

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

---

## Contas a Pagar

### GET `/contas/pagar`

**Obtém contas a pagar**

Obtém contas a pagar paginadas.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| pagina | query | No | integer | N° da página da listagem |
| limite | query | No | integer | Quantidade de registros que devem ser exibidos por página |
| dataEmissaoInicial | query | No | string | Data de emissão inicial da conta a pagar |
| dataEmissaoFinal | query | No | string | Data de emissão final da conta a pagar |
| dataVencimentoInicial | query | No | string | Data de vencimento inicial da conta a pagar |
| dataVencimentoFinal | query | No | string | Data de vencimento final da conta a pagar |
| dataPagamentoInicial | query | No | string | Data de pagamento inicial da conta |
| dataPagamentoFinal | query | No | string | Data de pagamento final da conta |
| situacao | query | No | integer (enum) | `1` Em aberto <br>`2` Recebido <br>`3` Parcialmente recebido <br>`4` Devolvido <br>`5` Cancelado |
| idContato | query | No | integer | ID do contato |

#### Responses

**200** - 

---

### POST `/contas/pagar`

**Cria uma conta a pagar**

Cria uma conta a pagar.

#### Request Body

**Content-Type:** `application/json`

#### Responses

**201** - 

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

---

### GET `/contas/pagar/{idContaPagar}`

**Obtém uma conta a pagar**

Obtém uma conta a pagar pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idContaPagar | path | **Yes** | integer | ID da conta a pagar |

#### Responses

**200** - 

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

---

### PUT `/contas/pagar/{idContaPagar}`

**Atualiza uma conta a pagar**

Atualiza uma conta a pagar pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idContaPagar | path | **Yes** | integer | ID da conta a pagar |

#### Request Body

**Content-Type:** `application/json`

#### Responses

**200** - 

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

---

### DELETE `/contas/pagar/{idContaPagar}`

**Remove uma conta a pagar**

Remove uma conta a pagar pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idContaPagar | path | **Yes** | integer | ID da conta a pagar |

#### Responses

**204** - No content.

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

---

### POST `/contas/pagar/{idContaPagar}/baixar`

**Cria o recebimento de uma conta a pagar**

Cria o recebimento de uma conta a pagar.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idContaPagar | path | **Yes** | integer | ID da conta a pagar |

#### Request Body

**Content-Type:** `application/json`

#### Responses

**200** - 

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

---

## Contas a Receber

### GET `/contas/receber`

**Obtém contas a receber**

Obtém contas a receber paginadas.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| pagina | query | No | integer | N° da página da listagem |
| limite | query | No | integer | Quantidade de registros que devem ser exibidos por página |
| situacoes[] | query | No | array (enum) | `1` Em aberto <br>`2` Recebido <br>`3` Parcialmente recebido <br>`4` Devolvido <br>`5` Cancelado |
| tipoFiltroData | query | No | string (enum) | Referente ao campo que será considerado ao filtrar por data inicial e final<br>`E` Data de emissão <br> `V` Data de vencimento <br> `R` Data de recebimento |
| dataInicial | query | No | string | Data inicial. Por padrão, um ano antes da data atual. |
| dataFinal | query | No | string | Data final. Por padrão, a data atual. |
| idsCategorias[] | query | No | array&lt;integer&gt; | IDs das categorias de receitas e despesas |
| idPortador | query | No | integer | ID da conta financeira |
| idContato | query | No | integer | ID do contato |
| idVendedor | query | No | integer | ID do vendedor |
| idFormaPagamento | query | No | integer | ID da forma de pagamento |
| boletoGerado | query | No | integer (enum) | Obtém contas com ou sem boletos emitidos via integração, `0` para boletos não emitidos e `1` para boletos emitidos |

#### Responses

**200** - 

---

### POST `/contas/receber`

**Cria uma conta a receber**

Cria uma conta a receber.

#### Request Body

**Content-Type:** `application/json`

#### Responses

**201** - 

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

---

### GET `/contas/receber/{idContaReceber}`

**Obtém uma conta a receber**

Obtém uma conta a receber pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idContaReceber | path | **Yes** | integer | ID da conta a receber |

#### Responses

**200** - 

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

---

### PUT `/contas/receber/{idContaReceber}`

**Altera uma conta a receber**

Altera uma conta a receber pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idContaReceber | path | **Yes** | integer | ID da conta a receber |

#### Request Body

**Content-Type:** `application/json`

#### Responses

**204** - No content.

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

---

### DELETE `/contas/receber/{idContaReceber}`

**Remove uma conta a receber**

Remove uma conta a receber pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idContaReceber | path | **Yes** | integer | ID da conta a receber |

#### Responses

**204** - No content.

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

---

### POST `/contas/receber/{idContaReceber}/baixar`

**Cria o recebimento de uma conta a receber**

Cria o recebimento de uma conta a receber.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idContaReceber | path | **Yes** | integer | ID da conta a receber |

#### Request Body

**Content-Type:** `application/json`

#### Responses

**200** - 

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

---

### GET `/contas/receber/boletos`

**Obtém boletos de contas a receber**

Obtém os boletos vinculados a um idOrigem, o qual corresponde ao ID de uma venda ou nota fiscal.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idOrigem | query | **Yes** | integer | ID da venda ou nota fiscal |
| situacoes[] | query | No | array (enum) | `1` Em aberto <br>`2` Recebido <br>`3` Parcialmente recebido <br>`4` Devolvido <br>`5` Parcialmente devolvido <br>`6` Cancelado |

#### Responses

**200** - 

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

---

### POST `/contas/receber/boletos/cancelar`

**Cancela boletos de contas a receber**

Cancela um ou todos os boletos em aberto vinculados a uma venda ou nota fiscal.

#### Request Body

**Content-Type:** `application/json`

#### Responses

**204** - No content.

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

---

## Contatos

### GET `/contatos`

**Obtém contatos**

Obtém contatos paginados.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| pagina | query | No | integer | N° da página da listagem |
| limite | query | No | integer | Quantidade de registros que devem ser exibidos por página |
| pesquisa | query | No | string | Nome, CPF/CNPJ, fantasia, e-mail ou código do contato |
| criterio | query | No | integer (enum) | Criterio de listagem <br> `1` Todos <br> `2` Excluídos <br> `3` Últimos incluídos <br> `4` Sem movimento |
| dataInclusaoInicial | query | No | string | Data de inclusão inicial |
| dataInclusaoFinal | query | No | string | Data de inclusão final |
| dataAlteracaoInicial | query | No | string | Data de alteração inicial |
| dataAlteracaoFinal | query | No | string | Data de alteração final |
| idTipoContato | query | No | integer | ID do tipo do contato |
| idVendedor | query | No | integer | ID do vendedor relacionado ao contato |
| uf | query | No | string | UF do contato |
| telefone | query | No | string | Telefone do contato |
| idsContatos[] | query | No | array&lt;integer&gt; | IDs dos contatos |
| numeroDocumento | query | No | string |  CPF/CNPJ, desconsiderando a pontuação |
| tipoPessoa | query | No | integer (enum) | Tipo de pessoa <br> `1` Física <br> `2` Jurídica <br> `3` Estrangeiro |

#### Responses

**200** - 

#### Code Examples

**cURL**

```bash
curl -X GET "https://api.bling.com.br/Api/v3/contatos" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json"
```

**Python (requests)**

```python
import requests

url = "https://api.bling.com.br/Api/v3/contatos"
headers = {
    "Authorization": "Bearer YOUR_ACCESS_TOKEN",
    "Content-Type": "application/json"
}

response = requests.get(url, headers=headers)
print(response.json())
```

**JavaScript (fetch)**

```javascript
const url = "https://api.bling.com.br/Api/v3/contatos";
const headers = {
  "Authorization": "Bearer YOUR_ACCESS_TOKEN",
  "Content-Type": "application/json"
};

fetch(url, {
  method: "GET",
  headers: headers
})
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error("Error:", error));
```

---

### POST `/contatos`

**Cria um contato**

Cria um contato.

#### Request Body

**Content-Type:** `application/json`

**Example Request**

```json
{
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
}
```

#### Responses

**201** - 

**Example Response (201)**

```json
{
  "data": {
    "id": 12345678,
    "nome": "João Silva",
    "codigo": "CLI-001",
    "situacao": "A",
    "numeroDocumento": "12345678901",
    "email": "joao.silva@email.com"
  }
}
```

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

#### Code Examples

**cURL**

```bash
curl -X POST "https://api.bling.com.br/Api/v3/contatos" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
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
}'
```

**Python (requests)**

```python
import requests

url = "https://api.bling.com.br/Api/v3/contatos"
headers = {
    "Authorization": "Bearer YOUR_ACCESS_TOKEN",
    "Content-Type": "application/json"
}

data = {
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
}

response = requests.post(url, headers=headers, json=data)
print(response.json())
```

**JavaScript (fetch)**

```javascript
const url = "https://api.bling.com.br/Api/v3/contatos";
const headers = {
  "Authorization": "Bearer YOUR_ACCESS_TOKEN",
  "Content-Type": "application/json"
};

const data = {
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
};

fetch(url, {
  method: "POST",
  headers: headers,
  body: JSON.stringify(data)
})
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error("Error:", error));
```

---

### DELETE `/contatos`

**Remove múltiplos contatos**

Remove múltiplos contatos pelos IDs.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idsContatos[] | query | **Yes** | array&lt;integer&gt; | IDs dos contatos |

#### Responses

**200** - 

**Example Response (200)**

```json
{
  "data": {
    "id": 12345678,
    "nome": "João Silva",
    "codigo": "CLI-001",
    "situacao": "A",
    "numeroDocumento": "12345678901",
    "email": "joao.silva@email.com"
  }
}
```

**204** - No content.

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

#### Code Examples

**cURL**

```bash
curl -X DELETE "https://api.bling.com.br/Api/v3/contatos" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json"
```

**Python (requests)**

```python
import requests

url = "https://api.bling.com.br/Api/v3/contatos"
headers = {
    "Authorization": "Bearer YOUR_ACCESS_TOKEN",
    "Content-Type": "application/json"
}

response = requests.delete(url, headers=headers)
print(response.json())
```

**JavaScript (fetch)**

```javascript
const url = "https://api.bling.com.br/Api/v3/contatos";
const headers = {
  "Authorization": "Bearer YOUR_ACCESS_TOKEN",
  "Content-Type": "application/json"
};

fetch(url, {
  method: "DELETE",
  headers: headers
})
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error("Error:", error));
```

---

### GET `/contatos/{idContato}`

**Obtém um contato**

Obtém um contato pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idContato | path | **Yes** | integer | ID do contato |

#### Responses

**200** - 

**Example Response (200)**

```json
{
  "data": {
    "id": 12345678,
    "nome": "João Silva",
    "codigo": "CLI-001",
    "situacao": "A",
    "numeroDocumento": "12345678901",
    "email": "joao.silva@email.com"
  }
}
```

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

#### Code Examples

**cURL**

```bash
curl -X GET "https://api.bling.com.br/Api/v3/contatos/{idContato}" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json"
```

**Python (requests)**

```python
import requests

url = "https://api.bling.com.br/Api/v3/contatos/{idContato}"
headers = {
    "Authorization": "Bearer YOUR_ACCESS_TOKEN",
    "Content-Type": "application/json"
}

response = requests.get(url, headers=headers)
print(response.json())
```

**JavaScript (fetch)**

```javascript
const url = "https://api.bling.com.br/Api/v3/contatos/{idContato}";
const headers = {
  "Authorization": "Bearer YOUR_ACCESS_TOKEN",
  "Content-Type": "application/json"
};

fetch(url, {
  method: "GET",
  headers: headers
})
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error("Error:", error));
```

---

### PUT `/contatos/{idContato}`

**Altera um contato**

Altera um contato pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idContato | path | **Yes** | integer | ID do contato |

#### Request Body

**Content-Type:** `application/json`

**Example Request**

```json
{
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
}
```

#### Responses

**204** - No content.

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

#### Code Examples

**cURL**

```bash
curl -X PUT "https://api.bling.com.br/Api/v3/contatos/{idContato}" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
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
}'
```

**Python (requests)**

```python
import requests

url = "https://api.bling.com.br/Api/v3/contatos/{idContato}"
headers = {
    "Authorization": "Bearer YOUR_ACCESS_TOKEN",
    "Content-Type": "application/json"
}

data = {
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
}

response = requests.put(url, headers=headers, json=data)
print(response.json())
```

**JavaScript (fetch)**

```javascript
const url = "https://api.bling.com.br/Api/v3/contatos/{idContato}";
const headers = {
  "Authorization": "Bearer YOUR_ACCESS_TOKEN",
  "Content-Type": "application/json"
};

const data = {
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
};

fetch(url, {
  method: "PUT",
  headers: headers,
  body: JSON.stringify(data)
})
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error("Error:", error));
```

---

### DELETE `/contatos/{idContato}`

**Remove um contato**

Remove um contato pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idContato | path | **Yes** | integer | ID do contato |

#### Responses

**204** - No content.

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

#### Code Examples

**cURL**

```bash
curl -X DELETE "https://api.bling.com.br/Api/v3/contatos/{idContato}" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json"
```

**Python (requests)**

```python
import requests

url = "https://api.bling.com.br/Api/v3/contatos/{idContato}"
headers = {
    "Authorization": "Bearer YOUR_ACCESS_TOKEN",
    "Content-Type": "application/json"
}

response = requests.delete(url, headers=headers)
print(response.json())
```

**JavaScript (fetch)**

```javascript
const url = "https://api.bling.com.br/Api/v3/contatos/{idContato}";
const headers = {
  "Authorization": "Bearer YOUR_ACCESS_TOKEN",
  "Content-Type": "application/json"
};

fetch(url, {
  method: "DELETE",
  headers: headers
})
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error("Error:", error));
```

---

### GET `/contatos/{idContato}/tipos`

**Obtém os tipos de contato de um contato**

Obtém os tipos de contato de um contato pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idContato | path | **Yes** | integer | ID do contato |

#### Responses

**200** - 

**Example Response (200)**

```json
{
  "data": {
    "id": 12345678,
    "nome": "João Silva",
    "codigo": "CLI-001",
    "situacao": "A",
    "numeroDocumento": "12345678901",
    "email": "joao.silva@email.com"
  }
}
```

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

#### Code Examples

**cURL**

```bash
curl -X GET "https://api.bling.com.br/Api/v3/contatos/{idContato}/tipos" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json"
```

**Python (requests)**

```python
import requests

url = "https://api.bling.com.br/Api/v3/contatos/{idContato}/tipos"
headers = {
    "Authorization": "Bearer YOUR_ACCESS_TOKEN",
    "Content-Type": "application/json"
}

response = requests.get(url, headers=headers)
print(response.json())
```

**JavaScript (fetch)**

```javascript
const url = "https://api.bling.com.br/Api/v3/contatos/{idContato}/tipos";
const headers = {
  "Authorization": "Bearer YOUR_ACCESS_TOKEN",
  "Content-Type": "application/json"
};

fetch(url, {
  method: "GET",
  headers: headers
})
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error("Error:", error));
```

---

### GET `/contatos/consumidor-final`

**Obtém os dados do contato Consumidor Final**

Obtém os dados do contato Consumidor Final. O consumidor final é um contato padrão do sistema que é criado automaticamente e não pode ser alterado.

#### Responses

**200** - 

#### Code Examples

**cURL**

```bash
curl -X GET "https://api.bling.com.br/Api/v3/contatos/consumidor-final" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json"
```

**Python (requests)**

```python
import requests

url = "https://api.bling.com.br/Api/v3/contatos/consumidor-final"
headers = {
    "Authorization": "Bearer YOUR_ACCESS_TOKEN",
    "Content-Type": "application/json"
}

response = requests.get(url, headers=headers)
print(response.json())
```

**JavaScript (fetch)**

```javascript
const url = "https://api.bling.com.br/Api/v3/contatos/consumidor-final";
const headers = {
  "Authorization": "Bearer YOUR_ACCESS_TOKEN",
  "Content-Type": "application/json"
};

fetch(url, {
  method: "GET",
  headers: headers
})
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error("Error:", error));
```

---

### PATCH `/contatos/{idContato}/situacoes`

**Altera a situação de um contato**

Altera a situação de um contato pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idContato | path | **Yes** | integer | ID do contato |

#### Request Body

**Content-Type:** `application/json`

**Example Request**

```json
{
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
}
```

#### Responses

**204** - No content.

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

#### Code Examples

**cURL**

```bash
curl -X PATCH "https://api.bling.com.br/Api/v3/contatos/{idContato}/situacoes" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
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
}'
```

**Python (requests)**

```python
import requests

url = "https://api.bling.com.br/Api/v3/contatos/{idContato}/situacoes"
headers = {
    "Authorization": "Bearer YOUR_ACCESS_TOKEN",
    "Content-Type": "application/json"
}

data = {
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
}

response = requests.patch(url, headers=headers, json=data)
print(response.json())
```

**JavaScript (fetch)**

```javascript
const url = "https://api.bling.com.br/Api/v3/contatos/{idContato}/situacoes";
const headers = {
  "Authorization": "Bearer YOUR_ACCESS_TOKEN",
  "Content-Type": "application/json"
};

const data = {
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
};

fetch(url, {
  method: "PATCH",
  headers: headers,
  body: JSON.stringify(data)
})
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error("Error:", error));
```

---

### POST `/contatos/situacoes`

**Altera a situação de múltiplos contatos**

Altera a situação de múltiplos contatos pelos IDs.

#### Request Body

**Content-Type:** `application/json`

**Example Request**

```json
{
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
}
```

#### Responses

**200** - 

**Example Response (200)**

```json
{
  "data": {
    "id": 12345678,
    "nome": "João Silva",
    "codigo": "CLI-001",
    "situacao": "A",
    "numeroDocumento": "12345678901",
    "email": "joao.silva@email.com"
  }
}
```

**204** - No content.

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

#### Code Examples

**cURL**

```bash
curl -X POST "https://api.bling.com.br/Api/v3/contatos/situacoes" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
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
}'
```

**Python (requests)**

```python
import requests

url = "https://api.bling.com.br/Api/v3/contatos/situacoes"
headers = {
    "Authorization": "Bearer YOUR_ACCESS_TOKEN",
    "Content-Type": "application/json"
}

data = {
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
}

response = requests.post(url, headers=headers, json=data)
print(response.json())
```

**JavaScript (fetch)**

```javascript
const url = "https://api.bling.com.br/Api/v3/contatos/situacoes";
const headers = {
  "Authorization": "Bearer YOUR_ACCESS_TOKEN",
  "Content-Type": "application/json"
};

const data = {
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
};

fetch(url, {
  method: "POST",
  headers: headers,
  body: JSON.stringify(data)
})
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error("Error:", error));
```

---

## Contatos - Tipos

### GET `/contatos/tipos`

**Obtém tipos de contato**

Obtém tipos de contato pelo ID.

#### Responses

**200** - 

---

## Contratos

### GET `/contratos`

**Obtém contratos**

Obtém contratos paginados.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| pagina | query | No | integer | N° da página da listagem |
| limite | query | No | integer | Quantidade de registros que devem ser exibidos por página |
| dataCriacaoInicio | query | No | string | Data inicial de criação |
| dataCriacaoFinal | query | No | string | Data final de criação |
| dataBaseInicio | query | No | string | Data base inicial para geração de cobranças |
| dataBaseFinal | query | No | string | Data base final para geração de cobranças |
| situacao | query | No | string (enum) | `0` Inativo<br>`1` Ativo<br>`2` Baixado<br>`3` Isento |
| idContato | query | No | integer | ID do contato |
| idContatoCobranca | query | No | integer | ID do contato de cobrança |

#### Responses

**200** - 

---

### POST `/contratos`

**Cria um contrato**

Cria um contrato.

#### Request Body

**Content-Type:** `application/json`

#### Responses

**201** - 

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

---

### GET `/contratos/{idContrato}`

**Obtém um contrato**

Obtém um contrato pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idContrato | path | **Yes** | integer | ID do contrato |

#### Responses

**200** - 

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

---

### PUT `/contratos/{idContrato}`

**Altera um contrato**

Altera um contrato pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idContrato | path | **Yes** | integer | ID do contrato |

#### Request Body

**Content-Type:** `application/json`

#### Responses

**201** - 

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

---

### DELETE `/contratos/{idContrato}`

**Remove um contrato**

Remove um contrato pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idContrato | path | **Yes** | integer | ID do contrato |

#### Responses

**204** - No content.

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

---

## Depósitos

### GET `/depositos`

**Obtém depósitos**

Obtém depósitos paginados.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| pagina | query | No | integer | N° da página da listagem |
| limite | query | No | integer | Quantidade de registros que devem ser exibidos por página |
| descricao | query | No | string | Descrição do depósito |
| situacao | query | No | integer (enum) | `0` Inativo <br> `1` Ativo |

#### Responses

**200** - 

---

### POST `/depositos`

**Cria um depósito**

Cria um depósito. Até 100 depósitos podem ser criados.

#### Request Body

**Content-Type:** `application/json`

#### Responses

**201** - 

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

---

### GET `/depositos/{idDeposito}`

**Obtém um depósito**

Obtém um depósito pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idDeposito | path | **Yes** | integer | ID do depósito |

#### Responses

**200** - 

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

---

### PUT `/depositos/{idDeposito}`

**Altera um depósito**

Altera um depósito pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idDeposito | path | **Yes** | integer | ID do depósito |

#### Request Body

**Content-Type:** `application/json`

#### Responses

**200** - 

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

---

## Empresas

### GET `/empresas/me/dados-basicos`

**Obtém dados básicos da empresa**

Obtém CNPJ, razão social e e-mail da empresa.

#### Responses

**200** - 

---

## Estoques

### GET `/estoques/saldos/{idDeposito}`

**Obtém o saldo em estoque de produtos por depósito**

Obtém o saldo em estoque de produtos pelo ID do depósito.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idDeposito | path | **Yes** | integer | ID do depósito |
| idsProdutos[] | query | **Yes** | array&lt;integer&gt; | IDs dos produtos |
| codigos[] | query | No | array&lt;string&gt; | Códigos dos produtos |
| filtroSaldoEstoque | query | No | integer (enum) | Filtra o saldo em estoque <br> `0` zerado <br> `1` positivo <br> `2` negativo |

#### Responses

**200** - 

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

---

### GET `/estoques/saldos`

**Obtém o saldo em estoque de produtos**

Obtém o saldo em estoque de produtos, em todos os depósitos.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idsProdutos[] | query | **Yes** | array&lt;integer&gt; | IDs dos produtos |
| codigos[] | query | No | array&lt;string&gt; | Códigos dos produtos |
| filtroSaldoEstoque | query | No | integer (enum) | Filtra o saldo em estoque <br> `0` zerado <br> `1` positivo <br> `2` negativo |

#### Responses

**200** - 

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

---

### POST `/estoques`

**Cria um registro de estoque**

Cria um registro de estoque.

#### Request Body

**Content-Type:** `application/json`

#### Responses

**201** - 

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

---

## Formas de Pagamentos

### GET `/formas-pagamentos`

**Obtém formas de pagamentos**

Obtém formas de pagamentos paginadas.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| pagina | query | No | integer | N° da página da listagem |
| limite | query | No | integer | Quantidade de registros que devem ser exibidos por página |
| descricao | query | No | string | Descrição da forma de pagamento |
| tiposPagamentos[] | query | No | array&lt;integer&gt; | `1` Dinheiro<br>`2` Cheque<br>`3` Cartão de Crédito<br>`4` Cartão de Débito<br>`5` Cartão da Loja (Private Label)<br>`10` Vale Alimentação<br>`11` Vale Refeição<br>`12` Vale Presente<br>`13` Vale Combustível<br>`14` Duplicata Mercantil<br>`15` Boleto Bancário<br>`16` Depósito Bancário<br>`17` Pagamento Instantâneo (PIX) - Dinâmico<br>`18` Transferência Bancária, Carteira Digital<br>`19` Programa de Fidelidade, Cashback, Crédito Virtual<br>`20` Pagamento Instantâneo (PIX) – Estático<br>`21` Crédito em loja<br>`22` Pagamento Eletrônico não Informado - falha de hardware do sistema emissor<br>`90` Sem pagamento<br>`99` Outros |
| situacao | query | No | integer (enum) | `0` Inativa<br>`1` Ativa |

#### Responses

**200** - 

---

### POST `/formas-pagamentos`

**Cria uma forma de pagamento**

Cria uma forma de pagamento.

#### Request Body

**Content-Type:** `application/json`

#### Responses

**201** - 

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

---

### GET `/formas-pagamentos/{idFormaPagamento}`

**Obtém uma forma de pagamento**

Obtém uma forma de pagamento pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idFormaPagamento | path | **Yes** | integer | ID da forma de pagamento |

#### Responses

**200** - 

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

---

### PUT `/formas-pagamentos/{idFormaPagamento}`

**Altera uma forma de pagamento**

Altera uma forma de pagamento pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idFormaPagamento | path | **Yes** | integer | ID da forma de pagamento |

#### Request Body

**Content-Type:** `application/json`

#### Responses

**200** - 

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

---

### DELETE `/formas-pagamentos/{idFormaPagamento}`

**Remove uma forma de pagamento**

Remove uma forma de pagamento pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idFormaPagamento | path | **Yes** | integer | ID da forma de pagamento |

#### Responses

**204** - No content.

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

---

### PATCH `/formas-pagamentos/{idFormaPagamento}/padrao`

**Altera o padrão de uma forma de pagamento**

Altera o padrão de uma forma de pagamento pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idFormaPagamento | path | **Yes** | integer | ID da forma de pagamento |

#### Request Body

**Content-Type:** `application/json`

#### Responses

**204** - No content.

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

---

### PATCH `/formas-pagamentos/{idFormaPagamento}/situacao`

**Altera a situação de uma forma de pagamento**

Altera a situação de uma forma de pagamento pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idFormaPagamento | path | **Yes** | integer | ID da forma de pagamento |

#### Request Body

**Content-Type:** `application/json`

#### Responses

**204** - No content.

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

---

## Grupos de Produtos

### GET `/grupos-produtos`

**Obtém grupos de produtos**

Obtém grupos de produtos paginados.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| nome | query | No | string | O nome do grupo |
| nomePai | query | No | string | O nome do grupo pai |
| pagina | query | No | integer | N° da página da listagem |
| limite | query | No | integer | Quantidade de registros que devem ser exibidos por página |

#### Responses

**200** - 

---

### POST `/grupos-produtos`

**Cria um grupo de produtos**

Cria um grupo de produtos.

#### Request Body

**Content-Type:** `application/json`

#### Responses

**201** - 

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

---

### DELETE `/grupos-produtos`

**Remove múltiplos grupos de produtos**

Remove múltiplos grupos de produtos pelos IDs.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idsGruposProdutos[] | query | **Yes** | array&lt;integer&gt; | IDs dos grupos de produtos |

#### Responses

**200** - 

**204** - No content.

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

---

### GET `/grupos-produtos/{idGrupoProduto}`

**Obtém um grupo de produtos**

Obtém um grupo de produtos pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idGrupoProduto | path | **Yes** | integer | ID do grupo de produto |

#### Responses

**200** - 

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

---

### PUT `/grupos-produtos/{idGrupoProduto}`

**Altera um grupo de produtos**

Altera um grupo de produtos pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idGrupoProduto | path | **Yes** | integer | ID do grupo de produto |

#### Request Body

**Content-Type:** `application/json`

#### Responses

**204** - No content.

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

---

### DELETE `/grupos-produtos/{idGrupoProduto}`

**Remove um grupo de produtos**

Remove um grupo de produtos pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idGrupoProduto | path | **Yes** | integer | ID do grupo de produto |

#### Responses

**204** - No content.

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

---

## Homologação

### GET `/homologacao/produtos`

**Obtém o produto da homologação**

Obtém o produto que será utilizado durante os demais passos da homologação, e, inicia o processo de validação, o qual deve ser acompanhando via interface do cadastro de aplicativos.

#### Responses

**200** - 

---

### POST `/homologacao/produtos`

**Cria o produto da homologação**

Cria o produto da homologação.

#### Request Body

**Content-Type:** `application/json`

#### Responses

**201** - 

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

---

### PUT `/homologacao/produtos/{idProdutoHomologacao}`

**Altera o produto da homologação**

Altera o produto da homologação pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idProdutoHomologacao | path | **Yes** | integer | ID do produto da homologação. |

#### Request Body

**Content-Type:** `application/json`

#### Responses

**204** - No content.

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

---

### DELETE `/homologacao/produtos/{idProdutoHomologacao}`

**Remove o produto da homologação**

Remove o produto da homologação pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idProdutoHomologacao | path | **Yes** | integer | ID do produto da homologação. |

#### Responses

**204** - No content.

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

---

### PATCH `/homologacao/produtos/{idProdutoHomologacao}/situacoes`

**Altera a situação do produto da homologação**

Altera a situação do produto da homologação pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idProdutoHomologacao | path | **Yes** | integer | ID do produto da homologação. |

#### Request Body

**Content-Type:** `application/json`

#### Responses

**204** - No content.

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

---

## Logísticas

### GET `/logisticas`

**Obtém logísticas**

Obtém logísticas paginados.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| pagina | query | No | integer | N° da página da listagem |
| limite | query | No | integer | Quantidade de registros que devem ser exibidos por página |
| tipoIntegracao | query | No | string (enum) | Parâmetro para filtrar os registros através do tipo da logística. |
| tiposIntegracoes[] | query | No | array&lt;string&gt; | Parâmetro para filtrar os registros através de uma lista de tipos de logística. |
| situacao | query | No | string (enum) | Parâmetro para filtrar os registros através da situação<br> `H` Habilitado<br> `D` Desabilitado |
| logisticasReversas | query | No | boolean | Parâmetro para filtrar apenas as logísticas que possuem serviço de reversão. É sobrescrito pelo parâmetro tipoIntegracao, caso enviado junto. |

#### Responses

**200** - 

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

---

### POST `/logisticas`

**Cria logística**

Cria uma logística.

#### Request Body

**Content-Type:** `application/json`

#### Responses

**201** - 

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

---

### GET `/logisticas/{idLogistica}`

**Obtém uma logística**

Obtém uma logística pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idLogistica | path | **Yes** | integer | ID da logística |
| listarServicosInativos | query | No | boolean | Parâmetro para incluir serviços inativos na resposta.<br> `true` Inclui serviços ativos e inativos<br> `false` Inclui apenas serviços ativos (padrão) |

#### Responses

**200** - 

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

---

### PUT `/logisticas/{idLogistica}`

**Altera uma logística**

Altera uma logística pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idLogistica | path | **Yes** | integer | ID da logística |

#### Request Body

**Content-Type:** `application/json`

#### Responses

**200** - 

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

---

### DELETE `/logisticas/{idLogistica}`

**Remove uma logística**

Remove uma logística pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idLogistica | path | **Yes** | integer | ID da logística |

#### Responses

**200** - 

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

---

## Logísticas - Etiquetas

### GET `/logisticas/etiquetas`

**Obtém etiquetas das vendas**

Obtém as etiquetas dos pedidos de venda a partir dos ID's dos pedidos. No momento, o filtro está limitado para apenas um ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| formato | query | **Yes** | string (enum) | Parâmetro para definir o formato do arquivo de impressão.<br> `PDF` - Formato PDF<br> `ZPL` - Formato ZPL |
| idsVendas[] | query | **Yes** | array&lt;integer&gt; | IDs dos pedidos de venda para impressão |

#### Responses

**200** - 

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

---

## Logísticas - Objetos

### GET `/logisticas/objetos/{idObjeto}`

**Obtém um objeto de logística**

Obtém um objeto de logística pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idObjeto | path | **Yes** | integer | ID do objeto logístico |

#### Responses

**200** - 

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

---

### PUT `/logisticas/objetos/{idObjeto}`

**Altera um objeto de logística pelo ID**

Altera dados de um objeto de logística personalizada pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idObjeto | path | **Yes** | integer | ID do objeto logístico |

#### Request Body

**Content-Type:** `application/json`

#### Responses

**200** - 

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

---

### DELETE `/logisticas/objetos/{idObjeto}`

**Remove um objeto de logística personalizada**

Remove um objeto de logística personalizada que não esteja em uma PLP.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idObjeto | path | **Yes** | integer | ID do objeto logístico |

#### Responses

**204** - 

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

---

### POST `/logisticas/objetos`

**Cria um objeto de logística**

Cria um objeto de logística personalizada.

#### Request Body

**Content-Type:** `application/json`

#### Responses

**201** - 

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

---

## Logísticas - Remessas

### GET `/logisticas/remessas/{idRemessa}`

**Obtém uma remessa de postagem**

Obtém uma remessa de postagem pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idRemessa | path | **Yes** | integer | ID da remessa de postagem |

#### Responses

**200** - 

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

---

### PUT `/logisticas/remessas/{idRemessa}`

**Altera uma remessa de postagem**

Altera uma remessa de postagem pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idRemessa | path | **Yes** | integer | ID da remessa de postagem |

#### Request Body

**Content-Type:** `application/json`

#### Responses

**200** - 

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

---

### DELETE `/logisticas/remessas/{idRemessa}`

**Remove uma remessa de postagem**

Remove uma remessa de postagem pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idRemessa | path | **Yes** | integer | ID da remessa de postagem |

#### Responses

**204** - 

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

---

### GET `/logisticas/{idLogistica}/remessas`

**Obtém as remessas de postagem de uma logística**

Obtém as remessas de postagem de uma logística pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idLogistica | path | **Yes** | integer | ID da logística |

#### Responses

**200** - 

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

---

### POST `/logisticas/remessas`

**Cria uma remessa de postagem de uma logística**

Cria uma remessa de postagem de uma logística.

#### Request Body

**Content-Type:** `application/json`

#### Responses

**201** - 

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

---

## Logísticas - Serviços

### GET `/logisticas/servicos`

**Obtém serviços de logísticas**

Obtém serviços de logísticas paginados.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| pagina | query | No | integer | N° da página da listagem |
| limite | query | No | integer | Quantidade de registros que devem ser exibidos por página |
| tipoIntegracao | query | No | string (enum) | Parâmetro para filtrar os registros através do tipo da logística. |

#### Responses

**200** - 

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

---

### POST `/logisticas/servicos`

**Cria um serviço de logística**

Cria um serviço de logística personalizada.

#### Request Body

**Content-Type:** `application/json`

#### Responses

**201** - 

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

---

### GET `/logisticas/servicos/{idLogisticaServico}`

**Obtém um servico de logística**

Obtém um servico de logística pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idLogisticaServico | path | **Yes** | integer | ID do serviço |

#### Responses

**200** - 

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

---

### PUT `/logisticas/servicos/{idLogisticaServico}`

**Altera um serviço de logística pelo ID**

Altera dados de um serviço de logística personalizada pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idLogisticaServico | path | **Yes** | integer | ID do serviço |

#### Request Body

**Content-Type:** `application/json`

#### Responses

**200** - 

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

---

### PATCH `/logisticas/{idLogisticaServico}/situacoes`

**Desativa ou ativa um serviço de uma logística**

Desativa ou ativa um serviço de uma logística personalizada pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idLogisticaServico | path | **Yes** | integer | ID do serviço |

#### Request Body

**Content-Type:** `application/json`

#### Responses

**204** - 

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

---

## Naturezas de Operações

### GET `/naturezas-operacoes`

**Obtém naturezas de operações**

Obtém naturezas de operação paginadas.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| pagina | query | No | integer | N° da página da listagem |
| limite | query | No | integer | Quantidade de registros que devem ser exibidos por página |
| situacao | query | No | integer (enum) | `0` Inativo <br> `1` Ativo |
| descricao | query | No | string | Descrição da natureza de operação |

#### Responses

**200** - 

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

---

### POST `/naturezas-operacoes/{idNaturezaOperacao}/obter-tributacao`

**Obtém regras de tributação da natureza de operação**

Obtém regras de tributação que incidem sobre o item, dada uma natureza de operação.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idNaturezaOperacao | path | **Yes** | integer | ID da natureza de operação |

#### Request Body

**Content-Type:** `application/json`

#### Responses

**200** - 

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

---

## Notas Fiscais Eletrônicas

### GET `/nfe`

**Obtém notas fiscais**

Obtém notas fiscais paginadas.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| pagina | query | No | integer | N° da página da listagem |
| limite | query | No | integer | Quantidade de registros que devem ser exibidos por página |
| numeroLoja | query | No | string | Número do pedido na loja |
| idTransportador | query | No | integer | ID do contato do transportador |
| chaveAcesso | query | No | integer | Chave de acesso |
| numero | query | No | integer | Número da nota fiscal |
| serie | query | No | integer | Série |
| situacao | query | No | integer (enum) | `1` Pendente<br>`2` Cancelada<br>`3` Aguardando recibo<br>`4` Rejeitada<br>`5` Autorizada<br>`6` Emitida DANFE<br>`7` Registrada<br>`8` Aguardando protocolo<br>`9` Denegada<br>`10` Consulta situação<br>`11` Bloqueada<br><br>**Observação:** Caso este parâmetro não seja informado, as notas canceladas não serão incluídas na consulta.<br><br> |
| tipo | query | No | string (enum) | `0` Entrada <br> `1` Saída |
| dataEmissaoInicial | query | No | string | Data e hora incial de emissão |
| dataEmissaoFinal | query | No | string | Data e hora final de emissão |

#### Responses

**200** - 

#### Code Examples

**cURL**

```bash
curl -X GET "https://api.bling.com.br/Api/v3/nfe" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json"
```

**Python (requests)**

```python
import requests

url = "https://api.bling.com.br/Api/v3/nfe"
headers = {
    "Authorization": "Bearer YOUR_ACCESS_TOKEN",
    "Content-Type": "application/json"
}

response = requests.get(url, headers=headers)
print(response.json())
```

**JavaScript (fetch)**

```javascript
const url = "https://api.bling.com.br/Api/v3/nfe";
const headers = {
  "Authorization": "Bearer YOUR_ACCESS_TOKEN",
  "Content-Type": "application/json"
};

fetch(url, {
  method: "GET",
  headers: headers
})
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error("Error:", error));
```

---

### POST `/nfe`

**Cria uma nota fiscal**

Cria uma nota fiscal.

#### Request Body

**Content-Type:** `application/json`

**Example Request**

```json
{
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
      "valor": 49.9,
      "descricao": "Camiseta Básica Preta"
    }
  ],
  "transporte": {
    "fretePorConta": 0,
    "transportador": {
      "nome": "Transportadora XYZ"
    }
  }
}
```

#### Responses

**201** - 

**Example Response (201)**

```json
{
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
```

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

#### Code Examples

**cURL**

```bash
curl -X POST "https://api.bling.com.br/Api/v3/nfe" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
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
      "valor": 49.9,
      "descricao": "Camiseta Básica Preta"
    }
  ],
  "transporte": {
    "fretePorConta": 0,
    "transportador": {
      "nome": "Transportadora XYZ"
    }
  }
}'
```

**Python (requests)**

```python
import requests

url = "https://api.bling.com.br/Api/v3/nfe"
headers = {
    "Authorization": "Bearer YOUR_ACCESS_TOKEN",
    "Content-Type": "application/json"
}

data = {
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
            "valor": 49.9,
            "descricao": "Camiseta Básica Preta"
        }
    ],
    "transporte": {
        "fretePorConta": 0,
        "transportador": {
            "nome": "Transportadora XYZ"
        }
    }
}

response = requests.post(url, headers=headers, json=data)
print(response.json())
```

**JavaScript (fetch)**

```javascript
const url = "https://api.bling.com.br/Api/v3/nfe";
const headers = {
  "Authorization": "Bearer YOUR_ACCESS_TOKEN",
  "Content-Type": "application/json"
};

const data = {
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
      "valor": 49.9,
      "descricao": "Camiseta Básica Preta"
    }
  ],
  "transporte": {
    "fretePorConta": 0,
    "transportador": {
      "nome": "Transportadora XYZ"
    }
  }
};

fetch(url, {
  method: "POST",
  headers: headers,
  body: JSON.stringify(data)
})
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error("Error:", error));
```

---

### DELETE `/nfe`

**Remove múltiplas notas fiscais**

Remove múltiplas notas fiscais por IDs.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idsNotas[] | query | **Yes** | array&lt;integer&gt; | IDs das notas fiscais |

#### Responses

**200** - 

**Example Response (200)**

```json
{
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
```

**204** - No content.

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

#### Code Examples

**cURL**

```bash
curl -X DELETE "https://api.bling.com.br/Api/v3/nfe" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json"
```

**Python (requests)**

```python
import requests

url = "https://api.bling.com.br/Api/v3/nfe"
headers = {
    "Authorization": "Bearer YOUR_ACCESS_TOKEN",
    "Content-Type": "application/json"
}

response = requests.delete(url, headers=headers)
print(response.json())
```

**JavaScript (fetch)**

```javascript
const url = "https://api.bling.com.br/Api/v3/nfe";
const headers = {
  "Authorization": "Bearer YOUR_ACCESS_TOKEN",
  "Content-Type": "application/json"
};

fetch(url, {
  method: "DELETE",
  headers: headers
})
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error("Error:", error));
```

---

### GET `/nfe/{idNotaFiscal}`

**Obtém uma nota fiscal**

Obtém uma nota fiscal pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idNotaFiscal | path | **Yes** | integer | ID da nota fiscal |

#### Responses

**200** - 

**Example Response (200)**

```json
{
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
```

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

#### Code Examples

**cURL**

```bash
curl -X GET "https://api.bling.com.br/Api/v3/nfe/{idNotaFiscal}" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json"
```

**Python (requests)**

```python
import requests

url = "https://api.bling.com.br/Api/v3/nfe/{idNotaFiscal}"
headers = {
    "Authorization": "Bearer YOUR_ACCESS_TOKEN",
    "Content-Type": "application/json"
}

response = requests.get(url, headers=headers)
print(response.json())
```

**JavaScript (fetch)**

```javascript
const url = "https://api.bling.com.br/Api/v3/nfe/{idNotaFiscal}";
const headers = {
  "Authorization": "Bearer YOUR_ACCESS_TOKEN",
  "Content-Type": "application/json"
};

fetch(url, {
  method: "GET",
  headers: headers
})
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error("Error:", error));
```

---

### PUT `/nfe/{idNotaFiscal}`

**Altera uma nota fiscal**

Altera uma nota fiscal pelo ID. Notas com vínculos possuem restrições de atualização. Notas autorizadas não podem ter dados fiscais alterados: valores, impostos, informações do destinatário e qualquer outro dado transmitido no XML da nota.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idNotaFiscal | path | **Yes** | integer | ID da nota fiscal |

#### Request Body

**Content-Type:** `application/json`

**Example Request**

```json
{
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
      "valor": 49.9,
      "descricao": "Camiseta Básica Preta"
    }
  ],
  "transporte": {
    "fretePorConta": 0,
    "transportador": {
      "nome": "Transportadora XYZ"
    }
  }
}
```

#### Responses

**200** - 

**Example Response (200)**

```json
{
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
```

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

#### Code Examples

**cURL**

```bash
curl -X PUT "https://api.bling.com.br/Api/v3/nfe/{idNotaFiscal}" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
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
      "valor": 49.9,
      "descricao": "Camiseta Básica Preta"
    }
  ],
  "transporte": {
    "fretePorConta": 0,
    "transportador": {
      "nome": "Transportadora XYZ"
    }
  }
}'
```

**Python (requests)**

```python
import requests

url = "https://api.bling.com.br/Api/v3/nfe/{idNotaFiscal}"
headers = {
    "Authorization": "Bearer YOUR_ACCESS_TOKEN",
    "Content-Type": "application/json"
}

data = {
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
            "valor": 49.9,
            "descricao": "Camiseta Básica Preta"
        }
    ],
    "transporte": {
        "fretePorConta": 0,
        "transportador": {
            "nome": "Transportadora XYZ"
        }
    }
}

response = requests.put(url, headers=headers, json=data)
print(response.json())
```

**JavaScript (fetch)**

```javascript
const url = "https://api.bling.com.br/Api/v3/nfe/{idNotaFiscal}";
const headers = {
  "Authorization": "Bearer YOUR_ACCESS_TOKEN",
  "Content-Type": "application/json"
};

const data = {
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
      "valor": 49.9,
      "descricao": "Camiseta Básica Preta"
    }
  ],
  "transporte": {
    "fretePorConta": 0,
    "transportador": {
      "nome": "Transportadora XYZ"
    }
  }
};

fetch(url, {
  method: "PUT",
  headers: headers,
  body: JSON.stringify(data)
})
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error("Error:", error));
```

---

### POST `/nfe/{idNotaFiscal}/enviar`

**Envia uma nota fiscal**

Envia uma nota fiscal pelo ID para emissão na Sefaz.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idNotaFiscal | path | **Yes** | integer | ID da nota fiscal |
| enviarEmail | query | No | boolean | Define se deve enviar email após a emissão da nota fiscal |

#### Responses

**200** - 

**Example Response (200)**

```json
{
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
```

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

#### Code Examples

**cURL**

```bash
curl -X POST "https://api.bling.com.br/Api/v3/nfe/{idNotaFiscal}/enviar" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
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
      "valor": 49.9,
      "descricao": "Camiseta Básica Preta"
    }
  ],
  "transporte": {
    "fretePorConta": 0,
    "transportador": {
      "nome": "Transportadora XYZ"
    }
  }
}'
```

**Python (requests)**

```python
import requests

url = "https://api.bling.com.br/Api/v3/nfe/{idNotaFiscal}/enviar"
headers = {
    "Authorization": "Bearer YOUR_ACCESS_TOKEN",
    "Content-Type": "application/json"
}

data = {
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
            "valor": 49.9,
            "descricao": "Camiseta Básica Preta"
        }
    ],
    "transporte": {
        "fretePorConta": 0,
        "transportador": {
            "nome": "Transportadora XYZ"
        }
    }
}

response = requests.post(url, headers=headers, json=data)
print(response.json())
```

**JavaScript (fetch)**

```javascript
const url = "https://api.bling.com.br/Api/v3/nfe/{idNotaFiscal}/enviar";
const headers = {
  "Authorization": "Bearer YOUR_ACCESS_TOKEN",
  "Content-Type": "application/json"
};

const data = {
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
      "valor": 49.9,
      "descricao": "Camiseta Básica Preta"
    }
  ],
  "transporte": {
    "fretePorConta": 0,
    "transportador": {
      "nome": "Transportadora XYZ"
    }
  }
};

fetch(url, {
  method: "POST",
  headers: headers,
  body: JSON.stringify(data)
})
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error("Error:", error));
```

---

### POST `/nfe/{idNotaFiscal}/lancar-contas`

**Lança as contas de uma nota fiscal**

Lança as contas de uma nota fiscal pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idNotaFiscal | path | **Yes** | integer | ID da nota fiscal |

#### Responses

**204** - No content.

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

#### Code Examples

**cURL**

```bash
curl -X POST "https://api.bling.com.br/Api/v3/nfe/{idNotaFiscal}/lancar-contas" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
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
      "valor": 49.9,
      "descricao": "Camiseta Básica Preta"
    }
  ],
  "transporte": {
    "fretePorConta": 0,
    "transportador": {
      "nome": "Transportadora XYZ"
    }
  }
}'
```

**Python (requests)**

```python
import requests

url = "https://api.bling.com.br/Api/v3/nfe/{idNotaFiscal}/lancar-contas"
headers = {
    "Authorization": "Bearer YOUR_ACCESS_TOKEN",
    "Content-Type": "application/json"
}

data = {
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
            "valor": 49.9,
            "descricao": "Camiseta Básica Preta"
        }
    ],
    "transporte": {
        "fretePorConta": 0,
        "transportador": {
            "nome": "Transportadora XYZ"
        }
    }
}

response = requests.post(url, headers=headers, json=data)
print(response.json())
```

**JavaScript (fetch)**

```javascript
const url = "https://api.bling.com.br/Api/v3/nfe/{idNotaFiscal}/lancar-contas";
const headers = {
  "Authorization": "Bearer YOUR_ACCESS_TOKEN",
  "Content-Type": "application/json"
};

const data = {
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
      "valor": 49.9,
      "descricao": "Camiseta Básica Preta"
    }
  ],
  "transporte": {
    "fretePorConta": 0,
    "transportador": {
      "nome": "Transportadora XYZ"
    }
  }
};

fetch(url, {
  method: "POST",
  headers: headers,
  body: JSON.stringify(data)
})
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error("Error:", error));
```

---

### POST `/nfe/{idNotaFiscal}/estornar-contas`

**Estorna as contas de uma nota fiscal**

Estorna as contas de uma nota fiscal pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idNotaFiscal | path | **Yes** | integer | ID da nota fiscal |

#### Responses

**204** - No content.

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

#### Code Examples

**cURL**

```bash
curl -X POST "https://api.bling.com.br/Api/v3/nfe/{idNotaFiscal}/estornar-contas" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
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
      "valor": 49.9,
      "descricao": "Camiseta Básica Preta"
    }
  ],
  "transporte": {
    "fretePorConta": 0,
    "transportador": {
      "nome": "Transportadora XYZ"
    }
  }
}'
```

**Python (requests)**

```python
import requests

url = "https://api.bling.com.br/Api/v3/nfe/{idNotaFiscal}/estornar-contas"
headers = {
    "Authorization": "Bearer YOUR_ACCESS_TOKEN",
    "Content-Type": "application/json"
}

data = {
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
            "valor": 49.9,
            "descricao": "Camiseta Básica Preta"
        }
    ],
    "transporte": {
        "fretePorConta": 0,
        "transportador": {
            "nome": "Transportadora XYZ"
        }
    }
}

response = requests.post(url, headers=headers, json=data)
print(response.json())
```

**JavaScript (fetch)**

```javascript
const url = "https://api.bling.com.br/Api/v3/nfe/{idNotaFiscal}/estornar-contas";
const headers = {
  "Authorization": "Bearer YOUR_ACCESS_TOKEN",
  "Content-Type": "application/json"
};

const data = {
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
      "valor": 49.9,
      "descricao": "Camiseta Básica Preta"
    }
  ],
  "transporte": {
    "fretePorConta": 0,
    "transportador": {
      "nome": "Transportadora XYZ"
    }
  }
};

fetch(url, {
  method: "POST",
  headers: headers,
  body: JSON.stringify(data)
})
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error("Error:", error));
```

---

### POST `/nfe/{idNotaFiscal}/lancar-estoque`

**Lança o estoque de uma nota fiscal no depósito padrão**

Lança o estoque de uma nota fiscal pelo ID, no depósito padrão.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idNotaFiscal | path | **Yes** | integer | ID da nota fiscal |

#### Responses

**204** - No content.

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

#### Code Examples

**cURL**

```bash
curl -X POST "https://api.bling.com.br/Api/v3/nfe/{idNotaFiscal}/lancar-estoque" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
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
      "valor": 49.9,
      "descricao": "Camiseta Básica Preta"
    }
  ],
  "transporte": {
    "fretePorConta": 0,
    "transportador": {
      "nome": "Transportadora XYZ"
    }
  }
}'
```

**Python (requests)**

```python
import requests

url = "https://api.bling.com.br/Api/v3/nfe/{idNotaFiscal}/lancar-estoque"
headers = {
    "Authorization": "Bearer YOUR_ACCESS_TOKEN",
    "Content-Type": "application/json"
}

data = {
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
            "valor": 49.9,
            "descricao": "Camiseta Básica Preta"
        }
    ],
    "transporte": {
        "fretePorConta": 0,
        "transportador": {
            "nome": "Transportadora XYZ"
        }
    }
}

response = requests.post(url, headers=headers, json=data)
print(response.json())
```

**JavaScript (fetch)**

```javascript
const url = "https://api.bling.com.br/Api/v3/nfe/{idNotaFiscal}/lancar-estoque";
const headers = {
  "Authorization": "Bearer YOUR_ACCESS_TOKEN",
  "Content-Type": "application/json"
};

const data = {
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
      "valor": 49.9,
      "descricao": "Camiseta Básica Preta"
    }
  ],
  "transporte": {
    "fretePorConta": 0,
    "transportador": {
      "nome": "Transportadora XYZ"
    }
  }
};

fetch(url, {
  method: "POST",
  headers: headers,
  body: JSON.stringify(data)
})
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error("Error:", error));
```

---

### POST `/nfe/{idNotaFiscal}/lancar-estoque/{idDeposito}`

**Lança o estoque de uma nota fiscal especificando o depósito**

Lança o estoque de uma nota fiscal pelo ID, especificando o ID do depósito.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idNotaFiscal | path | **Yes** | integer | ID da nota fiscal |
| idDeposito | path | **Yes** | integer | ID do depósito |

#### Responses

**204** - No content.

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

#### Code Examples

**cURL**

```bash
curl -X POST "https://api.bling.com.br/Api/v3/nfe/{idNotaFiscal}/lancar-estoque/{idDeposito}" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
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
      "valor": 49.9,
      "descricao": "Camiseta Básica Preta"
    }
  ],
  "transporte": {
    "fretePorConta": 0,
    "transportador": {
      "nome": "Transportadora XYZ"
    }
  }
}'
```

**Python (requests)**

```python
import requests

url = "https://api.bling.com.br/Api/v3/nfe/{idNotaFiscal}/lancar-estoque/{idDeposito}"
headers = {
    "Authorization": "Bearer YOUR_ACCESS_TOKEN",
    "Content-Type": "application/json"
}

data = {
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
            "valor": 49.9,
            "descricao": "Camiseta Básica Preta"
        }
    ],
    "transporte": {
        "fretePorConta": 0,
        "transportador": {
            "nome": "Transportadora XYZ"
        }
    }
}

response = requests.post(url, headers=headers, json=data)
print(response.json())
```

**JavaScript (fetch)**

```javascript
const url = "https://api.bling.com.br/Api/v3/nfe/{idNotaFiscal}/lancar-estoque/{idDeposito}";
const headers = {
  "Authorization": "Bearer YOUR_ACCESS_TOKEN",
  "Content-Type": "application/json"
};

const data = {
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
      "valor": 49.9,
      "descricao": "Camiseta Básica Preta"
    }
  ],
  "transporte": {
    "fretePorConta": 0,
    "transportador": {
      "nome": "Transportadora XYZ"
    }
  }
};

fetch(url, {
  method: "POST",
  headers: headers,
  body: JSON.stringify(data)
})
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error("Error:", error));
```

---

### POST `/nfe/{idNotaFiscal}/estornar-estoque`

**Estorna o estoque de uma nota fiscal**

Estorna o estoque de uma nota fiscal pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idNotaFiscal | path | **Yes** | integer | ID da nota fiscal |

#### Responses

**204** - No content.

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

#### Code Examples

**cURL**

```bash
curl -X POST "https://api.bling.com.br/Api/v3/nfe/{idNotaFiscal}/estornar-estoque" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
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
      "valor": 49.9,
      "descricao": "Camiseta Básica Preta"
    }
  ],
  "transporte": {
    "fretePorConta": 0,
    "transportador": {
      "nome": "Transportadora XYZ"
    }
  }
}'
```

**Python (requests)**

```python
import requests

url = "https://api.bling.com.br/Api/v3/nfe/{idNotaFiscal}/estornar-estoque"
headers = {
    "Authorization": "Bearer YOUR_ACCESS_TOKEN",
    "Content-Type": "application/json"
}

data = {
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
            "valor": 49.9,
            "descricao": "Camiseta Básica Preta"
        }
    ],
    "transporte": {
        "fretePorConta": 0,
        "transportador": {
            "nome": "Transportadora XYZ"
        }
    }
}

response = requests.post(url, headers=headers, json=data)
print(response.json())
```

**JavaScript (fetch)**

```javascript
const url = "https://api.bling.com.br/Api/v3/nfe/{idNotaFiscal}/estornar-estoque";
const headers = {
  "Authorization": "Bearer YOUR_ACCESS_TOKEN",
  "Content-Type": "application/json"
};

const data = {
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
      "valor": 49.9,
      "descricao": "Camiseta Básica Preta"
    }
  ],
  "transporte": {
    "fretePorConta": 0,
    "transportador": {
      "nome": "Transportadora XYZ"
    }
  }
};

fetch(url, {
  method: "POST",
  headers: headers,
  body: JSON.stringify(data)
})
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error("Error:", error));
```

---

## Notas Fiscais de Consumidor Eletrônicas

### GET `/nfce`

**Obtém notas fiscais de consumidor**

Obtém notas fiscais de consumidor paginadas.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| pagina | query | No | integer | N° da página da listagem |
| limite | query | No | integer | Quantidade de registros que devem ser exibidos por página |
| idTransportador | query | No | integer | ID do contato do transportador |
| chaveAcesso | query | No | integer | Chave de acesso |
| numero | query | No | integer | Número da nota fiscal de consumidor |
| serie | query | No | integer | Série |
| situacao | query | No | integer (enum) | `1` Pendente<br>`2` Cancelada<br>`3` Aguardando recibo<br>`4` Rejeitada<br>`5` Autorizada<br>`6` Emitida DANFE<br>`7` Registrada<br>`8` Aguardando protocolo<br>`9` Denegada<br>`10` Consulta situação<br>`11` Bloqueada |
| dataEmissaoInicial | query | No | string | Data e hora inicial de emissão |
| dataEmissaoFinal | query | No | string | Data e hora final de emissão |

#### Responses

**200** - 

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

#### Code Examples

**cURL**

```bash
curl -X GET "https://api.bling.com.br/Api/v3/nfce" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json"
```

**Python (requests)**

```python
import requests

url = "https://api.bling.com.br/Api/v3/nfce"
headers = {
    "Authorization": "Bearer YOUR_ACCESS_TOKEN",
    "Content-Type": "application/json"
}

response = requests.get(url, headers=headers)
print(response.json())
```

**JavaScript (fetch)**

```javascript
const url = "https://api.bling.com.br/Api/v3/nfce";
const headers = {
  "Authorization": "Bearer YOUR_ACCESS_TOKEN",
  "Content-Type": "application/json"
};

fetch(url, {
  method: "GET",
  headers: headers
})
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error("Error:", error));
```

---

### POST `/nfce`

**Cria uma nota fiscal de consumidor**

Cria uma nota fiscal de consumidor.

#### Request Body

**Content-Type:** `application/json`

**Example Request**

```json
{
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
      "valor": 49.9,
      "descricao": "Camiseta Básica Preta"
    }
  ],
  "transporte": {
    "fretePorConta": 0,
    "transportador": {
      "nome": "Transportadora XYZ"
    }
  }
}
```

#### Responses

**201** - 

**Example Response (201)**

```json
{
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
```

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

#### Code Examples

**cURL**

```bash
curl -X POST "https://api.bling.com.br/Api/v3/nfce" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
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
      "valor": 49.9,
      "descricao": "Camiseta Básica Preta"
    }
  ],
  "transporte": {
    "fretePorConta": 0,
    "transportador": {
      "nome": "Transportadora XYZ"
    }
  }
}'
```

**Python (requests)**

```python
import requests

url = "https://api.bling.com.br/Api/v3/nfce"
headers = {
    "Authorization": "Bearer YOUR_ACCESS_TOKEN",
    "Content-Type": "application/json"
}

data = {
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
            "valor": 49.9,
            "descricao": "Camiseta Básica Preta"
        }
    ],
    "transporte": {
        "fretePorConta": 0,
        "transportador": {
            "nome": "Transportadora XYZ"
        }
    }
}

response = requests.post(url, headers=headers, json=data)
print(response.json())
```

**JavaScript (fetch)**

```javascript
const url = "https://api.bling.com.br/Api/v3/nfce";
const headers = {
  "Authorization": "Bearer YOUR_ACCESS_TOKEN",
  "Content-Type": "application/json"
};

const data = {
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
      "valor": 49.9,
      "descricao": "Camiseta Básica Preta"
    }
  ],
  "transporte": {
    "fretePorConta": 0,
    "transportador": {
      "nome": "Transportadora XYZ"
    }
  }
};

fetch(url, {
  method: "POST",
  headers: headers,
  body: JSON.stringify(data)
})
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error("Error:", error));
```

---

### GET `/nfce/{idNotaFiscalConsumidor}`

**Obtém uma nota fiscal de consumidor**

Obtém uma nota fiscal de consumidor pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idNotaFiscalConsumidor | path | **Yes** | integer | ID da nota fiscal de consumidor |

#### Responses

**200** - 

**Example Response (200)**

```json
{
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
```

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

#### Code Examples

**cURL**

```bash
curl -X GET "https://api.bling.com.br/Api/v3/nfce/{idNotaFiscalConsumidor}" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json"
```

**Python (requests)**

```python
import requests

url = "https://api.bling.com.br/Api/v3/nfce/{idNotaFiscalConsumidor}"
headers = {
    "Authorization": "Bearer YOUR_ACCESS_TOKEN",
    "Content-Type": "application/json"
}

response = requests.get(url, headers=headers)
print(response.json())
```

**JavaScript (fetch)**

```javascript
const url = "https://api.bling.com.br/Api/v3/nfce/{idNotaFiscalConsumidor}";
const headers = {
  "Authorization": "Bearer YOUR_ACCESS_TOKEN",
  "Content-Type": "application/json"
};

fetch(url, {
  method: "GET",
  headers: headers
})
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error("Error:", error));
```

---

### PUT `/nfce/{idNotaFiscalConsumidor}`

**Altera uma nota fiscal de consumidor**

Altera uma nota fiscal de consumidor.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idNotaFiscalConsumidor | path | **Yes** | integer | ID da nota fiscal de consumidor |

#### Request Body

**Content-Type:** `application/json`

**Example Request**

```json
{
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
      "valor": 49.9,
      "descricao": "Camiseta Básica Preta"
    }
  ],
  "transporte": {
    "fretePorConta": 0,
    "transportador": {
      "nome": "Transportadora XYZ"
    }
  }
}
```

#### Responses

**200** - 

**Example Response (200)**

```json
{
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
```

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

#### Code Examples

**cURL**

```bash
curl -X PUT "https://api.bling.com.br/Api/v3/nfce/{idNotaFiscalConsumidor}" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
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
      "valor": 49.9,
      "descricao": "Camiseta Básica Preta"
    }
  ],
  "transporte": {
    "fretePorConta": 0,
    "transportador": {
      "nome": "Transportadora XYZ"
    }
  }
}'
```

**Python (requests)**

```python
import requests

url = "https://api.bling.com.br/Api/v3/nfce/{idNotaFiscalConsumidor}"
headers = {
    "Authorization": "Bearer YOUR_ACCESS_TOKEN",
    "Content-Type": "application/json"
}

data = {
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
            "valor": 49.9,
            "descricao": "Camiseta Básica Preta"
        }
    ],
    "transporte": {
        "fretePorConta": 0,
        "transportador": {
            "nome": "Transportadora XYZ"
        }
    }
}

response = requests.put(url, headers=headers, json=data)
print(response.json())
```

**JavaScript (fetch)**

```javascript
const url = "https://api.bling.com.br/Api/v3/nfce/{idNotaFiscalConsumidor}";
const headers = {
  "Authorization": "Bearer YOUR_ACCESS_TOKEN",
  "Content-Type": "application/json"
};

const data = {
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
      "valor": 49.9,
      "descricao": "Camiseta Básica Preta"
    }
  ],
  "transporte": {
    "fretePorConta": 0,
    "transportador": {
      "nome": "Transportadora XYZ"
    }
  }
};

fetch(url, {
  method: "PUT",
  headers: headers,
  body: JSON.stringify(data)
})
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error("Error:", error));
```

---

### POST `/nfce/{idNotaFiscalConsumidor}/enviar`

**Envia uma nota de consumidor**

Envia uma nota de consumidor pelo ID para emissão na Sefaz.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idNotaFiscalConsumidor | path | **Yes** | integer | ID da nota fiscal de consumidor |

#### Responses

**200** - 

**Example Response (200)**

```json
{
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
```

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

#### Code Examples

**cURL**

```bash
curl -X POST "https://api.bling.com.br/Api/v3/nfce/{idNotaFiscalConsumidor}/enviar" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
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
      "valor": 49.9,
      "descricao": "Camiseta Básica Preta"
    }
  ],
  "transporte": {
    "fretePorConta": 0,
    "transportador": {
      "nome": "Transportadora XYZ"
    }
  }
}'
```

**Python (requests)**

```python
import requests

url = "https://api.bling.com.br/Api/v3/nfce/{idNotaFiscalConsumidor}/enviar"
headers = {
    "Authorization": "Bearer YOUR_ACCESS_TOKEN",
    "Content-Type": "application/json"
}

data = {
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
            "valor": 49.9,
            "descricao": "Camiseta Básica Preta"
        }
    ],
    "transporte": {
        "fretePorConta": 0,
        "transportador": {
            "nome": "Transportadora XYZ"
        }
    }
}

response = requests.post(url, headers=headers, json=data)
print(response.json())
```

**JavaScript (fetch)**

```javascript
const url = "https://api.bling.com.br/Api/v3/nfce/{idNotaFiscalConsumidor}/enviar";
const headers = {
  "Authorization": "Bearer YOUR_ACCESS_TOKEN",
  "Content-Type": "application/json"
};

const data = {
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
      "valor": 49.9,
      "descricao": "Camiseta Básica Preta"
    }
  ],
  "transporte": {
    "fretePorConta": 0,
    "transportador": {
      "nome": "Transportadora XYZ"
    }
  }
};

fetch(url, {
  method: "POST",
  headers: headers,
  body: JSON.stringify(data)
})
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error("Error:", error));
```

---

### POST `/nfce/{idNotaFiscalConsumidor}/lancar-contas`

**Lança as contas de uma nota fiscal**

Lança as contas de uma nota fiscal pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idNotaFiscalConsumidor | path | **Yes** | integer | ID da nota fiscal de consumidor |

#### Responses

**204** - No content.

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

#### Code Examples

**cURL**

```bash
curl -X POST "https://api.bling.com.br/Api/v3/nfce/{idNotaFiscalConsumidor}/lancar-contas" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
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
      "valor": 49.9,
      "descricao": "Camiseta Básica Preta"
    }
  ],
  "transporte": {
    "fretePorConta": 0,
    "transportador": {
      "nome": "Transportadora XYZ"
    }
  }
}'
```

**Python (requests)**

```python
import requests

url = "https://api.bling.com.br/Api/v3/nfce/{idNotaFiscalConsumidor}/lancar-contas"
headers = {
    "Authorization": "Bearer YOUR_ACCESS_TOKEN",
    "Content-Type": "application/json"
}

data = {
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
            "valor": 49.9,
            "descricao": "Camiseta Básica Preta"
        }
    ],
    "transporte": {
        "fretePorConta": 0,
        "transportador": {
            "nome": "Transportadora XYZ"
        }
    }
}

response = requests.post(url, headers=headers, json=data)
print(response.json())
```

**JavaScript (fetch)**

```javascript
const url = "https://api.bling.com.br/Api/v3/nfce/{idNotaFiscalConsumidor}/lancar-contas";
const headers = {
  "Authorization": "Bearer YOUR_ACCESS_TOKEN",
  "Content-Type": "application/json"
};

const data = {
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
      "valor": 49.9,
      "descricao": "Camiseta Básica Preta"
    }
  ],
  "transporte": {
    "fretePorConta": 0,
    "transportador": {
      "nome": "Transportadora XYZ"
    }
  }
};

fetch(url, {
  method: "POST",
  headers: headers,
  body: JSON.stringify(data)
})
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error("Error:", error));
```

---

### POST `/nfce/{idNotaFiscalConsumidor}/estornar-contas`

**Estorna as contas de uma nota fiscal**

Estorna as contas de uma nota fiscal pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idNotaFiscalConsumidor | path | **Yes** | integer | ID da nota fiscal de consumidor |

#### Responses

**204** - No content.

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

#### Code Examples

**cURL**

```bash
curl -X POST "https://api.bling.com.br/Api/v3/nfce/{idNotaFiscalConsumidor}/estornar-contas" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
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
      "valor": 49.9,
      "descricao": "Camiseta Básica Preta"
    }
  ],
  "transporte": {
    "fretePorConta": 0,
    "transportador": {
      "nome": "Transportadora XYZ"
    }
  }
}'
```

**Python (requests)**

```python
import requests

url = "https://api.bling.com.br/Api/v3/nfce/{idNotaFiscalConsumidor}/estornar-contas"
headers = {
    "Authorization": "Bearer YOUR_ACCESS_TOKEN",
    "Content-Type": "application/json"
}

data = {
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
            "valor": 49.9,
            "descricao": "Camiseta Básica Preta"
        }
    ],
    "transporte": {
        "fretePorConta": 0,
        "transportador": {
            "nome": "Transportadora XYZ"
        }
    }
}

response = requests.post(url, headers=headers, json=data)
print(response.json())
```

**JavaScript (fetch)**

```javascript
const url = "https://api.bling.com.br/Api/v3/nfce/{idNotaFiscalConsumidor}/estornar-contas";
const headers = {
  "Authorization": "Bearer YOUR_ACCESS_TOKEN",
  "Content-Type": "application/json"
};

const data = {
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
      "valor": 49.9,
      "descricao": "Camiseta Básica Preta"
    }
  ],
  "transporte": {
    "fretePorConta": 0,
    "transportador": {
      "nome": "Transportadora XYZ"
    }
  }
};

fetch(url, {
  method: "POST",
  headers: headers,
  body: JSON.stringify(data)
})
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error("Error:", error));
```

---

### POST `/nfce/{idNotaFiscalConsumidor}/lancar-estoque`

**Lança o estoque de uma nota fiscal no depósito padrão**

Lança o estoque de uma nota fiscal pelo ID, no depósito padrão.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idNotaFiscalConsumidor | path | **Yes** | integer | ID da nota fiscal de consumidor |

#### Responses

**204** - No content.

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

#### Code Examples

**cURL**

```bash
curl -X POST "https://api.bling.com.br/Api/v3/nfce/{idNotaFiscalConsumidor}/lancar-estoque" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
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
      "valor": 49.9,
      "descricao": "Camiseta Básica Preta"
    }
  ],
  "transporte": {
    "fretePorConta": 0,
    "transportador": {
      "nome": "Transportadora XYZ"
    }
  }
}'
```

**Python (requests)**

```python
import requests

url = "https://api.bling.com.br/Api/v3/nfce/{idNotaFiscalConsumidor}/lancar-estoque"
headers = {
    "Authorization": "Bearer YOUR_ACCESS_TOKEN",
    "Content-Type": "application/json"
}

data = {
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
            "valor": 49.9,
            "descricao": "Camiseta Básica Preta"
        }
    ],
    "transporte": {
        "fretePorConta": 0,
        "transportador": {
            "nome": "Transportadora XYZ"
        }
    }
}

response = requests.post(url, headers=headers, json=data)
print(response.json())
```

**JavaScript (fetch)**

```javascript
const url = "https://api.bling.com.br/Api/v3/nfce/{idNotaFiscalConsumidor}/lancar-estoque";
const headers = {
  "Authorization": "Bearer YOUR_ACCESS_TOKEN",
  "Content-Type": "application/json"
};

const data = {
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
      "valor": 49.9,
      "descricao": "Camiseta Básica Preta"
    }
  ],
  "transporte": {
    "fretePorConta": 0,
    "transportador": {
      "nome": "Transportadora XYZ"
    }
  }
};

fetch(url, {
  method: "POST",
  headers: headers,
  body: JSON.stringify(data)
})
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error("Error:", error));
```

---

### POST `/nfce/{idNotaFiscalConsumidor}/lancar-estoque/{idDeposito}`

**Lança o estoque de uma nota fiscal especificando o depósito**

Lança o estoque de uma nota fiscal pelo ID, especificando o ID do depósito.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idNotaFiscalConsumidor | path | **Yes** | integer | ID da nota fiscal de consumidor |
| idDeposito | path | **Yes** | integer | ID do depósito |

#### Responses

**204** - No content.

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

#### Code Examples

**cURL**

```bash
curl -X POST "https://api.bling.com.br/Api/v3/nfce/{idNotaFiscalConsumidor}/lancar-estoque/{idDeposito}" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
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
      "valor": 49.9,
      "descricao": "Camiseta Básica Preta"
    }
  ],
  "transporte": {
    "fretePorConta": 0,
    "transportador": {
      "nome": "Transportadora XYZ"
    }
  }
}'
```

**Python (requests)**

```python
import requests

url = "https://api.bling.com.br/Api/v3/nfce/{idNotaFiscalConsumidor}/lancar-estoque/{idDeposito}"
headers = {
    "Authorization": "Bearer YOUR_ACCESS_TOKEN",
    "Content-Type": "application/json"
}

data = {
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
            "valor": 49.9,
            "descricao": "Camiseta Básica Preta"
        }
    ],
    "transporte": {
        "fretePorConta": 0,
        "transportador": {
            "nome": "Transportadora XYZ"
        }
    }
}

response = requests.post(url, headers=headers, json=data)
print(response.json())
```

**JavaScript (fetch)**

```javascript
const url = "https://api.bling.com.br/Api/v3/nfce/{idNotaFiscalConsumidor}/lancar-estoque/{idDeposito}";
const headers = {
  "Authorization": "Bearer YOUR_ACCESS_TOKEN",
  "Content-Type": "application/json"
};

const data = {
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
      "valor": 49.9,
      "descricao": "Camiseta Básica Preta"
    }
  ],
  "transporte": {
    "fretePorConta": 0,
    "transportador": {
      "nome": "Transportadora XYZ"
    }
  }
};

fetch(url, {
  method: "POST",
  headers: headers,
  body: JSON.stringify(data)
})
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error("Error:", error));
```

---

### POST `/nfce/{idNotaFiscalConsumidor}/estornar-estoque`

**Estorna o estoque de uma nota fiscal**

Estorna o estoque de uma nota fiscal pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idNotaFiscalConsumidor | path | **Yes** | integer | ID da nota fiscal de consumidor |

#### Responses

**204** - No content.

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

#### Code Examples

**cURL**

```bash
curl -X POST "https://api.bling.com.br/Api/v3/nfce/{idNotaFiscalConsumidor}/estornar-estoque" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
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
      "valor": 49.9,
      "descricao": "Camiseta Básica Preta"
    }
  ],
  "transporte": {
    "fretePorConta": 0,
    "transportador": {
      "nome": "Transportadora XYZ"
    }
  }
}'
```

**Python (requests)**

```python
import requests

url = "https://api.bling.com.br/Api/v3/nfce/{idNotaFiscalConsumidor}/estornar-estoque"
headers = {
    "Authorization": "Bearer YOUR_ACCESS_TOKEN",
    "Content-Type": "application/json"
}

data = {
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
            "valor": 49.9,
            "descricao": "Camiseta Básica Preta"
        }
    ],
    "transporte": {
        "fretePorConta": 0,
        "transportador": {
            "nome": "Transportadora XYZ"
        }
    }
}

response = requests.post(url, headers=headers, json=data)
print(response.json())
```

**JavaScript (fetch)**

```javascript
const url = "https://api.bling.com.br/Api/v3/nfce/{idNotaFiscalConsumidor}/estornar-estoque";
const headers = {
  "Authorization": "Bearer YOUR_ACCESS_TOKEN",
  "Content-Type": "application/json"
};

const data = {
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
      "valor": 49.9,
      "descricao": "Camiseta Básica Preta"
    }
  ],
  "transporte": {
    "fretePorConta": 0,
    "transportador": {
      "nome": "Transportadora XYZ"
    }
  }
};

fetch(url, {
  method: "POST",
  headers: headers,
  body: JSON.stringify(data)
})
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error("Error:", error));
```

---

## Notas Fiscais de Serviço Eletrônicas

### GET `/nfse`

**Obtém notas de serviços**

Obtém notas de serviços paginadas.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| pagina | query | No | integer | N° da página da listagem |
| limite | query | No | integer | Quantidade de registros que devem ser exibidos por página |
| situacao | query | No | integer (enum) | `0` Pendente <br> `1` Emitida <br> `2` Disponível para consulta <br> `3` Cancelada |
| dataEmissaoInicial | query | No | string | Data incial do período de emissão |
| dataEmissaoFinal | query | No | string | Data final do período de emissão |

#### Responses

**200** - 

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

---

### POST `/nfse`

**Cria uma nota de serviço**

Cria uma nota de serviço.

#### Request Body

**Content-Type:** `application/json`

**Example Request**

```json
{
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
      "valor": 49.9,
      "descricao": "Camiseta Básica Preta"
    }
  ],
  "transporte": {
    "fretePorConta": 0,
    "transportador": {
      "nome": "Transportadora XYZ"
    }
  }
}
```

#### Responses

**201** - 

**Example Response (201)**

```json
{
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
```

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

---

### GET `/nfse/{idNotaServico}`

**Obtém uma nota de serviço**

Obtém uma nota de serviço pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idNotaServico | path | **Yes** | integer | ID da nota de serviço |

#### Responses

**200** - 

**Example Response (200)**

```json
{
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
```

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

---

### DELETE `/nfse/{idNotaServico}`

**Exclui uma nota de serviço**

Exclui uma nota de serviço pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idNotaServico | path | **Yes** | integer | ID da nota de serviço |

#### Responses

**204** - No content.

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

---

### POST `/nfse/{idNotaServico}/enviar`

**Envia uma nota de serviço**

Envia uma nota de serviço pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idNotaServico | path | **Yes** | integer | ID da nota de serviço |

#### Responses

**200** - 

**Example Response (200)**

```json
{
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
```

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

---

### POST `/nfse/{idNotaServico}/cancelar`

**Cancela uma nota de serviço**

Cancela uma nota de serviço pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idNotaServico | path | **Yes** | integer | ID da nota de serviço |

#### Request Body

**Content-Type:** `application/json`

**Example Request**

```json
{
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
      "valor": 49.9,
      "descricao": "Camiseta Básica Preta"
    }
  ],
  "transporte": {
    "fretePorConta": 0,
    "transportador": {
      "nome": "Transportadora XYZ"
    }
  }
}
```

#### Responses

**204** - No content.

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

---

### GET `/nfse/configuracoes`

**Configurações de nota de serviço**

Obtém todas as configurações de nota de serviço.

#### Responses

**200** - 

---

### PUT `/nfse/configuracoes`

**Configurações de nota de serviço**

Cria e altera configurações para emissão de notas de serviço.

#### Request Body

**Content-Type:** `application/json`

**Example Request**

```json
{
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
      "valor": 49.9,
      "descricao": "Camiseta Básica Preta"
    }
  ],
  "transporte": {
    "fretePorConta": 0,
    "transportador": {
      "nome": "Transportadora XYZ"
    }
  }
}
```

#### Responses

**204** - No content.

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

---

## Notificações

### GET `/notificacoes`

**Obtém todas as notificações de uma empresa em um período**

Obtém todas as notificações de uma empresa no período informado. Caso período não seja informado, será considerado o ano atual.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| periodo | query | No | string | Apenas ano ou ano e mês em que a empresa foi notificada. Caso não informado, será utilizado o ano atual. |

#### Responses

**200** - 

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

---

### POST `/notificacoes/{idNotificacao}/confirmar-leitura`

**Marca notificação como lida**

Marca a notificação relacionada à empresa como lida.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idNotificacao | path | **Yes** | string | ULID da notificação. |

#### Responses

**200** - 

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

---

### GET `/notificacoes/quantidade`

**Obtém a quantidade de notificações de uma empresa em um período**

Obtém a quantidade de notificações de uma empresa no período informado. Caso período não seja informado, será considerado o ano atual.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| periodo | query | No | string | Apenas ano ou ano e mês em que a empresa foi notificada. Caso não informado, será utilizado o ano atual. |

#### Responses

**200** - 

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

---

## Ordens de Produção

### GET `/ordens-producao`

**Obtém ordens de produção**

Obtém ordens de produção paginadas.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| pagina | query | No | integer | N° da página da listagem |
| limite | query | No | integer | Quantidade de registros que devem ser exibidos por página |
| idsSituacoes[] | query | No | array&lt;integer&gt; | IDs das situações |

#### Responses

**200** - 

---

### POST `/ordens-producao`

**Cria uma ordem de produção**

Cria uma ordem de produção.

#### Request Body

**Content-Type:** `application/json`

#### Responses

**201** - 

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

---

### GET `/ordens-producao/{idOrdemProducao}`

**Obtém uma ordem de produção**

Obtém uma ordem de produção pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idOrdemProducao | path | **Yes** | integer | ID da ordem de produção |

#### Responses

**200** - 

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

---

### PUT `/ordens-producao/{idOrdemProducao}`

**Altera uma ordem de produção**

Altera uma ordem de produção pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idOrdemProducao | path | **Yes** | integer | ID da ordem de produção |

#### Request Body

**Content-Type:** `application/json`

#### Responses

**204** - No content.

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

---

### DELETE `/ordens-producao/{idOrdemProducao}`

**Remove uma ordem de produção**

Remove uma ordem de produção pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idOrdemProducao | path | **Yes** | integer | ID da ordem de produção |

#### Responses

**204** - No content.

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

---

### PUT `/ordens-producao/{idOrdemProducao}/situacoes`

**Altera a situação de uma ordem de produção**

Altera a situação de uma ordem de produção pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idOrdemProducao | path | **Yes** | integer | ID da ordem de produção |

#### Request Body

**Content-Type:** `application/json`

#### Responses

**204** - No content.

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

---

### POST `/ordens-producao/gerar-sob-demanda`

**Gera ordens de produção sob demanda**

Gera ordens de produção sob demanda (abaixo do estoque mínimo).

#### Responses

**201** - 

---

## Pedidos - Compras

### GET `/pedidos/compras`

**Obtém pedidos de compras**

Obtém pedidos de compras paginados.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| pagina | query | No | integer | N° da página da listagem |
| limite | query | No | integer | Quantidade de registros que devem ser exibidos por página |
| idFornecedor | query | No | integer | ID do contato do tipo fornecedor |
| valorSituacao | query | No | integer | Valor da situação |
| idSituacao | query | No | integer | ID da situação |
| dataInicial | query | No | string | Data inicial do período da compra |
| dataFinal | query | No | string | Data final do período da compra |
| idsNotasFiscais[] | query | No | array&lt;integer&gt; | IDs das notas fiscais de entrada |

#### Responses

**200** - 

#### Code Examples

**cURL**

```bash
curl -X GET "https://api.bling.com.br/Api/v3/pedidos/compras" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json"
```

**Python (requests)**

```python
import requests

url = "https://api.bling.com.br/Api/v3/pedidos/compras"
headers = {
    "Authorization": "Bearer YOUR_ACCESS_TOKEN",
    "Content-Type": "application/json"
}

response = requests.get(url, headers=headers)
print(response.json())
```

**JavaScript (fetch)**

```javascript
const url = "https://api.bling.com.br/Api/v3/pedidos/compras";
const headers = {
  "Authorization": "Bearer YOUR_ACCESS_TOKEN",
  "Content-Type": "application/json"
};

fetch(url, {
  method: "GET",
  headers: headers
})
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error("Error:", error));
```

---

### POST `/pedidos/compras`

**Cria um pedido de compra**

Cria um pedido de compra.

#### Request Body

**Content-Type:** `application/json`

**Example Request**

```json
{
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
      "valor": 49.9,
      "descricao": "Camiseta Básica Preta"
    }
  ],
  "parcelas": [
    {
      "data": "2024-01-15",
      "valor": 99.8,
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
    "valorFrete": 15.0
  }
}
```

#### Responses

**201** - 

**Example Response (201)**

```json
{
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
    "total": 114.8
  }
}
```

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

#### Code Examples

**cURL**

```bash
curl -X POST "https://api.bling.com.br/Api/v3/pedidos/compras" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
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
      "valor": 49.9,
      "descricao": "Camiseta Básica Preta"
    }
  ],
  "parcelas": [
    {
      "data": "2024-01-15",
      "valor": 99.8,
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
    "valorFrete": 15.0
  }
}'
```

**Python (requests)**

```python
import requests

url = "https://api.bling.com.br/Api/v3/pedidos/compras"
headers = {
    "Authorization": "Bearer YOUR_ACCESS_TOKEN",
    "Content-Type": "application/json"
}

data = {
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
            "valor": 49.9,
            "descricao": "Camiseta Básica Preta"
        }
    ],
    "parcelas": [
        {
            "data": "2024-01-15",
            "valor": 99.8,
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
        "valorFrete": 15.0
    }
}

response = requests.post(url, headers=headers, json=data)
print(response.json())
```

**JavaScript (fetch)**

```javascript
const url = "https://api.bling.com.br/Api/v3/pedidos/compras";
const headers = {
  "Authorization": "Bearer YOUR_ACCESS_TOKEN",
  "Content-Type": "application/json"
};

const data = {
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
      "valor": 49.9,
      "descricao": "Camiseta Básica Preta"
    }
  ],
  "parcelas": [
    {
      "data": "2024-01-15",
      "valor": 99.8,
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
    "valorFrete": 15.0
  }
};

fetch(url, {
  method: "POST",
  headers: headers,
  body: JSON.stringify(data)
})
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error("Error:", error));
```

---

### GET `/pedidos/compras/{idPedidoCompra}`

**Obtém um pedido de compra**

Obtém um pedido de compra pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idPedidoCompra | path | **Yes** | integer | ID do pedido de compra |

#### Responses

**200** - 

**Example Response (200)**

```json
{
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
    "total": 114.8
  }
}
```

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

#### Code Examples

**cURL**

```bash
curl -X GET "https://api.bling.com.br/Api/v3/pedidos/compras/{idPedidoCompra}" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json"
```

**Python (requests)**

```python
import requests

url = "https://api.bling.com.br/Api/v3/pedidos/compras/{idPedidoCompra}"
headers = {
    "Authorization": "Bearer YOUR_ACCESS_TOKEN",
    "Content-Type": "application/json"
}

response = requests.get(url, headers=headers)
print(response.json())
```

**JavaScript (fetch)**

```javascript
const url = "https://api.bling.com.br/Api/v3/pedidos/compras/{idPedidoCompra}";
const headers = {
  "Authorization": "Bearer YOUR_ACCESS_TOKEN",
  "Content-Type": "application/json"
};

fetch(url, {
  method: "GET",
  headers: headers
})
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error("Error:", error));
```

---

### PUT `/pedidos/compras/{idPedidoCompra}`

**Altera um pedido de compra**

Altera um pedido de compra pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idPedidoCompra | path | **Yes** | integer | ID do pedido de compra |

#### Request Body

**Content-Type:** `application/json`

**Example Request**

```json
{
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
      "valor": 49.9,
      "descricao": "Camiseta Básica Preta"
    }
  ],
  "parcelas": [
    {
      "data": "2024-01-15",
      "valor": 99.8,
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
    "valorFrete": 15.0
  }
}
```

#### Responses

**200** - 

**Example Response (200)**

```json
{
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
    "total": 114.8
  }
}
```

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

#### Code Examples

**cURL**

```bash
curl -X PUT "https://api.bling.com.br/Api/v3/pedidos/compras/{idPedidoCompra}" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
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
      "valor": 49.9,
      "descricao": "Camiseta Básica Preta"
    }
  ],
  "parcelas": [
    {
      "data": "2024-01-15",
      "valor": 99.8,
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
    "valorFrete": 15.0
  }
}'
```

**Python (requests)**

```python
import requests

url = "https://api.bling.com.br/Api/v3/pedidos/compras/{idPedidoCompra}"
headers = {
    "Authorization": "Bearer YOUR_ACCESS_TOKEN",
    "Content-Type": "application/json"
}

data = {
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
            "valor": 49.9,
            "descricao": "Camiseta Básica Preta"
        }
    ],
    "parcelas": [
        {
            "data": "2024-01-15",
            "valor": 99.8,
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
        "valorFrete": 15.0
    }
}

response = requests.put(url, headers=headers, json=data)
print(response.json())
```

**JavaScript (fetch)**

```javascript
const url = "https://api.bling.com.br/Api/v3/pedidos/compras/{idPedidoCompra}";
const headers = {
  "Authorization": "Bearer YOUR_ACCESS_TOKEN",
  "Content-Type": "application/json"
};

const data = {
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
      "valor": 49.9,
      "descricao": "Camiseta Básica Preta"
    }
  ],
  "parcelas": [
    {
      "data": "2024-01-15",
      "valor": 99.8,
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
    "valorFrete": 15.0
  }
};

fetch(url, {
  method: "PUT",
  headers: headers,
  body: JSON.stringify(data)
})
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error("Error:", error));
```

---

### DELETE `/pedidos/compras/{idPedidoCompra}`

**Remove um pedido de compra**

Remove um pedido de compra pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idPedidoCompra | path | **Yes** | integer | ID do pedido de compra |

#### Responses

**204** - No content.

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

#### Code Examples

**cURL**

```bash
curl -X DELETE "https://api.bling.com.br/Api/v3/pedidos/compras/{idPedidoCompra}" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json"
```

**Python (requests)**

```python
import requests

url = "https://api.bling.com.br/Api/v3/pedidos/compras/{idPedidoCompra}"
headers = {
    "Authorization": "Bearer YOUR_ACCESS_TOKEN",
    "Content-Type": "application/json"
}

response = requests.delete(url, headers=headers)
print(response.json())
```

**JavaScript (fetch)**

```javascript
const url = "https://api.bling.com.br/Api/v3/pedidos/compras/{idPedidoCompra}";
const headers = {
  "Authorization": "Bearer YOUR_ACCESS_TOKEN",
  "Content-Type": "application/json"
};

fetch(url, {
  method: "DELETE",
  headers: headers
})
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error("Error:", error));
```

---

### PATCH `/pedidos/compras/{idPedidoCompra}/situacoes`

**Altera a situação de um pedido de compra**

Altera a situação de um pedido de compra pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idPedidoCompra | path | **Yes** | integer | ID do pedido de compra |

#### Request Body

**Content-Type:** `application/json`

**Example Request**

```json
{
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
      "valor": 49.9,
      "descricao": "Camiseta Básica Preta"
    }
  ],
  "parcelas": [
    {
      "data": "2024-01-15",
      "valor": 99.8,
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
    "valorFrete": 15.0
  }
}
```

#### Responses

**204** - No content.

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

#### Code Examples

**cURL**

```bash
curl -X PATCH "https://api.bling.com.br/Api/v3/pedidos/compras/{idPedidoCompra}/situacoes" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
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
      "valor": 49.9,
      "descricao": "Camiseta Básica Preta"
    }
  ],
  "parcelas": [
    {
      "data": "2024-01-15",
      "valor": 99.8,
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
    "valorFrete": 15.0
  }
}'
```

**Python (requests)**

```python
import requests

url = "https://api.bling.com.br/Api/v3/pedidos/compras/{idPedidoCompra}/situacoes"
headers = {
    "Authorization": "Bearer YOUR_ACCESS_TOKEN",
    "Content-Type": "application/json"
}

data = {
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
            "valor": 49.9,
            "descricao": "Camiseta Básica Preta"
        }
    ],
    "parcelas": [
        {
            "data": "2024-01-15",
            "valor": 99.8,
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
        "valorFrete": 15.0
    }
}

response = requests.patch(url, headers=headers, json=data)
print(response.json())
```

**JavaScript (fetch)**

```javascript
const url = "https://api.bling.com.br/Api/v3/pedidos/compras/{idPedidoCompra}/situacoes";
const headers = {
  "Authorization": "Bearer YOUR_ACCESS_TOKEN",
  "Content-Type": "application/json"
};

const data = {
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
      "valor": 49.9,
      "descricao": "Camiseta Básica Preta"
    }
  ],
  "parcelas": [
    {
      "data": "2024-01-15",
      "valor": 99.8,
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
    "valorFrete": 15.0
  }
};

fetch(url, {
  method: "PATCH",
  headers: headers,
  body: JSON.stringify(data)
})
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error("Error:", error));
```

---

### POST `/pedidos/compras/{idPedidoCompra}/lancar-contas`

**Lança as contas de um pedido de compra**

Lança as contas de um pedido de compra pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idPedidoCompra | path | **Yes** | integer | ID do pedido de compra |

#### Responses

**204** - No content.

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

#### Code Examples

**cURL**

```bash
curl -X POST "https://api.bling.com.br/Api/v3/pedidos/compras/{idPedidoCompra}/lancar-contas" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
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
      "valor": 49.9,
      "descricao": "Camiseta Básica Preta"
    }
  ],
  "parcelas": [
    {
      "data": "2024-01-15",
      "valor": 99.8,
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
    "valorFrete": 15.0
  }
}'
```

**Python (requests)**

```python
import requests

url = "https://api.bling.com.br/Api/v3/pedidos/compras/{idPedidoCompra}/lancar-contas"
headers = {
    "Authorization": "Bearer YOUR_ACCESS_TOKEN",
    "Content-Type": "application/json"
}

data = {
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
            "valor": 49.9,
            "descricao": "Camiseta Básica Preta"
        }
    ],
    "parcelas": [
        {
            "data": "2024-01-15",
            "valor": 99.8,
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
        "valorFrete": 15.0
    }
}

response = requests.post(url, headers=headers, json=data)
print(response.json())
```

**JavaScript (fetch)**

```javascript
const url = "https://api.bling.com.br/Api/v3/pedidos/compras/{idPedidoCompra}/lancar-contas";
const headers = {
  "Authorization": "Bearer YOUR_ACCESS_TOKEN",
  "Content-Type": "application/json"
};

const data = {
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
      "valor": 49.9,
      "descricao": "Camiseta Básica Preta"
    }
  ],
  "parcelas": [
    {
      "data": "2024-01-15",
      "valor": 99.8,
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
    "valorFrete": 15.0
  }
};

fetch(url, {
  method: "POST",
  headers: headers,
  body: JSON.stringify(data)
})
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error("Error:", error));
```

---

### POST `/pedidos/compras/{idPedidoCompra}/estornar-contas`

**Estorna as contas de um pedido de compra**

Estorna as contas de um pedido de compra pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idPedidoCompra | path | **Yes** | integer | ID do pedido de compra |

#### Responses

**204** - No content.

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

#### Code Examples

**cURL**

```bash
curl -X POST "https://api.bling.com.br/Api/v3/pedidos/compras/{idPedidoCompra}/estornar-contas" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
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
      "valor": 49.9,
      "descricao": "Camiseta Básica Preta"
    }
  ],
  "parcelas": [
    {
      "data": "2024-01-15",
      "valor": 99.8,
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
    "valorFrete": 15.0
  }
}'
```

**Python (requests)**

```python
import requests

url = "https://api.bling.com.br/Api/v3/pedidos/compras/{idPedidoCompra}/estornar-contas"
headers = {
    "Authorization": "Bearer YOUR_ACCESS_TOKEN",
    "Content-Type": "application/json"
}

data = {
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
            "valor": 49.9,
            "descricao": "Camiseta Básica Preta"
        }
    ],
    "parcelas": [
        {
            "data": "2024-01-15",
            "valor": 99.8,
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
        "valorFrete": 15.0
    }
}

response = requests.post(url, headers=headers, json=data)
print(response.json())
```

**JavaScript (fetch)**

```javascript
const url = "https://api.bling.com.br/Api/v3/pedidos/compras/{idPedidoCompra}/estornar-contas";
const headers = {
  "Authorization": "Bearer YOUR_ACCESS_TOKEN",
  "Content-Type": "application/json"
};

const data = {
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
      "valor": 49.9,
      "descricao": "Camiseta Básica Preta"
    }
  ],
  "parcelas": [
    {
      "data": "2024-01-15",
      "valor": 99.8,
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
    "valorFrete": 15.0
  }
};

fetch(url, {
  method: "POST",
  headers: headers,
  body: JSON.stringify(data)
})
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error("Error:", error));
```

---

### POST `/pedidos/compras/{idPedidoCompra}/lancar-estoque`

**Lança o estoque de um pedido de compra**

Lança o estoque de um pedido de compra pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idPedidoCompra | path | **Yes** | integer | ID do pedido de compra |

#### Responses

**204** - No content.

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

#### Code Examples

**cURL**

```bash
curl -X POST "https://api.bling.com.br/Api/v3/pedidos/compras/{idPedidoCompra}/lancar-estoque" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
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
      "valor": 49.9,
      "descricao": "Camiseta Básica Preta"
    }
  ],
  "parcelas": [
    {
      "data": "2024-01-15",
      "valor": 99.8,
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
    "valorFrete": 15.0
  }
}'
```

**Python (requests)**

```python
import requests

url = "https://api.bling.com.br/Api/v3/pedidos/compras/{idPedidoCompra}/lancar-estoque"
headers = {
    "Authorization": "Bearer YOUR_ACCESS_TOKEN",
    "Content-Type": "application/json"
}

data = {
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
            "valor": 49.9,
            "descricao": "Camiseta Básica Preta"
        }
    ],
    "parcelas": [
        {
            "data": "2024-01-15",
            "valor": 99.8,
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
        "valorFrete": 15.0
    }
}

response = requests.post(url, headers=headers, json=data)
print(response.json())
```

**JavaScript (fetch)**

```javascript
const url = "https://api.bling.com.br/Api/v3/pedidos/compras/{idPedidoCompra}/lancar-estoque";
const headers = {
  "Authorization": "Bearer YOUR_ACCESS_TOKEN",
  "Content-Type": "application/json"
};

const data = {
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
      "valor": 49.9,
      "descricao": "Camiseta Básica Preta"
    }
  ],
  "parcelas": [
    {
      "data": "2024-01-15",
      "valor": 99.8,
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
    "valorFrete": 15.0
  }
};

fetch(url, {
  method: "POST",
  headers: headers,
  body: JSON.stringify(data)
})
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error("Error:", error));
```

---

### POST `/pedidos/compras/{idPedidoCompra}/estornar-estoque`

**Estorna o estoque de um pedido de compra**

Estorna o estoque de um pedido de compra pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idPedidoCompra | path | **Yes** | integer | ID do pedido de compra |

#### Responses

**204** - No content.

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

#### Code Examples

**cURL**

```bash
curl -X POST "https://api.bling.com.br/Api/v3/pedidos/compras/{idPedidoCompra}/estornar-estoque" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
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
      "valor": 49.9,
      "descricao": "Camiseta Básica Preta"
    }
  ],
  "parcelas": [
    {
      "data": "2024-01-15",
      "valor": 99.8,
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
    "valorFrete": 15.0
  }
}'
```

**Python (requests)**

```python
import requests

url = "https://api.bling.com.br/Api/v3/pedidos/compras/{idPedidoCompra}/estornar-estoque"
headers = {
    "Authorization": "Bearer YOUR_ACCESS_TOKEN",
    "Content-Type": "application/json"
}

data = {
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
            "valor": 49.9,
            "descricao": "Camiseta Básica Preta"
        }
    ],
    "parcelas": [
        {
            "data": "2024-01-15",
            "valor": 99.8,
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
        "valorFrete": 15.0
    }
}

response = requests.post(url, headers=headers, json=data)
print(response.json())
```

**JavaScript (fetch)**

```javascript
const url = "https://api.bling.com.br/Api/v3/pedidos/compras/{idPedidoCompra}/estornar-estoque";
const headers = {
  "Authorization": "Bearer YOUR_ACCESS_TOKEN",
  "Content-Type": "application/json"
};

const data = {
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
      "valor": 49.9,
      "descricao": "Camiseta Básica Preta"
    }
  ],
  "parcelas": [
    {
      "data": "2024-01-15",
      "valor": 99.8,
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
    "valorFrete": 15.0
  }
};

fetch(url, {
  method: "POST",
  headers: headers,
  body: JSON.stringify(data)
})
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error("Error:", error));
```

---

## Pedidos - Vendas

### GET `/pedidos/vendas`

**Obtém pedidos de vendas**

Obtém pedidos de vendas paginados.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| pagina | query | No | integer | N° da página da listagem |
| limite | query | No | integer | Quantidade de registros que devem ser exibidos por página |
| idContato | query | No | integer | ID do contato |
| idsSituacoes[] | query | No | array&lt;integer&gt; | Conjunto de situações |
| dataInicial | query | No | string | Data incial |
| dataFinal | query | No | string | Data final |
| dataAlteracaoInicial | query | No | string | Data inicial da alteração |
| dataAlteracaoFinal | query | No | string | Data final da alteração |
| dataPrevistaInicial | query | No | string | Data inicial prevista |
| dataPrevistaFinal | query | No | string | Data final prevista |
| numero | query | No | integer | Número do pedido de venda |
| idLoja | query | No | integer | ID da loja |
| idVendedor | query | No | integer | ID do vendedor |
| idControleCaixa | query | No | integer | ID do controle de caixa |
| numerosLojas[] | query | No | array&lt;string&gt; | Conjunto de números de pedidos nas lojas |

#### Responses

**200** - 

#### Code Examples

**cURL**

```bash
curl -X GET "https://api.bling.com.br/Api/v3/pedidos/vendas" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json"
```

**Python (requests)**

```python
import requests

url = "https://api.bling.com.br/Api/v3/pedidos/vendas"
headers = {
    "Authorization": "Bearer YOUR_ACCESS_TOKEN",
    "Content-Type": "application/json"
}

response = requests.get(url, headers=headers)
print(response.json())
```

**JavaScript (fetch)**

```javascript
const url = "https://api.bling.com.br/Api/v3/pedidos/vendas";
const headers = {
  "Authorization": "Bearer YOUR_ACCESS_TOKEN",
  "Content-Type": "application/json"
};

fetch(url, {
  method: "GET",
  headers: headers
})
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error("Error:", error));
```

---

### POST `/pedidos/vendas`

**Cria um pedido de venda**

Cria um pedido de venda.

#### Request Body

**Content-Type:** `application/json`

**Example Request**

```json
{
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
      "valor": 49.9,
      "descricao": "Camiseta Básica Preta"
    }
  ],
  "parcelas": [
    {
      "data": "2024-01-15",
      "valor": 99.8,
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
    "valorFrete": 15.0
  }
}
```

#### Responses

**201** - 

**Example Response (201)**

```json
{
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
    "total": 114.8
  }
}
```

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

#### Code Examples

**cURL**

```bash
curl -X POST "https://api.bling.com.br/Api/v3/pedidos/vendas" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
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
      "valor": 49.9,
      "descricao": "Camiseta Básica Preta"
    }
  ],
  "parcelas": [
    {
      "data": "2024-01-15",
      "valor": 99.8,
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
    "valorFrete": 15.0
  }
}'
```

**Python (requests)**

```python
import requests

url = "https://api.bling.com.br/Api/v3/pedidos/vendas"
headers = {
    "Authorization": "Bearer YOUR_ACCESS_TOKEN",
    "Content-Type": "application/json"
}

data = {
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
            "valor": 49.9,
            "descricao": "Camiseta Básica Preta"
        }
    ],
    "parcelas": [
        {
            "data": "2024-01-15",
            "valor": 99.8,
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
        "valorFrete": 15.0
    }
}

response = requests.post(url, headers=headers, json=data)
print(response.json())
```

**JavaScript (fetch)**

```javascript
const url = "https://api.bling.com.br/Api/v3/pedidos/vendas";
const headers = {
  "Authorization": "Bearer YOUR_ACCESS_TOKEN",
  "Content-Type": "application/json"
};

const data = {
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
      "valor": 49.9,
      "descricao": "Camiseta Básica Preta"
    }
  ],
  "parcelas": [
    {
      "data": "2024-01-15",
      "valor": 99.8,
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
    "valorFrete": 15.0
  }
};

fetch(url, {
  method: "POST",
  headers: headers,
  body: JSON.stringify(data)
})
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error("Error:", error));
```

---

### DELETE `/pedidos/vendas`

**Remove pedidos de vendas**

Remove pedidos de vendas pelos IDs.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idsPedidosVendas[] | query | **Yes** | array&lt;integer&gt; | IDs dos pedidos de vendas |

#### Responses

**200** - 

**Example Response (200)**

```json
{
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
    "total": 114.8
  }
}
```

**204** - No content.

#### Code Examples

**cURL**

```bash
curl -X DELETE "https://api.bling.com.br/Api/v3/pedidos/vendas" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json"
```

**Python (requests)**

```python
import requests

url = "https://api.bling.com.br/Api/v3/pedidos/vendas"
headers = {
    "Authorization": "Bearer YOUR_ACCESS_TOKEN",
    "Content-Type": "application/json"
}

response = requests.delete(url, headers=headers)
print(response.json())
```

**JavaScript (fetch)**

```javascript
const url = "https://api.bling.com.br/Api/v3/pedidos/vendas";
const headers = {
  "Authorization": "Bearer YOUR_ACCESS_TOKEN",
  "Content-Type": "application/json"
};

fetch(url, {
  method: "DELETE",
  headers: headers
})
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error("Error:", error));
```

---

### GET `/pedidos/vendas/{idPedidoVenda}`

**Obtém um pedido de venda**

Obtém um pedido de venda pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idPedidoVenda | path | **Yes** | integer | ID do pedido de venda |

#### Responses

**200** - 

**Example Response (200)**

```json
{
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
    "total": 114.8
  }
}
```

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

#### Code Examples

**cURL**

```bash
curl -X GET "https://api.bling.com.br/Api/v3/pedidos/vendas/{idPedidoVenda}" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json"
```

**Python (requests)**

```python
import requests

url = "https://api.bling.com.br/Api/v3/pedidos/vendas/{idPedidoVenda}"
headers = {
    "Authorization": "Bearer YOUR_ACCESS_TOKEN",
    "Content-Type": "application/json"
}

response = requests.get(url, headers=headers)
print(response.json())
```

**JavaScript (fetch)**

```javascript
const url = "https://api.bling.com.br/Api/v3/pedidos/vendas/{idPedidoVenda}";
const headers = {
  "Authorization": "Bearer YOUR_ACCESS_TOKEN",
  "Content-Type": "application/json"
};

fetch(url, {
  method: "GET",
  headers: headers
})
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error("Error:", error));
```

---

### PUT `/pedidos/vendas/{idPedidoVenda}`

**Altera um pedido de venda**

Altera um pedido de venda pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idPedidoVenda | path | **Yes** | integer | ID do pedido de venda |

#### Request Body

**Content-Type:** `application/json`

**Example Request**

```json
{
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
      "valor": 49.9,
      "descricao": "Camiseta Básica Preta"
    }
  ],
  "parcelas": [
    {
      "data": "2024-01-15",
      "valor": 99.8,
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
    "valorFrete": 15.0
  }
}
```

#### Responses

**200** - 

**Example Response (200)**

```json
{
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
    "total": 114.8
  }
}
```

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

#### Code Examples

**cURL**

```bash
curl -X PUT "https://api.bling.com.br/Api/v3/pedidos/vendas/{idPedidoVenda}" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
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
      "valor": 49.9,
      "descricao": "Camiseta Básica Preta"
    }
  ],
  "parcelas": [
    {
      "data": "2024-01-15",
      "valor": 99.8,
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
    "valorFrete": 15.0
  }
}'
```

**Python (requests)**

```python
import requests

url = "https://api.bling.com.br/Api/v3/pedidos/vendas/{idPedidoVenda}"
headers = {
    "Authorization": "Bearer YOUR_ACCESS_TOKEN",
    "Content-Type": "application/json"
}

data = {
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
            "valor": 49.9,
            "descricao": "Camiseta Básica Preta"
        }
    ],
    "parcelas": [
        {
            "data": "2024-01-15",
            "valor": 99.8,
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
        "valorFrete": 15.0
    }
}

response = requests.put(url, headers=headers, json=data)
print(response.json())
```

**JavaScript (fetch)**

```javascript
const url = "https://api.bling.com.br/Api/v3/pedidos/vendas/{idPedidoVenda}";
const headers = {
  "Authorization": "Bearer YOUR_ACCESS_TOKEN",
  "Content-Type": "application/json"
};

const data = {
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
      "valor": 49.9,
      "descricao": "Camiseta Básica Preta"
    }
  ],
  "parcelas": [
    {
      "data": "2024-01-15",
      "valor": 99.8,
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
    "valorFrete": 15.0
  }
};

fetch(url, {
  method: "PUT",
  headers: headers,
  body: JSON.stringify(data)
})
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error("Error:", error));
```

---

### DELETE `/pedidos/vendas/{idPedidoVenda}`

**Remove um pedido de venda**

Remove um pedido de venda pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idPedidoVenda | path | **Yes** | integer | ID do pedido de venda |

#### Responses

**204** - No content.

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

#### Code Examples

**cURL**

```bash
curl -X DELETE "https://api.bling.com.br/Api/v3/pedidos/vendas/{idPedidoVenda}" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json"
```

**Python (requests)**

```python
import requests

url = "https://api.bling.com.br/Api/v3/pedidos/vendas/{idPedidoVenda}"
headers = {
    "Authorization": "Bearer YOUR_ACCESS_TOKEN",
    "Content-Type": "application/json"
}

response = requests.delete(url, headers=headers)
print(response.json())
```

**JavaScript (fetch)**

```javascript
const url = "https://api.bling.com.br/Api/v3/pedidos/vendas/{idPedidoVenda}";
const headers = {
  "Authorization": "Bearer YOUR_ACCESS_TOKEN",
  "Content-Type": "application/json"
};

fetch(url, {
  method: "DELETE",
  headers: headers
})
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error("Error:", error));
```

---

### PATCH `/pedidos/vendas/{idPedidoVenda}/situacoes/{idSituacao}`

**Altera a situação de um pedido de venda**

Altera a situação de um pedido de venda pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idPedidoVenda | path | **Yes** | integer | ID do pedido de venda |
| idSituacao | path | **Yes** | integer | ID da situação do pedido de venda |

#### Responses

**204** - No content.

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

#### Code Examples

**cURL**

```bash
curl -X PATCH "https://api.bling.com.br/Api/v3/pedidos/vendas/{idPedidoVenda}/situacoes/{idSituacao}" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
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
      "valor": 49.9,
      "descricao": "Camiseta Básica Preta"
    }
  ],
  "parcelas": [
    {
      "data": "2024-01-15",
      "valor": 99.8,
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
    "valorFrete": 15.0
  }
}'
```

**Python (requests)**

```python
import requests

url = "https://api.bling.com.br/Api/v3/pedidos/vendas/{idPedidoVenda}/situacoes/{idSituacao}"
headers = {
    "Authorization": "Bearer YOUR_ACCESS_TOKEN",
    "Content-Type": "application/json"
}

data = {
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
            "valor": 49.9,
            "descricao": "Camiseta Básica Preta"
        }
    ],
    "parcelas": [
        {
            "data": "2024-01-15",
            "valor": 99.8,
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
        "valorFrete": 15.0
    }
}

response = requests.patch(url, headers=headers, json=data)
print(response.json())
```

**JavaScript (fetch)**

```javascript
const url = "https://api.bling.com.br/Api/v3/pedidos/vendas/{idPedidoVenda}/situacoes/{idSituacao}";
const headers = {
  "Authorization": "Bearer YOUR_ACCESS_TOKEN",
  "Content-Type": "application/json"
};

const data = {
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
      "valor": 49.9,
      "descricao": "Camiseta Básica Preta"
    }
  ],
  "parcelas": [
    {
      "data": "2024-01-15",
      "valor": 99.8,
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
    "valorFrete": 15.0
  }
};

fetch(url, {
  method: "PATCH",
  headers: headers,
  body: JSON.stringify(data)
})
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error("Error:", error));
```

---

### POST `/pedidos/vendas/{idPedidoVenda}/lancar-estoque/{idDeposito}`

**Lança o estoque de um pedido de venda especificando o depósito**

Lança o estoque de um pedido de venda pelo ID, especificando o ID do depósito.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idPedidoVenda | path | **Yes** | integer | ID do pedido de venda |
| idDeposito | path | **Yes** | integer | ID do depósito de estoque |

#### Responses

**204** - No content.

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

#### Code Examples

**cURL**

```bash
curl -X POST "https://api.bling.com.br/Api/v3/pedidos/vendas/{idPedidoVenda}/lancar-estoque/{idDeposito}" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
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
      "valor": 49.9,
      "descricao": "Camiseta Básica Preta"
    }
  ],
  "parcelas": [
    {
      "data": "2024-01-15",
      "valor": 99.8,
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
    "valorFrete": 15.0
  }
}'
```

**Python (requests)**

```python
import requests

url = "https://api.bling.com.br/Api/v3/pedidos/vendas/{idPedidoVenda}/lancar-estoque/{idDeposito}"
headers = {
    "Authorization": "Bearer YOUR_ACCESS_TOKEN",
    "Content-Type": "application/json"
}

data = {
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
            "valor": 49.9,
            "descricao": "Camiseta Básica Preta"
        }
    ],
    "parcelas": [
        {
            "data": "2024-01-15",
            "valor": 99.8,
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
        "valorFrete": 15.0
    }
}

response = requests.post(url, headers=headers, json=data)
print(response.json())
```

**JavaScript (fetch)**

```javascript
const url = "https://api.bling.com.br/Api/v3/pedidos/vendas/{idPedidoVenda}/lancar-estoque/{idDeposito}";
const headers = {
  "Authorization": "Bearer YOUR_ACCESS_TOKEN",
  "Content-Type": "application/json"
};

const data = {
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
      "valor": 49.9,
      "descricao": "Camiseta Básica Preta"
    }
  ],
  "parcelas": [
    {
      "data": "2024-01-15",
      "valor": 99.8,
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
    "valorFrete": 15.0
  }
};

fetch(url, {
  method: "POST",
  headers: headers,
  body: JSON.stringify(data)
})
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error("Error:", error));
```

---

### POST `/pedidos/vendas/{idPedidoVenda}/lancar-estoque`

**Lança o estoque de um pedido de venda no depósito padrão**

Lança o estoque de um pedido de venda pelo ID, no depósito padrão.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idPedidoVenda | path | **Yes** | integer | ID do pedido de venda |

#### Responses

**204** - No content.

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

#### Code Examples

**cURL**

```bash
curl -X POST "https://api.bling.com.br/Api/v3/pedidos/vendas/{idPedidoVenda}/lancar-estoque" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
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
      "valor": 49.9,
      "descricao": "Camiseta Básica Preta"
    }
  ],
  "parcelas": [
    {
      "data": "2024-01-15",
      "valor": 99.8,
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
    "valorFrete": 15.0
  }
}'
```

**Python (requests)**

```python
import requests

url = "https://api.bling.com.br/Api/v3/pedidos/vendas/{idPedidoVenda}/lancar-estoque"
headers = {
    "Authorization": "Bearer YOUR_ACCESS_TOKEN",
    "Content-Type": "application/json"
}

data = {
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
            "valor": 49.9,
            "descricao": "Camiseta Básica Preta"
        }
    ],
    "parcelas": [
        {
            "data": "2024-01-15",
            "valor": 99.8,
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
        "valorFrete": 15.0
    }
}

response = requests.post(url, headers=headers, json=data)
print(response.json())
```

**JavaScript (fetch)**

```javascript
const url = "https://api.bling.com.br/Api/v3/pedidos/vendas/{idPedidoVenda}/lancar-estoque";
const headers = {
  "Authorization": "Bearer YOUR_ACCESS_TOKEN",
  "Content-Type": "application/json"
};

const data = {
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
      "valor": 49.9,
      "descricao": "Camiseta Básica Preta"
    }
  ],
  "parcelas": [
    {
      "data": "2024-01-15",
      "valor": 99.8,
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
    "valorFrete": 15.0
  }
};

fetch(url, {
  method: "POST",
  headers: headers,
  body: JSON.stringify(data)
})
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error("Error:", error));
```

---

### POST `/pedidos/vendas/{idPedidoVenda}/estornar-estoque`

**Estorna o estoque de um pedido de venda**

Estorna o estoque de um pedido de venda pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idPedidoVenda | path | **Yes** | integer | ID do pedido de venda |

#### Responses

**204** - No content.

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

#### Code Examples

**cURL**

```bash
curl -X POST "https://api.bling.com.br/Api/v3/pedidos/vendas/{idPedidoVenda}/estornar-estoque" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
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
      "valor": 49.9,
      "descricao": "Camiseta Básica Preta"
    }
  ],
  "parcelas": [
    {
      "data": "2024-01-15",
      "valor": 99.8,
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
    "valorFrete": 15.0
  }
}'
```

**Python (requests)**

```python
import requests

url = "https://api.bling.com.br/Api/v3/pedidos/vendas/{idPedidoVenda}/estornar-estoque"
headers = {
    "Authorization": "Bearer YOUR_ACCESS_TOKEN",
    "Content-Type": "application/json"
}

data = {
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
            "valor": 49.9,
            "descricao": "Camiseta Básica Preta"
        }
    ],
    "parcelas": [
        {
            "data": "2024-01-15",
            "valor": 99.8,
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
        "valorFrete": 15.0
    }
}

response = requests.post(url, headers=headers, json=data)
print(response.json())
```

**JavaScript (fetch)**

```javascript
const url = "https://api.bling.com.br/Api/v3/pedidos/vendas/{idPedidoVenda}/estornar-estoque";
const headers = {
  "Authorization": "Bearer YOUR_ACCESS_TOKEN",
  "Content-Type": "application/json"
};

const data = {
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
      "valor": 49.9,
      "descricao": "Camiseta Básica Preta"
    }
  ],
  "parcelas": [
    {
      "data": "2024-01-15",
      "valor": 99.8,
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
    "valorFrete": 15.0
  }
};

fetch(url, {
  method: "POST",
  headers: headers,
  body: JSON.stringify(data)
})
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error("Error:", error));
```

---

### POST `/pedidos/vendas/{idPedidoVenda}/lancar-contas`

**Lança as contas de um pedido de venda**

Lança as contas de um pedido de venda pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idPedidoVenda | path | **Yes** | integer | ID do pedido de venda |

#### Responses

**204** - No content.

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

#### Code Examples

**cURL**

```bash
curl -X POST "https://api.bling.com.br/Api/v3/pedidos/vendas/{idPedidoVenda}/lancar-contas" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
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
      "valor": 49.9,
      "descricao": "Camiseta Básica Preta"
    }
  ],
  "parcelas": [
    {
      "data": "2024-01-15",
      "valor": 99.8,
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
    "valorFrete": 15.0
  }
}'
```

**Python (requests)**

```python
import requests

url = "https://api.bling.com.br/Api/v3/pedidos/vendas/{idPedidoVenda}/lancar-contas"
headers = {
    "Authorization": "Bearer YOUR_ACCESS_TOKEN",
    "Content-Type": "application/json"
}

data = {
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
            "valor": 49.9,
            "descricao": "Camiseta Básica Preta"
        }
    ],
    "parcelas": [
        {
            "data": "2024-01-15",
            "valor": 99.8,
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
        "valorFrete": 15.0
    }
}

response = requests.post(url, headers=headers, json=data)
print(response.json())
```

**JavaScript (fetch)**

```javascript
const url = "https://api.bling.com.br/Api/v3/pedidos/vendas/{idPedidoVenda}/lancar-contas";
const headers = {
  "Authorization": "Bearer YOUR_ACCESS_TOKEN",
  "Content-Type": "application/json"
};

const data = {
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
      "valor": 49.9,
      "descricao": "Camiseta Básica Preta"
    }
  ],
  "parcelas": [
    {
      "data": "2024-01-15",
      "valor": 99.8,
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
    "valorFrete": 15.0
  }
};

fetch(url, {
  method: "POST",
  headers: headers,
  body: JSON.stringify(data)
})
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error("Error:", error));
```

---

### POST `/pedidos/vendas/{idPedidoVenda}/estornar-contas`

**Estorna as contas de um pedido de venda**

Estorna as contas de um pedido de venda pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idPedidoVenda | path | **Yes** | integer | ID do pedido de venda |

#### Responses

**204** - No content.

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

#### Code Examples

**cURL**

```bash
curl -X POST "https://api.bling.com.br/Api/v3/pedidos/vendas/{idPedidoVenda}/estornar-contas" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
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
      "valor": 49.9,
      "descricao": "Camiseta Básica Preta"
    }
  ],
  "parcelas": [
    {
      "data": "2024-01-15",
      "valor": 99.8,
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
    "valorFrete": 15.0
  }
}'
```

**Python (requests)**

```python
import requests

url = "https://api.bling.com.br/Api/v3/pedidos/vendas/{idPedidoVenda}/estornar-contas"
headers = {
    "Authorization": "Bearer YOUR_ACCESS_TOKEN",
    "Content-Type": "application/json"
}

data = {
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
            "valor": 49.9,
            "descricao": "Camiseta Básica Preta"
        }
    ],
    "parcelas": [
        {
            "data": "2024-01-15",
            "valor": 99.8,
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
        "valorFrete": 15.0
    }
}

response = requests.post(url, headers=headers, json=data)
print(response.json())
```

**JavaScript (fetch)**

```javascript
const url = "https://api.bling.com.br/Api/v3/pedidos/vendas/{idPedidoVenda}/estornar-contas";
const headers = {
  "Authorization": "Bearer YOUR_ACCESS_TOKEN",
  "Content-Type": "application/json"
};

const data = {
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
      "valor": 49.9,
      "descricao": "Camiseta Básica Preta"
    }
  ],
  "parcelas": [
    {
      "data": "2024-01-15",
      "valor": 99.8,
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
    "valorFrete": 15.0
  }
};

fetch(url, {
  method: "POST",
  headers: headers,
  body: JSON.stringify(data)
})
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error("Error:", error));
```

---

### POST `/pedidos/vendas/{idPedidoVenda}/gerar-nfe`

**Gera nota fiscal eletrônica a partir do pedido de venda**

Gera nota fiscal eletrônica a partir do pedido de venda pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idPedidoVenda | path | **Yes** | integer | ID do pedido de venda |

#### Responses

**201** - 

**Example Response (201)**

```json
{
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
    "total": 114.8
  }
}
```

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

#### Code Examples

**cURL**

```bash
curl -X POST "https://api.bling.com.br/Api/v3/pedidos/vendas/{idPedidoVenda}/gerar-nfe" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
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
      "valor": 49.9,
      "descricao": "Camiseta Básica Preta"
    }
  ],
  "parcelas": [
    {
      "data": "2024-01-15",
      "valor": 99.8,
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
    "valorFrete": 15.0
  }
}'
```

**Python (requests)**

```python
import requests

url = "https://api.bling.com.br/Api/v3/pedidos/vendas/{idPedidoVenda}/gerar-nfe"
headers = {
    "Authorization": "Bearer YOUR_ACCESS_TOKEN",
    "Content-Type": "application/json"
}

data = {
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
            "valor": 49.9,
            "descricao": "Camiseta Básica Preta"
        }
    ],
    "parcelas": [
        {
            "data": "2024-01-15",
            "valor": 99.8,
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
        "valorFrete": 15.0
    }
}

response = requests.post(url, headers=headers, json=data)
print(response.json())
```

**JavaScript (fetch)**

```javascript
const url = "https://api.bling.com.br/Api/v3/pedidos/vendas/{idPedidoVenda}/gerar-nfe";
const headers = {
  "Authorization": "Bearer YOUR_ACCESS_TOKEN",
  "Content-Type": "application/json"
};

const data = {
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
      "valor": 49.9,
      "descricao": "Camiseta Básica Preta"
    }
  ],
  "parcelas": [
    {
      "data": "2024-01-15",
      "valor": 99.8,
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
    "valorFrete": 15.0
  }
};

fetch(url, {
  method: "POST",
  headers: headers,
  body: JSON.stringify(data)
})
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error("Error:", error));
```

---

### POST `/pedidos/vendas/{idPedidoVenda}/gerar-nfce`

**Gera nota fiscal de consumidor eletrônica a partir do pedido de venda**

Gera nota fiscal de consumidor eletrônica a partir do pedido de venda pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idPedidoVenda | path | **Yes** | integer | ID do pedido de venda |

#### Responses

**201** - 

**Example Response (201)**

```json
{
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
    "total": 114.8
  }
}
```

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

#### Code Examples

**cURL**

```bash
curl -X POST "https://api.bling.com.br/Api/v3/pedidos/vendas/{idPedidoVenda}/gerar-nfce" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
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
      "valor": 49.9,
      "descricao": "Camiseta Básica Preta"
    }
  ],
  "parcelas": [
    {
      "data": "2024-01-15",
      "valor": 99.8,
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
    "valorFrete": 15.0
  }
}'
```

**Python (requests)**

```python
import requests

url = "https://api.bling.com.br/Api/v3/pedidos/vendas/{idPedidoVenda}/gerar-nfce"
headers = {
    "Authorization": "Bearer YOUR_ACCESS_TOKEN",
    "Content-Type": "application/json"
}

data = {
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
            "valor": 49.9,
            "descricao": "Camiseta Básica Preta"
        }
    ],
    "parcelas": [
        {
            "data": "2024-01-15",
            "valor": 99.8,
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
        "valorFrete": 15.0
    }
}

response = requests.post(url, headers=headers, json=data)
print(response.json())
```

**JavaScript (fetch)**

```javascript
const url = "https://api.bling.com.br/Api/v3/pedidos/vendas/{idPedidoVenda}/gerar-nfce";
const headers = {
  "Authorization": "Bearer YOUR_ACCESS_TOKEN",
  "Content-Type": "application/json"
};

const data = {
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
      "valor": 49.9,
      "descricao": "Camiseta Básica Preta"
    }
  ],
  "parcelas": [
    {
      "data": "2024-01-15",
      "valor": 99.8,
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
    "valorFrete": 15.0
  }
};

fetch(url, {
  method: "POST",
  headers: headers,
  body: JSON.stringify(data)
})
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error("Error:", error));
```

---

## Produtos

### GET `/produtos`

**Obtém produtos**

Obtém produtos paginados.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| pagina | query | No | integer | N° da página da listagem |
| limite | query | No | integer | Quantidade de registros que devem ser exibidos por página |
| criterio | query | No | integer (enum) | Critério de listagem <br> `1` Últimos incluídos <br> `2` Ativos <br> `3` Inativos <br> `4` Excluídos <br> `5` Todos |
| tipo | query | No | string (enum) | `T` Todos <br> `P` Produtos <br> `S` Serviços <br> `E` Composições <br> `PS` Produtos simples <br> `C` Com variações <br> `V` Variações |
| idComponente | query | No | integer | ID do componente. Utilizado quando o filtro **tipo** for `E`. |
| dataInclusaoInicial | query | No | string | Data de inclusão inicial |
| dataInclusaoFinal | query | No | string | Data de inclusão final |
| dataAlteracaoInicial | query | No | string | Data de alteração inicial |
| dataAlteracaoFinal | query | No | string | Data de alteração final |
| idCategoria | query | No | integer | ID da categoria do produto |
| idLoja | query | No | integer | ID da loja |
| nome | query | No | string | Nome do produto |
| idsProdutos[] | query | No | array&lt;integer&gt; | IDs dos produtos |
| codigos[] | query | No | array&lt;string&gt; | Códigos (SKU) dos produtos |
| gtins[] | query | No | array&lt;string&gt; | GTINs/EANs dos produtos |
| filtroSaldoEstoque | query | No | integer (enum) | Filtra o saldo em estoque <br> `0` zerado <br> `1` positivo <br> `2` negativo |
| filtroSaldoEstoqueDeposito | query | No | integer | ID do depósito para considerar no filtro de saldo em estoque. Se omitido, considera todos os depósitos. |

#### Responses

**200** - 

**Example Response (200)**

```json
{
  "data": [
    {
      "id": 12345678,
      "nome": "Camiseta Básica Preta",
      "codigo": "CAM-BAS-PTA-M",
      "preco": 49.9,
      "tipo": "P",
      "situacao": "A",
      "formato": "S"
    },
    {
      "id": 12345679,
      "nome": "Camiseta Básica Branca",
      "codigo": "CAM-BAS-BCA-M",
      "preco": 49.9,
      "tipo": "P",
      "situacao": "A",
      "formato": "S"
    }
  ]
}
```

#### Code Examples

**cURL**

```bash
curl -X GET "https://api.bling.com.br/Api/v3/produtos" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json"
```

**Python (requests)**

```python
import requests

url = "https://api.bling.com.br/Api/v3/produtos"
headers = {
    "Authorization": "Bearer YOUR_ACCESS_TOKEN",
    "Content-Type": "application/json"
}

response = requests.get(url, headers=headers)
print(response.json())
```

**JavaScript (fetch)**

```javascript
const url = "https://api.bling.com.br/Api/v3/produtos";
const headers = {
  "Authorization": "Bearer YOUR_ACCESS_TOKEN",
  "Content-Type": "application/json"
};

fetch(url, {
  method: "GET",
  headers: headers
})
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error("Error:", error));
```

---

### POST `/produtos`

**Cria um produto**

Cria um produto.

#### Request Body

**Content-Type:** `application/json`

**Example Request**

```json
{
  "nome": "Camiseta Básica Preta",
  "codigo": "CAM-BAS-PTA-M",
  "preco": 49.9,
  "tipo": "P",
  "situacao": "A",
  "formato": "S",
  "descricaoCurta": "Camiseta básica 100% algodão",
  "descricaoComplementar": "Camiseta básica preta, tamanho M, 100% algodão",
  "unidade": "UN",
  "pesoLiquido": 0.2,
  "pesoBruto": 0.25,
  "gtin": "7891234567890",
  "gtinEmbalagem": "17891234567897",
  "dimensoes": {
    "largura": 30,
    "altura": 40,
    "profundidade": 2,
    "unidadeMedida": 7
  }
}
```

#### Responses

**201** - 

**Example Response (201)**

```json
{
  "data": {
    "id": 12345678,
    "nome": "Camiseta Básica Preta",
    "codigo": "CAM-BAS-PTA-M",
    "preco": 49.9,
    "tipo": "P",
    "situacao": "A",
    "formato": "S",
    "descricaoCurta": "Camiseta básica 100% algodão",
    "unidade": "UN",
    "pesoLiquido": 0.2,
    "pesoBruto": 0.25
  }
}
```

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

**403** - 

#### Code Examples

**cURL**

```bash
curl -X POST "https://api.bling.com.br/Api/v3/produtos" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
  "nome": "Camiseta Básica Preta",
  "codigo": "CAM-BAS-PTA-M",
  "preco": 49.9,
  "tipo": "P",
  "situacao": "A",
  "formato": "S",
  "descricaoCurta": "Camiseta básica 100% algodão",
  "descricaoComplementar": "Camiseta básica preta, tamanho M, 100% algodão",
  "unidade": "UN",
  "pesoLiquido": 0.2,
  "pesoBruto": 0.25,
  "gtin": "7891234567890",
  "gtinEmbalagem": "17891234567897",
  "dimensoes": {
    "largura": 30,
    "altura": 40,
    "profundidade": 2,
    "unidadeMedida": 7
  }
}'
```

**Python (requests)**

```python
import requests

url = "https://api.bling.com.br/Api/v3/produtos"
headers = {
    "Authorization": "Bearer YOUR_ACCESS_TOKEN",
    "Content-Type": "application/json"
}

data = {
    "nome": "Camiseta Básica Preta",
    "codigo": "CAM-BAS-PTA-M",
    "preco": 49.9,
    "tipo": "P",
    "situacao": "A",
    "formato": "S",
    "descricaoCurta": "Camiseta básica 100% algodão",
    "descricaoComplementar": "Camiseta básica preta, tamanho M, 100% algodão",
    "unidade": "UN",
    "pesoLiquido": 0.2,
    "pesoBruto": 0.25,
    "gtin": "7891234567890",
    "gtinEmbalagem": "17891234567897",
    "dimensoes": {
        "largura": 30,
        "altura": 40,
        "profundidade": 2,
        "unidadeMedida": 7
    }
}

response = requests.post(url, headers=headers, json=data)
print(response.json())
```

**JavaScript (fetch)**

```javascript
const url = "https://api.bling.com.br/Api/v3/produtos";
const headers = {
  "Authorization": "Bearer YOUR_ACCESS_TOKEN",
  "Content-Type": "application/json"
};

const data = {
  "nome": "Camiseta Básica Preta",
  "codigo": "CAM-BAS-PTA-M",
  "preco": 49.9,
  "tipo": "P",
  "situacao": "A",
  "formato": "S",
  "descricaoCurta": "Camiseta básica 100% algodão",
  "descricaoComplementar": "Camiseta básica preta, tamanho M, 100% algodão",
  "unidade": "UN",
  "pesoLiquido": 0.2,
  "pesoBruto": 0.25,
  "gtin": "7891234567890",
  "gtinEmbalagem": "17891234567897",
  "dimensoes": {
    "largura": 30,
    "altura": 40,
    "profundidade": 2,
    "unidadeMedida": 7
  }
};

fetch(url, {
  method: "POST",
  headers: headers,
  body: JSON.stringify(data)
})
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error("Error:", error));
```

---

### DELETE `/produtos`

**Remove múltiplos produtos**

Remove múltiplos produtos pelos IDs.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idsProdutos[] | query | **Yes** | array&lt;integer&gt; | IDs dos produtos |

#### Responses

**200** - 

**Example Response (200)**

```json
{
  "data": {
    "id": 12345678,
    "nome": "Camiseta Básica Preta",
    "codigo": "CAM-BAS-PTA-M",
    "preco": 49.9,
    "tipo": "P",
    "situacao": "A",
    "formato": "S",
    "descricaoCurta": "Camiseta básica 100% algodão",
    "unidade": "UN",
    "pesoLiquido": 0.2,
    "pesoBruto": 0.25
  }
}
```

**204** - No content.

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

#### Code Examples

**cURL**

```bash
curl -X DELETE "https://api.bling.com.br/Api/v3/produtos" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json"
```

**Python (requests)**

```python
import requests

url = "https://api.bling.com.br/Api/v3/produtos"
headers = {
    "Authorization": "Bearer YOUR_ACCESS_TOKEN",
    "Content-Type": "application/json"
}

response = requests.delete(url, headers=headers)
print(response.json())
```

**JavaScript (fetch)**

```javascript
const url = "https://api.bling.com.br/Api/v3/produtos";
const headers = {
  "Authorization": "Bearer YOUR_ACCESS_TOKEN",
  "Content-Type": "application/json"
};

fetch(url, {
  method: "DELETE",
  headers: headers
})
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error("Error:", error));
```

---

### GET `/produtos/{idProduto}`

**Obtém um produto**

Obtém um produto pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idProduto | path | **Yes** | integer | ID do produto |

#### Responses

**200** - 

**Example Response (200)**

```json
{
  "data": {
    "id": 12345678,
    "nome": "Camiseta Básica Preta",
    "codigo": "CAM-BAS-PTA-M",
    "preco": 49.9,
    "tipo": "P",
    "situacao": "A",
    "formato": "S",
    "descricaoCurta": "Camiseta básica 100% algodão",
    "unidade": "UN",
    "pesoLiquido": 0.2,
    "pesoBruto": 0.25
  }
}
```

**403** - 

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

#### Code Examples

**cURL**

```bash
curl -X GET "https://api.bling.com.br/Api/v3/produtos/{idProduto}" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json"
```

**Python (requests)**

```python
import requests

url = "https://api.bling.com.br/Api/v3/produtos/{idProduto}"
headers = {
    "Authorization": "Bearer YOUR_ACCESS_TOKEN",
    "Content-Type": "application/json"
}

response = requests.get(url, headers=headers)
print(response.json())
```

**JavaScript (fetch)**

```javascript
const url = "https://api.bling.com.br/Api/v3/produtos/{idProduto}";
const headers = {
  "Authorization": "Bearer YOUR_ACCESS_TOKEN",
  "Content-Type": "application/json"
};

fetch(url, {
  method: "GET",
  headers: headers
})
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error("Error:", error));
```

---

### PUT `/produtos/{idProduto}`

**Altera um produto**

Altera um produto pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idProduto | path | **Yes** | integer | ID do produto |

#### Request Body

**Content-Type:** `application/json`

**Example Request**

```json
{
  "nome": "Camiseta Básica Preta",
  "codigo": "CAM-BAS-PTA-M",
  "preco": 49.9,
  "tipo": "P",
  "situacao": "A",
  "formato": "S",
  "descricaoCurta": "Camiseta básica 100% algodão",
  "descricaoComplementar": "Camiseta básica preta, tamanho M, 100% algodão",
  "unidade": "UN",
  "pesoLiquido": 0.2,
  "pesoBruto": 0.25,
  "gtin": "7891234567890",
  "gtinEmbalagem": "17891234567897",
  "dimensoes": {
    "largura": 30,
    "altura": 40,
    "profundidade": 2,
    "unidadeMedida": 7
  }
}
```

#### Responses

**200** - 

**Example Response (200)**

```json
{
  "data": {
    "id": 12345678,
    "nome": "Camiseta Básica Preta",
    "codigo": "CAM-BAS-PTA-M",
    "preco": 49.9,
    "tipo": "P",
    "situacao": "A",
    "formato": "S",
    "descricaoCurta": "Camiseta básica 100% algodão",
    "unidade": "UN",
    "pesoLiquido": 0.2,
    "pesoBruto": 0.25
  }
}
```

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

**403** - 

#### Code Examples

**cURL**

```bash
curl -X PUT "https://api.bling.com.br/Api/v3/produtos/{idProduto}" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
  "nome": "Camiseta Básica Preta",
  "codigo": "CAM-BAS-PTA-M",
  "preco": 49.9,
  "tipo": "P",
  "situacao": "A",
  "formato": "S",
  "descricaoCurta": "Camiseta básica 100% algodão",
  "descricaoComplementar": "Camiseta básica preta, tamanho M, 100% algodão",
  "unidade": "UN",
  "pesoLiquido": 0.2,
  "pesoBruto": 0.25,
  "gtin": "7891234567890",
  "gtinEmbalagem": "17891234567897",
  "dimensoes": {
    "largura": 30,
    "altura": 40,
    "profundidade": 2,
    "unidadeMedida": 7
  }
}'
```

**Python (requests)**

```python
import requests

url = "https://api.bling.com.br/Api/v3/produtos/{idProduto}"
headers = {
    "Authorization": "Bearer YOUR_ACCESS_TOKEN",
    "Content-Type": "application/json"
}

data = {
    "nome": "Camiseta Básica Preta",
    "codigo": "CAM-BAS-PTA-M",
    "preco": 49.9,
    "tipo": "P",
    "situacao": "A",
    "formato": "S",
    "descricaoCurta": "Camiseta básica 100% algodão",
    "descricaoComplementar": "Camiseta básica preta, tamanho M, 100% algodão",
    "unidade": "UN",
    "pesoLiquido": 0.2,
    "pesoBruto": 0.25,
    "gtin": "7891234567890",
    "gtinEmbalagem": "17891234567897",
    "dimensoes": {
        "largura": 30,
        "altura": 40,
        "profundidade": 2,
        "unidadeMedida": 7
    }
}

response = requests.put(url, headers=headers, json=data)
print(response.json())
```

**JavaScript (fetch)**

```javascript
const url = "https://api.bling.com.br/Api/v3/produtos/{idProduto}";
const headers = {
  "Authorization": "Bearer YOUR_ACCESS_TOKEN",
  "Content-Type": "application/json"
};

const data = {
  "nome": "Camiseta Básica Preta",
  "codigo": "CAM-BAS-PTA-M",
  "preco": 49.9,
  "tipo": "P",
  "situacao": "A",
  "formato": "S",
  "descricaoCurta": "Camiseta básica 100% algodão",
  "descricaoComplementar": "Camiseta básica preta, tamanho M, 100% algodão",
  "unidade": "UN",
  "pesoLiquido": 0.2,
  "pesoBruto": 0.25,
  "gtin": "7891234567890",
  "gtinEmbalagem": "17891234567897",
  "dimensoes": {
    "largura": 30,
    "altura": 40,
    "profundidade": 2,
    "unidadeMedida": 7
  }
};

fetch(url, {
  method: "PUT",
  headers: headers,
  body: JSON.stringify(data)
})
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error("Error:", error));
```

---

### PATCH `/produtos/{idProduto}`

**Altera parcialmente um produto**

Altera parcialmente um produto pelo ID. Somente os campos informados terão o valor alterado.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idProduto | path | **Yes** | integer | ID do produto |

#### Request Body

**Content-Type:** `application/json`

**Example Request**

```json
{
  "nome": "Camiseta Básica Preta",
  "codigo": "CAM-BAS-PTA-M",
  "preco": 49.9,
  "tipo": "P",
  "situacao": "A",
  "formato": "S",
  "descricaoCurta": "Camiseta básica 100% algodão",
  "descricaoComplementar": "Camiseta básica preta, tamanho M, 100% algodão",
  "unidade": "UN",
  "pesoLiquido": 0.2,
  "pesoBruto": 0.25,
  "gtin": "7891234567890",
  "gtinEmbalagem": "17891234567897",
  "dimensoes": {
    "largura": 30,
    "altura": 40,
    "profundidade": 2,
    "unidadeMedida": 7
  }
}
```

#### Responses

**200** - 

**Example Response (200)**

```json
{
  "data": {
    "id": 12345678,
    "nome": "Camiseta Básica Preta",
    "codigo": "CAM-BAS-PTA-M",
    "preco": 49.9,
    "tipo": "P",
    "situacao": "A",
    "formato": "S",
    "descricaoCurta": "Camiseta básica 100% algodão",
    "unidade": "UN",
    "pesoLiquido": 0.2,
    "pesoBruto": 0.25
  }
}
```

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

**403** - 

#### Code Examples

**cURL**

```bash
curl -X PATCH "https://api.bling.com.br/Api/v3/produtos/{idProduto}" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
  "nome": "Camiseta Básica Preta",
  "codigo": "CAM-BAS-PTA-M",
  "preco": 49.9,
  "tipo": "P",
  "situacao": "A",
  "formato": "S",
  "descricaoCurta": "Camiseta básica 100% algodão",
  "descricaoComplementar": "Camiseta básica preta, tamanho M, 100% algodão",
  "unidade": "UN",
  "pesoLiquido": 0.2,
  "pesoBruto": 0.25,
  "gtin": "7891234567890",
  "gtinEmbalagem": "17891234567897",
  "dimensoes": {
    "largura": 30,
    "altura": 40,
    "profundidade": 2,
    "unidadeMedida": 7
  }
}'
```

**Python (requests)**

```python
import requests

url = "https://api.bling.com.br/Api/v3/produtos/{idProduto}"
headers = {
    "Authorization": "Bearer YOUR_ACCESS_TOKEN",
    "Content-Type": "application/json"
}

data = {
    "nome": "Camiseta Básica Preta",
    "codigo": "CAM-BAS-PTA-M",
    "preco": 49.9,
    "tipo": "P",
    "situacao": "A",
    "formato": "S",
    "descricaoCurta": "Camiseta básica 100% algodão",
    "descricaoComplementar": "Camiseta básica preta, tamanho M, 100% algodão",
    "unidade": "UN",
    "pesoLiquido": 0.2,
    "pesoBruto": 0.25,
    "gtin": "7891234567890",
    "gtinEmbalagem": "17891234567897",
    "dimensoes": {
        "largura": 30,
        "altura": 40,
        "profundidade": 2,
        "unidadeMedida": 7
    }
}

response = requests.patch(url, headers=headers, json=data)
print(response.json())
```

**JavaScript (fetch)**

```javascript
const url = "https://api.bling.com.br/Api/v3/produtos/{idProduto}";
const headers = {
  "Authorization": "Bearer YOUR_ACCESS_TOKEN",
  "Content-Type": "application/json"
};

const data = {
  "nome": "Camiseta Básica Preta",
  "codigo": "CAM-BAS-PTA-M",
  "preco": 49.9,
  "tipo": "P",
  "situacao": "A",
  "formato": "S",
  "descricaoCurta": "Camiseta básica 100% algodão",
  "descricaoComplementar": "Camiseta básica preta, tamanho M, 100% algodão",
  "unidade": "UN",
  "pesoLiquido": 0.2,
  "pesoBruto": 0.25,
  "gtin": "7891234567890",
  "gtinEmbalagem": "17891234567897",
  "dimensoes": {
    "largura": 30,
    "altura": 40,
    "profundidade": 2,
    "unidadeMedida": 7
  }
};

fetch(url, {
  method: "PATCH",
  headers: headers,
  body: JSON.stringify(data)
})
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error("Error:", error));
```

---

### DELETE `/produtos/{idProduto}`

**Remove um produto**

Remove um produto pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idProduto | path | **Yes** | integer | ID do produto |

#### Responses

**204** - No content.

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

#### Code Examples

**cURL**

```bash
curl -X DELETE "https://api.bling.com.br/Api/v3/produtos/{idProduto}" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json"
```

**Python (requests)**

```python
import requests

url = "https://api.bling.com.br/Api/v3/produtos/{idProduto}"
headers = {
    "Authorization": "Bearer YOUR_ACCESS_TOKEN",
    "Content-Type": "application/json"
}

response = requests.delete(url, headers=headers)
print(response.json())
```

**JavaScript (fetch)**

```javascript
const url = "https://api.bling.com.br/Api/v3/produtos/{idProduto}";
const headers = {
  "Authorization": "Bearer YOUR_ACCESS_TOKEN",
  "Content-Type": "application/json"
};

fetch(url, {
  method: "DELETE",
  headers: headers
})
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error("Error:", error));
```

---

### PATCH `/produtos/{idProduto}/situacoes`

**Altera a situação de um produto**

Altera a situação de um produto pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idProduto | path | **Yes** | integer | ID do produto |

#### Request Body

**Content-Type:** `application/json`

**Example Request**

```json
{
  "nome": "Camiseta Básica Preta",
  "codigo": "CAM-BAS-PTA-M",
  "preco": 49.9,
  "tipo": "P",
  "situacao": "A",
  "formato": "S",
  "descricaoCurta": "Camiseta básica 100% algodão",
  "descricaoComplementar": "Camiseta básica preta, tamanho M, 100% algodão",
  "unidade": "UN",
  "pesoLiquido": 0.2,
  "pesoBruto": 0.25,
  "gtin": "7891234567890",
  "gtinEmbalagem": "17891234567897",
  "dimensoes": {
    "largura": 30,
    "altura": 40,
    "profundidade": 2,
    "unidadeMedida": 7
  }
}
```

#### Responses

**204** - No content.

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

#### Code Examples

**cURL**

```bash
curl -X PATCH "https://api.bling.com.br/Api/v3/produtos/{idProduto}/situacoes" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
  "nome": "Camiseta Básica Preta",
  "codigo": "CAM-BAS-PTA-M",
  "preco": 49.9,
  "tipo": "P",
  "situacao": "A",
  "formato": "S",
  "descricaoCurta": "Camiseta básica 100% algodão",
  "descricaoComplementar": "Camiseta básica preta, tamanho M, 100% algodão",
  "unidade": "UN",
  "pesoLiquido": 0.2,
  "pesoBruto": 0.25,
  "gtin": "7891234567890",
  "gtinEmbalagem": "17891234567897",
  "dimensoes": {
    "largura": 30,
    "altura": 40,
    "profundidade": 2,
    "unidadeMedida": 7
  }
}'
```

**Python (requests)**

```python
import requests

url = "https://api.bling.com.br/Api/v3/produtos/{idProduto}/situacoes"
headers = {
    "Authorization": "Bearer YOUR_ACCESS_TOKEN",
    "Content-Type": "application/json"
}

data = {
    "nome": "Camiseta Básica Preta",
    "codigo": "CAM-BAS-PTA-M",
    "preco": 49.9,
    "tipo": "P",
    "situacao": "A",
    "formato": "S",
    "descricaoCurta": "Camiseta básica 100% algodão",
    "descricaoComplementar": "Camiseta básica preta, tamanho M, 100% algodão",
    "unidade": "UN",
    "pesoLiquido": 0.2,
    "pesoBruto": 0.25,
    "gtin": "7891234567890",
    "gtinEmbalagem": "17891234567897",
    "dimensoes": {
        "largura": 30,
        "altura": 40,
        "profundidade": 2,
        "unidadeMedida": 7
    }
}

response = requests.patch(url, headers=headers, json=data)
print(response.json())
```

**JavaScript (fetch)**

```javascript
const url = "https://api.bling.com.br/Api/v3/produtos/{idProduto}/situacoes";
const headers = {
  "Authorization": "Bearer YOUR_ACCESS_TOKEN",
  "Content-Type": "application/json"
};

const data = {
  "nome": "Camiseta Básica Preta",
  "codigo": "CAM-BAS-PTA-M",
  "preco": 49.9,
  "tipo": "P",
  "situacao": "A",
  "formato": "S",
  "descricaoCurta": "Camiseta básica 100% algodão",
  "descricaoComplementar": "Camiseta básica preta, tamanho M, 100% algodão",
  "unidade": "UN",
  "pesoLiquido": 0.2,
  "pesoBruto": 0.25,
  "gtin": "7891234567890",
  "gtinEmbalagem": "17891234567897",
  "dimensoes": {
    "largura": 30,
    "altura": 40,
    "profundidade": 2,
    "unidadeMedida": 7
  }
};

fetch(url, {
  method: "PATCH",
  headers: headers,
  body: JSON.stringify(data)
})
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error("Error:", error));
```

---

### POST `/produtos/situacoes`

**Altera a situação de múltiplos produtos**

Altera a situação de múltiplos produtos pelos IDs.

#### Request Body

**Content-Type:** `application/json`

**Example Request**

```json
{
  "nome": "Camiseta Básica Preta",
  "codigo": "CAM-BAS-PTA-M",
  "preco": 49.9,
  "tipo": "P",
  "situacao": "A",
  "formato": "S",
  "descricaoCurta": "Camiseta básica 100% algodão",
  "descricaoComplementar": "Camiseta básica preta, tamanho M, 100% algodão",
  "unidade": "UN",
  "pesoLiquido": 0.2,
  "pesoBruto": 0.25,
  "gtin": "7891234567890",
  "gtinEmbalagem": "17891234567897",
  "dimensoes": {
    "largura": 30,
    "altura": 40,
    "profundidade": 2,
    "unidadeMedida": 7
  }
}
```

#### Responses

**200** - 

**Example Response (200)**

```json
{
  "data": {
    "id": 12345678,
    "nome": "Camiseta Básica Preta",
    "codigo": "CAM-BAS-PTA-M",
    "preco": 49.9,
    "tipo": "P",
    "situacao": "A",
    "formato": "S",
    "descricaoCurta": "Camiseta básica 100% algodão",
    "unidade": "UN",
    "pesoLiquido": 0.2,
    "pesoBruto": 0.25
  }
}
```

**204** - No content.

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

#### Code Examples

**cURL**

```bash
curl -X POST "https://api.bling.com.br/Api/v3/produtos/situacoes" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
  "nome": "Camiseta Básica Preta",
  "codigo": "CAM-BAS-PTA-M",
  "preco": 49.9,
  "tipo": "P",
  "situacao": "A",
  "formato": "S",
  "descricaoCurta": "Camiseta básica 100% algodão",
  "descricaoComplementar": "Camiseta básica preta, tamanho M, 100% algodão",
  "unidade": "UN",
  "pesoLiquido": 0.2,
  "pesoBruto": 0.25,
  "gtin": "7891234567890",
  "gtinEmbalagem": "17891234567897",
  "dimensoes": {
    "largura": 30,
    "altura": 40,
    "profundidade": 2,
    "unidadeMedida": 7
  }
}'
```

**Python (requests)**

```python
import requests

url = "https://api.bling.com.br/Api/v3/produtos/situacoes"
headers = {
    "Authorization": "Bearer YOUR_ACCESS_TOKEN",
    "Content-Type": "application/json"
}

data = {
    "nome": "Camiseta Básica Preta",
    "codigo": "CAM-BAS-PTA-M",
    "preco": 49.9,
    "tipo": "P",
    "situacao": "A",
    "formato": "S",
    "descricaoCurta": "Camiseta básica 100% algodão",
    "descricaoComplementar": "Camiseta básica preta, tamanho M, 100% algodão",
    "unidade": "UN",
    "pesoLiquido": 0.2,
    "pesoBruto": 0.25,
    "gtin": "7891234567890",
    "gtinEmbalagem": "17891234567897",
    "dimensoes": {
        "largura": 30,
        "altura": 40,
        "profundidade": 2,
        "unidadeMedida": 7
    }
}

response = requests.post(url, headers=headers, json=data)
print(response.json())
```

**JavaScript (fetch)**

```javascript
const url = "https://api.bling.com.br/Api/v3/produtos/situacoes";
const headers = {
  "Authorization": "Bearer YOUR_ACCESS_TOKEN",
  "Content-Type": "application/json"
};

const data = {
  "nome": "Camiseta Básica Preta",
  "codigo": "CAM-BAS-PTA-M",
  "preco": 49.9,
  "tipo": "P",
  "situacao": "A",
  "formato": "S",
  "descricaoCurta": "Camiseta básica 100% algodão",
  "descricaoComplementar": "Camiseta básica preta, tamanho M, 100% algodão",
  "unidade": "UN",
  "pesoLiquido": 0.2,
  "pesoBruto": 0.25,
  "gtin": "7891234567890",
  "gtinEmbalagem": "17891234567897",
  "dimensoes": {
    "largura": 30,
    "altura": 40,
    "profundidade": 2,
    "unidadeMedida": 7
  }
};

fetch(url, {
  method: "POST",
  headers: headers,
  body: JSON.stringify(data)
})
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error("Error:", error));
```

---

## Produtos - Estruturas

### GET `/produtos/estruturas/{idProdutoEstrutura}`

**Obtém a estrutura de um produto com composição**

Obtém a estrutura de um produto com composição pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idProdutoEstrutura | path | **Yes** | integer | ID do produto com composição |

#### Responses

**200** - 

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

---

### PUT `/produtos/estruturas/{idProdutoEstrutura}`

**Altera a estrutura de um produto com composição**

Altera a estrutura de um produto com composição pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idProdutoEstrutura | path | **Yes** | integer | ID do produto com composição |

#### Request Body

**Content-Type:** `application/json`

#### Responses

**204** - No content.

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

---

### POST `/produtos/estruturas/{idProdutoEstrutura}/componentes`

**Adiciona componente(s) a uma estrutura**

Adiciona múltiplos componentes a uma estrutura pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idProdutoEstrutura | path | **Yes** | integer | ID do produto com composição |

#### Request Body

**Content-Type:** `application/json`

#### Responses

**204** - No content.

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

---

### DELETE `/produtos/estruturas/{idProdutoEstrutura}/componentes`

**Remove componentes específicos de um produto com composição**

Remove os componentes de um produto com composição pelos IDs dos componentes.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idProdutoEstrutura | path | **Yes** | integer | ID do produto com composição |
| idsComponentes[] | query | **Yes** | array&lt;integer&gt; | IDs dos produtos |

#### Responses

**204** - No content.

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

---

### PATCH `/produtos/estruturas/{idProdutoEstrutura}/componentes/{idComponente}`

**Altera um componente de uma estrutura**

Altera um componente de uma estrutura pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idProdutoEstrutura | path | **Yes** | integer | ID do produto com composição |
| idComponente | path | **Yes** | integer | ID do componente |

#### Request Body

**Content-Type:** `application/json`

#### Responses

**204** - No content.

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

---

### DELETE `/produtos/estruturas`

**Remove a estrutura de múltiplos produtos**

Remove a estrutura de múltiplos produtos com composição pelos IDs.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idsProdutos[] | query | **Yes** | array&lt;integer&gt; | IDs dos produtos |

#### Responses

**200** - 

**204** - No content.

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

---

## Produtos - Fornecedores

### GET `/produtos/fornecedores`

**Obtém produtos fornecedores**

Obtém produtos fornecedores paginados.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| pagina | query | No | integer | N° da página da listagem |
| limite | query | No | integer | Quantidade de registros que devem ser exibidos por página |
| idProduto | query | No | integer | ID do produto |
| idFornecedor | query | No | integer | ID do contato do tipo fornecedor |

#### Responses

**200** - 

---

### POST `/produtos/fornecedores`

**Cria um produto fornecedor**

Cria um produto fornecedor.

#### Request Body

**Content-Type:** `application/json`

#### Responses

**201** - 

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

---

### GET `/produtos/fornecedores/{idProdutoFornecedor}`

**Obtém um produto fornecedor**

Obtém um produto fornecedor pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idProdutoFornecedor | path | **Yes** | integer | ID do produto fornecedor |

#### Responses

**200** - 

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

---

### PUT `/produtos/fornecedores/{idProdutoFornecedor}`

**Altera um produto fornecedor**

Altera um produto fornecedor pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idProdutoFornecedor | path | **Yes** | integer | ID do produto fornecedor |

#### Request Body

**Content-Type:** `application/json`

#### Responses

**200** - 

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

---

### DELETE `/produtos/fornecedores/{idProdutoFornecedor}`

**Remove um produto fornecedor**

Remove um produto fornecedor pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idProdutoFornecedor | path | **Yes** | integer | ID do produto fornecedor |

#### Responses

**204** - No content.

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

---

## Produtos - Lojas

### GET `/produtos/lojas`

**Obtém vínculos de produtos com lojas**

Obtém vínculos de produtos com lojas paginados.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| pagina | query | No | integer | N° da página da listagem |
| limite | query | No | integer | Quantidade de registros que devem ser exibidos por página |
| idProduto | query | No | integer | ID do produto |
| idLoja | query | No | integer | ID da loja |
| idCategoriaProduto | query | No | integer | ID da categoria do produto vinculada à loja |
| dataAlteracaoInicial | query | No | string | Data de alteração inicial |
| dataAlteracaoFinal | query | No | string | Data de alteração final |

#### Responses

**200** - 

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

---

### POST `/produtos/lojas`

**Cria o vínculo de um produto com uma loja**

Cria o vínculo de um produto com uma loja.

#### Request Body

**Content-Type:** `application/json`

#### Responses

**201** - 

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

---

### GET `/produtos/lojas/{idProdutoLoja}`

**Obtém um vínculo de produto com loja**

Obtém um vínculo de produto com loja pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idProdutoLoja | path | **Yes** | integer | ID do vínculo do produto com a loja |

#### Responses

**200** - 

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

---

### PUT `/produtos/lojas/{idProdutoLoja}`

**Altera o vínculo de um produto com uma loja**

Altera o vínculo de um produto com uma loja pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idProdutoLoja | path | **Yes** | integer | ID do vínculo do produto com a loja |

#### Request Body

**Content-Type:** `application/json`

#### Responses

**200** - 

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

---

### DELETE `/produtos/lojas/{idProdutoLoja}`

**Remove o vínculo de um produto com uma loja**

Remove o vínculo de um produto com uma loja pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idProdutoLoja | path | **Yes** | integer | ID do vínculo do produto com a loja |

#### Responses

**204** - No content.

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

---

## Produtos - Lotes

### GET `/produtos/lotes`

**Obtém lotes de produtos**

Obtém lotes de produtos paginados.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| pagina | query | No | integer | N° da página da listagem |
| limite | query | No | integer | Quantidade de registros que devem ser exibidos por página |
| idsProdutos[] | query | **Yes** | array&lt;integer&gt; | IDs dos produtos |
| idsLotes[] | query | No | array&lt;string&gt; | IDs dos lotes |
| idsDepositos[] | query | No | array&lt;integer&gt; | IDs dos depósitos |
| codigosLotes[] | query | No | array&lt;string&gt; | Códigos dos lotes |
| status | query | No | string (enum) | Status do lote |
| dataValidadeInicial | query | No | string | Data de validade inicial |
| dataValidadeFinal | query | No | string | Data de validade final |
| dataFabricacaoInicial | query | No | string | Data de fabricação inicial |
| dataFabricacaoFinal | query | No | string | Data de fabricação final |
| dataCriacaoInicial | query | No | string | Data de inclusão inicial |
| dataCriacaoFinal | query | No | string | Data de inclusão final |

#### Responses

**200** - 

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

---

### PUT `/produtos/lotes`

**Salva lotes de produtos**

Cria/altera lotes de produtos.

#### Request Body

**Content-Type:** `application/json`

#### Responses

**200** - 

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

---

### DELETE `/produtos/lotes`

**Remove lotes de produtos**

Remove lotes de produtos pelos IDs.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idsLotes[] | query | **Yes** | array&lt;integer&gt; | IDs dos lotes |

#### Responses

**204** - No content

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

---

### GET `/produtos/lotes/{idLote}`

**Obtém um lote de um produto**

Obtém um lote de um produto pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idLote | path | **Yes** | integer | ID do lote |

#### Responses

**200** - 

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

---

### PUT `/produtos/lotes/{idLote}`

**Altera um lote de um produto**

Altera um lote de um produto pelo ID.

#### Request Body

**Content-Type:** `application/json`

#### Responses

**204** - No content.

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

---

### GET `/produtos/lotes/controla-lote`

**Obtém a informação se determinados produtos possuem controle de lote**

Obtém a informação se determinados produtos possuem controle de lote.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idsProdutos[] | query | **Yes** | array&lt;integer&gt; | IDs dos produtos |

#### Responses

**200** - 

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

---

### POST `/produtos/{idProduto}/lotes/controla-lote/desativar`

**Desativa controle de lotes para o produto**

Desativa controle de lotes para o produto pelo ID do produto.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idProduto | path | **Yes** | integer | ID do produto |

#### Responses

**200** - 

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

---

### PATCH `/produtos/lotes/{idLote}/status`

**Altera o status de um lote do produto**

Altera o status de um lote do produto pelo ID.

#### Request Body

**Content-Type:** `application/json`

#### Responses

**204** - No content

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

---

## Produtos - Lotes Lançamentos

### GET `/produtos/lotes/{idLote}/lancamentos`

**Obtém os lançamentos de um lote de produto**

Obtém os lançamentos de um lote de produto pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idLote | path | **Yes** | integer | ID do lote |

#### Responses

**200** - 

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

---

### POST `/produtos/lotes/{idLote}/lancamentos`

**Cria um lançamento de um lote**

Inclui lançamento de um lote.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idLote | path | **Yes** | integer | ID do lote |

#### Request Body

**Content-Type:** `application/json`

#### Responses

**200** - 

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

---

### GET `/produtos/lotes/lancamentos/{idLancamento}`

**Obtém um lançamento de um lote de produto**

Obtém um lançamento de um lote de produto pelo ID do lançamento.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idLancamento | path | **Yes** | integer | ID do lançamento |

#### Responses

**200** - 

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

---

### PATCH `/produtos/lotes/lancamentos/{idLancamento}`

**Altera a observação de um lançamento de um lote de um produto**

Altera a observação de um lançamento de um lote de um produto pelo ID do lançamento.

#### Request Body

**Content-Type:** `application/json`

#### Responses

**200** - 

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

---

### GET `/produtos/{idProduto}/lotes/{idLote}/depositos/{idDeposito}/saldo`

**Obtém o saldo de um lote de produto**

Obtém o saldo de um lote de produto.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idLote | path | **Yes** | integer | ID do lote |
| idProduto | path | **Yes** | integer | ID do produto |
| idDeposito | path | **Yes** | integer | ID do depósito |

#### Responses

**200** - 

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

---

### GET `/produtos/{idProduto}/lotes/depositos/{idDeposito}/saldo`

**Obtém os saldos dos lotes de um produto por depósito**

Obtém os saldos dos lotes de um produto por depósito.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idsLotes[] | query | **Yes** | array&lt;integer&gt; | IDs dos lotes |
| idProduto | path | **Yes** | integer | ID do produto |
| idDeposito | path | **Yes** | integer | ID do depósito |

#### Responses

**200** - 

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

---

### GET `/produtos/{idProduto}/lotes/depositos/{idDeposito}/saldo/soma`

**Obtém a soma dos saldos dos lotes de um produto em um depósito**

Obtém a soma dos saldos dos lotes de um produto em um depósito.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idProduto | path | **Yes** | integer | ID do produto |
| idDeposito | path | **Yes** | integer | ID do depósito |

#### Responses

**200** - 

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

---

### GET `/produtos/{idProduto}/lotes/saldo/soma`

**Obtém o saldo total dos lotes de um produto**

Obtém o saldo total dos lotes de um produto pelo ID do produto.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idProduto | path | **Yes** | integer | ID do produto |

#### Responses

**200** - 

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

---

## Produtos - Variações

### GET `/produtos/variacoes/{idProdutoPai}`

**Obtém o produto e variações**

Obtém o produto e variações pelo ID do produto pai.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idProdutoPai | path | **Yes** | integer | ID do produto pai |

#### Responses

**200** - 

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

---

### POST `/produtos/variacoes/atributos/gerar-combinacoes`

**Retorna o produto pai com combinações de novas variações**

Ação responsável por retornar o produto pai com combinação de novas variações a partir dos atributos. Esta ação não persistirá os dados.

#### Request Body

**Content-Type:** `application/json`

#### Responses

**200** - 

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

---

### PATCH `/produtos/variacoes/{idProdutoPai}/atributos`

**Altera o nome do atributo nas variações**

Altera o nome do atributo nas variações de um produto pai.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idProdutoPai | path | **Yes** | integer | ID do produto pai |

#### Request Body

**Content-Type:** `application/json`

#### Responses

**200** - 

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

---

## Propostas Comerciais

### GET `/propostas-comerciais`

**Obtém propostas comerciais**

Obtém propostas comerciais paginadas.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| situacao | query | No | string | O valor referente a situação da proposta: Pendente, Aguardando, Não aprovado, Aprovado, Concluido, Rascunho. Para mais situações, pesquisar pelo número separado por vírgula. |
| idContato | query | No | integer | ID do contato |
| dataInicial | query | No | string | Data inicial |
| dataFinal | query | No | string | Data final |
| pagina | query | No | integer | N° da página da listagem |
| limite | query | No | integer | Quantidade de registros que devem ser exibidos por página |

#### Responses

**200** - 

---

### POST `/propostas-comerciais`

**Cria uma proposta comercial**

Cria uma proposta comercial.

#### Request Body

**Content-Type:** `application/json`

#### Responses

**201** - 

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

---

### DELETE `/propostas-comerciais`

**Remove múltiplas propostas comerciais**

Remove múltiplas propostas comerciais pelos IDs.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idsPropostasComerciais[] | query | **Yes** | array&lt;integer&gt; | IDs das propostas comerciais |

#### Responses

**200** - 

**204** - No content.

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

---

### GET `/propostas-comerciais/{idPropostaComercial}`

**Obtém uma proposta comercial**

Obtém uma proposta comercial pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idPropostaComercial | path | **Yes** | integer | ID da proposta comercial |

#### Responses

**200** - 

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

---

### PUT `/propostas-comerciais/{idPropostaComercial}`

**Altera uma proposta comercial**

Altera uma proposta comercial pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idPropostaComercial | path | **Yes** | integer | ID da proposta comercial |

#### Request Body

**Content-Type:** `application/json`

#### Responses

**204** - No content.

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

---

### DELETE `/propostas-comerciais/{idPropostaComercial}`

**Remove uma proposta comercial**

Remove uma proposta comercial pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idPropostaComercial | path | **Yes** | integer | ID da proposta comercial |

#### Responses

**204** - No content.

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

---

### PATCH `/propostas-comerciais/{idPropostaComercial}/situacoes`

**Altera a situação de uma proposta comercial**

Altera a situação de uma proposta comercial pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idPropostaComercial | path | **Yes** | integer | ID da proposta comercial |

#### Request Body

**Content-Type:** `application/json`

#### Responses

**204** - No content.

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

---

## Situações

### GET `/situacoes/{idSituacao}`

**Obtém uma situação**

Obtém uma situação pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idSituacao | path | **Yes** | integer | ID da situação |

#### Responses

**200** - 

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

---

### PUT `/situacoes/{idSituacao}`

**Altera uma situação**

Altera uma situação pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idSituacao | path | **Yes** | integer | ID da situação |

#### Request Body

**Content-Type:** `application/json`

#### Responses

**200** - 

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

---

### DELETE `/situacoes/{idSituacao}`

**Remove uma situação**

Remove uma situação pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idSituacao | path | **Yes** | integer | ID da situação |

#### Responses

**204** - No content.

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

---

### POST `/situacoes`

**Cria uma situação**

Cria uma situação.

#### Request Body

**Content-Type:** `application/json`

#### Responses

**201** - 

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

---

## Situações - Módulos

### GET `/situacoes/modulos`

**Obtém módulos**

Obtém módulos.

#### Responses

**200** - 

---

### GET `/situacoes/modulos/{idModuloSistema}`

**Obtém situações de um módulo**

Obtém situações de um módulo pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idModuloSistema | path | **Yes** | integer | ID do módulo do sistema |

#### Responses

**200** - 

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

---

### GET `/situacoes/modulos/{idModuloSistema}/acoes`

**Obtém as ações de um módulo**

Obtém as ações de um módulo pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idModuloSistema | path | **Yes** | integer | ID do módulo do sistema |

#### Responses

**200** - 

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

---

### GET `/situacoes/modulos/{idModuloSistema}/transicoes`

**Obtém as transições de um módulo**

Obtém as transições de um módulo pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idModuloSistema | path | **Yes** | integer | ID do módulo do sistema |

#### Responses

**200** - 

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

---

## Situações - Transições

### GET `/situacoes/transicoes/{idTransicao}`

**Obtém uma transição**

Obtém uma transição pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idTransicao | path | **Yes** | integer | ID da transição |

#### Responses

**200** - 

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

---

### PUT `/situacoes/transicoes/{idTransicao}`

**Altera uma transição**

Altera uma transição pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idTransicao | path | **Yes** | integer | ID da transição |

#### Request Body

**Content-Type:** `application/json`

#### Responses

**200** - 

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

---

### DELETE `/situacoes/transicoes/{idTransicao}`

**Remove uma transição**

Remove uma transição pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idTransicao | path | **Yes** | integer | ID da transição |

#### Responses

**204** - No content.

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

---

### POST `/situacoes/transicoes`

**Cria uma transição**

Cria uma transição.

#### Request Body

**Content-Type:** `application/json`

#### Responses

**201** - 

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

---

## Usuários

### POST `/usuarios/recuperar-senha`

**Envia solicitação de recuperação de senha**

Envia solicitação de recuperação de senha por e-mail.

#### Request Body

**Content-Type:** `application/json`

#### Responses

**200** - 

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

---

### PATCH `/usuarios/redefinir-senha`

**Redefine senha do usuário**

Redefine senha do usuário utilizando token enviado por e-mail.

#### Request Body

**Content-Type:** `application/json`

#### Responses

**204** - No content.

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

---

### GET `/usuarios/verificar-hash`

**Valida o hash recebido**

Valida o hash recebido por e-mail.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| hash | query | **Yes** | string |  |

#### Responses

**200** - 

**400** - 

**Example Response (400)**

```json
{
  "error": {
    "type": "validation_error",
    "message": "Dados inválidos fornecidos",
    "fields": {
      "nome": [
        "O campo nome é obrigatório"
      ]
    }
  }
}
```

---

## Vendedores

### GET `/vendedores`

**Obtém vendedores**

Obtém vendedores paginados.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| pagina | query | No | integer | N° da página da listagem |
| limite | query | No | integer | Quantidade de registros que devem ser exibidos por página |
| nomeContato | query | No | string | Nome do contato do vendedor |
| situacaoContato | query | No | string (enum) | Situação do contato do vendedor<br>`A` Ativo<br>`I` Inativo<br>`S` Sem movimento<br>`E` Excluído<br>`T` Todos |
| idContato | query | No | integer | ID do contato do vendedor |
| idLoja | query | No | integer | ID da loja vinculada ao vendedor |
| dataAlteracaoInicial | query | No | string | Data de alteração inicial |
| dataAlteracaoFinal | query | No | string | Data de alteração final |

#### Responses

**200** - 

---

### GET `/vendedores/{idVendedor}`

**Obtém um vendedor**

Obtém um vendedor pelo ID.

#### Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| idVendedor | path | **Yes** | integer | ID do vendedor |

#### Responses

**200** - 

**404** - 

**Example Response (404)**

```json
{
  "error": {
    "type": "not_found",
    "message": "Recurso não encontrado"
  }
}
```

---
