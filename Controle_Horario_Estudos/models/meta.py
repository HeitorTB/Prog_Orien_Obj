from datetime import datetime

class Meta:
    def __init__(self, id, descricao, data_limite, data_conclusao, status, id_usuario):
        self.set_id(id)
        self.set_descricao(descricao)
        self.set_data_limite(data_limite)
        self.set_data_conclusao(data_conclusao)
        self.set_status(status)
        self.set_id_usuario(id_usuario)

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
        # Conforme seu CSV, este campo não pode ser nulo.
        self.__validar_data(data, "Data Conclusão")
        self.__data_conclusao = data

    def set_status(self, valor):
        # Aceita booleano (True/False) ou Inteiro do banco (1/0)
        if isinstance(valor, int):
            self.__status = bool(valor)
        else:
            self.__status = bool(valor)

    def set_id_usuario(self, id_usuario):
        if id_usuario is None:
            raise ValueError("A meta deve estar vinculada a um usuário.")
        self.__id_usuario = int(id_usuario)

    def __validar_data(self, data_str, nome_campo):
        """Valida se a string está no formato YYYY-MM-DD"""
        if not data_str:
            raise ValueError(f"{nome_campo} é obrigatória.")
        try:
            # Tenta converter apenas para validar o formato
            datetime.strptime(data_str, '%Y-%m-%d')
        except ValueError:
            raise ValueError(f"{nome_campo} deve estar no formato AAAA-MM-DD (ex: 2024-12-31).")

    # Getters
    def get_id(self): return self.__id
    def get_descricao(self): return self.__descricao
    def get_data_limite(self): return self.__data_limite
    def get_data_conclusao(self): return self.__data_conclusao
    def get_status(self): return self.__status # Retorna True/False
    def get_status_sql(self): return 1 if self.__status else 0 # Retorna 1/0 para o banco
    def get_id_usuario(self): return self.__id_usuario

    def __str__(self):
        status_str = "Concluída" if self.__status else "Pendente"
        return f"{self.__descricao} (Até: {self.__data_limite}) - {status_str}"

from DAO_sql.DAO import DAO 

class MetaDAO(DAO):

    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        sql = """
            INSERT INTO meta (descricao, data_limite, data_conclusao, status, id_usuario)
            VALUES (?, ?, ?, ?, ?)
        """
        # Note o uso de obj.get_status_sql() para enviar 0 ou 1 ao banco
        cls.execute(sql, (
            obj.get_descricao(), 
            obj.get_data_limite(), 
            obj.get_data_conclusao(), 
            obj.get_status_sql(), 
            obj.get_id_usuario()
        ))
        cls.fechar()

    @classmethod
    def listar(cls):
        cls.abrir()
        sql = "SELECT * FROM meta"
        cursor = cls.execute(sql)
        rows = cursor.fetchall()
        
        # Mapeia as colunas na ordem do CREATE TABLE
        # id, descricao, data_limite, data_conclusao, status, id_usuario
        objs = [Meta(id, desc, dt_lim, dt_conc, status, id_user) 
                for (id, desc, dt_lim, dt_conc, status, id_user) in rows]
        
        cls.fechar()
        return objs

    @classmethod
    def listar_por_usuario(cls, id_usuario):
        cls.abrir()
        sql = "SELECT * FROM meta WHERE id_usuario = ?"
        cursor = cls.execute(sql, (id_usuario,))
        rows = cursor.fetchall()
        
        objs = [Meta(id, desc, dt_lim, dt_conc, status, id_user) 
                for (id, desc, dt_lim, dt_conc, status, id_user) in rows]
        
        cls.fechar()
        return objs

    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        sql = "SELECT * FROM meta WHERE id = ?"
        cursor = cls.execute(sql, (id,))
        row = cursor.fetchone()
        
        obj = Meta(*row) if row else None
        
        cls.fechar()
        return obj

    @classmethod
    def atualizar(cls, obj):
        cls.abrir()
        sql = """
            UPDATE meta 
            SET descricao=?, data_limite=?, data_conclusao=?, status=?, id_usuario=?
            WHERE id=?
        """
        cls.execute(sql, (
            obj.get_descricao(), 
            obj.get_data_limite(), 
            obj.get_data_conclusao(), 
            obj.get_status_sql(),
            obj.get_id_usuario(),
            obj.get_id()
        ))
        cls.fechar()

    @classmethod
    def excluir(cls, obj):
        cls.abrir()
        sql = "DELETE FROM meta WHERE id=?"
        cls.execute(sql, (obj.get_id(),))
        cls.fechar()