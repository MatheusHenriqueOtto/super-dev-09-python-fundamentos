class Veiculo:
    def __init__(self, marca: str, modelo: str, ano: str) -> None:
        self.marca = marca
        self.modelo = modelo
        self.ano = ano


    def apresentar_dados_veiculo(self):
        print(f"Modelo: {self.modelo}\nAno: {self.ano}\nMarca: {self.marca}\n\n\n")


class Carro(Veiculo):
    def __init__(self, marca: str, modelo: str, ano: str, quantiadade_portas: int) -> None:
        super().__init__(marca, modelo, ano)
        self.quantidade_portas = quantiadade_portas
        pass

    def apresentar_dados_carro(self):
        print(f"Modelo: {self.modelo}\nAno: {self.ano}\nMarca: {self.marca}\n\n\n")


class OffRoad(Carro):
    def __init__(self, marca: str, modelo: str, ano: str, quantiadade_portas: int, altura_solo: float):
        super().__init__(marca, modelo, ano, quantiadade_portas)
        self.altura_solo = altura_solo

    def verificador_off_road(self):
        if self.altura_solo > 180:
            pass

def exemplos_carros():
    mclaren = Carro("Mclaren","720S Coupe", "2018", 2)
    tesla = Carro("Tesla","Model Y L","2026", 4)
    tesla.apresentar_dados_carro()
    mclaren.apresentar_dados_carro()


class Funcionario:
    def __init__(self, nome: str, cpf: str, salario_base: float) -> None:
        self.nome = nome
        self.cpf = cpf
        self.salario_base = salario_base

    def calcular_salario(self, bonus= 0.00) -> float:
        return (self.salario_base + bonus)
    
    def apresentar_dados(self):
        print(f"Nome: {self.nome}\nCPF: {self.cpf}\nSalario: {self.calcular_salario()}")

class Gerente(Funcionario):
    def __init__(self, nome: str, cpf: str, salario_base: float, bonus_gerente: float) -> None:
        super().__init__(nome, cpf, salario_base)
        self.bonus = bonus_gerente

    def calcular_salario_gerente(self) -> float:
        return super().calcular_salario(self.bonus)
    
    def apresentar_dados_gerente(self):
        print(f"Nome: {self.nome}\nCPF: {self.cpf}\nSalario: {self.calcular_salario_gerente()}\n\n\n")


def exemplo_gerente_funcionario():
    ronaldo = Gerente("Ronaldo", "123456789", 2300.00, 600.00)
    flavia = Gerente("Flavia", "123132435", 2600.00, 400)

    ronaldo.apresentar_dados_gerente()
    flavia.apresentar_dados_gerente()

    print("_"*20)

    boberto = Funcionario("Boberto", "1231234351", 5000)

    boberto.apresentar_dados()


class Pessoa:
    def __init__(self, nome: str, numero: str, email: str):
        self.nome = nome
        self.numero = numero
        self.email = email

    def apresentar_dados(self):
        print(f"Nome: {self.nome}\nNumero: {self.numero}\nEmail: {self.email}")


class Professor(Pessoa):
    def __init__(self, nome: str, numero: str, email: str, salario: float):
        super().__init__(nome, numero, email)
        self.salario = salario

    def apresentar_dados(self):
        super().apresentar_dados()
        print(f"Salario: {self.salario}")


class Aluno(Pessoa):
    def __init__(self, nome: str, numero: str, email: str, nota1: float, nota2: float, nota3: float):
        super().__init__(nome, numero, email)
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
        self.media = self.calcular_media()

    def apresentar_dados(self):
        super().apresentar_dados()
        print(f"Primeira nota: {self.nota1}\nSegunda nota: {self.nota2}\nTerceira nota: {self.nota3}\nMedia: {self.media}")

    def calcular_media(self):
        media = (self.nota1 + self.nota2 + self.nota3)/3
        return media
    

def exemplo_pessoa_professor_aluno():
    vetor = Pessoa("Vitor", "65966467", "vitor67@gmail.com")
    francisco = Professor("Francisco", "6587659679", "franciscosensaulas@gmail.com", 20_000.00)
    matheus = Aluno("Matheus", "3456789987", "matheusotto1906@gmail.com", 8.5, 5.3, 9.2)

    vetor.apresentar_dados()
    print("_"*20)
    francisco.apresentar_dados()
    print("_"*20)
    matheus.apresentar_dados()
    



