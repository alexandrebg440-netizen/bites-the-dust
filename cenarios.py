import numpy as np
import matplotlib.pyplot as plt

#=====================================================
#Simulaçâo de cenarios
#=====================================================

cenarios = {
    "normal": {
        "rf": 0.14,
        "acos": 0.12,
        "dolar": 0.05,
        "ouro": 0.06
    },
    "otimista": {
        "rf": 0.13,
        "acos": 0.18,
        "dolar": 0.08,
        "ouro": 0.10
    },
    "crise": {
        "rf": 0.14,
        "acos": -0.05,
        "dolar": 0.15,
        "ouro": 0.12
    }
}

#=====================================================
#Perfis de investidor
#=====================================================

perfis = {
    "conservador": {
        "rf": 0.70,
        "acos": 0.10,
        "dolar": 0.10,
        "ouro": 0.10
    },
    "moderado": {
        "rf": 0.50,
        "acos": 0.25,
        "dolar": 0.15,
        "ouro": 0.10
    },
    "agressivo": {
        "rf": 0.30,
        "acos": 0.40,
        "dolar": 0.20,
        "ouro": 0.10
    }
}

#=====================================================
#simuladore monte carlo simples
#=====================================================

def simular(perfil, cenario, inicial, aporte, meses, n_sim=50):
    resultados = []

    for _ in range(n_sim):
        saldo = inicial
        historico = []

        for _ in range(meses):
            #aportes
            saldo += aporte

            #retorno ponderado do perfil + cenario
            retorno = (
                perfil["rf"] * cenario["rf"] +
                perfil["acos"] * cenario["acos"] +
                perfil["dolar"] * cenario["dolar"] +
                perfil["ouro"] * cenario["ouro"]
            )

            #volatilidade aleatoria
            ruido = np.random.normal(0,0.02)  # Ruído aleatório para simular volatilidade

            saldo *= (1 + retorno / 12 + ruido)

            historico.append(saldo)

        resultados.append(historico)

    return np.array(resultados)


#=====================================================
#entrada
#=====================================================

inicial = float(input("Valor inicial (R$): "))
aporte = float(input("Aporte mensal (R$): "))
meses = int(input("Quantidade de meses: "))

#=====================================================
#execução + grafico
#=====================================================

dados_finais = {}
nomes_barras = []

for nomes_perfil, perfil in perfis.items():
    dados_finais[nomes_perfil] = []

    for nomes_cenario, cenario in cenarios.items():
        sim = simular(perfil, cenario, inicial, aporte, meses)
        media = sim.mean(axis=0)
        final = media[-1]

        dados_finais[nomes_perfil].append(final)
        label = f"{nomes_perfil} - {nomes_cenario}"

        print(f"\n {label}")
        print(f"Final Médio: R$ {final:.2f}")

    if not nomes_barras:
        nomes_barras = list(cenarios.keys())

# Criar grafico de culunas agrupadas
plt.figure(figsize=(12, 6))

x = np.arange(len(nomes_barras))
largura = 0.25

for i, (perfil, valores) in enumerate(dados_finais.items()):
    plt.bar(x + i * largura, valores, largura, label=perfil)

plt.title("Simulação de Investumentos - Valor Final por Perfil e Cenário")
plt.xlabel("Cenário")
plt.ylabel("Patrimônio Final (R$)")
plt.xticks(x + largura, nomes_barras)
plt.legend()
plt.grid(axis="y", alpha=0.3)

plt.tight_layout()
plt.show()
