from api import ma
from marshmallow import fields
from ..models import usuario_model


class UsuarioGet(ma.SQLAlchemySchema):
    class Meta:
        model = usuario_model.Usuario
        fields = ('id', 'nome', 'data_nascimento', 'cpf', 'cep')


    nome = fields.String(required=True)
    data_nascimento = fields.Date(required=True)
    cpf = fields.String(required=True, unique=True)
    cep = fields.String(required=True)