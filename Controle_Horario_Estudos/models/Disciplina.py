# Importação corrigida conforme sua estrutura de pastas
from DAO_sql.DAO import DAO

class Disciplina:
    def __init__(self, id, nome, id_professor):
        self.set_id(id)
        self.set_nome(nome)
        self.set_id_professor(id_professor)

    def set_id(self, id_cliente):
        self.__id = id_cliente

    def set_nome(self, nome):
        if not nome or not nome.strip():
            raise ValueError("Nome não pode ser vazio")
        self.__nome = nome

    def set_id_professor(self, id):
        if not id: 
            raise ValueError("Professor obrigatório")
        self.__id_professor = int(id)

    # Getters
    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_id_professor(self): return self.__id_professor

    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__id_professor}"


class DisciplinaDAO(DAO):
    
    @classmethod
    def inserir(cls, disciplina):
        cls.abrir()
        sql = "INSERT INTO disciplina (nome, id_professor) VALUES (?, ?)"
        
        params = (disciplina.get_nome(), disciplina.get_id_professor())
        
        cls.execute(sql, params)
        cls.fechar()

    @classmethod
    def listar(cls):
        """ 
        Lista todas as disciplinas do banco e retorna 
        uma lista de OBJETOS da classe Disciplina.
        """
        cls.abrir()
        sql = "SELECT * FROM disciplina"
        
        cursor = cls.execute(sql)
        linhas = cursor.fetchall()
        
        cls.fechar()
        
        objetos = []
        for l in linhas:
            objetos.append(Disciplina(l[0], l[1], l[2]))
        
        return objetos

    @classmethod
    def listar_com_nome_professor(cls):
        """
        Retorna uma lista de DICIONÁRIOS para facilitar o display no Streamlit.
        Faz o JOIN para pegar o nome do professor ao invés do ID.
        """
        cls.abrir()
        sql = """
            SELECT d.id, d.nome, p.nome 
            FROM disciplina d
            INNER JOIN professor p ON d.id_professor = p.id
        """
        cursor = cls.execute(sql)
        linhas = cursor.fetchall()
        cls.fechar()
        
        resultado = []
        for l in linhas:
            resultado.append({
                "id_disciplina": l[0],
                "nome_disciplina": l[1],
                "nome_professor": l[2],
                "display": f"{l[1]} (Prof. {l[2]})"
            })
        return resultado