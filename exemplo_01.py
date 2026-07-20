import os
import time


def exemplo_string():
    # declarando uma variavel do tipo string
    nome_livro_comeco: str = "harry potter"
    nome_livro_final: str = "as reliquias da morte"
    # declatando uma string e armazenando a concatenação
    # title => Pascal Case
    # upper => UPPER CASE
    # lower => lower case
    # capitalize => Abacate com pera e limão
    nome_livro: str = nome_livro_comeco.title() + " " + nome_livro_final.upper()
    print("Livro das filhas da Miranda:", nome_livro)


def primeiro_exemplo():
    print("Olá mundo")
    fruta: str = "Abacate"
    carro: str = "Corsa"
    quantidade_fruta: int = 6
    preco_unitario_fruta: float = 2.53
    print("Fruta:", fruta)
    print("Quantidade:", quantidade_fruta)
    print("Preço unitario", preco_unitario_fruta)
    print("Preço total", quantidade_fruta * preco_unitario_fruta)
    print("O carro", carro, " comprou a fruta:", fruta)


def exemplo_solicitar_dados():
    console: str = input("Digite o nome do console [XBOX/PS5]").upper().strip()
    quantidade: int = int(input("Digite a quantidade"))

    preco: float = 0
    if console == "XBOX":
        preco = 6696.00
    elif console == "PS5":
        preco = 4277.00
    else:
        print("Console inválido")
        return

    print("Preco:", preco)
    print("Quantidade:", quantidade)
    print("Total:", preco * quantidade)


def exemplo_if_alunos():
    # float(...) e a conversão pra float
    nota1: float = float(input("Digite a nota 1: "))
    nota2: float = float(input("Digite a nota 2: "))
    nota3: float = float(input("Digite a nota 3: "))

    media: float = (nota1 + nota2 + nota3) / 3

    #bool é boolean (true ou false)
    aprovado: bool = False

    if media >= 6 and media <= 10:
        aprovado = True
    else:
        aprovado = False

    print("Média:", media)

    if aprovado == True:
        print("Aprovado: sim")
    else:
        print("Aprovado: não")


def exemplos_while():
    def contar_ate_5():
        i = 0
        # apresentar de 0 ate 4
        while i < 5:
            print(i)
            i += 1

    def contagem_regressiva():
        i = 5
        print("Contagem regressiva")
        #Apresentar de 5 ate 0
        while i >= 0:
            print(i)
            i -= 1

    def solicitar_dados():
        i = 0
        total_mensal_salarios = 0
        while i < 3:
            jogador: str = input("Nome do jogador de futebol: ")
            posicao: str = input("Posicao do jogador: ")
            salario_anual: float = float(input("Salario anual: "))

            salario_mensal = salario_anual / 12
            #separador permite mudar o comportamento de como sera concatenado os dados no print
            #end permite mudar o que acontece depois que terminou de imprimir no terminal
            print("Jogador:", jogador, "Ganha R$", salario_mensal, sep="  ", end="\n\n\n\n\n\n")

            total_mensal_salarios = total_mensal_salarios + salario_mensal
            i += i
        print("Total mensal dos salarios: ", total_mensal_salarios)

    def escrever_arquivo_copa_mundo():
        # criar arquivo CSV com os dados que o usuario digitar
        texto_arquivo = "Time1;Time2;Placar\n"

        i = 0
        while i < 3:
            time1: str = input("Time 1: ")
            time1_gols: int = int(input("Gols " + time1 + ": "))

            time2: str = input("Time 2: ")
            time2_gols: int = int(input("Gols " + time2 + ": "))

            placar = str(time1_gols) + "X" + str(time2_gols)

            texto_arquivo += f"{time1};{time2};{placar}\n"
            print("\n\n\n--------------------------")

            if time1_gols > time2_gols:
                print(f"Resultado: Time {time1} ganhou")
            elif time2_gols > time1_gols:
                print(f"Resultado: Time {time2} ganhou")
            else:
                print("Resultado: Empate")

            time.sleep(2)

            limpar_terminal = input("Deseja limpar o terminal [y/n]")
            if limpar_terminal == "y":
                os.system("cls")
            i = i + 1

            with open("placar.csv", "w", encoding="utf-8") as arquivo:
                arquivo.write(texto_arquivo)
                print("Arquivo 'placar.csv' criado com sucesso")

                escrever_arquivo_copa_mundo()

        





exemplo_solicitar_dados()