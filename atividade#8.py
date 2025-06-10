valor = int(input('DIGITE ALGUM NUMERO PARA CALCULAR: '))
valor2 = int(input('DIGITE O SEGUNDO NUMERO PARA CALCULAR: '))
pergunta = input('QUAL TIPO DE OPERAÇÃO VOCÊ DESEJA REALIZAR? + | - | * | / ? ')

if pergunta == '+':
    while pergunta == '+':
        calculo = valor + valor2
        print(f'A RESPOSTA É = {calculo}')
        break
elif pergunta == '-':
    while pergunta == '-':
        calculo = valor - valor2
        print(f"A RESPOSTA É = {calculo}")
        break                
elif pergunta == '*':
    while pergunta == '*':
        calculo = valor * valor2
        print(f'A RESPOSTA É = {calculo}')
        break
elif pergunta == '/':
    while pergunta == '/':
        calculo = valor / valor2
        print(f"A RESPOSTA É = {calculo}")
        break
else:
     pergunta = input('QUAL TIPO DE OPERAÇÃO VOCÊ DESEJA REALIZAR? + | - | * | / ? ')
       