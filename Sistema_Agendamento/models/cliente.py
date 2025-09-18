class Cliente: 
    def __init__(self, id, nome, email, fone):
        self.set_id(id) 
        self.set_nome(nome)
        self.set_email(email) 
        self.set_fone(fone)

    def set_id(self, valor): 
        if valor < 0: raise ValueError("Valor inváido")
        self.__id = valor 
    def set_nome(self, nome): 
        if nome == "": raise ValueError("Valor inválido")
        self.__nome = nome
    def set_email(self, valor): 
        if valor == "": raise ValueError("Valor inválido")
        self.__email = valor 
    def set_fone(self, valor): 
        if valor == "": raise ValueError("Valor inválido")
        self.__fone = valor

    def get_id(self): return self.__id
    def get_nome(self): return self.__nome 
    def get_email(self): return self.__email
    def get_fone(self): return self.__fone

    def __str__(self): return f"{self.__id}-{self.__nome}-{self.__email}–{self.__fone}"

    def to_json(self): 
        dic = {
            "id": self.__id,
            "nome": self.__nome, 
            "email": self.__email, 
            "fone": self.__fone
        }
        return dic
    
    @staticmethod
    def from_json(dic): 
        return Cliente(dic["id"], dic["nome"], dic["email"], dic["fone"])

import json
class ClienteDAO:
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
                break  # Sai do loop depois de remover

    @classmethod
    def abrir(cls): 
        cls.__objetos = []
        try: 
            with open("clientes.json", mode = "r") as arquivo: 
                list_dic = json.load(arquivo)
                for dic in list_dic: 
                    obj = Cliente.from_json(dic)
                    cls.__objetos.append(obj)
        except FileNotFoundError: 
            pass

    @classmethod
    def salvar(cls):
        with open("clientes.json", mode="w") as arquivo: 
            json.dump(cls.__objetos, arquivo, default=Cliente.to_json)

