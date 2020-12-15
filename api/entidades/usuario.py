
class Usuario():
    def __init__(self, nome, data_nascimento, cpf, cep, rua, bairro, cidade, estado):
        self.__nome = nome
        self.__data_nascimento = data_nascimento
        self.__cpf = cpf
        self.__cep = cep
        self.__rua = rua
        self.__bairro = bairro
        self.__cidade = cidade
        self.__estado = estado

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
    def cep(self):
        return self.__cep 

    @cep.setter
    def cep(self, cep):
        self.__cep = cep
    
    @property
    def rua(self):
        return self.__rua 

    @rua.setter
    def rua(self, rua):
        self.__rua = rua

    @property
    def bairro(self):
        return self.__bairro

    @bairro.setter
    def bairro(self, bairro):
        self.__bairro = bairro

    @property
    def cidade(self):
        return self.__cidade

    @cidade.setter
    def cidade(self, cidade):
        self.__cidade = cidade  
    
    @property
    def estado(self):
        return self.__estado

    @estado.setter
    def estado(self, estado):
        self.__estado = estado 