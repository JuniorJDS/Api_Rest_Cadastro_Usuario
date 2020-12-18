# API para Cadastro de Usuário

## Descrição
Api para cadastro de usuários e salvá los em um banco de dados. O usuário deve 
passar os seguintes dados:
- nome
- data de nascimento
- cpf (será validado e permitido apenas um cadastro por usuário)
- cep (também será validado e, a partir dele, será preenchido os dados de endereço)

## Docker - ESTÁ COM ERRO (Precisa adcionar os migrations)


```
docker build -t api_user .
docker-compose up -d
```

## Clone o repositório e instale os requirements: 
```
    $ python3 -m venv venv

    $ source venv/bin/activate

    $ pip3 install --upgrade pip

    $ pip3 install -r requirements.txt

    doc http://127.0.0.1:5000/apidocs/
```
Crie um banco de dados Mysql com o nome "user_db" e migre as tabelas:
```
    $ export FLASK_APP=run.py

    $ flask db init

    $ flask db migrate

    $ flask db upgrade

    $ flask run
```
## Endpoints 
Inicialmente estão implementados os seguintes endpoints:

#### Usuários
- ``` usuario ``` - GET - Lista todos os usuários cadastrados
- ``` usuario ``` - POST - Cria um usuário 

### Documentação com swagger
```
http://127.0.0.1:5000/apidocs/
```
