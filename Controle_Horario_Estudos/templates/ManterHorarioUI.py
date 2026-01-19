import streamlit as st
import pandas as pd
import time
from views import View

class ManterHorarioUI:
    @staticmethod
    def main():
        st.header("Cronograma de Estudos")
        id_aluno = st.session_state["usuario_id"]

        todas_metas = View.meta_listar_aluno(id_aluno)

        metas_pendentes = [m for m in todas_metas if not m.get_status()]

        pode_agendar = True
        if not metas_pendentes:
            st.warning("⚠️ Você não possui metas pendentes para agendar. Crie uma nova meta ou reabra uma antiga.")
            pode_agendar = False

        if pode_agendar:
            with st.container(border=True):
                st.subheader("📅 Novo Agendamento")
                with st.form("form_horario"):
                    
                    # CORREÇÃO AQUI:
                    # Usamos a lista 'metas_pendentes' para criar o selectbox
                    mapa_metas = {f"{m.get_descricao()} (até {m.get_data_limite()})": m.get_id() for m in metas_pendentes}
                    
                    meta_selecionada = st.selectbox("Qual meta você vai estudar?", list(mapa_metas.keys()))
                    
                    col1, col2 = st.columns(2)
                    hora_inicio = col1.time_input("Hora de Início")
                    hora_fim = col2.time_input("Hora de Fim")

                    if st.form_submit_button("Adicionar ao Horário"):
                        id_meta = mapa_metas[meta_selecionada]
                        try:
                            View.horario_inserir(hora_inicio, hora_fim, id_aluno, id_meta)
                            st.success("Horário agendado com sucesso!")
                            time.sleep(1)
                            st.rerun()
                        except ValueError as e:
                            st.error(f"Erro de validação: {e}")
                        except Exception as e:
                            st.error(f"Erro no sistema: {e}")

        st.divider()

        st.subheader("🕑 Agenda Completa")
        horarios = View.horario_listar(id_aluno)
        
        if horarios:
            dados_horario = []
            for h in horarios:
                desc_meta = "Meta excluída/inválida"
                for m in todas_metas:
                    if m.get_id() == h.get_id_meta():
                        desc_meta = m.get_descricao()
                        if m.get_status():
                            desc_meta += " (Concluída)"
                        break
                
                dados_horario.append({
                    "Meta": desc_meta,
                    "Início": h.get_inicio(),
                    "Fim": h.get_fim()
                })

            df = pd.DataFrame(dados_horario)
            st.dataframe(df, use_container_width=True, hide_index=True)
        else:
            st.info("Nenhum horário agendado ainda.")