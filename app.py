from flask import Flask, render_template, request
import matplotlib

import os
print("Caminho atual:", os.getcwd())
print("Templates existe?", os.path.exists("templates"))
print("Index existe?", os.path.exists("templates/index.html"))

# Define um backend sem interface gráfica para o matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)


def sir_model(population, beta, gamma, days):
    """
    Simula o modelo epidemiológico SIR.

    S = Suscetíveis
    I = Infectados
    R = Recuperados
    """

    # Inicialização
    susceptible = [population - 1]
    infected = [1]
    recovered = [0]

    # Simulação diária
    for _ in range(days):
        s = susceptible[-1]
        i = infected[-1]
        r = recovered[-1]

        # Novas infecções
        new_infections = (beta * s * i) / population

        # Novas recuperações
        new_recoveries = gamma * i

        # Atualização dos grupos
        s_next = s - new_infections
        i_next = i + new_infections - new_recoveries
        r_next = r + new_recoveries

        susceptible.append(s_next)
        infected.append(i_next)
        recovered.append(r_next)

    return susceptible, infected, recovered


def generate_graph(susceptible, infected, recovered):
    """
    Gera o gráfico da simulação e retorna em base64.
    """

    plt.figure(figsize=(10, 5))

    plt.plot(susceptible, label='Suscetíveis')
    plt.plot(infected, label='Infectados')
    plt.plot(recovered, label='Recuperados')

    plt.title('Modelo Epidemiológico SIR')
    plt.xlabel('Dias')
    plt.ylabel('Pessoas')
    plt.legend()
    plt.grid(True)

    # Salva o gráfico em memória
    img = io.BytesIO()
    plt.savefig(img, format='png', bbox_inches='tight')
    img.seek(0)

    # Converte para base64
    graph_url = base64.b64encode(img.getvalue()).decode()

    plt.close()

    return graph_url


@app.route('/', methods=['GET', 'POST'])
def index():
    graph = None

    # Valores padrão
    population = 1000
    beta = 0.3
    gamma = 0.1
    days = 100

    susceptible_final = 0
    infected_final = 0
    recovered_final = 0

    if request.method == 'POST':
        population = int(request.form['population'])
        beta = float(request.form['infection_rate'])
        gamma = float(request.form['recovery_rate'])
        days = int(request.form['days'])

        # Executa a simulação
        susceptible, infected, recovered = sir_model(
            population,
            beta,
            gamma,
            days
        )

        # Valores finais
        susceptible_final = int(susceptible[-1])
        infected_final = int(infected[-1])
        recovered_final = int(recovered[-1])

        # Gera gráfico
        graph = generate_graph(
            susceptible,
            infected,
            recovered
        )

    return render_template(
    'index.html',
    graph=graph,
    population=population,
    beta=beta,
    gamma=gamma,
    days=days,
    susceptible=susceptible_final,
    infected=infected_final,
    recovered=recovered_final
)


if __name__ == '__main__':
    app.run(debug=True)