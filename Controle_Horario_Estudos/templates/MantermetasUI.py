import streamlit as st
import pandas as pd
import time
from views import View

class ManterMetasUI:
    @staticmethod
    def main():
        st.header("Gerenciar Metas")
        
        # Verifica se o usuário está logado
        if "usuario_id" not in st.session_state:
            st.error("Usuário não autenticado.")
            return
            
        id_aluno = st.session_state["usuario_id"]

        # ---------------------------------------------------------
        # 1. PRÉ-REQUISITO: DISCIPLINA
        # ---------------------------------------------------------
        # Buscamos apenas as disciplinas que têm professor (para garantir que haverá material)
        disciplinas = View.disciplina_listar_validas()
        
        if not disciplinas:
            st.warning("Nenhuma disciplina encontrada. Cadastre uma para continuar.")
            with st.form("form_disc_rapido"):
                nome_disc = st.text_input("Nome da Disciplina (ex: Matemática)")
                if st.form_submit_button("Cadastrar Disciplina"):
                    try:
                        View.disciplina_inserir(nome_disc)
                        st.success("Disciplina cadastrada!")
                        time.sleep(1)
                        st.rerun()
                    except ValueError as e:
                        st.error(e)
            return

        # ---------------------------------------------------------
        # 2. CRIAR NOVA META
        # ---------------------------------------------------------
        with st.expander("🎯 Criar Nova Meta"):
            with st.form("form_meta"):
                descricao = st.text_input("Descrição da Meta (ex: Terminar Cap. 4)")
                data_limite = st.date_input("Data Limite")
                
                # Mapa de disciplinas para o Selectbox
                mapa_disciplinas = {d.get_nome(): d.get_id() for d in disciplinas}
                sel_disciplina = st.selectbox("Matéria", list(mapa_disciplinas.keys()))
                
                if st.form_submit_button("Salvar Meta"):
                    try:
                        id_disc = mapa_disciplinas[sel_disciplina]
                        View.meta_inserir(descricao, str(data_limite), id_disc, id_aluno)
                        st.success("Meta criada com sucesso!")
                        time.sleep(1)
                        st.rerun()
                    except Exception as e:
                        st.error(f"Erro: {e}")

        # ---------------------------------------------------------
        # 3. LISTAR METAS, MATERIAIS E AÇÕES
        # ---------------------------------------------------------
        st.subheader("Minhas Metas")
        metas = View.meta_listar_aluno(id_aluno)
        
        if not metas:
            st.info("Você ainda não definiu nenhuma meta.")
        else:
            # Iteramos sobre cada meta para criar um visual interativo
            for m in metas:
                # Define cor/ícone baseada no status
                status_texto = "✅ Concluída" if m.get_status() else "🕒 Pendente"
                titulo_expander = f"{m.get_descricao()} - {status_texto}"
                
                with st.expander(titulo_expander):
                    col1, col2 = st.columns(2)
                    
                    # Identificar nome da disciplina
                    nome_disc = next((d.get_nome() for d in disciplinas if d.get_id() == m.get_id_disciplina()), "Desconhecida")
                    
                    with col1:
                        st.caption("Detalhes")
                        st.write(f"**Matéria:** {nome_disc}")
                        st.write(f"**Prazo:** {m.get_data_limite()}")
                        if m.get_data_conclusao():
                            st.write(f"**Concluído em:** {m.get_data_conclusao()}")

                    # --- FUNCIONALIDADE 1: VER MATERIAIS ---
                    with col2:
                        st.caption("📚 Materiais de Apoio")
                        materiais = View.material_listar_por_meta(m.get_id())
                        if materiais:
                            for mat in materiais:
                                st.markdown(f"**📄 {mat.get_titulo()}**")
                                st.text(f"{mat.get_descricao()}")
                                st.divider()
                        else:
                            st.write("_Nenhum material disponibilizado pelo professor._")

                    # --- FUNCIONALIDADE 2: CONCLUIR META ---
                    # Só mostra o botão se a meta estiver Pendente (False/0)
                    if not m.get_status():
                        st.divider()
                        # Usamos key=f"btn_{m.get_id()}" para o Streamlit não confundir os botões
                        if st.button("Marcar como Concluída", key=f"btn_concluir_{m.get_id()}"):
                            try:
                                View.meta_concluir(m.get_id())
                                st.success("Meta concluída! Parabéns!")
                                time.sleep(1)
                                st.rerun()
                            except Exception as e:
                                st.error(f"Erro ao concluir: {e}")