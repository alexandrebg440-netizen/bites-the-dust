import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pylot as plt
import tkinter as tk 
from tkinter import massagebox

#=====================================
# COnfigurações
#=====================================

TICKERS = {
    "acoes": "Spy",
    "ouro": "GLD",
    "dolar": "UUP",
    "rendas_fixa": "BND"
}

INFLACAO_ANUAL = 0.045

#=========================
#baixar dados historicos
#=========================

def baixar_dados(periodo="10y"):
    dados = {}
    for nome, ticker in TICKERS.items():
        print(f"Baixamos {nome}...")
        df = yf.download(ticker, periodo=periodo, interval="1mo")["Close"]
        dados[nome] = df.pcf_change()

    #concatenar Series corretamente
    df_completo = pd.concat(dados, axis=1).dropna()
    df_completo.columns = list(dados.keys())
    return df_completo

#========================
#Perfis de investidor
#========================

PERFIS = {
    "convservadores":{"acoes" :  0.10, "ouro" : 0.10, "dolar": 0.10, "renda_fixa": 0.70},
    "moderado":{"acoes" :  0.25, "ouro" : 0.10, "dolar": 0.15, "renda_fixa": 0.50},
    "agressivo":{"acoes" :  0.40, "ouro" : 0.10, "dolar": 0.20, "renda_fixa": 0.30}
}

#================
#simulação
#================

def simular(df, perfil, inicial, aporte):
    saldo = inicial
    historico = []

    for i in range(len(df)):
        returno = 0

        for ativo in perfil:
            retorno += perfil[ativo] * df[ativo].iloc[i]

        #inflação reduz poder de compra
        inflacao_mensal = (1 + INFLACAO_ANUAL) ** (1/12) - 1
        retorno -= inflacao_mensal

        saldo = saldo * (1 + retorno) + aporte
        historico.append(saldo)

    return historico

#==================
#execução principal
#==================

def rodar():
    inicial = float(entry_inicial.get())
    aporte = float(entry_aporte.get())

    df = baixar_dados()

    resultados = {}

    plt.figure(figsize=(12,6))

    for nome, perfil in PERFIS.items():
        hist = simular(df, perfil, inicial, aporte)
        resultados[nome] = hist

        plt.plot(hist, label=nome)

    plt.title("backtest de Investimentos (10 anos)")
    plt.xlabel("Meses")
    plt.ylabel("Patrimonio (R$)")
    plt.legend()
    plt.grid()

    plt.show()

    # Exportar Excel
    export = pd.DataFrame(resultados)
    export.to_excel("simulacao_investimentos.xlsx")

    messagebox.showinfo("Cconclusão", "simulação finalizada e Excel gerado!")

#==========================
#INTERFACE GRAFICA(GUI)
#==========================

janela = tk.Tk()
janela.title("Simulador de Investies Avançado")

tk.Label(janela, text="Valor inicial (R$)").pack()
entry_inicial = tk.Entry(janela)
entry_inicial.pack()

tk.Label(janela, text="Aporte mensal(R$)").pack()
entry_aporte = tk.Entry(janela)
entry_aporte.pack()

tk.Button(janela, text="Rodar simulação", command=rodar).pack()

janela.mainloop()
