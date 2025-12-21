import streamlit as st 
import pandas as pd
from datetime import datetime
from views import View

class MostrarAniversariantes: 
    def main():
        st.header("Aniversariantes do Dia")
        
        aniversariantes_c = View.mostrar_aniversariantes_clientes()
        aniversariantes_p = View.mostrar_aniversariantes_prof()
        
        total_aniversariantes = len(aniversariantes_c) + len(aniversariantes_p)
        
        if total_aniversariantes == 0:
            st.info("Nenhum aniversariante hoje")
        else:
            st.success(f"{total_aniversariantes} aniversariante(s) hoje!")
        
        if aniversariantes_c:
            st.subheader("Clientes Aniversariantes")
            
            dados_clientes = []
            for cliente in aniversariantes_c:
                idade = MostrarAniversariantes._calcular_idade(cliente.get_aniv())
                dados_clientes.append({
                    'Nome': cliente.get_nome(),
                    'Email': cliente.get_email(),
                    'Telefone': cliente.get_fone(),
                    'Data de Nascimento': cliente.get_aniv(),
                    'Idade': f"{idade} anos"
                })
            
            df_clientes = pd.DataFrame(dados_clientes)
            st.dataframe(
                df_clientes,
                use_container_width=True,
                hide_index=True
            )
        
        if aniversariantes_p:
            st.subheader("Profissionais Aniversariantes")
            
            dados_profissionais = []
            for prof in aniversariantes_p:
                idade = MostrarAniversariantes._calcular_idade(prof.get_aniv())
                dados_profissionais.append({
                    'Nome': prof.get_nome(),
                    'Email': prof.get_email(),
                    'Especialidade': prof.get_especialidade(),
                    'Conselho': prof.get_conselho(),
                    'Data de Nascimento': prof.get_aniv(),
                    'Idade': f"{idade} anos"
                })
            
            df_profissionais = pd.DataFrame(dados_profissionais)
            st.dataframe(
                df_profissionais,
                use_container_width=True,
                hide_index=True
            )

    def _calcular_idade(data_nascimento):
        if not data_nascimento:
            return "N/A"
            
        try:
            nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y")
            hoje = datetime.now()
            
            idade = hoje.year - nascimento.year
            
            if (hoje.month, hoje.day) < (nascimento.month, nascimento.day):
                idade -= 1
                
            return idade
        except ValueError:
            return "N/A"

    def _extrair_dia_mes(data_str):
        if not data_str:
            return None
            
        try:
            data = datetime.strptime(data_str, "%d/%m/%Y")
            return data.strftime("%d/%m")
        except ValueError:
            return None