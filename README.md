# 🔗 Encurtador de URL - FastAPI

Projeto simples de um **encurtador de URLs** utilizando **FastAPI** e **SQLAlchemy**, com sistema de expiração de links e com uma geração de códigos curtos usando Base62.


## 🚀 Funcionalidades

- Geração de URLs curtas únicas com Base62
- Expiração configurável dos links
- Redirecionamento automático para a URL original
- Interface HTML básica com formulário para encurtamento (SEM CSS)


## 📁 Estrutura do Projeto

├── main.py # Aplicação principal (FastAPI)
├── models.py # Modelos do banco de dados
├── schemas.py # Schemas Pydantic para validação
├── database.py # Configuração do banco de dados do app
├── utils.py # Funções auxiliares (ex: Base62)
├── templates/
│ └── form.html # Formulário HTML simples
│ └── resultado.html # Retorna o resultado
└── README.md # Documentação do projeto


## ⚙️ Como executar o APP

1. Clone o repositório:
```bash
-- git clone https://github.com/seuusuario/encurtador-fastapi.git #######
-- cd Encurtador_de_URL

2. Crie e ative um ambiente virtual: 
-- python -m venv venv
-- source venv/bin/activate  # Windows: venv\Scripts\activate

3. Instale as Dependências:
-- pip install fastapi uvicorn sqlalchemy jinja2

4. Execulte a aplicação:
-- uvicorn main:app --reload

5. Acesse via navegador:
-- http://localhost:8000

## 📌 Uso do APP

-- Encerrar uma URL via formulário web.

-- Acesse a página principal e insira a URL longa no campo disponível.

-- Clique em "Encurtar" para obter o link curto.

______________________
API para encurtar URL: 

POST /encurtar
Content-Type: application/json

{
  "long_url": "https://exemplo.com/pagina",
  "expires_in_minutes": 60
}

______________________
Resposta da API:

{
  "long_url": "https://exemplo.com/pagina",
  "short_code": "a1B9kP",
  "expires_at": "2025-07-21T20:00:00Z"
}

_______________________

Redirecionamento e expiração:

-- Ao acessar a URL curta, o sistema redireciona para a URL original.
-- Se o link estiver expirado, retorna erro HTTP 410 ("Link expirado").
-- Se não encontrado, retorna erro HTTP 404.

⚠️ Observações impoortantes

-- O banco de dados deve ser recriado após mudanças no modelo.
-- Expiração é validada no momento do redirecionamento.


👨‍💻 Autor
Senhor Luan – Desenvolvedor back-end
Contato: luanfamilia2015@gmail.com
GitHub: @Luan22Wolf