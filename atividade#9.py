import random

dados = []
pessoas = ['Joaquim', 'Agnesio', 'Joao', 'Antonio', 'Davi', 'Rafael', 'Deivid', 'Fabricio', 'Aquiles', 'Peter']

for i in range(10):
    salario = int(random.randint(50, 500))
    filhos = int(random.randint(0, 5))
    dados.append((salario, filhos))
#MEDIA SALARIAL
soma = 0
for salario, filhos in dados: 
    soma = soma + salario
media = soma / 10

#MEDIA FILHOS
soma2 = 0
for salario, filhos in dados:
    soma2 = soma2 + filhos
media2 = filhos / 10


#MAIOR SALARIO
maior_salario = 0

for salario, filhos in dados:
    if salario > maior_salario:
        maior_salario = salario


#PERCENTUAL
contador = 0
for salario, filhos in dados:
    if salario <= 100:
        contador = contador + 1
percentual = (contador / salario) * 100       


for i, (salario, filhos) in enumerate(dados):
    print (f"{pessoas[i]} Tem {filhos} filhos e recebe R${salario:.2f}")
    

print('_________________________')
print(f"MEDIA SALARIAL: R${media}")
print(f"MEDIA DE FILHOS: {media2}")
print(f"O MAIOR SALARIO É: R${maior_salario}")
print(f"O PERCENTUAL DE PESSOAS QUE RECEBE MENOS OU ATE R$100.00 É = {percentual:.2f}%")