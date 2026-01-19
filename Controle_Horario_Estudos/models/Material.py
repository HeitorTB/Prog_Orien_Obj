# --- Entidade Material ---
class Material:
    def __init__(self, id, titulo, descricao, id_professor, id_meta):
        self.set_id(id)
        self.set_titulo(titulo)
        self.set_descricao(descricao)
        self.set_id_professor(id_professor)
        self.set_id_meta(id_meta)

    def set_id(self, id_mat):
        self.__id = id_mat

    def set_titulo(self, titulo):
        if not titulo.strip(): raise ValueError("Título não pode ser vazio")
        self.__titulo = titulo

    def set_descricao(self, desc):
        if not desc.strip(): raise ValueError("Descrição não pode ser vazia")
        self.__descricao = desc

    def set_id_professor(self, id_prof):
        self.__id_professor = id_prof

    def set_id_meta(self, id_meta):
        self.__id_meta = id_meta

    def get_id(self): return self.__id
    def get_titulo(self): return self.__titulo
    def get_descricao(self): return self.__descricao
    def get_id_professor(self): return self.__id_professor
    def get_id_meta(self): return self.__id_meta

    def __str__(self):
        return f"{self.__id} - {self.__titulo} (Prof: {self.__id_professor})"

from DAO_sql.DAO import DAO
class MaterialDAO(DAO):
    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        sql = """
            INSERT INTO material (titulo, descricao, id_professor, id_meta)
            VALUES (?, ?, ?, ?)
        """
        cls.execute(sql, (obj.get_titulo(), obj.get_descricao(), obj.get_id_professor(), obj.get_id_meta()))
        cls.fechar()

    @classmethod
    def listar(cls):
        cls.abrir()
        sql = "SELECT * FROM material"
        cursor = cls.execute(sql)
        rows = cursor.fetchall()
        
        objs = [Material(id, titulo, desc, id_prof, id_meta) for (id, titulo, desc, id_prof, id_meta) in rows]
        
        cls.fechar()
        return objs

    @classmethod
    def listar_por_meta(cls, id_meta_filtro):
        """ Método extra útil: listar materiais de uma meta específica """
        cls.abrir()
        sql = "SELECT * FROM material WHERE id_meta = ?"
        cursor = cls.execute(sql, (id_meta_filtro,))
        rows = cursor.fetchall()
        objs = [Material(*row) for row in rows]
        cls.fechar()
        return objs

    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        cursor = cls.execute("SELECT * FROM material WHERE id = ?", (id,))
        row = cursor.fetchone()
        obj = Material(*row) if row else None
        cls.fechar()
        return obj

    @classmethod
    def atualizar(cls, obj):
        cls.abrir()
        sql = """
            UPDATE material SET titulo=?, descricao=?, id_professor=?, id_meta=?
            WHERE id=?
        """
        cls.execute(sql, (obj.get_titulo(), obj.get_descricao(), obj.get_id_professor(), obj.get_id_meta(), obj.get_id()))
        cls.fechar()

    @classmethod
    def excluir(cls, obj):
        cls.abrir()
        cls.execute("DELETE FROM material WHERE id=?", (obj.get_id(),))
        cls.fechar()