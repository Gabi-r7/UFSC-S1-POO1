#Exemplo 001  2025-1
#cadastro de Pessoa
class Pessoa:
    def __init__(self,nome1, idade1,peso1):
        self.nome = nome1
        self.idade = idade1
        self.peso = peso1
         
    def consulta_nome(self):   #get
        return self.nome
    
    def altera_nome(self,nome):  #set
        self.nome = nome
    
    def consulta_idade(self):
        return self.idade
    
    def altera_idade(self,idade):
        self.idade = idade
    
    def consulta_peso(self):
        return self.peso
    
    def altera_peso(self,peso):
        self.peso = peso
        
        
#main
#criando um objeto (instância da classe Pessoa)
p1 = Pessoa("Pedro", 20,80)


#lendo valores do teclado para criar um objeto (instancia) da Classe Pessoa
nome = input("Digite um nome: ")
idade = int(input("Digite a idade: "))
peso = int(input("Digite o peso: "))
#p2 é um objeto, ou seja, uma instância da Classe Pessoa
p2 = Pessoa(nome, idade, peso)



# imprimindo os valores dos atributos da instancia p1
# acessando diretamente o atributo  (não recomendado, porém possível)
print(p1.nome, p1.idade)
print(p2.nome,p2.idade)
print()

# alternativa recomendada (utilizar a invocação ao método)
print("Pessoa: ",p1.consulta_nome())
print("Pessoa: ",p1.consulta_idade())
print("Pessoa: ",p1.consulta_peso())


#utilizando métodos para pesquisar ou atualizar os valores dos atributos
#atualizando o valor do atributo nome da instancia p1
p1.altera_nome(input("Digite o novo nome: "))

p1.altera_idade(input("Digite a nova idade: "))
p1.altera_peso(int(input("Digite o novo peso: ")))

print("Nome atualizado: ", p1.consulta_nome())
print("Idade atualizado: ", p1.consulta_idade())
print("Peso atualizado: ", p1.consulta_peso())


#print("Pessoa 1:", p1)   #imprimi o endereço de memória (não o conteúdo)

