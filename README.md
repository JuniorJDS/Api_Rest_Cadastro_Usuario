# API para Cadastro de Usuário

## Descrição
Api para cadastro de usuários e salvá los em um banco de dados. O usuário deve 
passar os seguintes dados:
- nome
- data de nascimento
- cpf (será validado e permitido apenas um cadastro por usuário)
- cep (também será validado e, a partir dele, será preenchido os dados de endereço)

## Docker


```
docker build -t api_user .
docker-compose up -d
```

## clonando e rodando a aplicação
```
    $ python3 -m venv venv

    $ source venv/bin/activate

    $ pip3 install --upgrade pip

    $ pip3 install -r requirements.txt

    doc http://127.0.0.1:5000/apidocs/
```
