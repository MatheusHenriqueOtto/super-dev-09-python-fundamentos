class  Pessoa:
    def __init__(self, nome: str, sobrenome: str):
        self.nome = nome
        self.sobrenome = sobrenome

    def gerar_nome_copleto(self):
        return f"{self.nome} {self.sobrenome}"
    
## Heraça permite uma classe (filha) herdar da classe pai
class Funcionario(Pessoa): 
    def __init__(self, nome: str, sobrenome: str, cargo: str):
        #super() permite ter acesso ao constructor do pai
        super().__init__(nome, sobrenome)
        self.cargo = cargo

    def gerar_nome_copleto(self):
        return f"{self.nome} {self.sobrenome}"
    

def exemplo_funcionario():
    pessoa = Pessoa("Ronaldo", "femomemo")
    print("Nome completo: ", pessoa.gerar_nome_copleto())

    funcionario  = Funcionario("Lionel", "Messi", "adiministrativo")
    print("Nome completo do funcionaro: ", funcionario.gerar_nome_copleto())




