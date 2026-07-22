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
        return super().apresentar_dados()
    