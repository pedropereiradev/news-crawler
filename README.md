# News Crawler API

API em Flask para web scraping de notícias dos principais portais de notícias brasileiros.

## 📋 Descrição

Esta API realiza scraping de notícias dos portais:
- Globo (www.globo.com)
- UOL (www.uol.com.br)

A API coleta títulos, links e imagens das notícias em tempo real.

## 🚀 Tecnologias Utilizadas

- Python 3.8+
- Flask
- BeautifulSoup4
- Flask-CORS
- Requests
- UUID

## 💻 Pré-requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

## 🔧 Instalação

1. Clone o repositório
```bash
git clone https://github.com/seu-usuario/news-crawler.git
cd news-crawler/crawler-api
```

2. Crie e ative um ambiente virtual
```bash
python -m venv venv

# Windows
venv\Scripts\activate
# Linux/macOS
source venv/bin/activate
```

3. Instale as dependências
```bash
pip install -r requirements.txt
```

4. Execute a API
```bash
python app.py
```

A API estará disponível em `http://localhost:5000`

## 📍 Endpoints

### GET /search_news
Retorna todas as notícias coletadas dos portais configurados.

Exemplo de resposta:
```json
{
  "news": [
    {
      "id": "550e8400-e29b-41d4-a716-446655440000",
      "site": "GLOBO",
      "title": "Título da notícia",
      "link": "https://globo.com/noticia",
      "img": "https://globo.com/imagem.jpg"
    }
  ]
}
```

### GET /health
Endpoint para verificação de saúde da API.

Resposta:
```json
{
  "status": "healthy"
}
```

## 🏗️ Estrutura do Projeto

```
crawler-api/
├── app.py           # Aplicação principal e rotas
├── scraper.py       # Lógica de scraping
└── requirements.txt # Dependências Python
```

## ⚠️ Limitações Conhecidas

- O scraping pode falhar se os sites alterarem sua estrutura HTML
- O sistema não armazena histórico das notícias
- Não há sistema de cache implementado

## 🚀 Melhorias Futuras

### Funcionalidades
- [ ] Implementar sistema de cache para reduzir requisições aos portais
- [ ] Adicionar mais portais de notícias (Folha, Estadão, etc)
- [ ] Criar sistema de categorização de notícias (política, esportes, etc)
- [ ] Implementar histórico de notícias com banco de dados
- [ ] Adicionar sistema de busca por palavras-chave

### Performance
- [ ] Implementar scraping assíncrono para melhor performance
- [ ] Adicionar rate limiting para proteção da API
- [ ] Criar sistema de filas para processamento de scraping
- [ ] Implementar compressão de resposta

### Documentação
- [ ] Adicionar Swagger/OpenAPI
- [ ] Criar documentação técnica detalhada
- [ ] Adicionar exemplos de uso com diferentes linguagens
- [ ] Documentar processo de deploy
