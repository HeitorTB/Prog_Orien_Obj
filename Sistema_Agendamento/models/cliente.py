from models.DAO import DAO
from datetime import datetime
class Cliente:
    def __init__(self, id, nome, email, fone, senha, aniv):
        self.set_id(id)
        self.set_nome(nome)
        self.set_email(email)
        self.set_fone(fone)
        self.set_senha(senha)
        self.set_aniv(aniv)

    def set_id(self, id_cliente):
        self.__id = id_cliente

    def set_nome(self, nome):
        if not nome.strip():
            raise ValueError("Nome não pode ser vazio")
        self.__nome = nome

    def set_aniv(self, aniv):
        dt = datetime.strptime(aniv, '%d/%m/%Y')
        self.__aniv = dt.strftime('%d/%m/%Y')

    def set_email(self, valor):
        if not valor.strip():
            raise ValueError("E-mail não pode ser vazio")
        self.__email = valor

    def set_fone(self, valor):
        if not valor.strip():
            raise ValueError("Telefone não pode ser vazio")
        self.__fone = valor

    def set_senha(self, valor):
        if not valor.strip():
            raise ValueError("Senha não pode ser vazia")
        self.__senha = valor

    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_email(self): return self.__email
    def get_fone(self): return self.__fone
    def get_senha(self): return self.__senha
    def get_aniv(self): return self.__aniv

    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__email} - {self.__fone} - {self.__aniv}"

    def to_json(self):
        return {
            "id": self.__id,
            "nome": self.__nome,
            "email": self.__email,
            "fone": self.__fone,
            "senha": self.__senha,
            "Nascimento": self.__aniv
        }

    @staticmethod
    def from_json(dic):
        return Cliente(dic["id"], dic["nome"], dic["email"], dic["fone"], dic["senha"], dic["Nascimento"])

import json
class ClienteDAO(DAO):
    @classmethod
    def abrir(cls): 
        cls._objetos = []
        try: 
            with open("clientes.json", mode = "r") as arquivo: 
                list_dic = json.load(arquivo)
                for dic in list_dic: 
                    obj = Cliente.from_json(dic)
                    cls._objetos.append(obj)
        except FileNotFoundError: 
            pass

    @classmethod
    def salvar(cls):
        with open("clientes.json", mode="w") as arquivo: 
            json.dump(cls._objetos, arquivo, default=Cliente.to_json)

