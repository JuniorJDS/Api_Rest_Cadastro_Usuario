
class usuario():
    def __init__(self, nome, data_nascimento, cpf, endereco):
        self.__nome = nome
        self.__data_nascimento = data_nascimento
        self.__cpf = cpf
        self._endereco = endereco

    @property
    def nome(self):
        return self.__nome 

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def data_nascimento(self):
        return self.__data_nascimento 

    @data_nascimento.setter
    def data_nascimento(self, data_nascimento):
        self.__data_nascimento = data_nascimento

    @property
    def cpf(self):
        return self.__cpf 

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    @property
    def endereco(self):
        return self.__endereco 

    @endereco.setter
    def endereco(self, endereco):
        self.__endereco = endereco