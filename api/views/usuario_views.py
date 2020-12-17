from flask_restful import Resource
from api import api
from ..schemas import usuario_schema
from flask import request, make_response, jsonify
from ..entidades import usuario
from ..services import usuario_service
import pycep_correios

class Usuario(Resource):
    def get(self):
        """
        Lista todos os usuários cadastrados.
        ---
        tags:
            - Rotas referentes ao cadastro de usuário 
        responses:
            200:
                description: Lista de todos os usuários.
                schema:
                    id: usuario
                    properties:
                        nome:
                            type: string
                        data_nascimento:
                            type: string
                        cpf:
                            type: string
                        cep:
                            type: string
                        rua:
                            type: string
                        bairro:
                            type: string
                        cidade:
                            type: string
                        estado:
                            type: string

        """
        lista_de_usuarios = usuario_service.listar_usuarios()
        us = usuario_schema.Usuario(many=True)
        return make_response(us.jsonify(lista_de_usuarios), 200)

    def post(self):
        """
       Cadastra um usuário.
       ---
        tags:
            - Rotas referentes ao cadastro de usuário 
        parameters:
    
         - in: body
           name: Usuario
           descriptions: Criar novo Usuario
           schema:
            type: object
            required:
                - nome
                - data_nascimento
                - cpf
                - cep
            properties:
                nome:
                    type: string
                data_nascimento:
                    type: string
                cpf:
                    type: string
                cep:
                    type: string
        responses:
            201:
                descripition: usuario cadastrado com sucesso!
                schema:
                    id: usuario
                    properties:
                        nome:
                            type: string
                        data_nascimento:
                            type: string
                        cpf:
                            type: string
                        cep:
                            type: string
                        rua:
                            type: string
                        bairro:
                            type: string
                        cidade:
                            type: string
                        estado:
                            type: string
            400:
                description: Solicitação Inválida.
            404:
                description: Usuário não Encontrado.
            422:
                description: cep inválido ou não encontrado. 
        
        """
        usp = usuario_schema.UsuarioPost()
        errors = usp.validate(request.json)
        if errors:
            return make_response(jsonify(errors), 400)
        else:
            nome = request.json['nome']
            data_nascimento = request.json['data_nascimento']
            cpf = request.json['cpf']
            cep = request.json['cep']
            # buscar os dados da api viaCep
            try:
                endereco = pycep_correios.get_address_from_cep(cep)
            except:
                return make_response(jsonify({"erro":"cep inválido ou não encontrado"}), 422)
            
            rua = endereco['logradouro']
            bairro = endereco['bairro'] 
            cidade = endereco['cidade']
            estado = endereco['uf']

            usuario_novo = usuario.Usuario(nome=nome, data_nascimento=data_nascimento, 
                                           cpf=cpf, cep=cep, rua=rua, bairro=bairro, 
                                           cidade=cidade, estado=estado)
            resultado = usuario_service.cadastrar_cliente(usuario_novo)
            us = usuario_schema.Usuario()
            return make_response(us.jsonify(resultado), 201) 


class UsuarioDetail(Resource):
    def get(self, id):
        """
        Lista as informações de um usuário.
        ---
        tags:
            - Rotas referentes ao cadastro de usuário 
        parameters:
            - in: path
              name: id
              type: integer
              required: true
        responses:
            200:
                description: Lista de todos os usuários.
                schema:
                    id: usuario
                    properties:
                        nome:
                            type: string
                        data_nascimento:
                            type: string
                        cpf:
                            type: string
                        cep:
                            type: string
                        rua:
                            type: string
                        bairro:
                            type: string
                        cidade:
                            type: string
                        estado:
                            type: string
            404:
                description: Usuário não existe. 
        """
        usuario = usuario_service.listar_usuario_id(id=id)
        if usuario is None:
            return make_response(jsonify('Usuário não existe.'), 404)
        us = usuario_schema.Usuario()
        return make_response(us.jsonify(usuario), 200)

    def put(self, id):
        """
        Atualiza os dados de um usuário existente.
        ---
        tags:
            - Rotas referentes ao cadastro de usuário 
        parameters:
            - in: path
              name: id
              type: integer
              required: true
            - in: body
              name: Usuario
              descriptions: Criar novo Usuario
              schema:
                  type: object
                  required:
                      - nome
                      - data_nascimento
                      - cpf
                      - cep
                  properties:
                      nome:
                          type: string
                      data_nascimento:
                          type: string
                      cpf:
                          type: string
                      cep:
                          type: string
        responses:
            200:
                description: usuário editado com sucesso!
                schema:
                    id: usuario
                    properties:
                        nome:
                            type: string
                        data_nascimento:
                            type: string
                        cpf:
                            type: string
                        cep:
                            type: string
                        rua:
                            type: string
                        bairro:
                            type: string
                        cidade:
                            type: string
                        estado:
                            type: string
            400:
                description: Solicitação Inválida.
            404:
                description: Usuário não Encontrado.
            422:
                description: cep inválido ou não encontrado.    
        """
        usuario_db = usuario_service.listar_usuario_id(id=id)
        if usuario_db is None:
            return make_response(jsonify('Usuário não Encontrado!'), 404)
        usp = usuario_schema.UsuarioPut()

        errors = usp.validate(request.json)
        if errors:
            return make_response(jsonify(errors), 400)
        else:
            nome = request.json['nome']
            data_nascimento = request.json['data_nascimento']
            cpf = request.json['cpf']
            cep = request.json['cep']
            # buscar os dados pela api viaCep
            try:
                endereco = pycep_correios.get_address_from_cep(cep)
            except:
                return make_response(jsonify({"erro":"cep inválido ou não encontrado"}), 422)
            
            rua = endereco['logradouro']
            bairro = endereco['bairro'] 
            cidade = endereco['cidade']
            estado = endereco['uf']

            usuario_novo = usuario.Usuario(nome=nome, data_nascimento=data_nascimento, 
                                           cpf=cpf, cep=cep, rua=rua, bairro=bairro, 
                                           cidade=cidade, estado=estado)

            usuario_service.editar_usuario(usuario_db, usuario_novo)
            usuario_atualizado = usuario_service.listar_usuario_id(id=id)
            us = usuario_schema.Usuario()
            return make_response(us.jsonify(usuario_atualizado), 200)

    def delete(self, id):
        """
        Remove um usuário cadastrado.
        ---
        tags:
            - Rotas referentes ao cadastro de usuário 
        parameters:
            - in: path
              name: id
              type: integer
              required: true
        responses:
            204:
              description: Usuário removido com sucesso!
            404:
              description: Usuário não foi encontrado. 

        """
        usuario = usuario_service.listar_usuario_id(id=id)
        if usuario is None:
            return make_response(jsonify('Usuário Inexistente!'), 404)
        usuario_service.remover_usuario(usuario)
        return make_response('', 204)

api.add_resource(Usuario, '/usuario')
api.add_resource(UsuarioDetail, '/usuario/<int:id>')