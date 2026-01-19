import streamlit as st
import time
from datetime import datetime
from views import View

class ManterMetaUI:
    @staticmethod
    def main():
        st.header("Gerenciar Metas de Estudo")
        
        if "usuario_id" not in st.session_state or st.session_state.get("usuario_tipo") != "aluno":
            st.error("Acesso restrito a alunos.")
            return

        id_aluno = st.session_state["usuario_id"]

        with st.expander("Criar Nova Meta", expanded=False):
            with st.form("form_nova_meta"):
                descricao = st.text_input("Descrição da Meta (ex: Terminar Cap. 4)")
                
                data_input = st.date_input("Data Limite")
                disciplinas = View.disciplina_listar_para_select()
                
                opcoes = {}
                if disciplinas:
                    opcoes = {d['display']: d['id_disciplina'] for d in disciplinas}
                    selecao = st.selectbox("Disciplina", list(opcoes.keys()))
                else:
                    st.warning("Nenhuma disciplina disponível.")
                    selecao = None
                
                if st.form_submit_button("Salvar Meta"):
                    if not descricao:
                        st.error("Descrição obrigatória.")
                    elif not selecao:
                        st.error("Disciplina obrigatória.")
                    else:
                        try:
                            data_limite_str = data_input.strftime('%Y-%m-%d')
                            
                            id_disc = opcoes[selecao]
                            
                            View.meta_inserir(descricao, data_limite_str, id_disc, id_aluno)
                            
                            st.success("Meta criada!")
                            time.sleep(1)
                            st.rerun()
                        except Exception as e:
                            st.error(f"Erro: {e}")

        st.divider()
        
        st.subheader("Suas Metas Pendentes")
        
        # 1. Busca as metas do aluno
        metas = View.meta_listar_pendentes(id_aluno)
        
        if not metas:
            st.info("Você não tem metas pendentes no momento.")
        else:
            for m in metas:
                # Layout da linha da Meta
                with st.container(border=True):
                    col1, col2 = st.columns([5, 1])
                    
                    with col1:
                        st.markdown(f"### {m.get_descricao()}")
                        nome_disc = "Disciplina Geral"
                        if disciplinas:
                             for d in disciplinas:
                                if d['id_disciplina'] == m.get_id_disciplina():
                                    nome_disc = d['nome_disciplina']
                                    break
                        st.caption(f"Limite: {m.get_data_limite()} | {nome_disc}")

                        try:
                            materiais = View.material_listar_por_meta(m.get_id())
                            if materiais:
                                with st.expander(f"Materiais de Apoio Disponíveis ({len(materiais)})"):
                                    for mat in materiais:
                                        st.markdown(f"**🔹 {mat.get_titulo()}**")
                                        st.write(f"{mat.get_descricao()}")
                                        st.markdown("---")
                            else:
                                st.caption("Nenhum material de apoio anexado pelo professor.")
                        except AttributeError:
                            st.warning("Erro ao carregar materiais (Verifique a View).")

                    with col2:
                        st.write("")
                        if st.button("Concluir", key=f"btn_conc_{m.get_id()}"):
                            View.meta_concluir(m.get_id())
                            st.toast("Meta concluída! 🎉")
                            time.sleep(1)
                            st.rerun()