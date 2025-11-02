import streamlit as st 
import pandas as pd 
import time 
from views import View

class ManterProfissionalUI:
    def main():
        st.header("Cadastro de Profissionais")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir","Atualizar", "Excluir"])
        with tab1: ManterProfissionalUI.listar()
        with tab2: ManterProfissionalUI.inserir()
        with tab3: ManterProfissionalUI.atualizar()
        with tab4: ManterProfissionalUI.excluir()
    
    def listar():
        profissionais = View.Profissional_listar()
        if len(profissionais) == 0:
            st.write("Nenhum profissional cadastrado")
        else:
            list_dic = [obj.to_json() for obj in profissionais]
            df = pd.DataFrame(list_dic)
            st.dataframe(df)

    def inserir():
        nome = st.text_input("Informe o nome")
        especialidade = st.text_input("Informe a especialidade")
        conselho = st.text_input("Informe o conselho")
        email = st.text_input("Informe o e-mail")
        senha = st.text_input("Informe a senha", type="password")
        aniv = st.text_input("Informe a data de nascimento (dd/mm/aaaa)")
        if st.button("Inserir"):
            try:
                View.Profissional_inserir(nome, especialidade, conselho, senha, email, aniv)
                st.success("Profissional inserido com sucesso!")
            except ValueError as erro:
                st.error(f"Erro ao inserir profissional: {erro}")
            time.sleep(2)
            st.rerun()

    def atualizar():
        profissionais = View.Profissional_listar()
        if len(profissionais) == 0:
            st.write("Nenhum profissional cadastrado")
        else:
            op = st.selectbox("Atualização de profissionais", profissionais)
            nome = st.text_input("Informe o novo nome", op.get_nome())
            especialidade = st.text_input("Informe a nova especialidade", op.get_especialidade())
            conselho = st.text_input("Informe o novo conselho", op.get_conselho())
            email = st.text_input("Informe o novo e-mail", op.get_email())
            senha = st.text_input("Informe a nova senha", op.get_senha(), type="password")
            aniv = st.text_input("Informe a nova data de nascimento (dd/mm/aaaa)", op.get_aniv())
            if st.button("Atualizar"):
                try:
                    id = op.get_id()
                    View.Profissional_atualizar(id, nome, especialidade, conselho, senha, email, aniv)
                    st.success("Profissional atualizado com sucesso!")
                except ValueError as erro:
                    st.error(f"Erro ao atualizar profissional: {erro}")
                time.sleep(2)
                st.rerun()
                

    def excluir():
        profissionais = View.Profissional_listar()
        if len(profissionais) == 0:
            st.write("Nenhum profissional cadastrado")
        else:
            op = st.selectbox("Exclusão de profissionais", profissionais)
            if st.button("Excluir"):
                try:
                    id = op.get_id()
                    View.Profissional_excluir(id)
                    st.success("Profissional excluído com sucesso!")
                except ValueError as erro:
                    st.error(f"Erro ao excluir profissional: {erro}")
                time.sleep(2)
                st.rerun()

