# 📊 Análise Exploratória de Dados – Monitoramento de Estresse em Estudantes

Este projeto foi desenvolvido como parte da disciplina Modelagem Estatística e tem como objetivo realizar uma Análise Exploratória de Dados (EDA) no dataset Student Stress Monitoring. Disponível em https://www.kaggle.com/datasets/mdsultanulislamovi/student-stress-monitoring-datasets

A aplicação foi construída utilizando Python e Streamlit, permitindo uma visualização interativa dos resultados.

## 🎯 Objetivos

1. Explorar as variáveis relacionadas ao estresse de estudantes.
2. Identificar padrões, correlações e distribuições nos dados.
3. Criar visualizações interativas para facilitar a interpretação.
4. Aplicar conceitos estudados ao longo do primeiro bimestre da disciplina Modelagem Estatística

### 📂 Estrutura do Projeto
```
├── app.py                # Aplicação principal em Streamlit
├── requirements.txt      # Dependências do projeto
├── README.md             # Documentação
│
├── data/                 # Datasets utilizados
│
├── src/                  # Códigos visando modularização
|   ├── notebooks/            # Notebooks da análise 
│       └── eda.ipynb
│   ├── data_loader.py 
│   ├── preprocessing.py
│   ├── visualization.py
│   └── utils.py
│
└── reports/              # Relatórios
```

### ⚙️ Como executar via terminal

1. Clone o Repositório
```
git clone https://github.com/viabdon/EDA-Student-Stress-Dataset.git
cd EDA-Student-Stress-Dataset
```

2. Crie e ative um ambiente virtual (opcional, mas recomendado)
```
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Instale as dependências
```
pip install -r requirements.txt
```

5. Execute a aplicação
```
streamlit run app.py
```

5. OBS - Erros comuns: caso os comandos não funcionem, tente criar um terminal em **bash** para rodar os comandos. Outro problema comum costuma ser não ativar seu ambiente virtual, certifique-se de que no seu terminal aparece **(.venv)** antes do path dos seus comandos. Por fim, antes de executar a aplicação, recomenda-se que se cheque se as dependências foram instaladas corretamente com `pip list` e se o caminho para o interpretador python do seu ambiente virtual está selecionado corretamente.

### 📦 Dependências principais

- pandas
- numpy
- matplotlib
- seaborn
- plotly
- streamlit

### 👩‍🎓 Autores

Projeto desenvolvido por Pablo Vinícius e João Miguel como parte da disciplina de Modelagem Estatística.
