nota = int(input("DIGITE UMA NOTA: "))

while  nota > 100 or nota < 0: 
    print("Nota invalida!")
    nota = int(input("DIGITE UMA NOTA: "))


if nota >= 60:
    print("APROVADO") 
else:
    print("REPROVADO")       

