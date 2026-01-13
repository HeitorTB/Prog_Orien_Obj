import streamlit as st
from views import View
import time

class AbrirContaUI:
    def main():
        st.header("Criar Nova Conta")
        
        tipo = st.selectbox("Selecione o tipo de conta:", ["Aluno", "Professor"])
        
        with st.form("form_cadastro"):
            nome = st.text_input("Nome Completo")
            email = st.text_input("E-mail")
            senha = st.text_input("Senha", type="password")
            
            # Campo extra só aparece se for professor (visual)
            formacao = ""
            if tipo == "Professor":
                st.markdown("**Dados Profissionais**")
                formacao = st.text_input("Formação / Especialidade")
            
            if st.form_submit_button("Cadastrar"):
                try:
                    if tipo == "Aluno":
                        View.aluno_inserir(nome, email, senha)
                    else:
                        View.professor_inserir(nome, email, senha, formacao)
                        
                    st.success("Conta criada com sucesso!")
                    time.sleep(1)
                    st.rerun()
                except ValueError as e:
                    st.error(f"Erro: {e}")