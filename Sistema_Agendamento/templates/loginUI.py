import streamlit as st
from views import View

class LoginUI:
    def main():
        st.header("Entrar no Sistema")
        email = st.text_input("Informe o e-mail")
        senha = st.text_input("Informe a senha", type="password")

        if st.button("Entrar"):
            c = View.cliente_autenticar(email, senha)
            if c:
                st.session_state["usuario_tipo"] = "cliente"
                st.session_state["usuario_id"] = c["id"]
                st.session_state["usuario_nome"] = c["nome"]
                st.rerun()

            p = View.profissional_autenticar(email, senha)
            if p:
                st.session_state["usuario_tipo"] = "prof"
                st.session_state["usuario_id"] = p["id"]
                st.session_state["usuario_nome"] = p["nome"]
                st.rerun()

            if not c and not p:
                st.error("Email ou senha inválidos")
            