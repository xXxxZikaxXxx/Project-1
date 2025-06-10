
ano = int(input("DIGITE O ANO EM QUE ESTAMOS: "))
ano2 = int(input("DIGITE O ANO DE NASCIMENTO: ")) 

idade = ano - ano2

if idade > 0 and idade < 4:
    print(f"Você tem {idade} anos e é um BEBE!")
elif idade >= 4 and idade < 11:
    print(f"Você tem {idade} anos e é uma CRIANÇA!")
elif idade >= 11 and idade < 19:
    print(f"Você tem {idade} anos e é um ADOLESCENTE!")    
elif idade >= 19 and idade < 51:
    print(f"Você tem {idade} anos e é um ADULTO!")
else:
    print(f"Você tem {idade} anos e é um IDOSO!")    