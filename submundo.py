                                                                                    #ESTUDO DE POO
#IMPORTAÇÕES
import os
import random
from time import sleep

#Criação da classe
class Player():
    #Inicialização da função para inserir os atributos
    def __init__(self):
        self.personagem = ''
        self.forca = 0
        self.destreza = 0
        self.constituicao = 0
        self.inteligencia = 0
        self.sabedoria = 0
        self.carisma = 0
        self.vida = 0
        self.armas = ''
        self.skills = ''

player1 = Player()
player2 = Player()


def RolagemIniciativa():
    while True:
        os.system('cls')
        print('========== INICIATIVA ==========')

        iniciativa = input('Quem irá rolar a iniciativa primeiro? (digite 1 para o Player 1 ou 2 para o Player 2)\n')
        if (iniciativa == "1"):
            global rolagemIniciativa1
            global rolagemIniciativa2

            rolagemIniciativa1 = random.randrange(1, 20)
            rolagemIniciativa2 = random.randrange(1, 20)
            
            print('Girando iniciativa... ')
            sleep(5)
            print(f'Sua iniciativa foi: |{rolagemIniciativa1}|\n')
            print(f'Girando iniciativa do Player 2... ')
            sleep(5)
            print(f'Sua iniciativa foi: |{rolagemIniciativa2}|\n')
            break

        elif(iniciativa == "2"):
            rolagemIniciativa2 = random.randrange(1, 20)
            rolagemIniciativa1 = random.randrange(1, 20)
            print('Girando iniciativa... ')
            sleep(5)
            print(f'Sua iniciativa foi |{rolagemIniciativa2}|\n')
            print(f'Girando iniciativa do Player 1...')
            sleep(5)
            print(f'Sua iniciativa foi: |{rolagemIniciativa1}|\n')
            break
        
        else:
            print('Número de player inválido, por favor tente novamente: ')
            
def PersonagensPlayer1():
    
    #Limpar o terminal
    os.system('cls')
    print('========== SELEÇÃO DO PERSONAGEM PLAYER 1 ==========')
    
    #Laço de seleção de personagem
    while True:
        
        #Onde será feito a escolha1
        escolha1 = input('Player 1: Escolha um personagem:\n 1- Kenji\n 2- Aoki\n 3- Hei\n 4- Hideki\n 5- Edward\n \n Número: ')
        
        #Processamento das escolhas
        if (escolha1 == "1"):
            player1.personagem = 'Kenji'
            player1.forca = 1
            player1.destreza = 5
            player1.constituicao = 2
            player1.sabedoria = 0
            player1.carisma = 1
            player1.vida = 32
            player1.armas = ['Duas Wakizashis', 'Arco Longo', 'Corpo a Corpo']
            player1.skills = ['0- Golpe Esquentado', '1- Ataque com Arco Longo', '2- Ataque duplo de Wakizashi', '3- Cura com frasco de sangue']
            break
    
        elif (escolha1 == "2"):
            pass
            break

        elif(escolha1 == "3"):
            pass
            break
        elif(escolha1 == "4"):
            pass
            break
        elif (escolha1 == "5"):
            pass
            break
        else:
            print("\nNúmero inválido, digite a enumeração correta do personagem desejado\n")

def PersonagensPlayer2():

    
    #Limpar o terminal
    os.system('cls')
    print('========== SELEÇÃO DO PERSONAGEM PLAYER 2 ==========')
    
    #Laço de seleção de personagem
    while True:
        #Onde será feito a escolha1
        escolha2 = input("Player 1: Escolha um personagem:\n 1- Kenji\n 2- Aoki\n 3- Hei\n 4- Hideki\n 5- Edward\n \n Número: ")
        #Processamento das escolhas
        if (escolha2 == "1"):
            player2.personagem = 'Kenji'
            player2.forca = 1
            player2.destreza = 5
            player2.constituicao = 2
            player2.sabedoria = 0
            player2.carisma = 1
            player2.vida = 32
            player2.armas = ['Duas Wakizashis', 'Arco Longo', 'Corpo a Corpo']
            player2.skills = ['Golpe Esquentado', 'Ataque com Arco Longo', 'Ataque duplo de Wakizashi', 'Cura com frasco de sangue']
            break
    
        elif (escolha2 == "2"):
            pass
            break

        elif(escolha2 == "3"):
            pass
            break

        elif(escolha2 == "4"):
            pass
            break

        elif (escolha2 == "5"):
            pass
            break

        else:
            print("\nNúmero inválido, digite a enumeração correta do personagem desejado\n")

def Batalha():
        if (rolagemIniciativa1 > rolagemIniciativa2):
            print(f'{player1.personagem} começa a luta!\n| Seu turno: {player1.armas} {player1.skills}')

        else:
            print(f'{player2.personagem} começa a luta!\n| Seu turno: {player2.armas} {player2.skills}')

#Chamando função de PersonagensPlayer1
PersonagensPlayer1()
PersonagensPlayer2()
RolagemIniciativa()
Batalha()


