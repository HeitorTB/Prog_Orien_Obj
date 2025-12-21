# --- Entidade Disciplina ---
class Disciplina:
    def __init__(self, id, nome):
        self.set_id(id)
        self.set_nome(nome)

    def set_id(self, id_disc):
        self.__id = id_disc

    def set_nome(self, nome):
        if not nome.strip():
            raise ValueError("Nome da disciplina não pode ser vazio")
        self.__nome = nome

    def get_id(self): return self.__id
    def get_nome(self): return self.__nome

    def __str__(self):
        return f"{self.__id} - {self.__nome}"

from DAO_sql.DAO import DAO
# --- DAO Disciplina ---
class DisciplinaDAO(DAO):
    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        sql = "INSERT INTO disciplina (nome) VALUES (?)"
        cls.execute(sql, (obj.get_nome(),))
        cls.fechar()

    @classmethod
    def listar(cls):
        cls.abrir()
        cursor = cls.execute("SELECT * FROM disciplina")
        rows = cursor.fetchall()
        cls.fechar()
        return [Disciplina(*row) for row in rows]

    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        cursor = cls.execute("SELECT * FROM disciplina WHERE id = ?", (id,))
        row = cursor.fetchone()
        cls.fechar()
        return Disciplina(*row) if row else None

    @classmethod
    def atualizar(cls, obj):
        cls.abrir()
        sql = "UPDATE disciplina SET nome=? WHERE id=?"
        cls.execute(sql, (obj.get_nome(), obj.get_id()))
        cls.fechar()

    @classmethod
    def excluir(cls, obj):
        cls.abrir()
        cls.execute("DELETE FROM disciplina WHERE id=?", (obj.get_id(),))
        cls.fechar()