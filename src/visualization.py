import plotly.express as px
import plotly.subplots as sp
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Define paletas de cores
PALETA_ESTRESSE = {"Baixo": "#3D85C6", "Médio": "#FF9900", "Alto": "#E06666"}

# === Funções para o Dataset 'StressLevelDataset.csv' ===


def plot_stress_level_distribution(df):
    """Cria um gráfico de pizza da distribuição do nível de estresse."""
    counts = df["Nível de Estresse"].value_counts().reset_index()
    counts.columns = ["Nível de Estresse", "Contagem"]
    fig = px.pie(
        counts,
        names="Nível de Estresse",
        values="Contagem",
        color="Nível de Estresse",
        color_discrete_map=PALETA_ESTRESSE,
        hole=0.4,
    )
    fig.update_traces(textinfo="percent+label", pull=[0.05, 0.05, 0.05])
    return fig


def plot_correlation_heatmap(df):
    """Cria e retorna a figura de um mapa de calor de correlação."""
    numeric_df = df.select_dtypes(include=["number"])
    correlation_matrix = numeric_df.corr()

    fig, ax = plt.subplots(figsize=(10, 7))
    sns.heatmap(
        correlation_matrix,
        annot=True,
        fmt=".2f",
        cmap="coolwarm",
        ax=ax,
        annot_kws={"size": 8},
    )
    plt.xticks(rotation=45, ha="right", fontsize=9)
    plt.yticks(fontsize=9)
    plt.tight_layout()
    return fig


def plot_academic_performance_vs_stress(df):
    """Cria um box plot do desempenho acadêmico vs. nível de estresse."""
    fig = px.box(
        df,
        x="Nível de Estresse",
        y="Desempenho Acadêmico",
        color="Nível de Estresse",
        color_discrete_map=PALETA_ESTRESSE,
        category_orders={"Nível de Estresse": ["Baixo", "Médio", "Alto"]},
        points="all",
    )
    fig.update_layout(
        xaxis_title="Nível de Estresse", yaxis_title="Desempenho Acadêmico (Escala)"
    )
    return fig


def plot_mental_health_factors(df):
    """Cria subplots interativos de violino (Plotly) para fatores de saúde mental."""
    factors = ["Nível de Ansiedade", "Depressão", "Autoestima"]

    # Criar figura com 3 colunas
    fig = sp.make_subplots(rows=1, cols=3, subplot_titles=factors)

    for i, factor in enumerate(factors, start=1):
        violin = px.violin(
            df,
            x="Nível de Estresse",
            y=factor,
            color="Nível de Estresse",
            box=True,  # adiciona boxplot dentro do violino
            points="all",  # mostra todos os pontos
            color_discrete_map={"Baixo": "#3D85C6", "Médio": "#FF9900", "Alto": "#E06666"},
        )

        for trace in violin.data:
            fig.add_trace(trace, row=1, col=i)

    fig.update_layout(
        title_text="Fatores de Saúde Mental vs. Nível de Estresse",
        showlegend=True,
        height=600,
    )
    return fig


def plot_social_factors(df):
    """Cria subplots interativos de violino (Plotly) para fatores sociais."""
    factors = ["Pressão Externa", "Bullying", "Suporte Social"]

    fig = sp.make_subplots(rows=1, cols=3, subplot_titles=factors)

    for i, factor in enumerate(factors, start=1):
        violin = px.violin(
            df,
            x="Nível de Estresse",
            y=factor,
            color="Nível de Estresse",
            box=True,
            points="all",
            color_discrete_map={"Baixo": "#3D85C6", "Médio": "#FF9900", "Alto": "#E06666"},
        )

        for trace in violin.data:
            fig.add_trace(trace, row=1, col=i)

    fig.update_layout(
        title_text="Fatores Sociais vs. Nível de Estresse",
        showlegend=True,
        height=600,
    )
    return fig


# === Funções para o Dataset 'Stress_Dataset.csv' ===


def plot_question_heatmap(df, x_cols, y_col):
    """Cria um heatmap mostrando a contagem de respostas cruzadas."""

    df_melted = df.melt(
        id_vars=[y_col],
        value_vars=x_cols,
        var_name="Fator Acadêmico",
        value_name="Resposta",
    )

    df_grouped = (
        df_melted.groupby([y_col, "Fator Acadêmico", "Resposta"])
        .size()
        .reset_index(name="Contagem")
    )

    order = [
        "1. Nem um pouco",
        "2. Raramente",
        "3. Às vezes",
        "4. Frequentemente",
        "5. Extremamente",
    ]
    df_grouped["Resposta"] = pd.Categorical(
        df_grouped["Resposta"], categories=order, ordered=True
    )
    df_grouped[y_col] = pd.Categorical(
        df_grouped[y_col], categories=order, ordered=True
    )

    pivot_table = df_grouped.pivot_table(
        index=["Fator Acadêmico", "Resposta"], columns=y_col, values="Contagem"
    ).fillna(0)

    fig = px.imshow(
        pivot_table,
        labels=dict(
            x="Nível de Estresse Experienciado",
            y="Fator Acadêmico e Resposta",
            color="Nº de Estudantes",
        ),
        x=sorted(df[y_col].unique()),
        y=pivot_table.index.map(lambda x: f"{x[0]} ({x[1]})"),
        text_auto=True,
        aspect="auto",
        color_continuous_scale="Reds",
    )
    fig.update_layout(height=600)
    return fig
