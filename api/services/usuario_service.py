from api import db
from ..models import usuario_model


def cadastrar_cliente(usuario):
    tarefa_bd = usuario_model.Usuario(nome=usuario.nome, data_nascimento=usuario.data_nascimento,
                                      cpf=usuario.cpf, cep=usuario.cep, rua=usuario.rua, bairro=usuario.bairro,
                                      cidade=usuario.cidade, estado=usuario.estado)
    db.session.add(tarefa_bd)
    db.session.commit()
    return tarefa_bd

