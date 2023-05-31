import random


def jogar():

  print("*********************************")
  print("Bem vindo ao jogo de Adivinhação!")
  print("*********************************\n")

  numero_secreto = random.randrange(1, 101)
  total_de_tentativas = 0
  chute_str = "0"
  pontos = 1000

  print("Qual o nível de dificuldade?")
  print("(1) Fácil (2) Médio (3) Difícil")

  nivel = int(input("Defina o nível: "))

  if (nivel == 1):
    total_de_tentativas = 20
  elif (nivel == 2):
    total_de_tentativas = 10
  else:
    total_de_tentativas = 5
  while (chute_str != "x"):
    for rodada in range(1, total_de_tentativas + 1):
      print("Tentativa {} de {}".format(rodada, total_de_tentativas))
      chute_str = input(
        "Digite um número entre 1 e 100, ou digite x para sair: ")
      print("\nVocê digitou {}".format(chute_str))

      if (chute_str != "x"):
        chute = int(chute_str)

        if (chute < 1 or chute > 100):
          print("Você deve digitar um número entre 1 e 100!")
          continue

        acertou = numero_secreto == chute
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
          print(
            "\nParabéns, você acertou!!!!, seu total de pontos é {}".format(
              pontos))
          break

        else:
          if (maior):
            print("Você errou! O seu chute foi maior que o número secreto.\n")
            if (rodada == total_de_tentativas):
              print("O número secreto era {}. Você fez {}".format(
                numero_secreto, pontos))
          elif (menor):
            print("Você errou! O seu chute foi menor que o número secreto.\n")
            if (rodada == total_de_tentativas):
              print("O número secreto era {}. Você fez {}".format(
                numero_secreto, pontos))
          pontos_perdidos = abs(numero_secreto - chute)
          pontos = pontos - pontos_perdidos

      else:
        print("Você saiu do jogo!\n")
        break

    break
  print("Obrigado por jogar!")


if (__name__ == "__main__"):
  jogar()