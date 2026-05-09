Simulação da Propagação de Doenças Infecciosas com Modelo SIR em Aplicação Web com Flask
1. Resumo

Este artigo apresenta uma aplicação web educacional para simulação da propagação de doenças infecciosas utilizando o modelo epidemiológico SIR (Susceptíveis-Infectados-Recuperados). A ferramenta foi desenvolvida em Python, utilizando o framework Flask no backend, HTML e CSS na interface web e a biblioteca Matplotlib para geração de gráficos dinâmicos.

A aplicação permite a parametrização de variáveis como população inicial, taxa de infecção, taxa de recuperação e duração da simulação, possibilitando a análise do comportamento dinâmico da propagação da doença ao longo do tempo.

Os resultados obtidos evidenciam a evolução típica das curvas S, I e R, caracterizando o processo de disseminação e posterior estabilização da infecção. O projeto possui caráter educacional, visando facilitar a compreensão de conceitos fundamentais de epidemiologia computacional.

2. Introdução

A modelagem matemática de doenças infecciosas constitui uma ferramenta essencial na epidemiologia moderna, permitindo compreender e prever a dinâmica de propagação de agentes patogênicos em populações. Entre os modelos clássicos, destaca-se o modelo SIR, amplamente utilizado para descrever a evolução de epidemias em populações fechadas.

Com o avanço das tecnologias computacionais e o crescimento de aplicações web interativas, tornou-se possível o desenvolvimento de ferramentas educacionais capazes de auxiliar no ensino desses conceitos. Neste contexto, este trabalho propõe uma aplicação web baseada em Flask que simula o comportamento de uma epidemia utilizando o modelo SIR, permitindo a exploração interativa de diferentes cenários epidemiológicos.

3. Modelo SIR (Fundamentação Teórica)

O modelo SIR divide a população em três compartimentos:

S(t): indivíduos suscetíveis à infecção
I(t): indivíduos infectados e capazes de transmitir a doença
R(t): indivíduos recuperados e imunizados

O modelo é descrito pelo seguinte sistema de equações diferenciais:

$$
\frac{dS}{dt} = -\beta \frac{S I}{N}
$$

$$
\frac{dI}{dt} = \beta \frac{S I}{N} - \gamma I
$$

$$
\frac{dR}{dt} = \gamma I
$$

Onde:

β (beta) representa a taxa de infecção
γ (gamma) representa a taxa de recuperação
N é a população total

O sistema assume uma população fechada, sem nascimentos ou mortes naturais, e imunidade permanente após a recuperação. O modelo é resolvido numericamente por meio de discretização temporal.

4. Metodologia / Implementação
4.1 Uso do Flask

A aplicação foi desenvolvida utilizando o framework Flask, responsável pela criação do backend e gerenciamento das rotas HTTP. A rota principal ("/") recebe dados do usuário por meio de formulários HTML e executa a simulação com base nos parâmetros fornecidos.

4.2 Interface Web

A interface foi desenvolvida utilizando HTML e CSS, com foco em simplicidade e usabilidade. O usuário pode definir parâmetros como população inicial, taxa de infecção, taxa de recuperação e número de dias de simulação. Os resultados são exibidos dinamicamente na própria página.

4.3 Simulação Computacional

A simulação é realizada por meio de um método iterativo baseado em diferenças finitas, aproximando numericamente as equações diferenciais do modelo SIR. A cada iteração temporal, os valores de S, I e R são atualizados de acordo com as taxas de infecção e recuperação.

4.4 Geração de Gráficos

A biblioteca Matplotlib é utilizada para gerar as curvas epidemiológicas. Os gráficos são armazenados em memória e convertidos para base64, permitindo sua exibição direta na interface web sem necessidade de arquivos externos, facilitando a integração entre backend e frontend.

5. Resultados

Os resultados obtidos demonstram o comportamento clássico do modelo SIR. Inicialmente, observa-se um grande número de indivíduos suscetíveis e poucos infectados. Ao longo da simulação, ocorre um crescimento acelerado dos infectados, seguido por uma redução progressiva devido ao aumento dos recuperados.

As curvas apresentam o seguinte comportamento:

Suscetíveis (S): decrescem continuamente
Infectados (I): crescem até um pico e depois diminuem
Recuperados (R): aumentam até estabilização

Esse comportamento reflete a dinâmica típica de epidemias, caracterizada por uma fase inicial de propagação acelerada e posterior contenção natural da infecção.

6. Conclusão

Conclui-se que o sistema desenvolvido cumpre seu objetivo educacional ao permitir a visualização interativa da propagação de doenças infecciosas por meio do modelo SIR.

A utilização de Python, Flask e Matplotlib demonstrou-se adequada para a construção de uma aplicação simples e funcional, capaz de simular cenários epidemiológicos de forma intuitiva.

Como trabalhos futuros, propõe-se a expansão do modelo para incluir fatores adicionais, como mortalidade, vacinação e mobilidade populacional, tornando a simulação mais realista.
