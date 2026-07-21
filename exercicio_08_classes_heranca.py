class Pessoa:
    def __init__(self, nome: str, numero: str, email: str):
        self.nome = nome
        self.numero = numero
        self.email = email
        
    def apresentar_dados(self):
        print(f"Nome: {self.nome}\nNumero: {self.numero}\nEmail: {self.email}")

class Professor(Pessoa):
    def __init__(self, nome: str, numero: str, email: str, salario: float):
        pass