import streamlit as st
import pandas as pd
from views import View
import time
from datetime import datetime

class ManterHorarioUI:
    def main():
        st.header("Cadastro de Horários")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterHorarioUI.listar()
        with tab2: ManterHorarioUI.inserir()
        with tab3: ManterHorarioUI.atualizar()
        with tab4: ManterHorarioUI.excluir()

    def listar():
        horarios = View.horario_listar()
        if len(horarios) == 0:
            st.write("Nenhum horário cadastrado")
        else:
            dic = []
            for obj in horarios:
                cliente = View.cliente_listar_id(obj.get_id_cliente())
                servico = View.servico_listar_id(obj.get_id_servico())
                profissional = View.Profissional_listar_id(obj.get_id_Profissional())
                if cliente: cliente = cliente.get_nome()
                if servico: servico = servico.get_descricao()
                if profissional: profissional = profissional.get_nome()
                dic.append({
                    "ID": obj.get_id(),
                    "Data": obj.get_data().strftime("%d/%m/%Y %H:%M"),
                    "Confirmado": obj.get_confirmado(),
                    "Cliente": cliente,
                    "Serviço": servico,
                    "Profissional": profissional
                })
            df = pd.DataFrame(dic)
            st.dataframe(df)

    def inserir():
        clientes = View.cliente_listar()
        servicos = View.servico_listar()
        profissionais = View.Profissional_listar()

        data = st.text_input("Informe a data e horário do serviço (dd/mm/yyyy HH:MM)",
                             datetime.now().strftime("%d/%m/%Y %H:%M"))
        confirmado = st.checkbox("Confirmado")
        cliente = st.selectbox("Informe o cliente", clientes, index=None)
        servico = st.selectbox("Informe o serviço", servicos, index=None)
        profissional = st.selectbox("Informe o profissional", profissionais, index=None)

        if st.button("Inserir"):
            try:
                id_cliente = cliente.get_id() if cliente else None
                id_servico = servico.get_id() if servico else None
                id_profissional = profissional.get_id() if profissional else None

                View.horario_inserir(datetime.strptime(data, "%d/%m/%Y %H:%M"),
                                     confirmado, id_cliente, id_servico, id_profissional)

                st.success("Horário inserido com sucesso!")
                time.sleep(2)
                st.rerun()
            except ValueError as e:
                st.error(f"Erro: {e}")
            except Exception:
                st.error("Erro inesperado ao inserir o horário.")

    def atualizar():
        horarios = View.horario_listar()
        if len(horarios) == 0:
            st.write("Nenhum horário cadastrado")
        else:
            clientes = View.cliente_listar()
            servicos = View.servico_listar()
            profissionais = View.Profissional_listar()

            op = st.selectbox("Atualização de Horários", horarios)

            data = st.text_input("Informe a nova data e horário (dd/mm/yyyy HH:MM)",
                                 op.get_data().strftime("%d/%m/%Y %H:%M"))
            confirmado = st.checkbox("Confirmado", op.get_confirmado(), key="confirmado")

            cliente = st.selectbox("Cliente", clientes,
                                   index=next((i for i, c in enumerate(clientes)
                                               if c.get_id() == op.get_id_cliente()), None))
            servico = st.selectbox("Serviço", servicos,
                                   index=next((i for i, s in enumerate(servicos)
                                               if s.get_id() == op.get_id_servico()), None))
            profissional = st.selectbox("Profissional", profissionais,
                                        index=next((i for i, p in enumerate(profissionais)
                                                    if p.get_id() == op.get_id_Profissional()), None))

            if st.button("Atualizar"):
                try:
                    id_cliente = cliente.get_id() if cliente else None
                    id_servico = servico.get_id() if servico else None
                    id_profissional = profissional.get_id() if profissional else None

                    View.horario_atualizar(op.get_id(),
                                           datetime.strptime(data, "%d/%m/%Y %H:%M"),
                                           confirmado, id_cliente, id_servico, id_profissional)

                    st.success("Horário atualizado com sucesso!")
                    time.sleep(2)
                    st.rerun()
                except ValueError as e:
                    st.error(f"Erro: {e}")
                except Exception:
                    st.error("Erro inesperado ao atualizar o horário.")

    def excluir():
        horarios = View.horario_listar()
        if len(horarios) == 0:
            st.write("Nenhum horário cadastrado")
        else:
            op = st.selectbox("Exclusão de Horários", horarios)
            if st.button("Excluir"):
                try:
                    View.horario_excluir(op.get_id())
                    st.success("Horário excluído com sucesso!")
                    time.sleep(2)
                    st.rerun()
                except ValueError as e:
                    st.error(f"Erro: {e}")
                except Exception:
                    st.error("Erro inesperado ao excluir o horário.")