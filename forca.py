def jogar():
    import random

    print("***************************")
    print("Bem vindo ao jogo de Forca!")
    print("***************************\n")

    arquivo = open("palavras.txt", "r")
    palavras = []
    
    for linha in arquivo:
        palavras.append(linha.strip().upper())        
    arquivo.close()

    palavra_secreta = palavras[random.randrange(0, len(palavras))]
    forca = ["_" for letra in palavra_secreta]

    enforcou = False
    acertou = False
    erros = 0

    print(forca)

    # enquanto(True)
    while (not enforcou and not acertou):

        chute = input("Digite uma letra:").upper().strip()
        print("\n")

        if (chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if (chute == letra):
                    forca[index] = letra
                    print(forca[index], end=" ")
                else:
                    print(forca[index], end=" ")    
                index += 1
            print("\n\njogando...")
        else:
            print("Você errou! Tentativas restantes {}".format(5 - erros))
            print(forca)
            print("")
            erros += 1

        enforcou = erros == 6
        acertou = "_" not in forca

    if (acertou):
        print("Você ganhou!!!!")
    elif (enforcou):
        print("Você perdeu :( ")

    print("Obrigado por jogar!")


if (__name__ == "__main__"):
    jogar()
