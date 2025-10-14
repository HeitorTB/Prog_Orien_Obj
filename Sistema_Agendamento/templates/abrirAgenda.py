import streamlit as st 
from views import View
import time 

class AbrirAgendaUI: 
    def main(): 
        st.header("Abrir Minha Agenda")
        data = st.text_input("Informe a data no formato dd/mm/aaaa")
        horarioI = st.text_input("Informe o horário inicial no formato HH:MM")
        horarioF = st.text_input("Informe o horário final no formato HH:MM")
        intervalo = st.text_input("Informe o o intervalo entre os horários (min)")
        
        if st.button("Abrir Agenda"):
            View.Profissional_Agendar(data, horarioI, horarioF, int(intervalo), st.session_state['usuario_id'])
            st.success("Profissional agendado com sucesso")
            time.sleep(2)
            st.rerun()