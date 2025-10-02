class Profissional: 
    def __init__(self, id, nome, especialidade, conselho, senha):
        self.set_id(id)
        self.set_nome(nome)
        self.set_especialidade(especialidade)
        self.set_conselho(conselho)
        self.set_senha(senha)
    def set_id(self, valor): 
        if valor < 0: raise ValueError("Valor inválido")
        self.__id = valor
    def set_nome(self, valor): 
        if valor == "": raise ValueError("Valor inválido")
        self.__nome = valor
    def set_especialidade(self, valor): 
        if valor == "": raise ValueError("Valor inválido")
        self.__especialidade = valor
    def set_conselho(self, valor):
        if valor == "": raise ValueError("Valor inválido")
        self.__conselho = valor
    def set_senha(self, valor): 
        if valor == "": raise ValueError("Valor inválido")
        self.__senha = valor
    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_especialidade(self): return self.__especialidade
    def get_conselho(self): return self.__conselho
    def get_senha(self): return self.__senha

    def __str__(self): return f"{self.__id} - {self.__nome} - {self.__especialidade} - {self.__conselho}"

    def to_json(self): 
        dic = {
            "id": self.__id,
            "nome": self.__nome, 
            "especialidade": self.__especialidade,
            "conselho": self.__conselho,
            "senha": self.__senha
        }
        return dic
    
    @staticmethod
    def from_json(dic): 
        return Profissional(dic["id"], dic["nome"], dic["especialidade"], dic["conselho"], dic["senha"])
    

import json
class ProfissionalDAO:
    __objetos = []
    
    @classmethod
    def inserir(cls, obj): 
        cls.abrir()
        id = 0 
        for c in cls.__objetos: 
            if c.get_id() > id: id = c.get_id()
        obj.set_id(id + 1)
        cls.__objetos.append(obj)
        cls.salvar()
    
    @classmethod
    def listar(cls): 
        cls.abrir()
        return cls.__objetos
    
    @classmethod 
    def listar_id(cls, id): 
        cls.abrir()
        for c in cls.__objetos: 
            if c.get_id() == id: return c
        return None
    
    @classmethod
    def atualizar(cls, obj):
        aux = cls.listar_id(obj.get_id())
        if aux != None: 
            cls.__objetos.remove(aux)
            cls.__objetos.append(obj)
            cls.salvar() 
    
    @classmethod 
    def excluir(cls, id): 
        for c in cls.__objetos: 
            if c.get_id() == id:
                cls.__objetos.remove(c)
                cls.salvar()
                break  # importante sair do loop depois de remover

    
    @classmethod
    def abrir(cls): 
        cls.__objetos = []
        try: 
            with open("Profissionais.json", mode = "r") as arquivo:  # arquivo correto para serviços
                list_dic = json.load(arquivo)
                for dic in list_dic: 
                    obj = Profissional.from_json(dic)
                    cls.__objetos.append(obj)
        except FileNotFoundError: 
            pass

    @classmethod
    def salvar(cls):
        with open("Profissionais.json", mode="w") as arquivo:  # arquivo correto para serviços
            json.dump(cls.__objetos, arquivo, default=Profissional.to_json)


