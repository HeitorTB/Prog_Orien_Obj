import streamlit as st
from views import View
import time

class LoginUI:
    def main():
        st.header("Entrar no Sistema")
        
        email = st.text_input("E-mail")
        senha = st.text_input("Senha", type="password")
        
        if st.button("Entrar"):
            usuario = None
            
            # 1. Tenta achar na tabela de Professores
            usuario = View.professor_autenticar(email, senha)
            
            # 2. Se não achou, tenta na tabela de Alunos
            if not usuario:
                usuario = View.aluno_autenticar(email, senha)
                
            if usuario:
                st.success(f"Bem-vindo(a), {usuario['nome']}!")
                st.session_state["usuario_id"] = usuario["id"]
                st.session_state["usuario_nome"] = usuario["nome"]
                st.session_state["usuario_tipo"] = usuario["tipo"]
                time.sleep(1)
                st.rerun()
            else:
                st.error("E-mail ou senha inválidos.")