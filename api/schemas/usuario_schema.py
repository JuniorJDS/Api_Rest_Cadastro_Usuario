from api import ma
from marshmallow import fields, Schema, ValidationError
from marshmallow.validate import Length
from ..models import usuario_model
from pycpfcnpj import cpf


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



def validate_cpf(data):
    user = usuario_model.Usuario.query.filter_by(cpf=data).first()
    if user is not None:
            raise ValidationError('CPF já cadastrado!')

def validate_cpf_type(data):
    if not cpf.validate(data):
        raise ValidationError('CPF inválido!')


class UsuarioPost(ma.SQLAlchemySchema):
    class Meta:
        model = usuario_model.Usuario
        fields = ('nome', 'data_nascimento', 'cpf', 'cep')
        


    nome = fields.String(required=True)
    data_nascimento = fields.Date(required=True)
    cpf = fields.String(required=True, unique=True, validate= [validate_cpf, validate_cpf_type])
    cep = fields.String(required=True)

class UsuarioPut(ma.SQLAlchemySchema):
    class Meta:
        model = usuario_model.Usuario
        fields = ('nome', 'data_nascimento', 'cpf', 'cep')
        


    nome = fields.String(required=True)
    data_nascimento = fields.Date(required=True)
    cpf = fields.String(required=True, unique=True, validate=validate_cpf_type)
    cep = fields.String(required=True)