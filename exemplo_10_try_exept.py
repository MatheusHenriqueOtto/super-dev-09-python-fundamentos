def exemplo_sem_tratamento():
    print("Divisão ", 20/0)
    print("depois da divisão")
    #Lança a excessão: ZeroDivisionError: division by zero


def exemplo_com_tratamento():
    try:
        print("Divisão: ", 10/0)
    except ZeroDivisionError:
        print("Não da boa dividir por zero")
    print("O programa continuou normalmenteeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee")
    pass


def exemlo_com_tratamento_conversao():
    numero_digitado = "dois"
    try:
        numero: int = int(numero_digitado)
        print("Numero digitado: ", numero)

    except ValueError:
        print("Texto digitado não é um numero valido para inteiro")

    print("Acabou!!!!!!!!!!!!!!!!!!!")


def exemplo_multiplos_tratamento():
    numero1_digitado = "2"
    numero2_digitado = "4"

    try:
        resultado: int = int(numero1_digitado)/int(numero2_digitado)
        print("Resultado", resultado)
    except ZeroDivisionError:
        print("Não é possivel dividir um numero por zero")
    except ValueError:
        print("Os numeros não são validos")

    print("Obrigado por usar o sistema") 

def exemplo_mensagem_erro():
    try:
        aluno = {"nome": "Pedro", "nota1": 9.44}
        media_aluno = aluno["media"]
        print(media_aluno)
    except KeyError as erro: # 'as' serve para pegar a variavel do erro que ocorreu
        print("Mensagem de erro tentar acessar a chave: ", erro)

    print("Deu boa!!!!!!!!!!!!!!!!!")

    
#ponto de entrada da aplicação, deve ter um unico da aplicação inteira
if __name__ == "__main__":
#exemplo_sem_tatamento()
#exemplo_com_tratamento()
#exemlo_com_tratamento_conversao()
    exemplo_multiplos_tratamento()
