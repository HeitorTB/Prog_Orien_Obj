import streamlit as st
import time
from views import View

class PublicarMaterialUI:
    @staticmethod
    def main():
        st.header("Publicar Material de Apoio")
        id_prof = st.session_state["usuario_id"]

        # O professor vê TODAS as metas de todos os alunos (para saber o que eles estão estudando)
        # No futuro, pode filtrar por turmas, mas agora listamos todas.
        todas_metas = View.meta_listar_todas()

        if not todas_metas:
            st.info("Nenhum aluno cadastrou metas ainda. Aguarde os alunos definirem seus estudos.")
            return

        with st.form("form_material_prof"):
            st.write("Vincule seu material a um tópico (meta) que os alunos estão estudando.")
            
            titulo = st.text_input("Título do Material (Ex: PDF de Cálculo)")
            descricao = st.text_area("Descrição ou Link")
            
            # Mapeia { "Descrição (ID)": ID } usando Getters
            mapa_metas = {f"{m.get_descricao()} (ID: {m.get_id()})": m.get_id() for m in todas_metas}
            
            escolha = st.selectbox("Tópico/Meta Relacionada", list(mapa_metas.keys()))
            
            if st.form_submit_button("Publicar Material"):
                try:
                    id_meta = mapa_metas[escolha]
                    View.material_inserir(titulo, descricao, id_prof, id_meta)
                    st.success("Material publicado com sucesso!")
                    time.sleep(1)
                    st.rerun()
                except Exception as e:
                    st.error(f"Erro: {e}")