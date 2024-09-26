prueba= str(input("Quieres entrar?"))

if prueba== "Si" or "si" or "sI" or "SI":
    print("Tienes mas de 18?")

if prueba== "No" or "no" or "nO" or "NO":
    segunda_oportunidad= int(input("seguro?"))
    if segunda_oportunidad== "Si" or "si" or "sI" or "SI":
        print("Tienes mas de 18?")
    while segunda_oportunidad== "No" or "no" or "nO" or "NO":
        segunda_oportunidad = int(input("seguro?"))
