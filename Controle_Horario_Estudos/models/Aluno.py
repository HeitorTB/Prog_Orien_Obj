class aluno:
    def __init__(self, id, nome, email, senha):
        self.set_id(id)
        self.set_nome(nome)
        self.set_email(email)
        self.set_senha(senha)

    def set_id(self, id_cliente):
        self.__id = id_cliente

    def set_nome(self, nome):
        if not nome.strip():
            raise ValueError("Nome não pode ser vazio")
        self.__nome = nome

    def set_email(self, valor):
        if not valor.strip():
            raise ValueError("E-mail não pode ser vazio")
        self.__email = valor

    def set_senha(self, valor):
        if not valor.strip():
            raise ValueError("Senha não pode ser vazia")
        self.__senha = valor

    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_email(self): return self.__email
    def get_senha(self): return self.__senha

    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__email}"
    
from DAO_sql.DAO import DAO

class alunoDAO(DAO): 

    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        sql = """
            INSERT INTO aluno (nome, email, senha)
            VALUES (?, ?, ?)
        """
        cls.execute(sql, (obj.get_nome(), obj.get_email(), obj.get_senha()))
        cls.fechar()

    @classmethod
    def listar(cls):
        cls.abrir()
        sql = "SELECT * FROM aluno"
    
        cursor = cls.execute(sql) 
        rows = cursor.fetchall()
        
        objs = [aluno(id, nome, email, senha) for (id, nome, email, senha) in rows]
        
        cls.fechar()
        return objs

    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        sql = "SELECT * FROM aluno WHERE id = ?"
        cursor = cls.execute(sql, (id,))
        row = cursor.fetchone()
    
        obj = aluno(*row) if row else None
        
        cls.fechar()
        return obj

    @classmethod
    def atualizar(cls, obj):
        cls.abrir()
        sql = """
            UPDATE aluno SET nome=?, email=?, senha=?
            WHERE id=?
        """
        cls.execute(sql, (obj.get_nome(), obj.get_email(), obj.get_senha(), obj.get_id()))
        cls.fechar()

    @classmethod
    def excluir(cls, obj):
        cls.abrir()
        sql = "DELETE FROM aluno WHERE id=?"
        cls.execute(sql, (obj.get_id(),))
        cls.fechar()


