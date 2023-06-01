def jogar():

    print("***************************")
    print("Bem vindo ao jogo de Forca!")
    print("***************************\n")

    palavra_secreta = "BANANA"
    forca = ["_","_","_","_","_","_"]
    
    enforcou = False
    acertou = False

    print(forca)

    #enquanto(True)
    while(not enforcou and not acertou):
        
        chute = input("Digite uma letra:").upper().strip()
        print("\n")
        
        index = 0
        for letra in palavra_secreta:
            if(chute == letra):
                forca[index] = letra
                print(forca[index], end=" ")

            else:
                print(forca[index], end=" ")    
            index += 1
        

        print("\n\njogando...")
        

    print("Obrigado por jogar!")


if (__name__ == "__main__"):
    jogar()