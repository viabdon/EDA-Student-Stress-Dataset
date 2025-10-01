import pandas as pd
import streamlit as st


@st.cache_data
def load_data():
    """
    Carrega os dois datasets, renomeia colunas para português e mapeia
    valores categóricos para melhor legibilidade.
    """
    try:
        # Dataset 1: Níveis de Estresse
        df_stress_levels = pd.read_csv("src/archive/StressLevelDataset.csv")

        rename_dict_levels = {
            "anxiety_level": "Nível de Ansiedade",
            "self_esteem": "Autoestima",
            "mental_health_history": "Histórico de Saúde Mental",
            "depression": "Depressão",
            "headache": "Dor de Cabeça",
            "blood_pressure": "Pressão Sanguínea",
            "sleep_quality": "Qualidade do Sono",
            "breathing_problem": "Problema Respiratório",
            "noise_level": "Nível de Ruído",
            "living_conditions": "Condições de Moradia",
            "safety": "Segurança",
            "basic_needs": "Necessidades Básicas",
            "academic_performance": "Desempenho Acadêmico",
            "study_load": "Carga Horária de Estudos",
            "teacher_student_relationship": "Relação Professor-Aluno",
            "future_career_concerns": "Preocupações com a Carreira",
            "social_support": "Suporte Social",
            "peer_pressure": "Pressão Externa",
            "extracurricular_activities": "Atividades Extracurriculares",
            "bullying": "Bullying",
            "stress_level": "Nível de Estresse Num",
        }
        df_stress_levels = df_stress_levels.rename(columns=rename_dict_levels)

        df_stress_levels["Histórico de Saúde Mental"] = df_stress_levels[
            "Histórico de Saúde Mental"
        ].map({0: "Não", 1: "Sim"})
        df_stress_levels["Nível de Estresse"] = df_stress_levels[
            "Nível de Estresse Num"
        ].map({0: "Baixo", 1: "Médio", 2: "Alto"})

        # Dataset 2: Questionário de Estresse
        df_questions = pd.read_csv("src/archive/Stress_Dataset.csv")

        rename_dict_questions = {
            "Have you recently experienced stress in your life?": "Estresse na Vida",
            "Do you lack confidence in your choice of academic subjects?": "Confiança na Escolha",
            "Do you attend classes regularly?": "Frequência às Aulas",
            "Do you lack confidence in your academic performance?": "Confiança no Desempenho",
            "Do you feel overwhelmed with your academic workload?": "Sobrecarga de Trabalho",
            "Are you facing any difficulties with your professors or instructors?": "Dificuldades com Professores",
            "Academic and extracurricular activities conflicting for you?": "Conflito de Atividades",
            "Do you struggle to find time for relaxation and leisure activities?": "Falta de Lazer",
        }
        df_questions = df_questions.rename(columns=rename_dict_questions)

        frequencia_dict = {
            1: "1. Nem um pouco",
            2: "2. Raramente",
            3: "3. Às vezes",
            4: "4. Frequentemente",
            5: "5. Extremamente",
        }

        cols_to_map = list(rename_dict_questions.values())
        for col in cols_to_map:
            df_questions[col] = df_questions[col].map(frequencia_dict)

        return df_stress_levels, df_questions

    except FileNotFoundError as e:
        st.error(
            f"Erro ao carregar o arquivo: {e.filename}. Certifique-se de que os CSVs estão em 'src/archive/'."
        )
        return pd.DataFrame(), pd.DataFrame()
