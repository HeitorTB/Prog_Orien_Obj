import streamlit as st 
import pandas as pd 
import time 
from views import View

class ManterServicoUI:
    def main():
        st.header("Cadastro de Serviços")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir","Atualizar", "Excluir"])
        with tab1: ManterServicoUI.listar()
        with tab2: ManterServicoUI.inserir()
        with tab3: ManterServicoUI.atualizar()
        with tab4: ManterServicoUI.excluir()
    
    def listar():
        Servicos = View.servico_listar()
        if len(Servicos) == 0: st.write("Nenhum Servico cadastrado")
        else:
            list_dic = []
            for obj in Servicos: list_dic.append(obj.to_json())
            df = pd.DataFrame(list_dic)
            st.dataframe(df)

    def inserir():
        valor = st.text_input("Informe o Valor")
        descricao= st.text_input("Informe a Descrição")
        if st.button("Inserir"):
            try:
                View.servico_inserir(descricao, float(valor))
                st.success("Servico inserido com sucesso")
            except ValueError as erro:
                st.error(erro)
            time.sleep(2)
            st.rerun()

    def atualizar():
        Servicos = View.servico_listar()
        if len(Servicos) == 0: st.write("Nenhum Servico cadastrado")
        else:
            op = st.selectbox("Atualização de Servicos", Servicos)
            descricao = st.text_input("Informe a nova descrição", op.get_descricao())
            valor = st.text_input("Informe o novo valor", op.get_valor())
            if st.button("Atualizar"):
                try:
                    id = op.get_id()
                    View.servico_atualizar(id, descricao, float(valor))
                    st.success("Servico atualizado com sucesso")
                except ValueError as erro:
                    st.error(erro)
                time.sleep(2)
                st.rerun()

    def excluir():
        Servicos = View.servico_listar()
        if len(Servicos) == 0: st.write("Nenhum Servico cadastrado")
        else:
            op = st.selectbox("Exclusão de Servicos", Servicos)
            if st.button("Excluir"):
                try:
                    id = op.get_id()
                    View.servico_excluir(id)
                    st.success("Servico excluído com sucesso")
                except ValueError as erro:
                    st.error(erro)
                time.sleep(2)
                st.rerun()
