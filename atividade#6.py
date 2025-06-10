

#///////////////////////////// INICIO 

num = input("DIGITE UM NUMERO INTEIRO: ")

if num.isdigit():
    num_int = int(num)
    par_impar = num_int % 2 == 0
    imparText = 'IMPAR'

    if par_impar:
        imparText = 'PAR'

    print(f"O NUMERO DIGITADO É {imparText} ")
else:        
    print("ERRO! DIGITE UM NUMERO INTEIRO!")
   


#////////////////////////// MEIO

horas = float(input("INFORME AS HORAS: "))

if horas >= 0 and horas < 12:
    print(f"BOM DIA! {horas:.2f}pm")
elif horas >= 12 and horas < 17:
    print(f"BOA TARDE!! {horas:.2f}pm")
elif horas >= 18 and horas <= 23:
    print(f"BOA NOITE!!! {horas:.2f}pm")    


#////////////////////////// FIM

nome = input("ESCREVA O SEU NOME: ")
converte_nome = len(nome)
if converte_nome <= 4:
    print("SEU NOME É CURTO! ")
elif converte_nome  >= 5 and  converte_nome <= 6:
    print("SEU NOME É NORMAL! ") 
else:
    print("SEU NOME É MUITO GRANDE!")    
