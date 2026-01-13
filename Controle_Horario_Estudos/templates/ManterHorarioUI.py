import streamlit as st
import pandas as pd
import time
from views import View

class ManterHorarioUI:
    @staticmethod
    def main():
        st.header("Cronograma de Estudos")
        id_aluno = st.session_state["usuario_id"]

        # Busca as metas do aluno
        metas = View.meta_listar_aluno(id_aluno)

        # Se não tiver meta, avisa e para
        if not metas:
            st.warning("⚠️ Você precisa criar uma Meta antes de agendar um horário.")
            return

        # ---------------------------------------------------------
        # 1. AGENDAR HORÁRIO
        # ---------------------------------------------------------
        with st.container():
            st.write("Agende um horário para trabalhar em uma meta específica.")
            with st.form("form_horario"):
                
                # Mapeia { "Descrição da Meta": ID } usando Getters
                mapa_metas = {f"{m.get_descricao()} (até {m.get_data_limite()})": m.get_id() for m in metas}
                
                meta_selecionada = st.selectbox("Qual meta você vai estudar?", list(mapa_metas.keys()))
                
                col1, col2 = st.columns(2)
                hora_inicio = col1.time_input("Hora de Início")
                hora_fim = col2.time_input("Hora de Fim")

                if st.form_submit_button("Adicionar ao Horário"):
                    id_meta = mapa_metas[meta_selecionada]
                    try:
                        View.horario_inserir(hora_inicio, hora_fim, id_aluno, id_meta)
                        st.success("Horário agendado!")
                        time.sleep(1)
                        st.rerun()
                    except ValueError as e:
                        st.error(f"Erro de validação: {e}")
                    except Exception as e:
                        st.error(f"Erro no sistema: {e}")

        st.divider()

        # ---------------------------------------------------------
        # 2. MEUS HORÁRIOS
        # ---------------------------------------------------------
        st.subheader("Agenda")
        horarios = View.horario_listar(id_aluno)
        
        if horarios:
            dados_horario = []
            for h in horarios:
                # Opcional: Recuperar o nome da meta para exibir na tabela
                desc_meta = "Desconhecida"
                for m in metas:
                    if m.get_id() == h.get_id_meta():
                        desc_meta = m.get_descricao()
                        break
                
                dados_horario.append({
                    "Meta": desc_meta,
                    "Início": h.get_inicio(),
                    "Fim": h.get_fim()
                })
            
            st.dataframe(pd.DataFrame(dados_horario), use_container_width=True, hide_index=True)
        else:
            st.info("Nenhum horário agendado.")