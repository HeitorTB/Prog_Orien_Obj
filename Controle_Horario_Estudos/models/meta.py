from datetime import datetime
# Ensure this import path matches your project structure
from DAO_sql.database import Database as DAO 

class Meta:
    def __init__(self, id, descricao, data_limite, data_conclusao, status, id_disciplina, id_aluno):
        self.set_id(id)
        self.set_descricao(descricao)
        self.set_data_limite(data_limite)
        self.set_data_conclusao(data_conclusao)
        self.set_status(status)
        self.set_id_disciplina(id_disciplina) # Added this
        self.set_id_aluno(id_aluno)           # Renamed from id_usuario

    def set_id(self, id):
        self.__id = id

    def set_descricao(self, descricao):
        if not descricao or not descricao.strip():
            raise ValueError("A descrição da meta não pode ser vazia.")
        if len(descricao) > 150:
            raise ValueError("A descrição não pode exceder 150 caracteres.")
        self.__descricao = descricao

    def set_data_limite(self, data):
        self.__validar_data(data, "Data Limite")
        self.__data_limite = data

    def set_data_conclusao(self, data):
        # Assuming data_conclusao can be None if not finished, 
        # but your DB creates it as text. If it is optional in logic, adjust here.
        if data: 
            self.__validar_data(data, "Data Conclusão")
        self.__data_conclusao = data

    def set_status(self, valor):
        if isinstance(valor, int):
            self.__status = bool(valor)
        else:
            self.__status = bool(valor)

    def set_id_disciplina(self, id_disciplina):
        if id_disciplina is None:
            raise ValueError("A meta deve estar vinculada a uma disciplina.")
        self.__id_disciplina = int(id_disciplina)

    def set_id_aluno(self, id_aluno):
        if id_aluno is None:
            raise ValueError("A meta deve estar vinculada a um aluno.")
        self.__id_aluno = int(id_aluno)

    def __validar_data(self, data_str, nome_campo):
        if not data_str:
            return # Allow empty dates if logic permits
        try:
            datetime.strptime(data_str, '%Y-%m-%d')
        except ValueError:
            raise ValueError(f"{nome_campo} deve estar no formato AAAA-MM-DD (ex: 2024-12-31).")

    # Getters
    def get_id(self): return self.__id
    def get_descricao(self): return self.__descricao
    def get_data_limite(self): return self.__data_limite
    def get_data_conclusao(self): return self.__data_conclusao
    def get_status(self): return self.__status
    def get_status_sql(self): return 1 if self.__status else 0
    def get_id_disciplina(self): return self.__id_disciplina
    def get_id_aluno(self): return self.__id_aluno

    def __str__(self):
        status_str = "Concluída" if self.__status else "Pendente"
        return f"{self.__descricao} (Até: {self.__data_limite}) - {status_str}"


class MetaDAO(DAO):
    
    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        # Fixed: Added id_disciplina and changed id_usuario to id_aluno
        sql = """
            INSERT INTO meta (descricao, data_limite, data_conclusao, status, id_disciplina, id_aluno)
            VALUES (?, ?, ?, ?, ?, ?)
        """
        try:
            cls.execute(sql, (
                obj.get_descricao(), 
                obj.get_data_limite(), 
                obj.get_data_conclusao(), 
                obj.get_status_sql(), 
                obj.get_id_disciplina(),
                obj.get_id_aluno()
            ))
        except Exception as e:
            print(f"Erro ao inserir: {e}")
        finally:
            cls.fechar()

    @classmethod
    def listar(cls):
        cls.abrir()
        sql = "SELECT * FROM meta"
        cursor = cls.execute(sql)
        rows = cursor.fetchall()
        
        # Mapeia as 7 colunas do banco
        objs = []
        for row in rows:
            # row structure: (id, descricao, data_limite, data_conclusao, status, id_disciplina, id_aluno)
            objs.append(Meta(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
        
        cls.fechar()
        return objs

    @classmethod
    def listar_por_usuario(cls, id_aluno):
        # Kept method name for compatibility with your view, but logic uses id_aluno
        cls.abrir()
        # Fixed: WHERE id_aluno = ?
        sql = "SELECT * FROM meta WHERE id_aluno = ?"
        cursor = cls.execute(sql, (id_aluno,))
        rows = cursor.fetchall()
        
        objs = []
        for row in rows:
            objs.append(Meta(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
        
        cls.fechar()
        return objs
    
    @classmethod
    def marcar_concluida(cls, id_meta):
        """
        Atualiza o status para 1 (Concluído) e define a data de conclusão para hoje.
        """
        from datetime import datetime
        data_hoje = datetime.now().strftime('%Y-%m-%d')
        
        cls.abrir()
        sql = "UPDATE meta SET status = 1, data_conclusao = ? WHERE id = ?"
        cls.execute(sql, (data_hoje, id_meta))
        cls.fechar()

    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        sql = "SELECT * FROM meta WHERE id = ?"
        cursor = cls.execute(sql, (id,))
        row = cursor.fetchone()
        
        obj = None
        if row:
            obj = Meta(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
        
        cls.fechar()
        return obj

    @classmethod
    def atualizar(cls, obj):
        cls.abrir()
        # Fixed: Added id_disciplina and changed id_usuario to id_aluno
        sql = """
            UPDATE meta 
            SET descricao=?, data_limite=?, data_conclusao=?, status=?, id_disciplina=?, id_aluno=?
            WHERE id=?
        """
        cls.execute(sql, (
            obj.get_descricao(), 
            obj.get_data_limite(), 
            obj.get_data_conclusao(), 
            obj.get_status_sql(),
            obj.get_id_disciplina(),
            obj.get_id_aluno(),
            obj.get_id()
        ))
        cls.fechar()

    @classmethod
    def excluir(cls, obj):
        cls.abrir()
        sql = "DELETE FROM meta WHERE id=?"
        # Assuming obj is an instance, otherwise if passing ID directly, adjust here
        id_to_delete = obj.get_id() if isinstance(obj, Meta) else obj
        cls.execute(sql, (id_to_delete,))
        cls.fechar()