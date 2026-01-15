import streamlit as st
import time
from views import View

class PublicarMaterialUI:
    @staticmethod
    def main():
        st.header("Publicar Material de Apoio")
        
        # Verifica se é professor
        if "usuario_id" not in st.session_state or st.session_state.get("usuario_tipo") != "professor":
            st.error("Acesso restrito.")
            return

        id_prof = st.session_state["usuario_id"]

        # -----------------------------------------------------------
        # CORREÇÃO: VERIFICAR DADOS ANTES DO FORM
        # -----------------------------------------------------------
        todas_metas = View.meta_listar_geral()
        disciplinas = View.disciplina_listar()

        # Se não houver metas, NÃO abre o formulário (evita o erro do botão)
        if not todas_metas:
            st.warning("⚠️ Não é possível publicar materiais no momento.")
            st.info("Os alunos ainda não criaram nenhuma Meta de Estudo vinculada às disciplinas.")
            return

        # Prepara as opções do selectbox
        opcoes = {}
        for m in todas_metas:
            # Tenta achar o nome da disciplina para exibir bonito
            nome_disc = next((d.get_nome() for d in disciplinas if d.get_id() == m.get_id_disciplina()), "Disciplina")
            # Texto no Selectbox: "Estudar Cap 1 - [Física I]"
            label = f"{m.get_descricao()} - [{nome_disc}]"
            opcoes[label] = m.get_id()

        # -----------------------------------------------------------
        # FORMULÁRIO SEGURO
        # -----------------------------------------------------------
        with st.form("form_material"):
            titulo = st.text_input("Título do Material (ex: PDF Cap. 4)")
            descricao = st.text_area("Descrição / Link")
            
            st.write("Vincular este material a qual Meta (de Aluno)?")
            sel_meta = st.selectbox("Selecione a Meta Alvo", list(opcoes.keys()))
            
            # Botão sempre existe aqui dentro, pois já validamos os dados antes
            if st.form_submit_button("Publicar Material"):
                try:
                    if not titulo:
                        st.error("O título é obrigatório.")
                    else:
                        id_meta = opcoes[sel_meta]
                        View.material_inserir(titulo, descricao, id_prof, id_meta)
                        st.success("Material publicado com sucesso!")
                        time.sleep(1)
                        st.rerun()
                except Exception as e:
                    st.error(f"Erro: {e}")

        st.divider()
        st.caption("Nota: Os materiais publicados aparecerão para o aluno dentro da meta selecionada.")