import streamlit as st
from views import View
import time

class ConfirmarServicoUI:
    def main():
        st.header("Confirmar Serviço")

        if st.session_state.get("usuario_tipo") != "prof":
            st.warning("Apenas profissionais podem confirmar serviços.")
            return

        # Lista horários pendentes de confirmação com cliente
        horarios = [
            h for h in View.horario_prof_listar(st.session_state["usuario_id"])
            if h.get_id_cliente() is not None and not h.get_confirmado()
        ]

        if len(horarios) == 0:
            st.info("Nenhum serviço pendente de confirmação.")
            return

        # Selectbox de horários
        op = st.selectbox(
            "Informe o horário",
            horarios,
            format_func=lambda h: f"{h.get_id()} - {h.get_data().strftime('%d/%m/%Y %H:%M')} - {h.get_confirmado()}"
        )

        # Cliente formatado como selectbox (mesmo estilo do cadastro de horários)
        cliente = View.cliente_listar_id(op.get_id_cliente())
        clientes = [cliente] if cliente else []
        st.selectbox(
            "Cliente",
            clientes,
            format_func=lambda c: f"{c.get_id()} - {c.get_nome()} - {c.get_email()} - {c.get_fone()}",
            index=0,
            disabled=True
        )

        # Botão para confirmar
        if st.button("Confirmar"):
            View.confirmar_servico(op.get_id())
            st.success("Serviço confirmado com sucesso.")
            time.sleep(2)
            st.rerun()
