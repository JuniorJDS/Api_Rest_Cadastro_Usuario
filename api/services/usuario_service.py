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

def remover_usuario(usuario):
    db.session.delete(usuario)
    db.session.commit()

def editar_usuario(usuario_bd, usuario_novo):
    usuario_bd.nome  = usuario_novo.nome
    usuario_bd.data_nascimento  = usuario_novo.data_nascimento
    usuario_bd.cpf  = usuario_novo.cpf
    usuario_bd.cep  = usuario_novo.cep
    usuario_bd.rua  = usuario_novo.rua
    usuario_bd.bairro  = usuario_novo.bairro
    usuario_bd.cidade  = usuario_novo.cidade
    usuario_bd.estado  = usuario_novo.estado
    db.session.commit()
