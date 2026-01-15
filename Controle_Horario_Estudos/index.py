import streamlit as st
from DAO_sql.database import Database
from views import View

# --- IMPORTAÇÃO DAS TELAS (TEMPLATES) ---
from templates.loginUI import LoginUI
from templates.abrircontaUI import AbrirContaUI
from templates.MantermetasUI import ManterMetaUI   # Aluno
from templates.ManterHorarioUI import ManterHorarioUI # Aluno
from templates.PublicarMaterialUI import PublicarMaterialUI # Professor (Antigo)
from templates.ManterProfessorUI import ManterProfessorUI 

# Inicializa o Banco de Dados
if __name__ == "__main__":
    try:
        Database.criar_tabelas()
    except Exception as e:
        st.error(f"Erro ao conectar no banco: {e}")

class IndexUI:
    
    # --- MENU VISITANTE ---
    @staticmethod
    def menu_visitante():
        st.sidebar.header("Bem-vindo!")
        op = st.sidebar.selectbox("Acesso", ["Login", "Criar Conta"])
        if op == "Login": LoginUI.main()
        if op == "Criar Conta": AbrirContaUI.main()

    # --- MENU ALUNO ---
    @staticmethod
    def menu_aluno():
        st.sidebar.markdown(f"🎓 **{st.session_state.get('usuario_nome', 'Aluno')}**")
        st.sidebar.markdown("---")
        
        op = st.sidebar.radio("Menu Aluno", ["Meus Objetivos (Metas)", "Meu Horário"])

        if op == "Meus Objetivos (Metas)": 
            ManterMetaUI.main()
        
        if op == "Meu Horário": 
            ManterHorarioUI.main()

    # --- MENU PROFESSOR (ATUALIZADO) ---
    @staticmethod
    def menu_professor():
        st.sidebar.markdown(f"👨‍🏫 **Prof. {st.session_state.get('usuario_nome', 'Professor')}**")
        st.sidebar.markdown("---")
        
        # Adicionamos "Gerenciar Disciplinas" que leva para a tela nova
        op = st.sidebar.radio("Menu Professor", ["Gerenciar Disciplinas", "Publicar Material"])

        if op == "Gerenciar Disciplinas": 
            # Chama a tela criada no Passo 3 (Cadastro de matérias)
            ManterProfessorUI.main()

        if op == "Publicar Material": 
            PublicarMaterialUI.main()

    # --- CONTROLADOR PRINCIPAL ---
    @staticmethod
    def sidebar():
        # Verifica se há usuário logado na sessão
        if "usuario_id" not in st.session_state:
            IndexUI.menu_visitante()
        else:
            # Redireciona para o menu correto baseada no tipo (aluno/professor)
            tipo = st.session_state["usuario_tipo"]
            
            if tipo == "aluno":
                IndexUI.menu_aluno()
            elif tipo == "professor":
                IndexUI.menu_professor()
            
            # Botão de Sair (Logout)
            st.sidebar.markdown("---")
            if st.sidebar.button("Sair do Sistema"):
                for key in list(st.session_state.keys()):
                    del st.session_state[key]
                st.rerun()

    @staticmethod
    def main():
        IndexUI.sidebar()

if __name__ == "__main__":
    IndexUI.main()