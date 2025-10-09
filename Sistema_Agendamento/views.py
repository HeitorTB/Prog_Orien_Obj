from models.cliente import Cliente, ClienteDAO
from models.servico import Servico, ServicoDAO
from models.horario import Horario, HorarioDAO
from models.Profissional import Profissional, ProfissionalDAO

class View:
    def cliente_listar():
        return ClienteDAO.listar()
    
    def cliente_listar_id(id):
        return ClienteDAO.listar_id(id)
    
    def cliente_inserir(nome, email, fone, senha):
        cliente = Cliente(0, nome, email, fone, senha)
        ClienteDAO.inserir(cliente)

    def cliente_atualizar(id, nome, email, fone, senha):
        cliente = Cliente(id, nome, email, fone, senha)
        ClienteDAO.atualizar(cliente)
        
    def cliente_excluir(id):
        ClienteDAO.excluir(id)


    def servico_listar():
        return ServicoDAO.listar()
    
    def servico_listar_id(id):
        return ServicoDAO.listar_id(id)

    def servico_inserir(descricao, valor):
        servico = Servico(0, descricao, valor)
        ServicoDAO.inserir(servico)

    def servico_atualizar(id, descricao, valor):
        servico = Servico(id, descricao, valor)
        ServicoDAO.atualizar(servico)
        
    def servico_excluir(id):
        ServicoDAO.excluir(id)

    def horario_inserir(data, confirmado, id_cliente, id_servico, id_Profissional):
        c = Horario(0, data)
        c.set_confirmado(confirmado)
        c.set_id_cliente(id_cliente)
        c.set_id_servico(id_servico)
        c.set_id_Profissional(id_Profissional)
        HorarioDAO.inserir(c)

    def horario_listar():
        return HorarioDAO.listar()

    def horario_atualizar(id, data, confirmado, id_cliente, id_servico, id_Profissional):
        c = Horario(id, data)
        c.set_confirmado(confirmado)
        c.set_id_cliente(id_cliente)
        c.set_id_servico(id_servico)
        c.set_id_Profissional(id_Profissional)
        HorarioDAO.atualizar(c)

    def horario_excluir(id):
        c = Horario(id, None)
        HorarioDAO.excluir(c)
      
    def Profissional_listar():
        return ProfissionalDAO.listar()
    
    def Profissional_listar_id(id):
        return ProfissionalDAO.listar_id(id)
    
    def Profissional_inserir(nome, especialidade, conselho, senha, email):
        profissional = Profissional(0, nome, especialidade, conselho, senha, email)
        ProfissionalDAO.inserir(profissional)

    def Profissional_atualizar(id, nome, especialidade, conselho, senha, email):
        profissional = Profissional(id, nome, especialidade, conselho, senha, email)
        ProfissionalDAO.atualizar(profissional)
        
    def Profissional_excluir(id):
        ProfissionalDAO.excluir(id)
    
    def cliente_criar_admin():
        for c in View.cliente_listar():
            if c.get_email() == "admin": return
        View.cliente_inserir("admin", "admin", "fone", "1234")
    
    def cliente_autenticar(email, senha): 
        for c in View.cliente_listar():
            if c.get_email() == email and c.get_senha() == senha:
                return  {"id": c.get_id(), "nome": c.get_nome()}
        return None
    
    def profissional_autenticar(email, senha): 
        for c in View.Profissional_listar():
            if c.get_email() == email and c.get_senha() == senha:
                return  {"id": c.get_id(), "nome": c.get_nome()}
        return None

