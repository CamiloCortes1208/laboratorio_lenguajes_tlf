"""
    HECHO POR:
        SEBASTIÁN JARAMILLO CARDONA
        JUAN CAMILO CORTÉS DÁVILA
        SANTIAGO SEPÚLVEDA BRAN
        VALENTINA CASTAÑO ZULUAGA
"""

def crear_alfabeto():
    cantidad_palabras_alfabeto = int(input("Ingrese la cantidad de caracteres del alfabeto: "))
    alfabeto=[]
    for i in range(cantidad_palabras_alfabeto):
        bandera=False

        while not bandera:
            caracter = input("Ingrese el caracter " + str(i + 1) + " del alfabeto: ")
            if caracter not in alfabeto:
                alfabeto.append(caracter)
                bandera=True
            else:
                print("Caracter repetido!")
    return alfabeto

def  generar_cadenas(alfabeto: [], longitud: int):
    cadenas=alfabeto.copy()
    if longitud == 0:
        return ['ε']
    elif longitud == 1:
        return alfabeto
    else:
        for i in range(longitud-1):
            aux=[]
            print("Longitud: " + str(i))
            for j in range(len(cadenas)):
                for k in range(len(alfabeto)):
                    caracter = cadenas[j]+alfabeto[k]
                    aux.append(caracter)
            cadenas=aux
    return cadenas

def is_parte_lenguaje(palabra: str, lenguaje: []):
    return palabra in lenguaje

def verificar_cadena_cadena(palabra: str, lenguaje: []):
    ###La palabra debe iniciar con f
    if not palabra.startswith("f"):
        print("Debe empezar con el caracter f")
        return False
    else:
        return is_parte_lenguaje(palabra, lenguaje)

def insertar_sufijo_prefijo(lenguaje: []):
    prefijo = input("Ingrese el prefijo: ")
    sufijo = input("Ingrese el sufijo: ")
    cadena = []
    for i in range(len(lenguaje)):
        if lenguaje[i].startswith(prefijo) and lenguaje[i].endswith(sufijo):
            cadena.append(lenguaje[i])
    return cadena



if __name__ == '__main__':
    alfabeto = crear_alfabeto()
    cadenas = generar_cadenas(alfabeto, int(input("Ingrese la longitud de palabra: ")))
    print("Posibles cadenas: \n", cadenas)
    print("Hace parte del lenguaje? ",is_parte_lenguaje(input("Ingrese una palabra para verificar: "), cadenas))
    print("Hace parte del lenguaje (Con regla): ",verificar_cadena_cadena(input("Ingrese una palabra que empiece con f: "), cadenas))
    print("Lenguaje con prefijo y sufijo: ", insertar_sufijo_prefijo(cadenas))




