# Faça um conversor de temperatura para Fahrenheit e Kelvin

celsius =  float(input("Graus: "))
medida = input("Kelvin / Fahrenheit [K, F]: ").upper()

k = float(celsius+273.15)
f = float((celsius*(18/10))+32)

if medida == "K":
      print(f"{k} Graus Kelvin")
else:
      print(f"{f} Graus Fahrenheit")

