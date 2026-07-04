def exercicio_01_mensagens():
    print("Boas vindas")
    print("voce está aprendendo python")
    print("Python é usado para criar comandos")


def exercicio_02_variaveis():
    nome = "Matheus"
    idade = "17"
    cidade = "Blumenau"
    print(nome, idade, cidade)


def exercicio_03_input_nome():
    nome = input("Digite seu nome: ")
    print(f"Olá {nome}! Seja bem-vindo")


def exercicio_04_dados_pessoais():
    nome = input("Digite seu nome")
    bairro = input("Digite seu bairro")
    cidade = input("Digite sua cidade")

    print(f"Olá {nome}, voce mora em {bairro} que se localiza em {cidade}")


def exercicio_05_exibir_idade():
    idade = int(input("Digite sua idade: "))
    print(idade)


def exercicio_06_previsao_idade():
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sou idade: "))
    print(f"{nome} no proximo ano voce terá {idade + 1}")


def exercicio_07_duplicador():
    numero = int(input("Digite um numero: "))
    dobro = numero*2
    print(f"O dobro do numero é {dobro}")


def exercicio_08_maior_idade():
    idade = int(input("Digite sua idade"))
    if idade > 18:
        print("Voce é maior de idade!!")
    else:
        print("Voce não é maior de idade!!")


def exercicio_09_verificar_positivo():
    numero = int(input("Digite um numero: "))
    if numero > 0:
        print("O numero é positivo")
    else:
        print("O numero é negativo")


def exercicio_10_entrar_evento():
    idade = int(input("Digite sua idade: "))
    if idade <= 16:
        print("Voce não pode entrar no evento")
    else:
        print("Voce pode entrar no evento")


def exercicio_11_aprovado():
    nota = float(input("Digite sua nota: "))
    if nota <= 7: 
        print("Reprovado!!")
    else: 
        print("Aprovado!!")


def exercicio_12_debito():
    saldo = float(input("Digite o saldo: "))
    valor_compra = float(input("Digite o valor da compra: "))

    if saldo >= valor_compra:
        print("Voce pode comprar")
    else: 
        print("Voce não pode comprar")


def exercicio_13_aprovado_faltante():
    nota = float(input("Digite sua nota: "))
    frequencia = int(input("Digite sua frequencia: %"))

    if nota >= 7 and frequencia >= 75:
        print("Voce foi aprovado")
    else: 
        print("Reprovado")


def exercicio_14_entrada_gratuita():
    idade = int(input("Digite sua idade: "))
    if idade < 6 or idade > 60:
        print("Entrada gratuita")
    else:
        print("Entrada")


def exercicio_15_login():
    nome = input("Digite seu nome: ")
    senha = input("Digite sua senha: ")
    

    if nome == "admin" and senha == "1234":
        print("Login realizado com sucesso")
    else:
        print("Login errado")


def exercicio_16_repeticao():
    i = 0
    while i < 4:
        print("Matheus", i)
        i += 1 


def exercicio_17_pares():
    i = 0
    while i < 20:
        i += 2
        print(i)

def exercicio_18_repeticao_agendada():
    i = 0
    quantidade = int(input("Digite quantas vezes irá repetir a mensagem: "))
    while i < quantidade:
        print("Matheus", i)
        i += 1


def exercicio_19_somar_nvezes():
    numero = int(input("Digite um numero: "))
    i = numero
    soma = 0
    while i > 0:
        soma = soma + i
        i -= 1
    print(soma)


def exercicio_20_pedir_senha():
    senha = ""
    while senha != "1234":
        senha = input("Digite a senha: ")
        print("A senha não é essa, tente novamente")
    
    print("Voce conseguio descobrir a senha")


def exercicio_21_menu():
    verdadeiro = True
    while verdadeiro:
        opcao = input("Escolha uma opção:\n1 - Mensagem de boas Vindas\n2 - Mostrar mensagem repetidas\nResposta: ")
        if opcao == "1":
            exercicio_01_mensagens()
        elif opcao == "2":
            exercicio_16_repeticao()
        else:
            verdadeiro = False
        

def exercicio_22_tabuada():
    numero = int(input("Digite um numero: "))
    i = 1
    while i <= 10:
        print(f"{numero}x{i} = {numero*i}")
        i += 1


def exercicio_23_somar_indefinido():
    soma = 0
    i = 1
    while i != 0:
        numero = int(input("Digite um numero para somar: "))
        soma = soma + numero
        if numero == 0:
            break
        print(f"Resultado da soma até agora: {soma}")


exercicio_23_somar_indefinido()