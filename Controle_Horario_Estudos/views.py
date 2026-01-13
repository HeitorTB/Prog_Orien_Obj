from models.Aluno import aluno, alunoDAO
from models.Professor import Professor, ProfessorDAO
from models.Disciplina import Disciplina, DisciplinaDAO
from models.meta import Meta, MetaDAO
from models.horario_estudo import Cronograma, CronogramaDAO
from models.Material import Material, MaterialDAO

class View:
    # ----------------------------------------------------
    # MÉTODOS DE USUÁRIO (ALUNO / PROFESSOR)
    # ----------------------------------------------------
    @staticmethod
    def aluno_autenticar(email, senha):
        for a in alunoDAO.listar():
            if a.get_email() == email and a.get_senha() == senha:
                return {"id": a.get_id(), "nome": a.get_nome(), "tipo": "aluno"}
        return None

    @staticmethod
    def aluno_inserir(nome, email, senha):
        for a in alunoDAO.listar():
            if a.get_email() == email: raise ValueError("E-mail já cadastrado.")
        obj = aluno(None, nome, email, senha)
        alunoDAO.inserir(obj)

    @staticmethod
    def professor_autenticar(email, senha):
        for p in ProfessorDAO.listar():
            if p.get_email() == email and p.get_senha() == senha:
                return {"id": p.get_id(), "nome": p.get_nome(), "tipo": "professor"}
        return None

    @staticmethod
    def professor_inserir(nome, email, senha, formacao):
        for p in ProfessorDAO.listar():
            if p.get_email() == email: raise ValueError("E-mail já cadastrado.")
        obj = Professor(None, nome, email, senha, formacao)
        ProfessorDAO.inserir(obj)

    @staticmethod
    def aluno_listar():
        return alunoDAO.listar()
    
    # ----------------------------------------------------
    # MÉTODOS DE DISCIPLINA
    # ----------------------------------------------------
    @staticmethod
    def disciplina_listar():
        return DisciplinaDAO.listar()

    @staticmethod
    def disciplina_inserir(nome):
        if not nome: raise ValueError("Nome inválido")
        obj = Disciplina(None, nome)
        DisciplinaDAO.inserir(obj)

    # ----------------------------------------------------
    # MÉTODOS DE META (CORRIGIDO)
    # ----------------------------------------------------
    @staticmethod
    def meta_listar_aluno(id_aluno):
        # We use the method we defined in MetaDAO
        return MetaDAO.listar_por_usuario(id_aluno)
    
    @staticmethod
    def meta_listar_todas():
        return MetaDAO.listar()

    @staticmethod
    def meta_inserir(descricao, data_limite, id_disciplina, id_aluno):
        """
        FIXED: Now passes all required arguments to Meta constructor.
        Order: id, descricao, data_limite, data_conclusao, status, id_disciplina, id_aluno
        """
        # 1. Validate inputs
        if not id_disciplina:
            raise ValueError("É necessário selecionar uma disciplina.")
            
        # 2. Create Object (passing id_disciplina and id_aluno)
        obj = Meta(
            None,           # id (Auto)
            descricao,      # descricao
            data_limite,    # data_limite
            None,           # data_conclusao (starts empty)
            0,              # status (0 = Pending)
            id_disciplina,  # <--- WAS MISSING
            id_aluno        # <--- WAS MISSING
        )
        
        # 3. Call DAO
        MetaDAO.inserir(obj)

    # ----------------------------------------------------
    # MÉTODOS DE HORÁRIO (CORRIGIDO)
    # ----------------------------------------------------
    @staticmethod
    def horario_listar(id_aluno):
        return CronogramaDAO.listar_por_aluno(id_aluno)

    @staticmethod
    def horario_inserir(inicio, fim, id_aluno, id_meta):
        if str(inicio) >= str(fim): raise ValueError("Início deve ser antes do Fim")
        
        # FIXED: Was 'obj = CronogramaDAO(...)', changed to 'obj = Cronograma(...)'
        obj = Cronograma(None, str(inicio), str(fim), id_aluno, id_meta)
        CronogramaDAO.inserir(obj)

    # ----------------------------------------------------
    # MÉTODOS DE MATERIAL
    # ----------------------------------------------------
    @staticmethod
    def material_inserir(titulo, descricao, id_prof, id_meta):
        if not id_meta: raise ValueError("Selecione uma meta vinculada")
        obj = Material(None, titulo, descricao, id_prof, id_meta)
        MaterialDAO.inserir(obj)

    # ----------------------------------------------------
    # NOVO: MÉTODOS PARA O ALUNO (Materiais e Conclusão)
    # ----------------------------------------------------

    @staticmethod
    def material_listar_por_meta(id_meta):
        """ Retorna a lista de materiais de estudo para aquela meta """
        return MaterialDAO.listar_por_meta(id_meta)

    @staticmethod
    def meta_concluir(id_meta):
        """ Marca a meta como finalizada """
        if not id_meta:
            raise ValueError("ID da meta inválido.")
        MetaDAO.marcar_concluida(id_meta)

    @staticmethod
    def disciplina_listar_validas():
        """ Retorna apenas disciplinas que têm professor """
        return DisciplinaDAO.listar_com_professores()
    