# 📚 API Livros Vai Na Web

Este é o segundo desafio do módulo de Back-end do curso Vai Na Web, onde desenvolvemos uma API simples utilizando Flask e SQLite para cadastrar e listar livros. A API permite o cadastro de livros e sua visualização em uma lista organizada.

## 🚀 Funcionalidades
- Cadastrar um livro no banco de dados. (`POST /doar`)
- Listar todos os livros cadastrados. (`GET /livros`)
- Exibir uma página inicial personalizada. (`GET /`)

## 🔍 Requisitos Técnicos
1. **Framework:** Flask.
2. **Banco de Dados:** SQLite.
3. **Tabela:** `LIVROS` com os seguintes campos:
   - `id` (chave primária, autoincrementada)
   - `titulo` (texto, obrigatório)
   - `categoria` (texto, obrigatório)
   - `autor` (texto, obrigatório)
   - `image_url` (texto, obrigatório)

## 📥 Instalação

1. Clone o repositório:
```bash
    git clone https://github.com/seu-usuario/nome-do-repositorio.git
```

2. Entre no diretório do projeto:
```bash
    cd nome-do-repositorio
```

3. Crie um ambiente virtual e o ative:
```bash
    python3 -m venv venv
    source venv/bin/activate  # Linux / Mac
    venv\Scripts\activate  # Windows
```

4. Instale as dependências:
```bash
    pip install -r requirements.txt
```

5. Crie o banco de dados SQLite:
```bash
    python
    >>> from app import db
    >>> db.create_all()
    >>> exit()
```

6. Inicie o servidor Flask:
```bash
    flask run
```

## 📌 Rotas da API

### Página inicial
```http
GET /
```
Retorna uma mensagem personalizada de boas-vindas.

### Cadastrar um livro
```http
POST /doar
```
Envia um JSON com os dados do livro:
```json
{
  "titulo": "Livro Exemplo",
  "categoria": "Ficção",
  "autor": "Autor Exemplo",
  "image_url": "https://exemplo.com/imagem.jpg"
}
```
Resposta:
```json
{
  "message": "Livro cadastrado com sucesso!"
}
```
Status Code: `201`

### Listar todos os livros
```http
GET /livros
```
Retorna um JSON com todos os livros cadastrados.

## 📚 Tecnologias Utilizadas
- Python
- Flask
- SQLite


