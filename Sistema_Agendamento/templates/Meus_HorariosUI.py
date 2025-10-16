import streamlit as st
import pandas as pd
from views import View
import time
from datetime import datetime

class Meus_Horarios:
    def main():
        st.header("Meus Horários")
        if st.session_state["usuario_tipo"] == "prof":
            horarios = View.horario_prof_listar(st.session_state["usuario_id"])
            if len(horarios) == 0: st.write("Nenhum horário cadastrado")
            else:
                list_dic = []
                for obj in horarios: list_dic.append(obj.to_json())
                df = pd.DataFrame(list_dic)
                st.dataframe(df)
        elif st.session_state["usuario_tipo"] == "cliente":
            horarios = View.horario_cliente_listar(st.session_state["usuario_id"])
            if len(horarios) == 0: st.write("Nenhum horário cadastrado")
            else:
                list_dic = []
                for obj in horarios: list_dic.append(obj.to_json())
                df = pd.DataFrame(list_dic)
                st.dataframe(df)
        