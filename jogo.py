import random
jogo = True

while jogo:
    resposta = random.randrange(0, 5)
    guess = int(input("Digite um numero entre 0 e 4 (ou -1 para SAIR): "))

    if guess == -1:
        print("Jogo Terminado!")
        jogo = False
        continue
    elif guess >= 5:
        continue

    if guess != resposta:
        print(f"Você errou a resposta correta era {resposta}")
        
    else:
        print(f"Parabéns você acertou a resposta era {guess}")
        repeat = int(input("0 para continuar 1 para parar: "))

        while repeat not in [0, 1]:
            print("Opção inválida! Escolha apenas 0 ou 1.")
            repeat = int(input("0 para continuar 1 para parar: "))


        if repeat == 1:
            print("Jogo Terminado!")
            jogo = False





 