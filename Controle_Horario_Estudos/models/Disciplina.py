from DAO_sql.database import Database

class Disciplina:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome

    def get_id(self): return self.id
    def get_nome(self): return self.nome

class DisciplinaDAO(Database):
    
    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        sql = "INSERT INTO disciplina (nome) VALUES (?)"
        cls.execute(sql, (obj.get_nome(),))
        cls.fechar()

    @classmethod
    def listar(cls):
        # Lista TUDO (usado para o cadastro de disciplinas)
        cls.abrir()
        sql = "SELECT * FROM disciplina"
        cursor = cls.execute(sql)
        rows = cursor.fetchall()
        cls.fechar()
        return [Disciplina(row[0], row[1]) for row in rows]

    @classmethod
    def listar_com_professores(cls):
        """
        MÁGICA AQUI: Só retorna disciplinas que têm match com a formação de um professor.
        """
        cls.abrir()
        # O DISTINCT evita que 'Matemática' apareça 2 vezes se tiver 2 professores de Matemática
        sql = """
            SELECT DISTINCT d.id, d.nome 
            FROM disciplina d
            INNER JOIN professor p ON d.nome = p.formacao
        """
        try:
            cursor = cls.execute(sql)
            rows = cursor.fetchall()
            return [Disciplina(row[0], row[1]) for row in rows]
        except Exception as e:
            print(f"Erro ao filtrar disciplinas: {e}")
            return []
        finally:
            cls.fechar()