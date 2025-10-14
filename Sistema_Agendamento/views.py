from models.cliente import Cliente, ClienteDAO
from models.servico import Servico, ServicoDAO
from models.horario import Horario, HorarioDAO
from models.Profissional import Profissional, ProfissionalDAO
import streamlit as st
from datetime import datetime, timedelta

class View:
    def cliente_listar():
        r = ClienteDAO.listar()
        r.sort(key= lambda obj : obj.get_nome())
        return r
    
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
        r = ServicoDAO.listar()
        r.sort(key = lambda obj : obj.get_descricao())
        return r
    
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
        r= HorarioDAO.listar()
        r.sort(key= lambda obj : obj.get_data())
        return r

    def horario_filtrar_profissional(id_profissional):
        r = []
        for h in View.horario_listar():
            if h.get_id_profissional() == id_profissional:
                r.append(h)
        return r

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
    
    def horario_agendar_horario(id_profissional):
        r = []
        agora = datetime.now()
        for h in View.horario_listar():
            if h.get_data() >= agora and h.get_confirmado() == False and h.get_id_cliente() == None and h.get_id_profissional() == id_profissional: 
                r.append(h)
        r.sort(key = lambda h : h.get_data())
        return r
      
    def Profissional_listar():
        r = ProfissionalDAO.listar()
        r.sort(key = lambda obj : obj.get_nome())
        return r
    
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

    def Profissional_Agendar(data, horarioI, horarioF, intervalo, id_profissional): 
        primeiro_horario = datetime.strptime(data +  " " + horarioI, '%d/%m/%Y %H:%M')
        ultimo_horario = datetime.strptime(data + ' ' + horarioF, '%d/%m/%Y %H:%M')
        intervalo_min = timedelta(minutes=intervalo)
        y = ultimo_horario
        x = primeiro_horario
        while x <= y: 
            View.horario_inserir(x, False, None, None, id_profissional)
            x = x + intervalo_min
            print(x)


