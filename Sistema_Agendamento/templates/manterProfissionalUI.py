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
        Profissionais = View.Profissional_listar()
        if len(Profissionais) == 0: st.write("Nenhum Profissional cadastrado")
        else:
            list_dic = []
            for obj in Profissionais: list_dic.append(obj.to_json())
            df = pd.DataFrame(list_dic)
            st.dataframe(df)

    def inserir():
        nome = st.text_input("Informe o Nome")
        especialidade= st.text_input("Informe a Especialidade")
        conselho = st.text_input("Informe o Conselho")
        email = st.text_input("Informe o email")
        senha = st.text_input("Informe a senha", type="password")
        if st.button("Inserir"):
            View.Profissional_inserir(nome, especialidade, conselho, senha, email)
            st.success("Profissional inserido com sucesso")
            time.sleep(2)
            st.rerun()
    
    def atualizar():
        Profissionais = View.Profissional_listar()
        if len(Profissionais) == 0: st.write("Nenhum Profissional cadastrado")
        else:
            op = st.selectbox("Atualização de Profissionais", Profissionais)
            nome = st.text_input("Informe o novo nome", op.get_nome())
            especialidade = st.text_input("Informe a nova especialidade", op.get_especialidade())
            conselho = st.text_input("Informe o novo conselho", op.get_conselho())
            email = st.text_input("Informe o novo email", op.get_conselho())
            senha = st.text_input("Informe a nova senha", type="password")
            if st.button("Atualizar"):
                id = op.get_id()
                View.Profissional_atualizar(id, nome, especialidade, conselho, senha, email)
                st.success("Profissional atualizado com sucesso")
                time.sleep(2)
                st.rerun()

    def excluir():
        Profissionais = View.Profissional_listar()
        if len(Profissionais) == 0: st.write("Nenhum Profissional cadastrado")
        else:
            op = st.selectbox("Exclusão de Profissionais", Profissionais)
            if st.button("Excluir"):
                id = op.get_id()
                View.Profissional_excluir(id)
                st.success("Profissional excluído com sucesso")
                time.sleep(2)
                st.rerun()
