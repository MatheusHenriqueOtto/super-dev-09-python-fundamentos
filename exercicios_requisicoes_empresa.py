import requests
import questionary  


url_base = "https://api.franciscosensaulas.com"

def menu():
    opcoes_menu = [
        "Consultar",
        "Cadastrar",
        "Editar",
        "Apagar"
    ]

    menu_escolhido = ""

    while menu_escolhido != "Sair":
        menu_escolhido = questionary.select("Menu", choice=opcoes_menu).ask
    

    