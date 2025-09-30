# Relatório de Análise Exploratória: Fatores Associados ao Estresse Estudantil

### 1. Resumo Executivo

Esta análise investigou os fatores determinantes para o estresse em estudantes, utilizando dois datasets complementares. Embora a percepção inicial de 91% dos estudantes seja de que seu estresse é "positivo" (Eustress), a análise aprofundada revela um cenário mais complexo. Os resultados indicam que o estresse não é uma condição aleatória, mas uma consequência direta de fatores sociais e de saúde mental. A falta de apoio social e a exposição ao bullying emergiram como os preditores mais fortes de estresse elevado. Além disso, há uma correlação alarmante e positiva entre altos níveis de estresse e indicadores severos de depressão e ansiedade. A conclusão principal é que o bem-estar estudantil está mais associado à qualidade do ecossistema social do que a fatores puramente acadêmicos, desafiando a noção de que o estresse vivenciado é majoritariamente benéfico.

### 2. Introdução e Objetivos

O objetivo desta análise foi explorar os fatores que influenciam os níveis de estresse em estudantes. Para isso, foram utilizados dois conjuntos de dados:

    Stress_Dataset.csv: Um questionário com respostas em escala de 1 a 5, focado na frequência de sentimentos e situações.

    StressLevelDataset.csv: Um dataset com métricas de saúde mental, social e fisiológica, e uma variável-chave de nível de estresse (0 a 2).

A análise foi segmentada para entender como o estresse se relaciona com o desempenho acadêmico, a saúde mental e os fatores sociais.

### 3. Principais Observações (Key Findings)

A análise revelou padrões claros e, por vezes, contraintuitivos sobre o estresse estudantil.

- **3.1. Percepção Geral do Estresse**
A população estudantil mostrou-se quase perfeitamente dividida entre os três níveis de estresse: Sem Estresse (33,9%), Estresse Alto (33,5%) e Normal/Moderado (32,5%). O dado mais surpreendente é que 91% dos estudantes relataram seu estresse como "positivo" (Eustress), que em teoria os motiva. Esta percepção contrasta fortemente com os impactos negativos observados em outras áreas.

- **3.2. Fatores Acadêmicos e o Estresse**
Contrariando a hipótese inicial de que o estresse impacta diretamente o desempenho, a relação mostrou-se mais complexa:

    Frequência e Confiança: Fatores como a frequência às aulas e a confiança no desempenho ou na escolha do curso não apresentaram uma relação linear com o estresse. Notavelmente, estudantes com menor dúvida sobre suas escolhas acadêmicas e com alta frequência às aulas apresentaram, em alguns casos, níveis de estresse moderado mais elevados, sugerindo que o estresse pode estar ligado a um nível de desafio saudável ou a uma forma de autossabotagem.

    Conflito de Atividades: O conflito entre atividades acadêmicas e extracurriculares foi o fator acadêmico com a correlação mais forte com o estresse (0.407). Cerca de 42% dos estudantes com estresse alto também relataram sentir frequentemente este conflito, indicando que a má gestão do tempo e o excesso de compromissos são causas significativas de estresse.

- **3.3. Impacto na Saúde Mental**
Esta foi a área com as correlações mais fortes e preocupantes:

    Depressão e Ansiedade: A análise mostrou uma correlação positiva e alarmante entre estresse e sintomas de depressão (0.745) e ansiedade (0.716). Estudantes com depressão e ansiedade altas estão massivamente concentrados no grupo de "High Stress". A combinação de alta depressão e alta ansiedade resultou em 93,6% dos estudantes desse subgrupo apresentando estresse elevado.

    Autoestima: A relação com a autoestima foi não-linear. Estudantes com estresse "Normal/Moderado" apresentaram a melhor média de autoestima, enquanto os sem estresse tiveram a pior. A hipótese é que o estresse moderado, ligado a desafios superados, pode fortalecer a autoestima, enquanto a ausência de estresse pode estar ligada à apatia.

    Histórico de Saúde Mental: Este é um preditor extremamente forte. 60,7% dos estudantes com histórico de problemas de saúde mental relataram estresse alto, enquanto 60% dos estudantes sem histórico relataram ausência de estresse, mostrando uma clara inversão de comportamento.

- **3.4. Fatores Sociais como Preditores de Estresse**
A análise de proporcionalidade revelou que o ambiente social é o principal determinante do estresse:

    Apoio Social (Fator de Proteção): A falta de apoio social está diretamente ligada ao estresse: 83% dos estudantes com baixo apoio sofrem de estresse alto. Em contrapartida, um alto nível de apoio praticamente elimina o estresse elevado.

    Bullying e Pressão (Estressores Primários): Níveis elevados de bullying e pressão externa estão associados a uma probabilidade de quase 90% de o estudante sofrer de estresse alto.

    Interação de Fatores: A evidência mais contundente veio da combinação de fatores: no subgrupo de estudantes com alto bullying e baixo apoio social, 94,5% apresentam estresse alto. No cenário oposto, com baixo bullying e alto apoio social, a incidência de estresse alto é de 0%.

## 4. Conclusão e Recomendações

A análise conclui que, embora muitos estudantes percebam seu estresse como um fator motivacional "positivo", os dados demonstram que níveis elevados de estresse estão inegavelmente ligados a condições adversas de saúde mental e a um ambiente social negativo.

O estresse severo não é uma condição aleatória, mas uma consequência direta do equilíbrio entre estressores (bullying, pressão externa, conflito de atividades) e fatores de proteção (principalmente o apoio social). A forte correlação com depressão e ansiedade indica que o estresse elevado é um claro indicador de sofrimento psíquico, e não de desempenho otimizado.

- **Recomendações para futuras análises**:

    Explorar como os fatores preditores se inter-relacionam (ex: o excesso de atividades extracurriculares impacta a frequência às aulas?).

    Analisar subgrupos específicos para entender comportamentos mais detalhados (ex: como um aluno com depressão lida com a sobrecarga acadêmica em comparação a um com alto suporte social?).

Em suma, a mitigação do estresse estudantil severo parece depender mais da construção de um ecossistema acadêmico seguro e com redes de apoio fortalecidas do que apenas da resiliência individual do aluno.