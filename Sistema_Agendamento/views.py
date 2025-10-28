from models.cliente import Cliente, ClienteDAO
from models.servico import Servico, ServicoDAO
from models.horario import Horario, HorarioDAO
from models.Profissional import Profissional, ProfissionalDAO
import streamlit as st
from datetime import datetime, timedelta

class View:

    # ---------------------- CLIENTE ----------------------

    def cliente_listar():
        r = ClienteDAO.listar()
        r.sort(key=lambda obj: obj.get_nome())
        return r

    def cliente_listar_id(id):
        return ClienteDAO.listar_id(id)

    def cliente_inserir(nome, email, fone, senha):
        for c in ClienteDAO.listar():
            if c.get_email().lower() == email.lower():
                raise ValueError("Já existe um cliente com este e-mail.")

        for p in ProfissionalDAO.listar():
            if p.get_email().lower() == email.lower():
                raise ValueError("Já existe um profissional com este e-mail.")

        cliente = Cliente(0, nome, email, fone, senha)
        ClienteDAO.inserir(cliente)

    def cliente_atualizar(id, nome, email, fone, senha):
        # === VALIDAÇÕES ===
        if email.lower() == "admin":
            raise ValueError("O e-mail 'admin' é reservado para o administrador.")

        for c in ClienteDAO.listar():
            if c.get_id() != id and c.get_email().lower() == email.lower():
                raise ValueError("Já existe outro cliente com este e-mail.")

        for p in ProfissionalDAO.listar():
            if p.get_email().lower() == email.lower():
                raise ValueError("Já existe um profissional com este e-mail.")

        cliente = Cliente(id, nome, email, fone, senha)
        ClienteDAO.atualizar(cliente)

    def cliente_excluir(id):
        # === BLOQUEAR EXCLUSÃO SE TIVER HORÁRIO AGENDADO ===
        for h in HorarioDAO.listar():
            if h.get_id_cliente() == id:
                raise ValueError("Não é possível excluir este cliente, pois há horários agendados.")

        ClienteDAO.excluir(id)

    # ---------------------- SERVIÇO ----------------------

    def servico_listar():
        r = ServicoDAO.listar()
        r.sort(key=lambda obj: obj.get_descricao())
        return r

    def servico_listar_id(id):
        return ServicoDAO.listar_id(id)

    def servico_inserir(descricao, valor):
        for obj in View.servico_listar():
            if obj.get_descricao() == descricao:
                raise ValueError("Serviço já cadastrado")
        servico = Servico(0, descricao, valor)
        ServicoDAO.inserir(servico)

    def servico_atualizar(id, descricao, valor):
        for obj in View.servico_listar():
            if obj.get_id() != id and obj.get_descricao() == descricao:
                raise ValueError("Descrição já cadastrada em outro serviço")
        servico = Servico(id, descricao, valor)
        ServicoDAO.atualizar(servico)

    def servico_excluir(id):
        for obj in View.horario_listar():
            if obj.get_id_servico == id:
                raise ValueError("Serviço já agendado: Não é possível excluir")
        c = Servico(id, "sem descricao",0)
        ServicoDAO.excluir()

    # ---------------------- HORÁRIO ----------------------

    def horario_inserir(data, confirmado, id_cliente, id_servico, id_Profissional):
        # === VALIDAÇÕES ===
        for h in HorarioDAO.listar():
            if (
                h.get_data() == data and
                h.get_id_Profissional() == id_Profissional
            ):
                raise ValueError("Já existe um horário cadastrado com esta data e hora para este profissional.")

        c = Horario(0, data)
        c.set_confirmado(confirmado)
        c.set_id_cliente(id_cliente)
        c.set_id_servico(id_servico)
        c.set_id_Profissional(id_Profissional)
        HorarioDAO.inserir(c)

    def horario_listar():
        r = HorarioDAO.listar()
        r.sort(key=lambda obj: obj.get_data())
        return r

    def horario_filtrar_profissional(id_profissional):
        return [h for h in View.horario_listar() if h.get_id_profissional() == id_profissional]

    def horario_atualizar(id, data, confirmado, id_cliente, id_servico, id_Profissional):
        # === VALIDAÇÕES ===
        for h in HorarioDAO.listar():
            if (
                h.get_id() != id and
                h.get_data() == data and
                h.get_id_Profissional() == id_Profissional
            ):
                raise ValueError("Já existe outro horário com esta data e hora para este profissional.")

        c = Horario(id, data)
        c.set_confirmado(confirmado)
        c.set_id_cliente(id_cliente)
        c.set_id_servico(id_servico)
        c.set_id_Profissional(id_Profissional)
        HorarioDAO.atualizar(c)

    def horario_excluir(id):
        # === BLOQUEAR EXCLUSÃO SE O HORÁRIO ESTIVER AGENDADO POR UM CLIENTE ===
        h = HorarioDAO.listar_id(id)
        if h is None:
            raise ValueError("Horário não encontrado.")

        if h.get_id_cliente() not in [0, None]:
            raise ValueError("Não é possível excluir este horário, pois ele já foi agendado por um cliente.")

        HorarioDAO.excluir(h)

    def horario_agendar_horario(id_profissional):
        r = []
        agora = datetime.now()
        for h in View.horario_listar():
            if (
                h.get_data() >= agora and
                h.get_confirmado() == False and
                h.get_id_cliente() is None and
                h.get_id_Profissional() == id_profissional
            ):
                r.append(h)
        r.sort(key=lambda h: h.get_data())
        return r

    # ---------------------- PROFISSIONAL ----------------------

    
    def Profissional_listar():
        r = ProfissionalDAO.listar()
        r.sort(key=lambda obj: obj.get_nome())
        return r

    def Profissional_listar_id(id):
        return ProfissionalDAO.listar_id(id)

    def Profissional_inserir(nome, especialidade, conselho, senha, email):
        if email.lower() == "admin":
            raise ValueError("O e-mail 'admin' é reservado para o administrador.")

        for p in ProfissionalDAO.listar():
            if p.get_email().lower() == email.lower():
                raise ValueError("Já existe um profissional com este e-mail.")

        for c in ClienteDAO.listar():
            if c.get_email().lower() == email.lower():
                raise ValueError("Já existe um cliente com este e-mail.")

        profissional = Profissional(0, nome, especialidade, conselho, senha, email)
        ProfissionalDAO.inserir(profissional)

    def Profissional_atualizar(id, nome, especialidade, conselho, senha, email):
        if email.lower() == "admin":
            raise ValueError("O e-mail 'admin' é reservado para o administrador.")

        for p in ProfissionalDAO.listar():
            if p.get_id() != id and p.get_email().lower() == email.lower():
                raise ValueError("Já existe outro profissional com este e-mail.")

        for c in ClienteDAO.listar():
            if c.get_email().lower() == email.lower():
                raise ValueError("Já existe um cliente com este e-mail.")

        profissional = Profissional(id, nome, especialidade, conselho, senha, email)
        ProfissionalDAO.atualizar(profissional)

    def Profissional_excluir(id):
        for h in HorarioDAO.listar():
            if h.get_id_Profissional() == id:
                raise ValueError("Não é possível excluir este profissional, pois há horários cadastrados.")

        ProfissionalDAO.excluir(id)

    # ---------------------- ADMIN E AUTENTICAÇÃO ----------------------

    def cliente_criar_admin():
        for c in View.cliente_listar():
            if c.get_email().lower() == "admin":
                return
        View.cliente_inserir("admin", "admin", "fone", "1234")

    def cliente_autenticar(email, senha):
        for c in View.cliente_listar():
            if c.get_email() == email and c.get_senha() == senha:
                return {"id": c.get_id(), "nome": c.get_nome()}
        return None

    def profissional_autenticar(email, senha):
        for c in View.Profissional_listar():
            if c.get_email() == email and c.get_senha() == senha:
                return {"id": c.get_id(), "nome": c.get_nome()}
        return None

    def Profissional_Agendar(data, horarioI, horarioF, intervalo, id_profissional):
        primeiro_horario = datetime.strptime(data + " " + horarioI, '%d/%m/%Y %H:%M')
        ultimo_horario = datetime.strptime(data + ' ' + horarioF, '%d/%m/%Y %H:%M')
        intervalo_min = timedelta(minutes=intervalo)
        x = primeiro_horario
        while x <= ultimo_horario:
            View.horario_inserir(x, False, None, None, id_profissional)
            x = x + intervalo_min

    def horario_prof_listar(id_profissional):
        r = [h for h in View.horario_listar() if h.get_id_Profissional() == id_profissional]
        r.sort(key=lambda h: h.get_data())
        return r

    def horario_cliente_listar(id_cliente):
        r = [h for h in View.horario_listar() if h.get_id_cliente() == id_cliente]
        r.sort(key=lambda h: h.get_data())
        return r

    def cliente_visualizar_servicos(id_cliente):
        return View.horario_cliente_listar(id_cliente)

    def confirmar_servico(id_horario):
        h = HorarioDAO.listar_id(id_horario)
        if h:
            h.set_confirmado(True)
            HorarioDAO.atualizar(h)

    def alterar_senha_admin(nova_senha):
        for c in View.cliente_listar():
            if c.get_email().lower() == "admin":
                View.cliente_atualizar(c.get_id(), c.get_nome(), c.get_email(), c.get_fone(), nova_senha)
                break
