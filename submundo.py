                                                    #ESTUDO DE POO
import os

#Criação da classe
class Player():
    #Inicialização da função para inserir os atributos
    def __init__(self):
        self.forca = 0
        self.destreza = 0
        self.constituicao = 0
        self.inteligencia = 0
        self.sabedoria = 0
        self.carisma = 0
        self.vida = 32
        self.armas = ''
        
player1 = Player()
player2 = Player()

def PersonagensPlayer1():
    #Limpar o terminal
    os.system('cls')
    print('========== SELEÇÃO DO PERSONAGEM ==========')
    
    #Laço de seleção de personagem
    while True:
        #Onde será feito a escolha
        escolha = input("Escolha um personagem:\n 1- Kenji\n 2- Aoki\n 3- Hei\n 4- Hideki\n 5- Edward\n \n Número: ")
        
        #Processamento das escolhas
        if (escolha == "1"):
            player1.forca = 1
            player1.destreza = 5
            player1.constituicao = 2
            player1.sabedoria = 0
            player1.carisma = 1
            player1.vida = 32
            player1.armas = 'Duas Wakizashis'
            break
    
        elif (escolha == "2"):
            pass
            break
        elif(escolha == "3"):
            pass
            break
        elif(escolha == "4"):
            pass
            break
        elif (escolha == "5"):
            pass
            break
        else:
            print("\nNúmero inválido, digite a enumeração correta do personagem desejado\n")
            
#Chamando função de PersonagensPlayer1
PersonagensPlayer1()
print(player1.destreza)