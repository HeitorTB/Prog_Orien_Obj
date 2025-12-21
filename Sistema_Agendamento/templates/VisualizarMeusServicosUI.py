import streamlit as st
import pandas as pd
from views import View

class VisualizarMeusServicosUI:
    def main():
        st.header("Meus Serviços")

        # Verifica se o usuário é cliente
        if st.session_state.get("usuario_tipo") != "cliente":
            st.warning("Apenas clientes podem visualizar seus serviços.")
            return

        # Busca os horários agendados pelo cliente
        horarios = View.cliente_visualizar_servicos(st.session_state["usuario_id"])
        if len(horarios) == 0:
            st.info("Você ainda não tem serviços agendados.")
        else:
            dados = []
            for h in horarios:
                servico = View.servico_listar_id(h.get_id_servico())
                profissional = View.Profissional_listar_id(h.get_id_Profissional())

                dados.append({
                    "ID": h.get_id(),
                    "Data": h.get_data().strftime("%d/%m/%Y %H:%M"),
                    "Confirmado": h.get_confirmado(),
                    "Serviço": servico.get_descricao() if servico else "",
                    "Profissional": profissional.get_nome() if profissional else ""
                })

            df = pd.DataFrame(dados)
            st.dataframe(df)
