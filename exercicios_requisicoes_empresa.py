import os
import requests
import questionary  
from rich.console import Console
from rich.table import Table

url_base = "https://api.franciscosensaulas.com"
url = f"{url_base}/api/v1/empresa"

def menu():
    opcoes_menu = [
        "Consultar Todos",
        "Consultar por id",
        "Consultar por nome",
        "Consultar por cnpj",
        "Cadastrar",
        "Editar",
        "Apagar",
        "Sair"
    ]

    menu_escolhido = ""

    while menu_escolhido != "Sair":
        menu_escolhido = questionary.select("Menu", choices=opcoes_menu).ask()
        limpar_terminal()

        if menu_escolhido == "Consultar Todos":
            consultar_empresas()
        elif menu_escolhido == "Consultar por id":
            consultar_empresa_id()
        elif menu_escolhido == "Consultar por nome":
            consultar_empresa_nome()
        elif menu_escolhido == "Consultar por cnpj":
            consultar_empresa_cnpj()
        elif menu_escolhido == "Cadastrar":
            cadastrar_empresa()
        elif menu_escolhido == "Editar":
            editar_empresa()
        elif menu_escolhido == "Apagar":
            apagar_empresa()
        
        if menu_escolhido != "Sair":
            questionary.press_any_key_to_continue(
                "Digite qualquer tecla para continuar..."
            ).ask()
            limpar_terminal()



def apagar_empresa():
    id = int(questionary.text("Digite o id da empresa para apagar: ").ask())
    url_id = f"{url}/{id}"

    resposta = requests.delete(url_id)

    if resposta.status_code == 204:
        print("Sucesso ao apagar a empresa")
    elif resposta.status_code == 404:
        print("Não foi possivel encontrar a empresa com esse id")
    else:
        print("Não foi possivel apagar a empresa!")


def editar_empresa():
    id = int(questionary.text("Digite o id da empresa para aleterar: ").ask())
    url_api = f"{url}/{id}"

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

    resposta = requests.post(url, json=empresa)
    if resposta.status_code == 201:
        print("Empresa cadastrada com sucesso!!")
    else:
        print("Não foi possivel cadastrar a empresa!!")


def consultar_empresa_cnpj():
    cnpj_selecionado = questionary.text("Digite o cnpj para consultar: ").ask()

    resposta = requests.get(url)

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

    resposta = requests.get(url)

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

    resposta = requests.get(url)

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
    resposta = requests.get(url)

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