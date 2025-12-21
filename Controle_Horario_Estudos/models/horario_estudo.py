class Cronograma:
    def __init__(self, id, nome, id_usuario):
        self.set_id(id)
        self.set_nome(nome)
        self.set_id_usuario(id_usuario)

    def set_id(self, id):
        self.__id = id

    def set_nome(self, nome):
        if not nome or not nome.strip():
            raise ValueError("O nome do cronograma não pode ser vazio.")
        if len(nome) > 30:
            # Validação baseada no CSV: VARCHAR(30)
            raise ValueError("O nome do cronograma não pode exceder 30 caracteres.")
        self.__nome = nome

    def set_id_usuario(self, id_usuario):
        if id_usuario is None:
            raise ValueError("O cronograma deve estar vinculado a um usuário.")
        self.__id_usuario = int(id_usuario)

    # Getters
    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_id_usuario(self): return self.__id_usuario

    def __str__(self):
        return f"{self.__id} - {self.__nome}"
 
from DAO_sql.DAO import DAO 

class CronogramaDAO(DAO):

    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        sql = """
            INSERT INTO cronograma (nome, id_usuario)
            VALUES (?, ?)
        """
        cls.execute(sql, (obj.get_nome(), obj.get_id_usuario()))
        cls.fechar()

    @classmethod
    def listar(cls):
        cls.abrir()
        sql = "SELECT * FROM cronograma"
        cursor = cls.execute(sql)
        rows = cursor.fetchall()
        
        objs = [Cronograma(id, nome, id_user) for (id, nome, id_user) in rows]
        
        cls.fechar()
        return objs

    @classmethod
    def listar_por_usuario(cls, id_usuario):
        """
        Lista todos os cronogramas de um usuário específico.
        """
        cls.abrir()
        sql = "SELECT * FROM cronograma WHERE id_usuario = ?"
        cursor = cls.execute(sql, (id_usuario,))
        rows = cursor.fetchall()
        
        objs = [Cronograma(id, nome, id_user) for (id, nome, id_user) in rows]
        
        cls.fechar()
        return objs

    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        sql = "SELECT * FROM cronograma WHERE id = ?"
        cursor = cls.execute(sql, (id,))
        row = cursor.fetchone()
        
        obj = Cronograma(*row) if row else None
        
        cls.fechar()
        return obj

    @classmethod
    def atualizar(cls, obj):
        cls.abrir()
        sql = """
            UPDATE cronograma 
            SET nome=?, id_usuario=?
            WHERE id=?
        """
        cls.execute(sql, (obj.get_nome(), obj.get_id_usuario(), obj.get_id()))
        cls.fechar()

    @classmethod
    def excluir(cls, obj):
        cls.abrir()
        sql = "DELETE FROM cronograma WHERE id=?"
        cls.execute(sql, (obj.get_id(),))
        cls.fechar()