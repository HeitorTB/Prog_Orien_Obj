import sqlite3

DB_PATH = 'sistema_estudos.db'

class Disciplina:
    # Adicionamos id_professor na classe
    def __init__(self, id, nome, id_professor):
        self.id = id
        self.nome = nome
        self.id_professor = id_professor

    def get_id(self): return self.id
    def get_nome(self): return self.nome
    def get_id_professor(self): return self.id_professor

class DisciplinaDAO:
    @classmethod
    def abrir(cls):
        cls.conn = sqlite3.connect(DB_PATH)
        cls.cursor = cls.conn.cursor()
        
        # Cria a tabela já com a nova coluna id_professor
        cls.cursor.execute("""
            CREATE TABLE IF NOT EXISTS disciplina (
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                nome TEXT NOT NULL,
                id_professor INTEGER,
                FOREIGN KEY(id_professor) REFERENCES professor(id)
            )
        """)
        cls.conn.commit()

    @classmethod
    def fechar(cls):
        cls.conn.commit()
        cls.conn.close()

    @classmethod
    def inserir(cls, disciplina):
        cls.abrir()
        sql = "INSERT INTO disciplina (nome, id_professor) VALUES (?, ?)"
        cls.cursor.execute(sql, (disciplina.nome, disciplina.id_professor))
        cls.fechar()

    @classmethod
    def listar(cls):
        """ Lista todas as disciplinas cadastradas """
        cls.abrir()
        cls.cursor.execute("SELECT * FROM disciplina")
        linhas = cls.cursor.fetchall()
        cls.fechar()
        # linha: (id, nome, id_professor)
        return [Disciplina(l[0], l[1], l[2]) for l in linhas]

    @classmethod
    def listar_com_nome_professor(cls):
        """
        Retorna uma lista especial formatada para o Selectbox do Aluno.
        Ex: "Matemática (Prof. João)"
        """
        cls.abrir()
        sql = """
            SELECT d.id, d.nome, p.nome 
            FROM disciplina d
            INNER JOIN professor p ON d.id_professor = p.id
        """
        cls.cursor.execute(sql)
        linhas = cls.cursor.fetchall()
        cls.fechar()
        
        # Retorna uma lista de dicionários para facilitar na View
        resultado = []
        for l in linhas:
            resultado.append({
                "id_disciplina": l[0],
                "nome_disciplina": l[1],
                "nome_professor": l[2],
                "display": f"{l[1]} (Prof. {l[2]})"
            })
        return resultado