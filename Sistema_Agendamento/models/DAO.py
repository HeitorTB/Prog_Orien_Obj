from abc import ABC, abstractmethod

class DAO(ABC):
    _objetos = []

    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        id = 0
        for aux in cls._objetos:
            if aux.get_id() > id: id = aux.get_id()
        obj.set_id(id + 1)
        cls._objetos.append(obj)
        cls.salvar()
    
    @classmethod
    def listar(cls): 
        cls.abrir()
        return cls._objetos
    
    @classmethod
    def listar_id(cls,id):
        cls.abrir()
        for obj in cls._objetos:
            if obj.get_id() == id: return obj
        return None
    
    @classmethod
    def excluir(cls, obj):
        aux = cls.listar_id(obj.get_id())
        if aux != None:
            cls._objetos.remove(aux)
            cls.salvar()
    
    @classmethod
    def atualizar(cls, obj):
        cls.abrir()
        for i, aux in enumerate(cls._objetos):
            if aux.get_id() == obj.get_id():
                cls._objetos[i] = obj
                cls.salvar()
                return
        raise ValueError(f"Horário com id {obj.get_id()} não encontrado")

    @classmethod
    @abstractmethod
    def abrir(cls):
        pass

    @classmethod
    @abstractmethod
    def salvar(cls):
        pass