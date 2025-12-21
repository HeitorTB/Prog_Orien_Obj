from datetime import datetime
from models.DAO import DAO
class Profissional:
    def __init__(self, id, nome, especialidade, conselho, senha, email, aniv):
        self.set_id(id)
        self.set_nome(nome)
        self.set_especialidade(especialidade)
        self.set_conselho(conselho)
        self.set_senha(senha)
        self.set_email(email)
        self.set_aniv(aniv)

    # --------- SETTERS ---------
    def set_id(self, id):
        self.__id = id

    def set_nome(self, valor):
        if not valor.strip():
            raise ValueError("Nome não pode ser vazio.")
        self.__nome = valor

    def set_especialidade(self, valor):
        # Pode ser opcional, então não lança exceção
        self.__especialidade = valor.strip() if valor else ""

    def set_conselho(self, valor):
        # Pode ser opcional também
        self.__conselho = valor.strip() if valor else ""

    def set_senha(self, valor):
        if not valor.strip():
            raise ValueError("Senha não pode ser vazia.")
        self.__senha = valor

    def set_email(self, valor):
        if not valor.strip():
            raise ValueError("E-mail não pode ser vazio.")
        self.__email = valor

    def set_aniv(self, dt):
        dt = datetime.strptime(dt, '%d/%m/%Y')
        self.__aniv = dt.strftime('%d/%m/%Y')


    # --------- GETTERS ---------
    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_especialidade(self): return self.__especialidade
    def get_conselho(self): return self.__conselho
    def get_senha(self): return self.__senha
    def get_email(self): return self.__email
    def get_aniv(self): return self.__aniv

    # --------- OUTROS MÉTODOS ---------
    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__especialidade} - {self.__conselho}"

    def to_json(self):
        return {
            "id": self.__id,
            "nome": self.__nome,
            "especialidade": self.__especialidade,
            "conselho": self.__conselho,
            "senha": self.__senha,
            "email": self.__email,
            "Nascimento": self.__aniv
        }

    @staticmethod
    def from_json(dic):
        return Profissional(
            dic["id"], dic["nome"], dic["especialidade"],
            dic["conselho"], dic["senha"], dic["email"], dic["Nascimento"]
        )
    

import json
class ProfissionalDAO(DAO):
    @classmethod
    def abrir(cls): 
        cls._objetos = []
        try: 
            with open("Profissionais.json", mode = "r") as arquivo: 
                list_dic = json.load(arquivo)
                for dic in list_dic: 
                    obj = Profissional.from_json(dic)
                    cls._objetos.append(obj)
        except FileNotFoundError: 
            pass

    @classmethod
    def salvar(cls):
        with open("Profissionais.json", mode="w") as arquivo:  
            json.dump(cls._objetos, arquivo, default=Profissional.to_json)


