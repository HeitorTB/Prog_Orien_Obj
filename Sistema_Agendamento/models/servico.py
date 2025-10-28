class Servico: 
    def __init__(self, id, descricao, valor):
        if descricao == "": raise ValueError("Descrição Inválida")
        if valor < 0: raise ValueError("Valor Inválido")
        self.set_id(id)
        self.set_descricao(descricao)
        self.set_valor(valor)
    def set_id(self, valor): 
        if valor < 0: raise ValueError("Valor inválido")
        self.__id = valor
    def set_descricao(self, valor): 
        if valor == "": raise ValueError("Valor inválido")
        self.__descricao = valor
    def set_valor(self, valor): 
        if valor < 0: raise ValueError("Valor inválido")
        self.__valor = valor
    def get_id(self): return self.__id
    def get_descricao(self): return self.__descricao
    def get_valor(self): return self.__valor

    def __str__(self): return f"{self.__id}-{self.__descricao}-{self.__valor}"

    def to_json(self): 
        dic = {
            "id": self.__id,
            "descricao": self.__descricao, 
            "valor": self.__valor, 
        }
        return dic
    
    @staticmethod
    def from_json(dic): 
        return Servico(dic["id"], dic["descricao"], dic["valor"])
    

import json
class ServicoDAO:
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
            with open("servicos.json", mode = "r") as arquivo:  # arquivo correto para serviços
                list_dic = json.load(arquivo)
                for dic in list_dic: 
                    obj = Servico.from_json(dic)
                    cls.__objetos.append(obj)
        except FileNotFoundError: 
            pass

    @classmethod
    def salvar(cls):
        with open("servicos.json", mode="w") as arquivo:  # arquivo correto para serviços
            json.dump(cls.__objetos, arquivo, default=Servico.to_json)


