'''
 Finalidade Calculo Do imC

 Autor:
 data:
'''

peso = float(input("digite o peso"))
altura = float(input("digite a altura"))

imc = peso/(altura**2)
if(imc < 19.1):
    print("abaixo do peso")
elif (imc >= 19.1) and (imc <= 25.8):
    print("peso ideal")
elif (imc > 25.8) and (imc < 27.3):
    print("um pouco acima do peso")
elif (imc >= 27.3) and (imc <= 32.3):
    print("muito acima do peso")
elif (imc > 32.3):
    print("obeso")

else:
    print("algum error ocorreu no programa")

