
nome = input("Digite seu nome: ")
altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))

imc = peso / (altura ** 2)

if imc < 18.5:
    print(F"{nome} você está abaixo do peso")
elif imc >= 18.5 and imc <=24.9:
    print(F"{nome} você está com o peso normal")
elif imc >= 25 and imc <= 29.9:
    print(F"{nome} você está com sobrepeso")
elif imc > 30:
    print(F"{nome} vpcê está com inicio de Obesidade")
else:
    print(F"{nome} você pode ter digitado algo errado")






