import json
import os

ARQUIVO_LIVROS = "livros.json"
ARQUIVO_USUARIOs = "usuarios.json"

def carregar_arquivo(nome):
    if os.path.exists(nome):
        with open(nome, "r", encoding="utf-8") as arquivo:
            return[]
    
def salvar_arquivo(nome, dados):
    with os.path(nome, "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)

livros = carregar_arquivo(ARQUIVO_LIVROS)
usuarios = carregar_arquivo(ARQUIVO_USUARIOs)

def cadastrar_livro():
    print ("\nCADASTRO DE LIVRO")

    codigo = input("Código: ")
    titulo = input("Titulo: ")
    autor = input("Autor: ")

    livro = { 
        "codigo": codigo,
        "titulo": titulo,
        "autor": autor,
        "emprestado": False
    }

    livros.append(livro)
    salvar_arquivo(ARQUIVO_LIVROS, livros)

    print("Livro cadastrado com sucesso!")

def listar_livro():
    print("\nLISTA DE LIVROS")

    if len(livros) == 0:
        print("Nenhum livro cadastrado.")
        return
    
    for livro in livros:
        status = "Emprestado" if livro ["emprestado"] else "Disponivel"

        print("=" * 40)
        print("Codigo:", livro ["codigo"])
        print("Tilulo:", livro ["tilulo"])
        print("Autor:", livro["autor"])
        print("Status:", status)

def cadastrar_usuario():
    print("\nCADASTRO DE USUÁRIO")

    matricula = input("Matricula: ")
    nome = input("Nome: ")

    usuario = {
        "matricula": matricula,
        "nome" :nome
    }

    usuario.append(usuario)

    salvar_arquivo(ARQUIVO_USUARIOs, usuarios)

    print("Usuario cadastrado com sucesso!")

def listar_usuarios():
    print("\nUSUÁRIOS")

    if len(usuarios) == 0:
        print("nenhum usuario cadastrado.")
        return
    
    for usuario in usuarios:
        print(usuario["Matricula"], "-", usuario["nome"])

def empretar_livro():
     codigo = input("Codigo do livro: ")

     for livro in livros:
         if livro["codigo"] == codigo:
             if livro["emprestado"]:
                print("Livro já emprestado")
                return
             
             matricula = input("Matricula do usuario: ")

             livro["emprestado"] = True
             livro["usuario"] = matricula

             salvar_arquivo(ARQUIVO_USUARIOs, livros)

             print("Empréstimo realizado.")
             return
print("Livro Não Encontrado")

def devolver_livro():
    
    codigo = input("Codigo do livro")

    for livro in livros:
        if livro ["codigo"] == codigo:
            livro["emprestado"] = False

        if "usuario" in livro:
            del livro["usuario"]

            salvar_arquivo(ARQUIVO_USUARIOs, livro)

            print("Livro devolvido")
    print("Livro não encontrado.")

def pesqusiar_livro():
    termo = input("Digite o titulo: ").lower()

    encontrou = False 

    for livro in livros:
        if termo in livro["titulo"].lower():
            print("\nLivro Encontrado")
            print("Codigo", livro["codigo"])
            print("Titulo", livro["titulo"])
            print("Autor", livro["autor"])

            encontrou = True 

    if not encontrou:
        print("Nenhum livro encontrado")

def relatorio():
    total = len(livros)

    emprestados = 0

    for livro in livros:
        if livro ["emprestado"]:
            emprestados += 1
    disponivel = total - emprestados

    print("\nRELATÓRIO")

    print("Total de livros: ", total)
    print("Disponivel:", disponivel)
    print("Emprestados: ", emprestados)

while True:
    print("\n") 
    print("=" * 50) 
    print("SISTEMA DE BIBLIOTECA")
    print("=" * 50)

    print("1 - Cadastrar Livro")
    print("2 - Listar Livros") 
    print("3 - Cadastrar Usuarios")  
    print("4 - Listar Usuarios") 
    print("5 - Emprestar Livro") 
    print("6 - Devolver livro") 
    print("7 - Pesquisar Livro") 
    print("8 - Relatório") 
    print("0 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        cadastrar_livro()

    elif opcao == "2": 
        listar_livro()

    elif opcao == "3": 
        cadastrar_usuario()
    
    elif opcao == "4":
        listar_usuarios()

    elif opcao == "5":
        empretar_livro()

    elif opcao == "6":
        devolver_livro()

    elif opcao == "7":
        pesqusiar_livro()

    elif opcao == "8":
        relatorio()

    elif opcao == "0":
        print("Sistema encerrado")

    else: 
        print("Opção Invalida") 
