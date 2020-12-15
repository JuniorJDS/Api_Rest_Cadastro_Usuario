from api import ma
from marshmallow import fields
from ..models import usuario_model


class Usuario(ma.SQLAlchemySchema):
    class Meta:
        model = usuario_model.Usuario
        fields = ('id', 'nome', 'data_nascimento', 'cpf', 'cep', 'rua', 'bairro', 'cidade', 'estado')


    nome = fields.String(required=True)
    data_nascimento = fields.Date(required=True)
    cpf = fields.String(required=True, unique=True)
    cep = fields.String(required=True)
    rua = fields.String(required=True)
    bairro = fields.String(required=True)
    cidade = fields.String(required=True)
    estado = fields.String(required=True)

class UsuarioGet(ma.SQLAlchemySchema):
    class Meta:
        model = usuario_model.Usuario
        fields = ('id', 'nome', 'data_nascimento', 'cpf', 'cep')


    nome = fields.String(required=True)
    data_nascimento = fields.Date(required=True)
    cpf = fields.String(required=True, unique=True)
    cep = fields.String(required=True)