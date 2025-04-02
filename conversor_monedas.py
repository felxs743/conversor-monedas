# Tasas de cambio predefinidas (estas son tasas ficticias, debes actualizarlas si es necesario)
TASA_MXN_USD = 0.054
TASA_MXN_EUR = 0.048
TASA_MXN_GBP =0.043
TASA_USD_MXN =18.57
TASA_EUR_MXN =20.81
TASA_GBP_MXN =23.26

#Funcion para convertir pesos a otras monedas
def convertir_mxn_a_otra(moneda, cantidad ):
    if moneda == "USD":
        return cantidad * TASA_MXN_USD
    elif moneda == "EUR":
        return cantidad * TASA_MXN_USD
    elif moneda == "GBP":
        return cantidad * TASA_MXN_GBP
    else:
        return None

# Funcion para convertir de otra moneda a pesos
def convertir_otra_a_mxn(moneda, cantidad):
    if moneda ="USD":
        return cantidad * TASA_USD_MXN
    elif moneda == "EUR":
        return cantidad * TASA_EUR_MXN
    elif moneda == "GBP":
        return cantidad * TASA_GBP_MXN
    else:
        return None

# Menu de opciones 
print( "Bienvenido al conversor de monedas")
print( "Elige una opcion: ")
print( "1. Convertir de Pesos Mexicanos (MXN) a ptra moneda")
print( "2. Convertir de otra moneda a Pesos Mexicanos (MXN)")

# Validacion de entrada
try:
    opcion = int(input("Ingresa el numero de la opcion que deseas: "))

if opcion == 1:
    print("Monedas disponibles para convertir desde Pesos Mexicanos (MXN):")
    print("1. Convertir a Dolares (USD)")
    print("2. Convertir a Euros (EUR)")
    print("3. Convertir a Libras Esterlinas (GBP)")

    opcion_moneda = int(input("Selecciona el numero de la moneda a la que deseas convertir: "))
    cantidad = float(input("Ingresa la cantidad de Pesos Mexicanos (MXN): "))

    if opcion_moneda == 1:
        resultado = convertir_mxn_a_otra("USD", cantidad)
        print(f"{cantidad} MXN son {resultado} USD")
    elif opcion_moneda == 2:
        resultado = convertir_mxn_a_otra("EUR", cantidad)
        print(f"{cantidad} MXN son {resultado} EUR")
    elif opcion_moneda == 3:
        resultado= convertir_mxn_a_otra("GBP", cantidad)
        print(f"{cantidad} MXN son {resultado} GBP")
    else: 
        print( "Opcion no valida.")

elif opcion == 2:
    print("Monedas disponibles para convertir a Pesos Mexicanos (MXN):")
    print("1.Convertir desde Dolares (USD) a MXN")
    print("2. Convertir desde Euros (EUR) a MXN")
    print("3. Convertir desde Libras Esterlinas (GBP) a MXN")

    opcion_moneda = int(input("Selecciona el numero de la moneda desde la que deseas convertir:"))
    cantidad = float(input("Ingresa la cantidad de la moneda seleccionada: "))

    if opcion_moneda == 1:
        resultado= convertir_otra_a_mxn("USD", cantidad)
        print(f"{cantidad} USD son {resultado} MXN")
    elif opcion_moneda == 2:
        resultado = convertir_otra_a_mxn("EUR", cantidad)
        print(f"{cantidad} EUR son {resultado} MXN")
    elif opcion_moneda == 3:
        resultado = convertir_otra_a_mxn("GBP", cantidad)
        print(f"{cantidad} GBP son {resultado} MXN")
    else:
        print("Opcion no valida")

    else: 
        print("Opcion no valida. Por favor, selecciona una opcion entre 1 y 2")

except ValueError:
    print("Entrada no valida. Por favor, ingresa un numero valido")
        