from datetime import datetime
from pathlib import Path


def exemplo_sem_erro():
    try:
        resultado = 10/2
        print("Resultado: ", resultado)
    except ZeroDivisionError:
        print("Erro: divisão por zero.")
    finally:
        print("FINALLY: executei mesmo sem erro.")


def exemplo_com_erro():
    try:
        resulatado = 10/0
        print("Resultado: ", resulatado)
    except ZeroDivisionError: 
        print("Erro: divisão por zero.")
    finally:
        print("FINALLY: executei mesmo com erro.")


def exemplo_tratar_ciacao_diretorio():
    try:
        caminho_diretorio = Path("relatorios")
        caminho_diretorio.mkdir()
        print("Criado co sucesso")
    except FileExistsError:
        print("Diretório já existe")
    finally:
        mensagem = input("Digite ua mensagem para salvar no arquivo")
        caminho_arquivo = caminho_diretorio/"relatorio-2026-07-29.txt"
        with open(caminho_arquivo, "a", encoding="UTF-8") as file:
            data_hora_atual = datetime.now()
            file.write(str(data_hora_atual) + " " + mensagem + " \n")
            print("arquivo gerado ")


if __name__ == "__main__":
    exemplo_com_erro()