from DAO_sql.DAO import DAO

class Cronograma:
    def __init__(self, id, data_hora_inicio, data_hora_fim, id_aluno, id_meta):
        self.set_id(id)
        self.set_data_hora_inicio(data_hora_inicio)
        self.set_data_hora_fim(data_hora_fim)
        self.set_id_aluno(id_aluno)
        self.set_id_meta(id_meta)

    # --- Setters ---
    def set_id(self, id):
        self.__id = id

    def set_data_hora_inicio(self, data):
        if not data: raise ValueError("Data/Hora de início é obrigatória")
        self.__data_hora_inicio = data

    def set_data_hora_fim(self, data):
        if not data: raise ValueError("Data/Hora de fim é obrigatória")
        self.__data_hora_fim = data

    def set_id_aluno(self, id):
        if not id: raise ValueError("Aluno obrigatório")
        self.__id_aluno = int(id)

    def set_id_meta(self, id):
        if not id: raise ValueError("Meta obrigatória")
        self.__id_meta = int(id)

    def get_id(self): return self.__id
    def get_data_hora_inicio(self): return self.__data_hora_inicio
    def get_data_hora_fim(self): return self.__data_hora_fim
    def get_id_aluno(self): return self.__id_aluno
    def get_id_meta(self): return self.__id_meta

    def get_inicio(self): 
        return self.__data_hora_inicio
        
    def get_fim(self): 
        return self.__data_hora_fim
        
    def get_nome(self):
        return f"Estudo: {self.__data_hora_inicio}"

    def __str__(self):
        return f"Estudo: {self.__data_hora_inicio} até {self.__data_hora_fim}"


class CronogramaDAO(DAO):
    
    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        sql = """
            INSERT INTO horario_estudo (data_hora_inicio, data_hora_fim, id_aluno, id_meta)
            VALUES (?, ?, ?, ?)
        """
        try:
            cls.execute(sql, (
                obj.get_data_hora_inicio(),
                obj.get_data_hora_fim(),
                obj.get_id_aluno(),
                obj.get_id_meta()
            ))
        except Exception as e:
            print(f"Erro ao inserir horário: {e}")
        finally:
            cls.fechar()

    @classmethod
    def listar_por_aluno(cls, id_aluno):
        cls.abrir()
        sql = "SELECT * FROM horario_estudo WHERE id_aluno = ?"
        
        try:
            cursor = cls.execute(sql, (id_aluno,))
            rows = cursor.fetchall()
            
            objetos = []
            for row in rows:
                c = Cronograma(row[0], row[1], row[2], row[3], row[4])
                objetos.append(c)
            
            return objetos
        except Exception as e:
            print(f"Erro ao listar horários: {e}")
            return []
        finally:
            cls.fechar()

    @classmethod
    def excluir(cls, id_horario):
        cls.abrir()
        sql = "DELETE FROM horario_estudo WHERE id = ?"
        cls.execute(sql, (id_horario,))
        cls.fechar()