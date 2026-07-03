def simular_investimentos(nome, carteira, valor_inicial, aporte_mensal, meses):
    '''
    carteira = dicionário com percentuais e taxas anuais estimadas
    '''

    # converte taxa anual para mensal
    def taxa_mensal(taxa_anual):
        return (1 + taxa_anual) ** (1/12) - 1
    
    # Inicializa valores por classe
    valores = {ativo: valor_inicial * pct for ativo, pct in carteira['alocacao'].items()}

    for _ in range(meses):
        #rendimento de cada ativo
        for ativo in valores:
            valores[ativo] *= (1 + taxa_mensal(carteira['taxas'][ativo]))

        # aporte mensal dividido pela carteira
        for ativo in valores:
            valores[ativo] += aporte_mensal * carteira['alocacao'][ativo]

    total = sum(valores.values())

    print(f'\n Perfil: {nome}')
    print('-' * 40)
    for ativo, valor in valores.items():
        print(f'{ativo:15}: R$ {valor:,.2f}')
    print('-' * 40)
    print(f'Total final: R$ {total:,.2f}')
    return total


# =============================
# PERFIS DE INVESTIDOR
# =============================

perfis = {
    'Conservador': {
        'alocacao': {
            'Renda Fixa': 0.70,
            'Dólar/Euro': 0.10,
            'Ouro': 0.10,
            'Ações': 0.10
        },
        'taxas': {
            'Renda Fixa': 0.14,
            'Dólar/Euro': 0.05,
            'Ouro': 0.06,
            'Ações': 0.10
        }
    },

    'Moderado': {
        'alocacao': {
            'Renda Fixa': 0.50,
            'Dólar/Euro': 0.15,
            'Ouro': 0.10,
            'Ações': 0.25
        },
        'taxas': {
            'Renda Fixa': 0.14,
            'Dólar/Euro': 0.05,
            'Ouro': 0.06,
            'Ações': 0.12
        }
    },

    'Agressivo': {
        'alocacao': {
            'Renda Fixa': 0.30,
            'Dólar/Euro': 0.20,
            'Ouro': 0.10,
            'Ações': 0.40
        },
        'taxas': {
            'Renda Fixa': 0.14,
            'Dólar/Euro': 0.06,
            'Ouro': 0.06,
            'Ações': 0.15
        }
    }
}

# ============================
#  ENTRADAS DO USÁRIO
# ============================

valor_inicial = float(input('Valor inicial: R$ '))
aporte_mensal = float(input('Aporte mensal: R$ '))
meses = int(input('Meses de investimento: '))

# ============================
# SIMULAÇÃO
# ============================

resultados = {}

for nome, carteira in perfis.items():
    total = simular_investimentos(nome, carteira, valor_inicial, aporte_mensal, meses)
    resultados[nome] = total

# ============================
# MELHOR RESULTADO
# ============================

melhor = max(resultados, key=resultados.get)

print('\n MELHOR PERFIL NO PERÍODO')
print(f'{melhor} -> R$ {resultados[melhor]:,.2f}')
