# -*- Coding: utf-8 -*-

print("Você deseja calcular qual parte do triângulo? ")
print("DIGITE 1, se deseja calcular um dos CATETOS")
print("DIGITE 2, se deseja calcular a HIPOTENUSA")
r = input("RESPOSTA: ")

if r == "1":
    c1 = input("Digite o valor do primeiro cateto: ")
    h = input("Digite o valor da hipotenusa: ")
    if not c1 == int or not h == int:
        print("Erro!")
    else:
        c2 = (h*h - c1*c1)**(1/2)
        print(f"O valor do segundo cateto é: {c2}")
        if (c1 < h + c2) and (c2 < h + c1) and (h < c2 + c1):
            print("É UM TRIÂNGULO!")
        else: 
            print("NÃO É UM TRIÂNGULO!")

elif r != "2" and r != "2":
    print("RESPOSTA INVÁLIDA!")

else:
    c1 = input("Digite o valor do primeiro cateto: ")
    c2 = input("Digite o valor do segundo cateto: ")
    if not c1 == int or not c2 == int:
        print("Erro!")
    else:
        h = (c1*c1 + c2*c2)**(1/2) 
        print(f"O valor da hipotenusa é: {h}")
        if (c1 < h + c2) and (c2 < h + c1) and (h < c2 + c1):
            print("É UM TRIÂNGULO!")
        else:
            print("NÃO É UM TRIÂNGULO!")