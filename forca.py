import random
def jogar():
    
    palavra_secreta = carrega_palavra_secreta()
    forca = ["_" for letra in palavra_secreta]   

    enforcou = False
    acertou = False
    erros = 0

    limpa_tela()    
    desenha_forca(erros)
    imprime_forca(forca) 

    

    # enquanto(True)
    while (not enforcou and not acertou):
                 
        chute = input("Digite uma letra:").upper().strip()
         
        if (chute in palavra_secreta):
            limpa_tela()
            desenha_forca(erros)
            acerta_chute(chute, forca, palavra_secreta)            
        else:
            limpa_tela()
            erros += 1
            print("Você errou! Tentativas restantes {}".format(7 - erros))
            desenha_forca(erros)
            imprime_forca(forca)
            

        enforcou = erros == 7
        acertou = "_" not in forca

    if (acertou):
        limpa_tela()
        imprime_mensagem_vencedor()
    elif (enforcou):
        limpa_tela()        
        imprime_mensagem_perdedor(palavra_secreta)

    print("Obrigado por jogar!")


def inicializa_jogo():
    print("***************************")
    print("       JOGO DA FORCA!      ")
    print("***************************\n")


def carrega_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        palavras.append(linha.strip().upper())
    arquivo.close()

    palavra_secreta = palavras[random.randrange(0, len(palavras))]
    return palavra_secreta


def acerta_chute(chute, forca, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            forca[index] = letra
            print(forca[index], end=" ")
        else:
            print(forca[index], end=" ")
        index += 1
    print("\n")

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 0):
        print(" |            ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")    

def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def imprime_forca(forca):
    index = 0
    for letra in forca:
        print(forca[index],end=" ")
        index +=1
    print("\n")  

def limpa_tela():
    print("\x1b[2J\x1b[1;1H")
    inicializa_jogo()
    

if (__name__ == "__main__"):
    jogar()
