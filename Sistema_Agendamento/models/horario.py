from datetime import datetime
from models.DAO import DAO
class Horario:
    def __init__(self, id, data):
        self.set_id(id)
        self.set_data(data)
        self.set_confirmado(False)
        self.set_id_cliente(0)
        self.set_id_servico(0)
        self.set_id_Profissional(0)

    def __str__(self):
        data_str = self.__data.strftime('%d/%m/%Y %H:%M') if isinstance(self.__data, datetime) else str(self.__data)
        return f"ID - {self.__id} | DATA - {data_str} | CONFIRMADO - {self.__confirmado}"

    # ------------------- MÉTODOS GET -------------------

    def get_id(self): return self.__id
    def get_data(self): return self.__data
    def get_confirmado(self): return self.__confirmado
    def get_id_cliente(self): return self.__id_cliente
    def get_id_servico(self): return self.__id_servico
    def get_id_Profissional(self): return self.__id_Profissional

    # ------------------- MÉTODOS SET -------------------

    def set_id(self, id):
        self.__id = id

    def set_data(self, data):
        if not isinstance(data, datetime):
            raise ValueError("A data deve ser um objeto datetime.")

        if data.year < 2025:
            raise ValueError("Não é permitido cadastrar horários anteriores ao ano de 2025.")
        
        self.__data = data

    def set_confirmado(self, confirmado):
        if not isinstance(confirmado, bool):
            raise ValueError("O campo 'confirmado' deve ser do tipo booleano (True ou False).")
        self.__confirmado = confirmado

    def set_id_cliente(self, id_cliente):
        if id_cliente != None and id_cliente < 0:
            raise ValueError("O ID do cliente não pode ser negativo.")
        self.__id_cliente = id_cliente

    def set_id_servico(self, id_servico):
        if id_servico != None and id_servico < 0:
            raise ValueError("O ID do serviço não pode ser negativo.")
        self.__id_servico = id_servico

    def set_id_Profissional(self, id_Profissional):
        if id_Profissional != None and id_Profissional < 0:
            raise ValueError("O ID do profissional não pode ser negativo.")
        self.__id_Profissional = id_Profissional

    # ------------------- JSON -------------------

    def to_json(self):
        return {
            "id": self.__id,
            "data": self.__data.strftime("%d/%m/%Y %H:%M"),
            "confirmado": self.__confirmado,
            "id_cliente": self.__id_cliente,
            "id_servico": self.__id_servico,
            "id_Profissional": self.__id_Profissional
        }

    @staticmethod
    def from_json(dic):
        horario = Horario(dic["id"], datetime.strptime(dic["data"], "%d/%m/%Y %H:%M"))
        horario.set_confirmado(dic["confirmado"])
        horario.set_id_cliente(dic["id_cliente"])
        horario.set_id_servico(dic["id_servico"])
        horario.set_id_Profissional(dic["id_Profissional"])
        return horario

    
import json
class HorarioDAO(DAO):
    @classmethod
    def abrir(cls):
        cls._objetos = []
        try:
            with open("horarios.json", mode ="r") as arquivo:
                list_dic = json.load(arquivo)
                for dic in list_dic:
                    obj = Horario.from_json(dic)
                    cls._objetos.append(obj)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open("horarios.json", mode ="w") as arquivo:
            json.dump(cls._objetos, arquivo, default = Horario.to_json)