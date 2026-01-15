import streamlit as st
import time
from views import View

class ManterProfessorUI:
    @staticmethod
    def main():
        st.header("Área do Professor")
        
        # -----------------------------------------------------------
        # VERIFICAÇÃO DE SEGURANÇA
        # -----------------------------------------------------------
        if "usuario_id" not in st.session_state or st.session_state.get("usuario_tipo") != "professor":
            st.error("Acesso restrito a professores identificados.")
            return

        id_prof = st.session_state["usuario_id"]
        nome_prof = st.session_state.get("usuario_nome", "Professor")

        # Exibe a saudação diretamente na tela principal
        st.write(f"Bem-vindo, Prof. **{nome_prof}**!")
        st.markdown("---")

        # -----------------------------------------------------------
        # CADASTRAR DISCIPLINA (Agora é a tela principal)
        # -----------------------------------------------------------
        st.subheader("Nova Disciplina")
        
        with st.form("form_add_disc"):
            nome_disciplina = st.text_input("Nome da Matéria (ex: Física I)")
            
            if st.form_submit_button("Cadastrar Matéria"):
                try:
                    View.disciplina_inserir(nome_disciplina, id_prof)
                    st.success(f"Disciplina '{nome_disciplina}' cadastrada com sucesso!")
                    time.sleep(1)
                    st.rerun()
                except Exception as e:
                    st.error(f"Erro: {e}")
        
        st.divider()
        st.subheader("Disciplinas que você leciona")
        
        # Listagem das disciplinas
        todas = View.disciplina_listar()
        
        # Filtra apenas as desse professor
        minhas = [d for d in todas if d.get_id_professor() == id_prof]
        
        if minhas:
            for d in minhas:
                st.text(f"- {d.get_nome()}")
        else:
            st.info("Nenhuma disciplina cadastrada ainda.")