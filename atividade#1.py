



consumo = float(input("Quantos quilowats você consumiu? "))
calculo = consumo * 0.12
resultado = calculo * (18 / 100) + 100

print(f"O valor total a ser pago pelo usuario será R${resultado:.2f} acrescido de 18% de ICMS")
