from templates.manterclienteUI import ManterClienteUI
from templates.ManterServicoUI import ManterServicoUI
from templates.manterHorarioUI import ManterHorarioUI
from templates.manterProfissionalUI import ManterProfissionalUI
from templates.abrircontaUI import AbrirContaUI
from templates.loginUI import LoginUI
from templates.perfilclienteUI import PerfilClienteUI
from templates.PerfilProfissionalUI import PerfilProfissionalUI
from templates.agendarservicoUI import AgendarServicoUI
from templates.abrirAgenda import AbrirAgendaUI
from templates.Meus_HorariosUI import Meus_Horarios
from templates.VisualizarMeusServicosUI import VisualizarMeusServicosUI
from templates.ConfirmarServicoUI import ConfirmarServicoUI
from templates.AlterarSenhaAdminUI import AlterarSenhaAdminUI
from templates.Mostrar_AniversariantesUI import MostrarAniversariantes
from views import View
import streamlit as st

class IndexUI:
    def menu_admin():            
        op = st.sidebar.selectbox("Menu", ["Cadastro de Clientes", "Cadastro de Serviços", "Cadastro de Horários", "Cadastro de Profissionais", "Alterar Senha", "Aniversariantes"])
        if op == "Cadastro de Clientes": ManterClienteUI.main()
        if op == "Cadastro de Serviços": ManterServicoUI.main()
        if op == "Cadastro de Horários": ManterHorarioUI.main()
        if op == "Cadastro de Profissionais": ManterProfissionalUI.main()
        if op == "Alterar Senha": AlterarSenhaAdminUI.main()
        if op == "Aniversariantes": MostrarAniversariantes.main()
    
    def menu_visitante():
        op = st.sidebar.selectbox("Menu", ["Entrar no Sistema","Abrir Conta"])
        if op == "Entrar no Sistema": LoginUI.main()
        if op == "Abrir Conta": AbrirContaUI.main()

    def menu_cliente():
        op = st.sidebar.selectbox("Menu", ["Meus Dados", "Agendar Serviço", "Meus Serviços", "Aniversariantes"])
        if op == "Meus Dados": PerfilClienteUI.main()
        if op == "Agendar Serviço": AgendarServicoUI.main()
        if op == "Meus Serviços": VisualizarMeusServicosUI.main()
        if op == "Aniversariantes": MostrarAniversariantes.main()

    
    def menu_profissional():
        op = st.sidebar.selectbox("Menu", ["Meus Dados", "Minha Agenda", "Meus Horarios","Confirmar Serviço", "Aniversariantes"])
        if op == "Meus Dados": PerfilProfissionalUI.main()
        if op =="Minha Agenda": AbrirAgendaUI.main()
        if op =="Meus Horarios": Meus_Horarios.main()
        if op == "Confirmar Serviço": ConfirmarServicoUI.main()
        if op == "Aniversariantes": MostrarAniversariantes.main()


    def sair_do_sistema():
        if st.sidebar.button("Sair"):
            del st.session_state["usuario_id"]
            del st.session_state["usuario_nome"]
            st.rerun()

    def sidebar():
        if "usuario_id" not in st.session_state:
            IndexUI.menu_visitante()
        else:
            st.sidebar.write("Bem-vindo(a), " + st.session_state["usuario_nome"])
            tipo = st.session_state.get("usuario_tipo")
            admin = st.session_state["usuario_nome"] == "admin"

            if admin:
                IndexUI.menu_admin()
            elif tipo == "prof":
                IndexUI.menu_profissional()
            elif tipo == "cliente":
                IndexUI.menu_cliente()

            IndexUI.sair_do_sistema()


    def main():
        View.cliente_criar_admin()
        IndexUI.sidebar()

IndexUI.main()