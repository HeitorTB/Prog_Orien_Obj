# --- Entidade Professor ---
class Professor:
    def __init__(self, id, nome, email, senha, formacao):
        self.set_id(id)
        self.set_nome(nome)
        self.set_email(email)
        self.set_senha(senha)
        self.set_formacao(formacao)

    def set_id(self, id_prof):
        self.__id = id_prof

    def set_nome(self, nome):
        if not nome.strip(): raise ValueError("Nome inválido")
        self.__nome = nome

    def set_email(self, email):
        if not email.strip(): raise ValueError("Email inválido")
        self.__email = email

    def set_senha(self, senha):
        if not senha.strip(): raise ValueError("Senha inválida")
        self.__senha = senha

    def set_formacao(self, formacao):
        if not formacao.strip(): raise ValueError("Formação inválida")
        self.__formacao = formacao

    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_email(self): return self.__email
    def get_senha(self): return self.__senha
    def get_formacao(self): return self.__formacao

    def __str__(self):
        return f"{self.__id} - {self.__nome} ({self.__formacao})"

# --- DAO Professor ---
from DAO_sql.DAO import DAO

class ProfessorDAO(DAO):
    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        sql = "INSERT INTO professor (nome, email, senha, formacao) VALUES (?, ?, ?, ?)"
        cls.execute(sql, (obj.get_nome(), obj.get_email(), obj.get_senha(), obj.get_formacao()))
        cls.fechar()

    @classmethod
    def listar(cls):
        cls.abrir()
        cursor = cls.execute("SELECT * FROM professor")
        rows = cursor.fetchall()
        cls.fechar()
        return [Professor(*row) for row in rows]

    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        cursor = cls.execute("SELECT * FROM professor WHERE id = ?", (id,))
        row = cursor.fetchone()
        cls.fechar()
        return Professor(*row) if row else None

    @classmethod
    def atualizar(cls, obj):
        cls.abrir()
        sql = "UPDATE professor SET nome=?, email=?, senha=?, formacao=? WHERE id=?"
        cls.execute(sql, (obj.get_nome(), obj.get_email(), obj.get_senha(), obj.get_formacao(), obj.get_id()))
        cls.fechar()

    @classmethod
    def excluir(cls, obj):
        cls.abrir()
        cls.execute("DELETE FROM professor WHERE id=?", (obj.get_id(),))
        cls.fechar()