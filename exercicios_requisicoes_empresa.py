import os
import requests
import questionary  
from rich.console import Console
from rich.table import Table

url_base = "https://api.franciscosensaulas.com"
url_empresa = f"{url_base}/api/v1/empresa"
url_produto = f"{url_empresa}/produtos"

def menu():
    opcoes_menu_empresa = [
        "Consultar todas as Empresas",
        "Consultar empresa por id",
        "Consultar empresa por nome",
        "Consultar empresa por cnpj",
        "Cadastrar Empresa",
        "Editar Empresa",
        "Apagar Empresa",
        "Menu Produtos",
        "Sair"
    ]

    menu_empresa_escolhido = ""

    while menu_empresa_escolhido != "Sair":
        menu_empresa_escolhido = questionary.select("Menu", choices=opcoes_menu_empresa).ask()
        limpar_terminal()

        if menu_empresa_escolhido == "Consultar todas as Empresas":
            consultar_empresas()
        elif menu_empresa_escolhido == "Consultar empresa por id":
            consultar_empresa_id()
        elif menu_empresa_escolhido == "Consultar empresa por nome":
            consultar_empresa_nome()
        elif menu_empresa_escolhido == "Consultar empresa por cnpj":
            consultar_empresa_cnpj()
        elif menu_empresa_escolhido == "Cadastrar Empresa":
            cadastrar_empresa()
        elif menu_empresa_escolhido == "Editar Empresa":
            editar_empresa()
        elif menu_empresa_escolhido == "Apagar Empresa":
            apagar_empresa()
        elif menu_empresa_escolhido == "Menu Produtos":
            menu_produto()

        
        if menu_empresa_escolhido != "Sair":
            questionary.press_any_key_to_continue(
                "Digite qualquer tecla para continuar..."
            ).ask()
            limpar_terminal()


def menu_produto():
    opcoes_menu_produto = [
        "Consultar todos os Produtos",
        "Consultar produto por id",
        "Consultar produto(s) por nome",
        "Consultar produtos por categoria",
        "Cadastrar Produto",
        "Editar Produto",
        "Apagar Produto",
        "Voltar"
    ]

    menu_produto_escolhido = ""

    while menu_produto_escolhido != "Voltar":
        menu_produto_escolhido = questionary.select("Menu Produto", choices=opcoes_menu_produto).ask()
        limpar_terminal()

        if menu_produto_escolhido == "Consultar todos os Produtos":
            consultar_produtos()
        elif menu_produto_escolhido == "Consultar produto por id":
            consultar_produto_id()
        elif menu_produto_escolhido == "Consultar produto(s) por nome":
            consultar_produto_nome()
        elif menu_produto_escolhido == "Consultar produtos por categoria":
            consultar_produto_categoria()
        elif menu_produto_escolhido == "Cadastrar Produto":
            cadastrar_produto()
        elif menu_produto_escolhido == "Editar Produto":
            editar_produto()
        elif menu_produto_escolhido == "Apagar Produto":
            apagar_produto()


        if menu_produto_escolhido != "Voltar":
            questionary.press_any_key_to_continue(
                "Digite qualquer tecla para continuar..."
            ).ask()
            limpar_terminal()
        

def consultar_produtos():
    resposta = requests.get(url_produto)

    console = Console()

    table = Table(show_header=True, header_style="bold blue", show_lines=True)
    table.add_column("id")
    table.add_column("Nome")
    table.add_column("Preço")
    table.add_column("Categoria")

    produtos = resposta.json()

    for produto in produtos:
        table.add_row(str(produto["id"]), produto["nome"], str(produto["preco"]), produto["categoria"])

    console.print(table)


def consultar_produto_id():
    id_selecionado = int(questionary.text("Digite o id para consultar esta empresa: ").ask())

    resposta = requests.get(url_produto)

    console = Console()

    table = Table(show_header=True, header_style="bold blue", show_lines=True)
    table.add_column("ID")
    table.add_column("Nome")
    table.add_column("Preço")
    table.add_column("Categoria")

    produtos = resposta.json()

    for produto in produtos:
        for chave, valor in produto.items():
            if chave == "id":
                if valor == id_selecionado:
                    table.add_row(str(produto["id"]), produto["nome"], str(produto["preco"]), produto["categoria"])

    
    console.print(table)


def consultar_produto_nome():
    nome_selecionado = questionary.text("Digite o id para consultar esta empresa: ").ask()

    resposta = requests.get(url_produto)

    console = Console()

    table = Table(show_header=True, header_style="bold blue", show_lines=True)
    table.add_column("ID")
    table.add_column("Nome")
    table.add_column("Preço")
    table.add_column("Categoria")

    produtos = resposta.json()

    for produto in produtos:
        for chave, valor in produto.items():
            if chave == "nome":
                if valor == nome_selecionado:
                    table.add_row(str(produto["id"]), produto["nome"], str(produto["preco"]), produto["categoria"])
    
    console.print(table)


def consultar_produto_categoria():
    categoria_selecionada = questionary.text("Digite o id para consultar esta empresa: ").ask()

    resposta = requests.get(url_produto)

    console = Console()

    table = Table(show_header=True, header_style="bold blue", show_lines=True)
    table.add_column("ID")
    table.add_column("Nome")
    table.add_column("Preço")
    table.add_column("Categoria")

    produtos = resposta.json()

    for produto in produtos:
        for chave, valor in produto.items():
            if chave == "categoria":
                if valor == categoria_selecionada:
                    table.add_row(str(produto["id"]), produto["nome"], str(produto["preco"]), produto["categoria"])
    
    console.print(table)


def cadastrar_produto():
    nome_produto = questionary.text("Digite o nome do produto: ").ask()
    preco_produto = float(questionary.text("Digite o preço do produto: ").ask())
    categoria_produto = questionary.text("Digite a categoria do produto: ").ask()

    produto = {
        "nome": nome_produto,
        "preco": preco_produto,
        "categoria": categoria_produto
    }

    resposta = requests.post(url_produto, json=produto)
    if resposta.status_code == 201:
        print("Produto cadastrado com sucesso!")
    else:
        print("Não foi posivel cadastrar produto!!")


def editar_produto():
    id = int(questionary.text("Digite o id para editar: ").ask())
    url_id = f"{url_produto}/{id}"

    nome_alterado = questionary.text("Digite o nome para alterar:").ask()
    preco_alterado = float(questionary.text("Digite o preço para alterar:").ask())
    categoria_alterada = questionary.text("Digite a categoria para alterar:").ask()

    produto = {
        "nome": nome_alterado,
        "preco": preco_alterado,
        "categoria": categoria_alterada
    }

    resposta = requests.put(url_id, json=produto)
    if resposta.status_code == 204:
        print("Deu certo, produto alterado com sucesso!")
    elif resposta.status_code == 404:
        print("Não foi possivel encontrar o id!")
    else:
        print("Não deu para alterar o produto!!")


def apagar_produto():
    id_apagar = int(questionary.text("Digite o id para apagar: ").ask())
    url_id = f"{url_produto}/{id_apagar}"

    resposta = requests.delete(url_id)
    if resposta.status_code == 204:
        print("Produto apagado com sucesso!")
    elif resposta.status_code == 404:
        print("Id não encontrado!")
    else:
        print("Não foi possivel apagar!!")


def apagar_empresa():
    id = int(questionary.text("Digite o id da empresa para apagar: ").ask())
    url_id = f"{url_empresa}/{id}"

    resposta = requests.delete(url_id)

    if resposta.status_code == 204:
        print("Sucesso ao apagar a empresa")
    elif resposta.status_code == 404:
        print("Não foi possivel encontrar a empresa com esse id")
    else:
        print("Não foi possivel apagar a empresa!")


def editar_empresa():
    id = int(questionary.text("Digite o id da empresa para aleterar: ").ask())
    url_api = f"{url_empresa}/{id}"

    nome_empresa: str = questionary.text("Digite o nome da empresa: ").ask()
    cnpj_empresa: str = questionary.text("Digite o CNPJ da empresa: ").ask()

    empresa = {
        "nome": nome_empresa,
        "cnpj": cnpj_empresa
    }

    resposta = requests.put(url_api, json=empresa)
    if resposta.status_code == 204:
        print("Empresa alterada com sucesso")
    elif resposta.status_code == 404:
        print("Não foi possivel encontrar a empresa com esse id")
    else:
        print("Não foi possivel alterar a empresa!")


def cadastrar_empresa():
    nome_empresa: str = questionary.text("Digite o nome da empresa: ").ask()
    cnpj_empresa: str = questionary.text("Digite o CNPJ da empresa: ").ask()

    empresa = {
        "nome": nome_empresa,
        "cnpj": cnpj_empresa
    }

    resposta = requests.post(url_empresa, json=empresa)
    if resposta.status_code == 201:
        print("Empresa cadastrada com sucesso!!")
    else:
        print("Não foi possivel cadastrar a empresa!!")


def consultar_empresa_cnpj():
    cnpj_selecionado = questionary.text("Digite o cnpj para consultar: ").ask()

    resposta = requests.get(url_empresa)

    console = Console()

    table = Table(show_header=True, header_style="bold blue", show_lines=True)
    table.add_column("ID")
    table.add_column("Nome")
    table.add_column("CNPJ")

    empresas = resposta.json()

    for empresa in empresas:
        for chave, valor in empresa.items():
            if chave == "cnpj":
                if valor == cnpj_selecionado:
                    table.add_row(str(empresa["id"]), empresa["nome"], empresa["cnpj"])
    
    console.print(table)


def consultar_empresa_nome():
    nome_selecionado = questionary.text("Digite o nome para consultar esta empresa: ").ask()

    resposta = requests.get(url_empresa)

    console = Console()

    table = Table(show_header=True, header_style="bold blue", show_lines=True)
    table.add_column("ID")
    table.add_column("Nome")
    table.add_column("CNPJ")

    empresas = resposta.json()

    for empresa in empresas:
        for chave, valor in empresa.items():
            if chave == "nome":
                if valor == nome_selecionado:
                    table.add_row(str(empresa["id"]), empresa["nome"], empresa["cnpj"])
    
    console.print(table)


def consultar_empresa_id():
    id_selecionado = int(questionary.text("Digite o id para consultar esta empresa: ").ask())

    resposta = requests.get(url_empresa)

    console = Console()

    table = Table(show_header=True, header_style="bold blue", show_lines=True)
    table.add_column("ID")
    table.add_column("Nome")
    table.add_column("CNPJ")

    empresas = resposta.json()

    for empresa in empresas:
        for chave, valor in empresa.items():
            if chave == "id":
                if valor == id_selecionado:
                    table.add_row(str(empresa["id"]), empresa["nome"], empresa["cnpj"])
    
    console.print(table)


def consultar_empresas():
    resposta = requests.get(url_empresa)

    console = Console()

    table = Table(show_header=True, header_style="bold blue", show_lines=True)
    table.add_column("ID")
    table.add_column("Nome")
    table.add_column("CNPJ")

    empresas = resposta.json()

    for empresa in empresas:
        table.add_row(str(empresa["id"]), empresa["nome"], empresa["cnpj"])

    console.print(table)


def limpar_terminal():
    os.system("clear")
    

menu()