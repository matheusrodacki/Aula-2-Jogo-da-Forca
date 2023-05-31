import forca
import adivinhacao

print("***************************")
print("Bem vindo! Escolha um jogo:")
print("***************************\n")

print("(1) Forca (2) Adivinhação")

jogo = int(input("Qual o jogo?"))

if (jogo == 1):
  print("Jogando Forca...\n")
  forca.jogar()
elif (jogo == 2):
  print("Jogando Adivinhação...\n")
  adivinhacao.jogar()