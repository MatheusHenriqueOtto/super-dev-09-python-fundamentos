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



#pont de entrada da aplicação, deve ter um unico da aplicação inteira
if __name__ == "__main__":
#exemplo_sem_tatamento()
#exemplo_com_tratamento()
    exemlo_com_tratamento_conversao()

