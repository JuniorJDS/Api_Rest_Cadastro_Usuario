from api import db
from ..models import usuario_model


def cadastrar_cliente(usuario):
    usuario_bd = usuario_model.Usuario(nome=usuario.nome, data_nascimento=usuario.data_nascimento,
                                      cpf=usuario.cpf, cep=usuario.cep, rua=usuario.rua, bairro=usuario.bairro,
                                      cidade=usuario.cidade, estado=usuario.estado)
    db.session.add(usuario_bd)
    db.session.commit()
    return usuario_bd

def listar_usuarios():
    usuarios = usuario_model.Usuario.query.all()
    return usuarios

def listar_usuario_id(id):
    usuario = usuario_model.Usuario.query.filter_by(id=id).first()
    return usuario

