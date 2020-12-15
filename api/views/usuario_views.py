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


api.add_resource(Usuario, '/usuario')