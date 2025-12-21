import streamlit as st
from views import View
import time

class AlterarSenhaAdminUI:
    def main():
        st.header("Alterar Senha do Admin")

        # Verifica se é o admin
        if st.session_state.get("usuario_nome") != "admin":
            st.warning("Apenas o usuário admin pode acessar esta funcionalidade.")
            return

        nova_senha = st.text_input("Informe a nova senha", type="password")
        confirmar = st.text_input("Confirme a nova senha", type="password")

        if st.button("Alterar Senha"):
            if nova_senha != confirmar:
                st.error("As senhas não coincidem.")
            elif nova_senha.strip() == "":
                st.error("A senha não pode ser vazia.")
            else:
                View.alterar_senha_admin(nova_senha)
                st.success("Senha alterada com sucesso.")
                time.sleep(2)
                st.rerun()