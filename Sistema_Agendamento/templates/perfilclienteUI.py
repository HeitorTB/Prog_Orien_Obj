import streamlit as st
from views import View
import time

class PerfilClienteUI:
    def main():
        st.header("Meus Dados")

        op = View.cliente_listar_id(st.session_state["usuario_id"])
        nome = st.text_input("Informe o novo nome", op.get_nome())
        email = st.text_input("Informe o novo e-mail", op.get_email())
        fone = st.text_input("Informe o novo fone", op.get_fone())
        senha = st.text_input("Informe a nova senha", op.get_senha(), type="password")
        aniv = st.text_input("Informe o novo nascimento", op.get_aniv())

        if st.button("Atualizar"):
            try:
                View.cliente_atualizar(op.get_id(), nome, email, fone, senha, aniv)
                st.success("Dados atualizados com sucesso!")
            except Exception as erro:
                st.error(erro)
            time.sleep(2)
            st.rerun()
