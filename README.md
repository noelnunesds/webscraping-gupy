# 🕷️ Web Scraping Gupy

Este projeto realiza web scraping em uma URL fornecida, identifica todas as palavras com mais de 3 caracteres e armazena essas palavras em um banco de dados, junto com a contagem de ocorrências.  
Caso a palavra já exista no banco, a contagem é atualizada em vez de duplicada.

---

## 🚀 Como Executar

### ✅ Pré-requisitos

- Python instalado (versão 3.8+ recomendada)
- [Poetry](https://python-poetry.org/docs/#installation) para gerenciamento de dependências

### ⚙️ Passos para execução

1. Instale as dependências com o Poetry:
   ```bash
   poetry install
   ```

2. Execute o script principal:
   ```bash
   poetry run python main.py
   ```

3. Insira a URL no terminal quando solicitado, e aguarde o processamento.

---

## 💾 Funcionamento

- O script extrai o conteúdo HTML da URL.
- Todas as palavras com mais de 3 caracteres são contabilizadas.
- Os dados são salvos em um banco de dados SQLite (ou outro, se configurado).
- Palavras repetidas têm sua contagem atualizada automaticamente.
