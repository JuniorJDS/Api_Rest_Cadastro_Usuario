from flask_restful import Resource
from api import api
from ..schemas import usuario_schema
from flask import request, make_response, jsonify
from ..entidades import usuario
from ..services import usuario_service
import pycep_correios

class Usuario(Resource):
    def get(self):
        lista_de_usuarios = usuario_service.listar_usuarios()
        us = usuario_schema.Usuario(many=True)
        return make_response(us.jsonify(lista_de_usuarios), 200)

    def post(self):
        us = usuario_schema.UsuarioGet()
        validate = us.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            nome = request.json['nome']
            data_nascimento = request.json['data_nascimento']
            cpf = request.json['cpf']
            cep = request.json['cep']
            # buscar os dados da api viaCep
            try:
                endereco = pycep_correios.get_address_from_cep(cep)
            except:
                return make_response(jsonify({"erro":"cep inválido ou não encontrado"}), 400)
            #
            rua = endereco['logradouro']
            bairro = endereco['bairro'] 
            cidade = endereco['cidade']
            estado = endereco['uf']

            usuario_novo = usuario.Usuario(nome=nome, data_nascimento=data_nascimento, 
                                           cpf=cpf, cep=cep, rua=rua, bairro=bairro, 
                                           cidade=cidade, estado=estado)
            resultado = usuario_service.cadastrar_cliente(usuario_novo)
            usg = usuario_schema.Usuario()
            return make_response(usg.jsonify(resultado), 201) 


class UsuarioDetail(Resource):
    def get(self, id):
        usuario = usuario_service.listar_usuario_id(id=id)
        if usuario is None:
            return make_response(jsonify('Usuário Inexistente!'), 404)
        us = usuario_schema.Usuario()
        return make_response(us.jsonify(usuario), 200)

    def put(self, id):
        usuario_db = usuario_service.listar_usuario_id(id=id)
        if usuario_db is None:
            return make_response(jsonify('Usuário não Encontrado!'), 404)
        usg = usuario_schema.UsuarioGet()

        validate = usg.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            nome = request.json['nome']
            data_nascimento = request.json['data_nascimento']
            cpf = request.json['cpf']
            cep = request.json['cep']
            # buscar os dados pela api viaCep
            try:
                endereco = pycep_correios.get_address_from_cep(cep)
            except:
                return make_response(jsonify({"erro":"cep inválido ou não encontrado"}), 400)
            
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
        usuario = usuario_service.listar_usuario_id(id=id)
        if usuario is None:
            return make_response(jsonify('Usuário Inexistente!'), 404)
        usuario_service.remover_usuario(usuario)
        return make_response('', 204)

api.add_resource(Usuario, '/usuario')
api.add_resource(UsuarioDetail, '/usuario/<int:id>')