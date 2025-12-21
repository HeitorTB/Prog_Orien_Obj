import streamlit as st
import pandas as pd

# --- IMPORTAÇÃO DAS CLASSES ---
# Ajuste 'seu_projeto' para a pasta onde você salvou os arquivos das classes
# Exemplo: Se salvou tudo em 'classes.py', use: from classes import ...
try:
    from DAO_sql.DAO import DAO # Ajuste conforme sua estrutura
    from models.Aluno import aluno, alunoDAO
    from models.Professor import Professor, ProfessorDAO
    from DAO_sql.database import Database
except ImportError:
    # Bloco apenas para evitar erro se você copiar e colar sem ter os arquivos fisicos
    st.error("Erro de Importação: Verifique se os arquivos 'Aluno.py', 'Professor.py' e 'Database.py' estão acessíveis.")
    st.stop()

# --- CONFIGURAÇÃO INICIAL ---
st.set_page_config(page_title="Sistema de Estudos", layout="wide")

# Inicialização do Banco de Dados
try:
    Database.criar_tabelas() # O método criar_tabelas já abre e fecha a conexão internamente
except Exception as e:
    st.error(f"Erro ao inicializar banco de dados: {e}")

st.title("Sistema de Gestão Acadêmica")

# --- MENU LATERAL ---
menu = st.sidebar.selectbox(
    "Selecione o Módulo",
    ["Alunos", "Professores"]
)

# ==============================================================================
# MÓDULO: ALUNOS (Antigo Usuários)
# ==============================================================================
if menu == "Alunos":
    st.header("Gestão de Alunos")

    # --- Formulário de Cadastro ---
    with st.expander("Cadastrar Novo Aluno", expanded=False):
        with st.form("form_aluno"):
            col1, col2 = st.columns(2)
            nome = col1.text_input("Nome")
            email = col2.text_input("Email")
            senha = st.text_input("Senha", type="password")
            
            submitted = st.form_submit_button("Salvar Aluno")
            
            if submitted:
                try:
                    # ID é None na criação (AutoIncrement)
                    novo_aluno = aluno(None, nome, email, senha)
                    alunoDAO.inserir(novo_aluno)
                    st.success(f"Aluno '{nome}' cadastrado com sucesso!")
                    st.rerun() # Recarrega a página para atualizar a lista
                except Exception as e:
                    st.error(f"Erro ao salvar: {e}")

    # --- Listagem ---
    st.subheader("Alunos Cadastrados")
    try:
        lista = alunoDAO.listar()
        if lista:
            # Convertendo objetos para dicionário para exibir no DataFrame
            dados = [{
                "ID": a.get_id(), 
                "Nome": a.get_nome(), 
                "Email": a.get_email()
            } for a in lista]
            
            df = pd.DataFrame(dados)
            st.dataframe(df, use_container_width=True, hide_index=True)
        else:
            st.info("Nenhum aluno encontrado.")
    except Exception as e:
        st.error(f"Erro ao ler banco de dados: {e}")

# ==============================================================================
# MÓDULO: PROFESSORES (Novo)
# ==============================================================================
elif menu == "Professores":
    st.header("Gestão de Professores")

    # --- Formulário de Cadastro ---
    with st.expander("Cadastrar Novo Professor", expanded=False):
        with st.form("form_prof"):
            col1, col2 = st.columns(2)
            nome = col1.text_input("Nome")
            email = col2.text_input("Email")
            
            col3, col4 = st.columns(2)
            senha = col3.text_input("Senha", type="password")
            formacao = col4.text_input("Formação / Especialidade") # Campo específico
            
            submitted = st.form_submit_button("Salvar Professor")
            
            if submitted:
                try:
                    # ID None, inclui Formação
                    novo_prof = Professor(None, nome, email, senha, formacao)
                    ProfessorDAO.inserir(novo_prof)
                    st.success(f"Professor '{nome}' cadastrado com sucesso!")
                    st.rerun()
                except Exception as e:
                    st.error(f"Erro ao salvar: {e}")

    # --- Listagem ---
    st.subheader("Professores Cadastrados")
    try:
        lista = ProfessorDAO.listar()
        if lista:
            dados = [{
                "ID": p.get_id(), 
                "Nome": p.get_nome(), 
                "Email": p.get_email(),
                "Formação": p.get_formacao() # Coluna extra
            } for p in lista]
            
            df = pd.DataFrame(dados)
            st.dataframe(df, use_container_width=True, hide_index=True)
        else:
            st.info("Nenhum professor encontrado.")
    except Exception as e:
        st.error(f"Erro ao ler banco de dados: {e}")