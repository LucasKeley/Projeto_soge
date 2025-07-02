# Projeto SOGE: API de Sistema de Sugestões

Este projeto é uma API backend desenvolvida com FastAPI e SQLAlchemy para um sistema de caixa de sugestões. Ele permite que colaboradores se cadastrem, enviem sugestões de melhoria para diferentes setores e que os administradores gerenciem o status dessas sugestões.

# ✨ Funcionalidades Principais

* 👤 Gestão de Usuários: Rota segura para a criação de novas contas de colaboradores.
* 🔐 Segurança de Senhas: Utiliza bcrypt para a criptografia (hashing) de senhas, garantindo que elas não sejam armazenadas em texto plano no banco de dados.
* 💡 Envio de Sugestões: Endpoint para que os usuários possam enviar novas sugestões, que ficam atreladas ao seu cadastro.
* 📋 Listagem e Filtragem: Permite listar todas as sugestões cadastradas ou filtrá-las por setor ou status (ex: 'aberta', 'em análise', 'implementada').
* 🔄 Atualização de Status: Rota para que administradores (funcionalidade a ser expandida) possam alterar o status de uma sugestão específica.

# 🛠️ Tecnologias Utilizadas

* Python 3.10+
* FastAPI: Framework web moderno e de alta performance para a construção de APIs.
* SQLAlchemy: Toolkit SQL e Mapeador Objeto-Relacional (ORM) para interagir com o banco de dados.
* SQLite: Banco de dados relacional leve, utilizado para armazenamento dos dados.
* Uvicorn: Servidor ASGI de alta velocidade para rodar a aplicação.
* Passlib com Bcrypt: Para hashing e verificação de senhas.
* Pydantic: Para validação de dados e schemas.
* Python-dotenv: Para gerenciamento de variáveis de ambiente.

#🚀 Como Executar o Projeto
Siga os passos abaixo para configurar e executar o projeto em seu ambiente local.

### Pré-requisitos
* Python 3.10 ou superior
* pip (gerenciador de pacotes do Python)
  
### Instalação

1. Clone o repositório:
   
   `git clone https://github.com/LucasKeley/Projeto_soge.git`
   
    `cd seu-repositorio`
   
2. Crie e ative um ambiente virtual (recomendado):
   
```
#Para Linux/macOS
python3 -m venv venv
source venv/bin/activate

#Para Windows
python -m venv venv
.\venv\Scripts\activate
```

3. Instale as dependências:
Instale as dependências do arquivo requirements.txt que está raiz do projeto

`pip install -r requirements.txt`

4. Configure as variáveis de ambiente:
Crie um arquivo chamado .env na raiz do projeto e adicione a seguinte variável:

`SECRET_KEY="sua_chave_secreta_super_segura_aqui"`

Caso necessite acesso a chave para testar a função de criação de usuário envie um e-mail para: lucaskeley01@gmail.com

### Execução
1. Inicie o servidor:
Com o ambiente virtual ativado, execute o seguinte comando no terminal:

`uvicorn main:app --reload`

O --reload faz com que o servidor reinicie automaticamente após qualquer alteração no código.

2. Acesse a documentação interativa:
Abra seu navegador e acesse um dos seguintes URLs para interagir com a API através da documentação gerada automaticamente pelo FastAPI:

```
Swagger UI: http://127.0.0.1:8000/docs
ReDoc: http://127.0.0.1:8000/redoc
```

# 🗂️ Estrutura do Projeto

```
/
├── database/
│   └── banco.db          # Arquivo do banco de dados (criado automaticamente)
├── .env                  # Arquivo para variáveis de ambiente (crie manualmente)
├── auth_routes.py        # Rotas de autenticação (ex: /criar_conta)
├── register_routes.py    # Rotas de Registro (ex: /criar_sugestao)
├── alembic               # Gerenciamento e migrações de esquemas de banco de dado
├── dependencies.py       # Dependências do FastAPI (ex: pegar_sessao)
├── main.py               # Ponto de entrada da aplicação
├── models.py             # Modelos de dados do SQLAlchemy (Usuario, Sugestao)
├── schemas.py            # Esquemas Pydantic para validação de dados de entrada/saída
└── requirements.txt      # Dependências do projeto
```

# 🗄️ Estrutura do Banco de Dados
A API utiliza duas tabelas principais no banco de dados:
* usuarios: Armazena as informações dos colaboradores.
  * id: Identificador único (Chave Primária)
  * nome_colaborador: Nome do usuário
  * email: E-mail único para login
  * senha: Senha criptografada
  * admin: Flag booleana para permissões de administrador
  * data_cadastro: Data de criação do registro
 
* sugestoes: Armazena as sugestões enviadas.
  * id: Identificador único (Chave Primária)
  * nome_colaborador: ID do usuário que enviou (Chave Estrangeira para usuarios.id)
  * setor: Setor ao qual a sugestão se aplica
  * descricao: O texto da sugestão
  * status: O estado atual da sugestão ('aberta', 'em análise', 'implementada')
  * data_criacao: Data de criação do registro

# Endpoints da API
Aqui está um resumo dos endpoints disponíveis na API.

### Autenticação (/auth)
* `POST /auth/criar_conta` 
  * Descrição: Cria um novo usuário (colaborador) no sistema.
  * Corpo da Requisição:
    
```
{
  "nome_colaborador": "João Silva",
  "email": "joao.silva@email.com",
  "senha": "uma_senha_forte_123",
  "admin": false
}
```

* Resposta de Sucesso (200 OK):

```
{
  "mensagem": "usuário cadastrado com joao.silva@email.com"
}
```
### Sugestões (/sugestoes)
* `POST /sugestoes/criar_sugestao`
  * Descrição: Registra uma nova sugestão no sistema.
  * Corpo da Requisição:
 
{
  "id": 0,
  "nome_colaborador": "string",
  "setor": "string",
  "descricao": "string",
  "status": "aberta",
  "data_criacao": "2025-07-02T00:43:17.301Z"
}

* Resposta de Sucesso (200 OK):

```
{
  "Mensagem": "Sua Sugestão foi criada com sucesso. ID da sugestão: 1"
}
```

* `GET /sugestoes/listar_todas`
  * Descrição: Retorna uma lista com todas as sugestões cadastradas.

* `GET /sugestoes/filtrar`

  * Descrição: Filtra as sugestões com base nos parâmetros de query setor e/ou status.
  * Exemplo de Uso:
    ```
      http://127.0.0.1:8000/sugestoes/filtrar?setor=VIP
    ``` 

* `PATCH /sugestoes/{id}`
  * Descrição: Atualiza o status de uma sugestão específica pelo seu ID.
  * Exemplo de Uso:
    
    ```
    http://127.0.0.1:8000/sugestoes/2
    ```
  * Corpo da Requisição:
    
  ```
  {
    "status": "em análise"
  }

  ```


