#importa a biblioteca de aleatoriedade
import random

#mensagem inicial
print("PYTHON GAMES - IVAN JR (2025)")
print("SEJA BEM-VINDO AO PYTHON GAMES! AQUI ESTARÃO ALGUMAS OPÇÕES DE BRINCADEIRAS PARA VOCÊ SE DIVERTIR!")
print("1. Jogo da adivinhação de números")
print("2. Pedra, papel ou tesoura")
print("3. Piadas")

#O valor inicial de escolha será 0, ainda não foi escolhido pelo usuário
escolha = 0

#Enquanto escolha for diferente de uma das opções, sempre irá aparecer uma mensagem pro usuário escolher uma das alternativas
while escolha != 1 and escolha != 2 and escolha != 3:
    try:
        escolha = float(input("Faça a escolha: "))
    except:
        print("Digite uma das opções válidas!")

#Caso do usúario ter escolhido a primeira opção
if escolha == 1:
    jogarnovamente = "S"
    while jogarnovamente == "S":
        numeroescolhido = random.randint(1, 100) #O Número será escolhido aleatoriamente pelo programa


        print("Instruções: O jogo irá escolher um número entre 1 e 100, tente descobrir através das pistas")
        try:
            numerousuario = float(input("Tente acertar o número! Digite aqui: "))
            while numerousuario != numeroescolhido:
                if numerousuario > numeroescolhido: #Caso o número escolhido pelo usuário for maior que o do número escolhido pelo programa
                    print("O seu número escolhido é maior! Você não me pega! HA! HA! HA!")
                    try:
                        numerousuario = float(input("Teste outro número: "))
                    except:
                        print("Digite números válidos!")

                elif numerousuario < numeroescolhido: #Caso o número escolhido pelo usuário for menor que o do número escolhido pelo programa
                    print("O seu número é menor! Você não me pega! HA! HA! HA!")
                    try:
                        numerousuario = float(input("Teste outro número: "))
                    except:
                        print("Digite números válidos!")

            print(f"Droga! Você descobriu o número! Realmente era {numeroescolhido}")
            jogarnovamente = input("Jogar novamente? S ou N: ")
        except:
            print("Digite números válidos!")

#Caso do usuário ter escolhido a segunda opção
elif escolha == 2:
    print('Instruções: Digite "pedra", "papel" ou "tesoura" para escolher uma das opções do jogo')

    jogarnovamente = "S"
    while jogarnovamente == "S":
        escolhajokenpo = random.choice(["pedra", "papel", "tesoura"])
        escolhausuariojokenpo = input("Faça sua escolha: ")

        if (escolhajokenpo == "pedra" and escolhausuariojokenpo == "pedra") or (escolhajokenpo == "papel" and escolhausuariojokenpo == "papel") or (escolhajokenpo == "tesoura" and escolhausuariojokenpo == "tesoura"): #Em caso da escolha do usuário e programa forem iguais
            print(f"Escolhemos {escolhausuariojokenpo}, EMPATE!")
            jogarnovamente = input("Jogar novamente? S ou N: ")

        elif (escolhajokenpo == "pedra" and escolhausuariojokenpo == "tesoura") or (escolhajokenpo == "tesoura" and escolhausuariojokenpo == "papel") or (escolhajokenpo == "papel" and escolhausuariojokenpo == "pedra"): #Em caso do programa ter escolhido pedra e o jogador tesoura
            print(f"Escolhi {escolhajokenpo} e você {escolhausuariojokenpo}, EU GANHEI! VOCÊ PERDEU!!!")
            jogarnovamente = input("Jogar novamente? S ou N: ")

        elif (escolhajokenpo == "pedra" and escolhausuariojokenpo == "papel") or (escolhajokenpo == "papel" and escolhausuariojokenpo == "tesoura") or (escolhajokenpo == "tesoura" and escolhausuariojokenpo == "pedra"): #Em caso do usuário ganhar do programa
            print(f"Escolhi {escolhajokenpo} e você {escolhausuariojokenpo}, Droga! Você ganhou! Poxa...")
            jogarnovamente = input("Jogar novamente? S ou N: ")

#Caso do usuário ter escolhido a terceira opção
elif escolha == 3:
    resposta = "S"
    while resposta == 'S' or resposta == 'S':
        piadas = ['Por que uma idosa não tem relógio? Porque ela é uma "sem hora"!! HA! HA! HA!', 'Qual é o estado do Brasil que quer ser um carro? O "SER JEEP"!! HA! HA! HA!', 'Qual é o nome do filme em que um médico do futuro descobriu a cura de uma doença em que atualmente não possui cura? O "EXTERMINA DOR DO FUTURO"! HA! HA! HA!', 'O que a agulha disse pro imã? "Estou sendo atraída por você"! HA! HA! HA!', 'O que Peter Parker disse para a Mary Jane? "Tia May"! HA! HA! HA!']
        print(random.choice(piadas))
        resposta = input('Gostaria de ouvir outra piada? S ou N: ')