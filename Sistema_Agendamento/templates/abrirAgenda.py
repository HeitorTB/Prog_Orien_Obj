import streamlit as st
from views import View
import time

class AbrirAgendaUI:
    def main():
        st.header("Abrir Minha Agenda")
        data = st.text_input("Informe a data no formato dd/mm/aaaa")
        horarioI = st.text_input("Informe o horário inicial (HH:MM)")
        horarioF = st.text_input("Informe o horário final (HH:MM)")
        intervalo = st.text_input("Informe o intervalo entre os horários (minutos)")

        if st.button("Abrir Agenda"):
            try:
                View.Profissional_Agendar(data, horarioI, horarioF, int(intervalo),st.session_state['usuario_id'])
                st.success("Agenda aberta com sucesso!")
                time.sleep(2)
                st.rerun()
            except ValueError as e:
                st.error(f"Erro: {e}")