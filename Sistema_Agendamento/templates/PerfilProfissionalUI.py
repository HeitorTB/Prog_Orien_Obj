import streamlit as st
from views import View
import time

class PerfilProfissionalUI:
    def main():
        st.header("Meus Dados")

        op = View.Profissional_listar_id(st.session_state["usuario_id"])

        if op is None:
            st.error("Erro: profissional não encontrado. Verifique se você está logado corretamente.")
            return

        nome = st.text_input("Informe o novo nome", op.get_nome())
        email = st.text_input("Informe o novo e-mail", op.get_email())
        conselho = st.text_input("Informe o novo conselho", op.get_conselho())
        especialidade = st.text_input("Informe a nova especialidade", op.get_especialidade())
        senha = st.text_input("Informe a nova senha", op.get_senha(),type="password")
        aniv = st.text_input("Informe a nova data de nascimento (dd/mm/aaaa)", op.get_aniv())
        
        if st.button("Atualizar"):

            id = op.get_id()
            View.Profissional_atualizar(id, nome, especialidade, conselho, senha, email, aniv)
            st.success("Profissional atualizado com sucesso")