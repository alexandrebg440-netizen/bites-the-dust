# ================================================#
# CÓDIGO PYTHON COM TODOS OS COMANDOS PRINCIPAIS
#================================================#

# 1. COMENTARIOS
# Comentario de linha única (use #)
# Este é um comentario simples

"""
Comentario de multiplas linhas
usando aspas triplas suplas
(para docstrings ou blocos longos)
"""

'''
Aspas triplas simples tambem funcionam
para comentarios de multiplas linhas
'''

# 2. VARIÁVEIS E TIPOS DE DADOS
# Variaveis não precisam de declaração de tipo (tipagem dinâmica)

# Tipos numericos
numero_inteiro = 10              # int (inteiro)
numero_float = 10.5              # float (ponto flutuante)
numero_complexo = 3 + 4j         # complex (número complexo)

# Tipos de texto
texto = "Olá, mundo!"            # str (string)
texto_simples = 'Python'         # str tambem com asplas simples

# Tipos booleanos
verdadeiro = True                # bool (verdadeiro)
falso = False                    # bool (falso)

# Tipo None (nulo)
nulo = None                      # NoneType (nulo)

# Sequências 
lista = [1, 2, 3, 4, 5]          # list (lista - ordenada, mutável)
tupla = (1, 2, 3, 4, 5)          # tuple (tupla - ordenada, imutável)
conjunto = {1, 2, 3, 4, 5}       # set (conjunto - não ordenado, único)
dicionario = {'a': 1, 'b': 2}    # dict (dicionário - key-value)

# 3. OPERADORES
# Operadores aritméticos
soma =  10 + 5                   # +  (Adição)
subtracao = 10 - 5               # -  (Subtração)
multiplicacao = 10 * 5           # *  (Multiplicação) 
divisao = 10 / 5                 # /  (Divisão)
divisao_inteira = 10 // 3        # // (Divisão inteira)
resto_divisao = 10 % 5           # %  (Módulo - resto da divisão) 
potencia = 10 ** 5               # ** (Exponenciação)

# Operadores de comparação
igual = 10 == 5                  # == (Igual a)
diferente = 10 != 5              # != (Diferente de)
maior = 10 > 5                   # >  (Maior que)
menor = 10 < 5                   # <  (Menor que)
maior_igual = 10 >= 5            # >= (Maior ou igual a)
menor_igual = 10 <= 5            # <= (Menor ou igual a)

# Operadores lógicos
and_result = True and False      # and (E lógico) 
or_result = True or False        # or (Ou lógico)
not_result = not True            # not (Negação)

# Operadores de atribuição
x = 10                           # = (Atribuição simples)
x += 5                           # += (Atribuição de adição)
x -= 5                           # -= (Atribuição de subtração)
x *= 5                           # *= (Atribuição de multiplicação)
x /= 5                           # /= (Atribuição de divisão)

# Operadores de identidade
e_igual = x is 10                # is (Pe o mesmo objeto?) 
nao_e_igual = x is not 10        # is not (Não é o mesmo objeto?)

# Operadores de pertinência
esta_na_lista = 3 in lista      # in (esta na sequencia?)
nao_esta_na_lista = 3 not in lista  # not in (não esta na sequencia?)

# 4. ESTRUTURAS DE CONTROLE

# if, elif, else (condicionais),
idade = 18
if idade <12:
    print("Criança")
elif idade < 18:
    print("Adolescente")
else:
    print("Adulto")

# Operador ternário (if em uma linha)
mensagem = "Aprovado" if idade >= 18 else "Reprovado"

# while (loop enquanto)
contador = 0
while contador < 5:
    print(contador)
    contador += 1
    if contador == 3:
       break # sai do loop imediatamente

# for (loop para)
for i in range (5):
   print(i)

# for com lista
for item in lista:
    print(item)

# for com dicionário
for chave, valor in dicionario.items():
    print (f"{chave}: {valor}")

# continue (continua o loop mesmo após encontrar)   
for i in range (10):
    if i == 5:
        continue # continue: ignora o resto e continua o loop
    print(i)

# pass (não faz nada - placeholder)
def funcao_nao_implementada():
    pass #pass: ocupa espaço sem executar nada

# 5. FUNÇÕES
#definição de função simples
def saudacao(nome):
    return "Ola!"

# Função com argumentos
def somas(a,b):
    return a + b

#função com argumento default
def multiplicar(a, b=2):
    return a * b

#função com argumentos arbitrarios
def soma_tudo(*numero):
    total = 0
    for n in numero:
        total += n
    return total

#função com keyword arguments
def imprime_info(**info):
    for chave, valor in info.items():
        print(f"{chave}: {valor}")

# função com tipo de retorno especifico
def retornar_inteiro(x: int) -> int:
    return x 

# chamada de função
print(saudacao("Mundo"))
print(somas(10, 5))
print(multiplicar(10, 3))
print(soma_tudo(1, 2, 3, 4, 5))
imprime_info(nome="Alice", idade=30)
print(retornar_inteiro(10))

# 6. CLASSES E OBJETOS

# definição de classe
class Pessoa:
    # construtor(metodo inicializador)
    def __init__(self, nome, idade):
        self.nome = nome # self: referencia ao objeto atual
        self.idade = idade

    # método de classe
    def apresentar(self):
        return f"Ola, sou {self.nome} e tenho {self.idade} anos."
    
    # Metodo estatico
    @classmethod
    def metodo_statico():
        return "metopdo estatico"
    
    #metodo de classe
    def metodo_classe(cks):
        return "metodo de classe{cls.__name__}"
    
# Criando objeto (instancia)
pessoa1 = Pessoa("alice", 30)
print (pessoa1. apresentar())

# acesso a atribuytos
print(pessoa1.nome)
print(pessoa1.idade) 

# modificão de atributos
pessoa1.idade = 31
print(pessoa1.apresentar())

# metodo estetico e de classe
print(Pessoa.metodo_statico())
print(Pessoa.metodo_classe())

# Herança
class Estudante(Pessoa):
    def __init__(self, nome, idade, curso):
        super().__init__(nome, idade) #super():chama o construtor de pai
        self.curso = curso

    # sobrescrita de metodo
    def apresentar(self):
        return f"Sou {self.nome}, {self.idade} anos e estudo {self.curso}"  

estudante1 = Estudante("João", 20, "Engenharia")  
print(estudante1.apresentar())

# 7. processamento de listas e sequencias

# list comprehension (lista compacta)
lista_dobro = [x * 2 for x in lista]
print (lista_dobro)

# list comprehension com condição 
lista_even = [x for x in lista if x % 2 == 0 ]

# Dict comprehension 
dicionario_dobro ={k: v * 2 for k, v in dicionario.items()}
print(dicionario_dobro)

# set comprehension
set_quad = {x**2 for x in [1, 2, 3, 4, 5]}
print(set_quad)

# Map (aplica função a cada elemnto)
def dobro(x):
    return x * 2

lista_map = list(map(dobro, lista))
print (lista_map)

#Filter (filtrar elemento)
lista_filter = list (filter(lambda x: x > 2, lista))
print(lista_filter)

# Lambda (dunção anônima)
lambda_soma = lambda a, b: a + b
print(lambda_soma(5, 3))

# reduce (reduz a sequencia a um valor)
from functools import reduce
soma_reduce = reduce (lambda x, y: x + y, lista)
print(soma_reduce)

# 8 . manejo de exceçoes

# try, except, else, finally
try:
    resultado = 10 / 0 
except ZeroDivisionError:
    print("ERRO: divisão por zero!")
except Exception as e:
    print(f"Erro generico:{e}")
else:
    print("Nenhum erro ocorreu")
finally:("Executra sempre (dinal do try-except)")

#raise (levantar exceção)
def verificar_idade(idade):
    if idade < 0:
        raise ValueError("Idade não pode ser negativa")
    return idade

#try com raise
try:
    verificar_idade(-5)
except ValueError as e:
    print (f"Erro: {e}")

# 9 MODuLOS DE IMPORTS 

# import modulo inteiro
import math
print(math.sqrt(16)) #Raiz quadrada

#Import com alias
import numpy as np

# import função especifica
from math import pi, sin
print(pi)
print(sin(0))

#import de classe
from datetime import datetime
print(datetime.now())

#import relativo (para pacotes)
# from .mymodule import função

# ENTRADA E SAIDA (I/O)

#prin() - saida
print("texto na tela")
print(f"Valor formatado:{numero_inteiro}")

# input() - entrada
# nome = input("digite seu nome:") # Descomente para testar
# print(f"Ola, {nome})

# 11. MANEJO DE ARQUIVOS
 
# open() -  abre arquivo
#Modo 'w' (write) - escrever
with open ("exmplo.txt", "W", encoding="utf-8") as arquivo:
    arquivo.write("Ola, mundo!\n")
    arquivo.write(" Segunda linha")

# Modo 'r' (read) - ler
with open ("exemple.txt", "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

# Ler linha por linha
with open("exemple.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        print(linha.strip())  #strip( remove espaços extras)

# 12. FUNÇOES UTILES E METODOS

# len() - tamanho
print(len(lista)) # 5

# range() - sequencia
for i in range (1, 10, 2):
    print(i)

# enumerate() - indice e valore
for indice, valor in enumerate(lista):
    print(f"{indice}:{valor}")

# zip() - combina listas
lista2 = ['a', 'b', 'c']
for num,char in zip(lista, lista2):
    print(f"{num}: {char}")

# sorted() ordena
lista_ordenada = sorted([3, 1, 4, 2, 5])
print(lista_ordenada)

# reversed() - reverte
lista_reversa = list(reversed(lista))
print(lista_reversa)

# any() e all()
print(any([False, True, False]))  # True (alguem é true)
print(all([True, True, True]))    # True(todas são true)

#isinstance( - verificar tipo)

print(isinstance(numero_inteiro, int))  #True
print(isinstance(texto, str))           #True

# type(  - tipo de variavel)
print(type(numero_inteiro))
print(type(texto))

#str(), int(), float() - conversão
texto_num = "123"
print(int(texto_num))    #123
print(float(texto_num))  #123.0

#lis(), tuple(), set( ), dict(),- conversão de  tipos
print(list("abc"))
print(tuple([1, 2, 3]))
print(set([1, 2, 2, 3]))

# 13 Metodo de lista
lista.append(6)         # adiciona ao final
lista.extend([7, 8])    #adiciona multiplos
lista.insert(0, 0)      # adiciona posição
lista.remove(0)         #remove primeiro elemento igual
valor = lista.pop()     #remove e retorna ultimo
lista.clear()           #remove todos
lista.index(2)          #retorna indice
lista.count(2)          #conta ocorrencias
lista.sort              # ordena
lista.reverse           #reverte 
lista.copy              #copia lista

# 14. METODOS DE STRING
texto = " Ola, mundo!"
print(texto.upper())
print(texto.lower())
print(texto.strip())
print(texto.replace)
print(texto.split)
print(texto.find)
print(texto.startswith)
print(texto.endswith)
print(texto.isalnum)
print(texto.isalpha)
print(texto.isdigit)
print(texto.isspace)

# METODO DE DICIONARIO

dicionario.keys()
dicionario.values()
dicionario.items()
dicionario.get()
dicionario.update()
dicionario.pop()
dicionario.popitem()
dicionario.clear()
dicionario.copy()

#16 operador de decomposição

a, b, c = [1, 2, 3, 4]
print(a, b, c)

primeiro, * resto = [1,2, 3, 4]

#17 .generator
def gerador():
    for i in range(5):
        yield i

for num in gerador():
   print(num)

#18 decoradores
def meu_decorador(funcao):
    def wrapper():
        print(" Antes de função")
        funcao()
        print(" depois da função")
    return wrapper

meu_decorador
def funcao_decorada():
    print("Função executada")

funcao_decorada()

# ASSERT(verificação)
x = 10
assert x ==10,  "x deve ser 10"

#walrus operador
while (n:= len(lista)) < 10:
    lista.append(n)

#=================================
#          FIM DO CODIGO
#=================================
print("Todos os comandos Python foram demonstrados!")
