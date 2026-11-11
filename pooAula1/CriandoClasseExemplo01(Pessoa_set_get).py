#usando métodos acessores para ler e alterar o conteúdo de um atributo

class Pessoa:
    def __init__(self,nome, idade):
        self.nome = nome
        self.idade = idade
    
    def get_nome(self):
        return self.nome
    
    def get_idade(self):
        return self.idade
    
    def set_nome(self,nome):
        self.nome = nome
    
    def set_idade(self,idade):
        self.idade = idade
        
        
#main
nome = input("Digite um nome: ")
idade = int(input("Digite a idade: "))
p1 = Pessoa(nome, idade)

p2 = Pessoa("Ana", 45)

#para pesquisar o valor de um atributo (get)
print(p1.get_nome())
print(p1.get_idade())

print("nome do segundo usuário cadastrado: ")
print(p2.get_nome())
# para alterar o valor de um atributo (set)
# neste caso informar o novo valor do atributo (passagem de parâmetros)
p2.set_nome(input("Digite o novo nome:"))
print("Nome atualizado: ",p2.get_nome())

#verifica que atualização foi realizada com sucesso
print(p2.get_nome())
