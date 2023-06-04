print("Bienvenido a la calculadora de unidades")

unidad=input("Dime que unidad tiene, A:Grados celcius B:Grados Kelvin c:Grados Fahrenheit").lower()

if unidad == "a":
    valor_A=float(input("Dime el valor de este"))
    calor_A1=input("Dime que unidad desea pasarlo, A:Grados Kelvin B:Grados Fahrenheit ").lower()
    if calor_A1 =="a":
        resultado=float(valor_A) + 273.15
        print(resultado)
    elif calor_A1 =="b":
        resultado=float(valor_A) *1.8 + 32
        print(resultado )
    else:
        print("Porfavor, elije una de las opciones posibles (A) O (B)")
elif unidad =="b":
    valor_b=float(input("Dime el valor de este"))
    calor_b1=input("Dime que unidad desea pasarlo, A:Grados celcius B:Grados Fahrenheit ").lower()
    if calor_b1 =="a":
        resultado=float(valor_b) -273.15
        print(resultado)
    elif calor_b1 =="b":
        resultado=1.8*(float(valor_b) - 273.15) + 32
        print(resultado )
    else:
        print("Porfavor, elije una de las opciones posibles (A) O (B)")
elif unidad =="c":
    valor_c=float(input("Dime el valor de este"))
    calor_c1=input("Dime que unidad desea pasarlo, A:Grados celcius B:Grados Kelvin ").lower()
    if calor_c1 =="a":
        resultado=(float(valor_c) - 32) / 1.8
        print(resultado)
    elif calor_c1 =="b":
        resultado=5/9 * (float(valor_c) - 32) + 273.15
        print(resultado )
    else:
        print("Porfavor, elije una de las opciones posibles (A) O (B)")
else:
     print("Porfavor, elije una de las opciones posibles (A) O (B) O (C)")          
            
