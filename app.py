import streamlit as st
from src.pre_processing import load_data
from src.visualization import (
    plot_stress_level_distribution,
    plot_correlation_heatmap,
    plot_academic_performance_vs_stress,
    plot_mental_health_factors,
    plot_social_factors,
    plot_question_heatmap_by_category,
)

# Configuração da Página
st.set_page_config(
    page_title="Dashboard de Análise de Estresse em Estudantes",
    layout="wide",
)

# Título e Introdução
st.title("Dashboard Interativo sobre Estresse Acadêmico")
st.markdown("""
Este dashboard apresenta uma análise sobre os níveis de estresse 
entre estudantes, baseada em dois datasets complementares. Acesse o repositório no [GitHub](https://github.com/viabdon/EDA-Student-Stress-Dataset.git) para mais informações!
""")

# Pre-processamento dos Dados
df_stress_levels, df_questions = load_data()

# Layout em Abas para cada Dataset
tab1, tab2 = st.tabs(
    ["Análise de Fatores Acadêmicos (Questionário)", "Análise de Níveis de Estresse"]
)


###################### Aba 1: Análise do df_questions ######################
with tab1:
    st.header("Análise de Respostas a Perguntas Específicas")
    st.markdown(
        "Este conjunto de dados contém respostas de estudantes a um questionário sobre estresse, em uma escala de 1 (Nem um pouco) a 5 (Extremamente)."
    )

    # Filtro com seleção múltipla na Aba 1
    stress_experience_options = sorted(df_questions["Estresse na Vida"].unique())
    selected_stress_exp = st.multiselect(
        "Filtro: Como você avalia o estresse experienciado recentemente?",
        options=stress_experience_options,
        default=stress_experience_options,  # Todos selecionados por padrão
    )

    # Aplicação do Filtro na Aba 1
    if selected_stress_exp:
        filtered_df_questions = df_questions[
            df_questions["Estresse na Vida"].isin(selected_stress_exp)
        ]
    else:
        filtered_df_questions = df_questions.copy()

    if filtered_df_questions.empty:
        st.warning("Nenhum dado encontrado para o filtro selecionado.")
    else:
        st.subheader("Relação entre Fatores Acadêmicos e Nível de Estresse")
        st.markdown(
            "Os heatmaps abaixo foram agrupados por categoria para melhor visualização:"
        )

        # Categorias de perguntas
        categories = {
            "Confiança e Desempenho": [
                "Confiança na Escolha",
                "Confiança no Desempenho",
                "Frequência às Aulas",
            ],
            "Carga de Trabalho e Tempo": [
                "Sobrecarga de Trabalho",
                "Conflito de Atividades",
                "Falta de Lazer",
            ],
            "Relacionamento Acadêmico": [
                "Dificuldades com Professores",
            ],
        }

        # Criar heatmaps por categoria
        for category_name, cols in categories.items():
            st.markdown(f"### {category_name}")
            fig = plot_question_heatmap_by_category(
                filtered_df_questions, cols, "Estresse na Vida"
            )
            st.plotly_chart(fig, use_container_width=True)
            st.caption(
                f"Heatmap mostrando a relação entre {category_name.lower()} e o nível de estresse experienciado."
            )
            st.divider()

###################### Aba 2: Análise do df_stress_levels ######################
with tab2:
    st.header("Análise de Fatores Psicológicos, Sociais e de Saúde Mental")
    st.markdown(
        "Este conjunto de dados mede o estresse em uma escala de 0 (baixo) a 2 (alto), correlacionando-o com diversos indicadores."
    )

    # Barra Lateral de Filtros para a Aba 2
    st.subheader("Filtro de Desempenho Acadêmico (Escala de 0 a 5)")

    # Filtro para Desempenho Acadêmico
    academic_options = ["Todos"] + sorted(
        df_stress_levels["Desempenho Acadêmico"].unique()
    )

    selected_academic = st.selectbox(
        label="Selecione seu filtro:", options=academic_options, index=0
    )

    # Aplicação dos Filtros na Aba 2
    filtered_df_levels = df_stress_levels.copy()
    if selected_academic != "Todos":
        filtered_df_levels = filtered_df_levels[
            filtered_df_levels["Desempenho Acadêmico"] == selected_academic
        ]

    if filtered_df_levels.empty:
        st.warning("Nenhum dado encontrado para os filtros selecionados.")
    else:
        # Layout em colunas
        col1, col2 = st.columns([1, 2])
        with col1:
            st.subheader("Distribuição do Nível de Estresse")
            fig_stress_dist = plot_stress_level_distribution(filtered_df_levels)
            st.plotly_chart(fig_stress_dist, use_container_width=True)

        with col2:
            st.subheader("Mapa de Calor de Correlação")
            st.markdown(
                """- Quanto mais próximo de 0, menos correlação as colunas possuem entre si. Se for negativa, uma coluna tem o comportamento inverso da outra em seus valores. """
            )
            fig_corr = plot_correlation_heatmap(filtered_df_levels)
            st.plotly_chart(fig_corr, use_container_width=True)

        st.subheader("Desempenho Acadêmico vs. Estresse")
        fig_academic_stress = plot_academic_performance_vs_stress(filtered_df_levels)
        st.plotly_chart(fig_academic_stress, use_container_width=True)

        st.divider()

        st.subheader("Análise de Fatores de Saúde Mental")
        fig_mental_health = plot_mental_health_factors(filtered_df_levels)
        st.plotly_chart(fig_mental_health, use_container_width=True)

        st.subheader("Análise de Fatores Sociais")
        fig_social_factors = plot_social_factors(filtered_df_levels)
        st.plotly_chart(fig_social_factors, use_container_width=True)
