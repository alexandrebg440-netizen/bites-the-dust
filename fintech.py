import numpy as np

#==========================
#Banco simulado
#==========================

class Usuario:
    def __init__(self, nome):
        self.nome = nome
        self.saldo = 0
        self.carteira = {
            "acoes": 0.4,
            "renda_fixa": 0.4,
            "ouro": 0.1,
            "dolar": 0.1
        }
        self.historico = []
    
    def depositar(self, valor):
        self.saldo += valor

    def investir(self):
        retorno = {
            "acoes":np.random.normal(0.012, 0.05),
            "renda_fixa":np.random.normal(0.008, 0.01),
            "ouro":np.random.normal(0.006, 0.03),
            "dolar":np.random.normal(0.005, 0.02)
        }

        ganho = 0

        for ativo, peso in self.carteira.items():
            ganho += self.saldo * peso * retorno[ativo]
        
        self.saldo += ganho
        self.historico.append(self.saldo)

    def resumo(self):
        print(f"\n Usuario: {self.nome}")
        print(f" Saldo atual: R${self.saldo:,.2f}")
        print(f"Historico: {len(self.historico)} ciclos")


#================
#SIstema fintech
#================

class Fintech:
    def __init__(self):
        self.usuario = {}

    def criar_usuario(self, nome):
        self.usuario[nome] = Usuario(nome)
        print(f"Usuario {nome} criado")

    def depositar(self, nome, valor):
        self.usuario[nome].depositar(valor)

    def rodar_mes(self):
        for u in self.usuario.values():
            u.investir()

    def ranking(self):
        print("\n RANKING DE USUÁRIOS")
        ordenado = sorted(self.usuario.values(), key=lambda x: x.saldo, reverse=True)

        for i, u in enumerate(ordenado):
            print(f"{i+1}. {u.nome} - R$ {u.saldo:,.2f}")


#=====================
#demo do sitema
#=====================

app = Fintech()

app.criar_usuario("João")
app.criar_usuario("Maria")
app.criar_usuario("Carlos")

app.depositar("João", 10000)
app.depositar("Maria", 10000)
app.depositar("Carlos", 10000)

#simular 24 meses
for _ in range(24):
    app.rodar_mes()

app.ranking()
