personagens = []

def criar_personagem():
    nome = input("Digite o nome do seu personagem:")
    classe = input("Digite a classe do seu personagem:")
    nivel = int(input("Digite o nível do seu personagem:"))
   
    personagem = {
        "nome": nome,
        "classe": classe,
        "nivel": nivel
    }
    personagens.append(personagem)
   
   
quantidade=int(input("Quantos personagens deseja criar?"))
for i in range (quantidade):
    print(f"Criando personagem {i +1}")
    criar_personagem()
    
print ("---- Lista Personagem ----")
for personagem in personagens:
    print("-------------------")
    print("Nome:", personagem["nome"])
    print("Classe:", personagem["classe"])
    print("Nível:", personagem["nivel"])
    print("-------------------")
    