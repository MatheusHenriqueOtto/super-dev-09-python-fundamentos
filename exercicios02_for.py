def mostrar_cinco_vezes():
    for i in range(0, 5):
        print(f"Bem vindo {i}")


def apresentar_numeros():
    for i in range(15, 30):
        print(i)


def apresentar_tabuada():
    numero = int(input("Digite um numero: "))
    for i in range(0, 10):
        resultado = i*numero
        print(f"{numero} x {i} = {resultado}")



def perguntar_repetidamente():
    soma = 0
    for i in range(1, 6):
        numero = int(input(f"Digite o {i}º numero: "))
        soma = soma + numero
    print(f"A soma é de todas {soma}")



def vetor_nomes():
    nomes = []
    nome1 = "Matheus"
    nome2 = "Lucas"
    nome3 = "Samuel"
    nome4 = "Vitor"
    nomes.append(nome1, nome2, nome3, nome4)
    print(nomes[0])
    print(nomes[1])
    print(nomes[2])
    print(nomes[3])


def vetor_frutas():
    frutas = []
    fruta1 = input("Digite o nome de uma fruta: ")
    fruta2 = input("Digite uma fruta: ")
    fruta3 = input("Digite o nome da terceira fruta: ")
    frutas.append(fruta1, fruta2, fruta3)
    print(frutas[0])
    print(frutas[1])
    print(frutas[2])


def solicitar_inteiros():
    numeros = []
    numero1 = int(input("Digite o primeiro numero: "))
    numero2 = int(input("Digite o segundo numero: "))
    numero3 = int(input("Digite o terceiro numero: "))
    numero4 = int(input("Digite o quarto numero: "))
    numeros.append(numero1, numero2, numero3, numero4)
    print(numeros[0])
    print(numeros[1])
    print(numeros[2])
    print(numeros[3])


def vetor_notas():
    notas = []
    nota1 = float(input("Digite o primeira nota: "))
    nota2 = float(input("Digite o segunda nota: "))
    nota3 = float(input("Digite o terceira nota: "))
    nota4 = float(input("Digite o quarta nota: "))
    notas.append(nota1, nota2, nota3, nota4)
    print("Vetor original: ")
    print(notas[0])
    print(notas[1])
    print(notas[2])
    print(notas[3])
    print("-"*20)
    print(f"A primeira nota é: {notas[0]}")
    print(f"A ultima nota é: {notas[3]}")
    print("-"*20)
    notas.remove(nota4)
    notas[1] = 10.00
    print("Vetor final")
    print(notas[0])
    print(notas[1])
    print(notas[2])
    print("-"*20)
    print(f"Tamanho Final: {len(notas)}")
    print(f"A Media é de {(nota1 + nota2 + nota3)/3}")
    


def vetor_for_nomes():
    nomes = []
    nome1 = "Matheus"
    nome2 = "Lucas"
    nome3 = "Samuel"
    nome4 = "Vitor"
    nome5 = "Rafael"
    nomes.append(nome1, nome2, nome3, nome4, nome5)
    for i in  range(0, len(nomes)):
        print(nomes[i])


def solicitar_frutas():
    frutas = []
    for i in range(0, 5):
        fruta = input("Digite uma fruta: ")
        frutas.append(fruta)

    for i in range(0, len(frutas)):
        print(frutas[i])



def numeros_solicitados():
    numeros = []
    soma: int = 0
    numero: int = 0
    for i in range(0, 5):
        numero = int(input("Digite um numero: "))
        numeros.append(numero)


    for i in range(0, len(numeros)):
       soma = numeros[i] + soma

    print(soma)


def contando_pares():
    numeros = []
    numeros_pares = []
    for i in range(0, 6):
        numero = int(input("Digite um numero: "))
        numeros.append(numero)

    for i in range(0, len(numeros)):
        if numeros[i] % 2 == 0:
            numeros_pares.append(numeros[i])

    print("-"*10, "Numeros pares da lista", "-"*10)
    for i in range(0, len(numeros_pares)):
        print(numeros_pares[i])
    print(f"Quantidade de pares: {len(numeros_pares)}")

def calculando_media():
    notas = []
    soma = 0
    for i in range(0, 4):
        nota = float(input("Digite sua nota: "))
        notas.append(nota)

    for i in range(0, len(notas)):
        soma = soma + notas[i]

    media = soma / len(notas)
    situacao = "Reprovado"

    if media >= 7:
        situacao = "Aprovado"


    print("-"*10, "Notas digitadas", "-"*10)
    for i in range(0, len(notas)):
        print(notas[i])
    print(f"Media final: {media}")
    print(f"Situação: {situacao}")





