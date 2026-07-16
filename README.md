# OpenAI API em Python

Este projeto foi desenvolvido como parte dos meus estudos em Python e tem como objetivo demonstrar como utilizar a API da OpenAI para interagir com modelos de Inteligência Artificial diretamente pelo código, sem utilizar a interface do ChatGPT.

A aplicação realiza uma conversa simples pelo terminal, enviando a mensagem do usuário para a API e exibindo a resposta gerada pelo modelo.

---

## 🚀 Funcionalidades

* Integração com a API da OpenAI utilizando a biblioteca oficial.
* Utilização do cliente `OpenAI()` (nova sintaxe da biblioteca).
* Configuração de uma **System Message** para definir o comportamento da IA.
* Controle da criatividade das respostas através do parâmetro `temperature`.
* Limitação do tamanho das respostas utilizando `max_tokens`.
* Entrada de dados pelo terminal utilizando `input()`.
* Carregamento seguro da chave da API por meio de variáveis de ambiente (`.env`).

---

## 🛠️ Tecnologias utilizadas

* Python 3
* OpenAI Python SDK (`openai >= 1.0.0`)
* python-dotenv

---

## 📂 Estrutura do projeto

```text
openai-api-python/
│
├── main.py
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

---

## ⚙️ Instalação

Clone o repositório:

```bash
git clone https://github.com/chegos/openai-api-python.git
```

Acesse a pasta do projeto:

```bash
cd openai-api-python
```

Crie um ambiente virtual:

```bash
python -m venv venv
```

Ative o ambiente virtual.

### Windows

```powershell
venv\Scripts\activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

---

## 🔑 Configuração da API

Crie um arquivo chamado `.env` na raiz do projeto.

Exemplo:

```env
OPENAI_API_KEY=sua_chave_da_api
```

---

## ▶️ Executando o projeto

Execute o arquivo principal:

```bash
python main.py
```

Digite uma pergunta no terminal e aguarde a resposta da IA.

Para encerrar o programa, digite:

```text
sair
```

---

## 💡 Observação

Atualmente, a API da OpenAI exige uma chave de API com créditos ou faturamento habilitado.

Caso sua conta não possua acesso à API, será exibido um erro semelhante a:

```text
429 - insufficient_quota
```

Isso não significa que o código está incorreto, apenas que a conta utilizada não possui créditos disponíveis para realizar chamadas à API.

---

## 🆓 Alternativa gratuita

Se você deseja testar um projeto semelhante sem custos, pode adaptar este código para utilizar outros provedores de modelos de IA que oferecem planos gratuitos para desenvolvimento e testes, como:

* Google Gemini API
* Groq API
* OpenRouter (modelos gratuitos)

A estrutura do projeto permanece praticamente a mesma, alterando apenas a biblioteca utilizada e a configuração do cliente.

---

## 👨‍💻 Autor

**Luis Fernando de Oliveira Rodrigues**

GitHub: https://github.com/chegos
