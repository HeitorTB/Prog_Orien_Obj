from models.Aluno import aluno, alunoDAO
from models.Professor import Professor, ProfessorDAO
from models.Disciplina import Disciplina, DisciplinaDAO
from models.meta import Meta, MetaDAO
from models.horario_estudo import Cronograma, CronogramaDAO 
from models.Material import Material, MaterialDAO

class View:
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

    @staticmethod
    def aluno_excluir(id):
        alunoDAO.excluir(id)

    @staticmethod
    def professor_listar():
        return ProfessorDAO.listar()

    @staticmethod
    def professor_excluir(id):
        ProfessorDAO.excluir(id)

    @staticmethod
    def disciplina_inserir(nome, id_professor):
        if not nome: raise ValueError("O nome da disciplina é obrigatório")
        obj = Disciplina(0, nome, id_professor)
        DisciplinaDAO.inserir(obj)

    @staticmethod
    def disciplina_listar_para_select():
        return DisciplinaDAO.listar_com_nome_professor()
    
    @staticmethod
    def disciplina_listar():
        return DisciplinaDAO.listar()

    @staticmethod
    def meta_listar_aluno(id_aluno):
        return MetaDAO.listar_por_usuario(id_aluno)

    @staticmethod
    def meta_listar_pendentes(id_aluno):
        return MetaDAO.listar_pendentes_por_aluno(id_aluno)

    @staticmethod
    def meta_inserir(descricao, data_limite, id_disciplina, id_aluno):
        if not id_disciplina: raise ValueError("É necessário selecionar uma disciplina.")
        obj = Meta(
            id=0,
            descricao=descricao,
            data_limite=data_limite,
            data_conclusao=None,
            status=0, 
            id_disciplina=id_disciplina,
            id_aluno=id_aluno
        )
        MetaDAO.inserir(obj)

    @staticmethod
    def meta_concluir(id_meta):
        if not id_meta: raise ValueError("ID da meta inválido.")
        MetaDAO.marcar_concluida(id_meta)
    
    @staticmethod
    def meta_listar_geral():
        return MetaDAO.listar_todas()

    @staticmethod
    def material_inserir(titulo, descricao, id_prof, id_meta):
        if not id_meta: raise ValueError("Selecione uma meta vinculada")
        obj = Material(0, titulo, descricao, id_prof, id_meta)
        MaterialDAO.inserir(obj)

    @staticmethod
    def material_listar_por_meta(id_meta):
        return MaterialDAO.listar_por_meta(id_meta)
    
    @staticmethod
    def horario_listar(id_aluno):
        return CronogramaDAO.listar_por_aluno(id_aluno)

    @staticmethod
    def horario_inserir(inicio, fim, id_aluno, id_meta):
        if str(inicio) >= str(fim): raise ValueError("Hora de Início deve ser antes do Fim")
        
        obj = Cronograma(0, str(inicio), str(fim), id_aluno, id_meta)
        CronogramaDAO.inserir(obj)