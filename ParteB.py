import random

import ParteA
import ParteA as parteA

"""
    HECHO POR:
        SEBASTIÁN JARAMILLO CARDONA
        JUAN CAMILO CORTÉS DÁVILA
        VALENTINA CASTAÑO ZULUAGA
        
        
        X 1. Definir tres lenguajes a partir de ellos.
        X 2. Aplicar operaciones como unión, concatenación y estrella (a cada uno).
        FALTA 3. Implementar una o varias funciones para generar palíndromos.
        X 4. Pedir al usuario que ingrese una cadena y verificar si es un palíndromo.
        FALTA 5. Implementar una o varias funciones para transformar cadenas de acuerdo con reglas específicas como reemplazo de caracteres e inversión de cadenas.
        FALTA 6. Crear un menú donde se contengan los puntos anteriores y el usuario seleccione el proceso a realizar, en este ítem pueden utilizar Tkinder u otra librería que facilite la parte gráfica.

        
        NO USAR INVERTIR NI REEMPLAZAR
"""


# Crear alfabeto / se define para la UI
def obtener_alfabeto(simbolos):
    # Usar split para dividir la cadena por espacios
    elementos = simbolos.split()
    return elementos


# Se definen tres lenguajes a partir de los elementos del alfabeto
def definir_lenguajes(alfabeto: []):
    cantidad_lenguajes = 3  # int(input("Ingrese la cantidad de lenguajes"))  3 veces
    lenguajes = []
    for i in range(cantidad_lenguajes):
        lista_temporal = []
        cantidad_elementos_lenguaje: int = random.randint(1, 5)
        lista_cadenas = parteA.generar_cadenas(alfabeto, cantidad_elementos_lenguaje)
        for j in range(cantidad_elementos_lenguaje):
            palabra = random.choice(lista_cadenas)
            if palabra not in lista_temporal:
                lista_temporal.append(palabra)
                j -= 1
        lenguajes.append(lista_temporal)
    return lenguajes


# Unión de lenguajes
def unir_lenguajes(lista: []):
    conjunto_union = []
    for conjunto in lista:
        for elemento_conjunto in conjunto:
            if elemento_conjunto not in conjunto_union:
                conjunto_union.append(elemento_conjunto)
    return conjunto_union


# Concatenación de lenguajes
def concatenar_lenguajes(lista: []):
    lenguaje_concatenacion = []
    for i in range(len(lista[0])):
        for j in range(len(lista[1])):
            palabra = lista[0][i] + lista[1][j]
            lenguaje_concatenacion.append(palabra)
    return lenguaje_concatenacion


def generar_estrella(lenguajes: []):
    lista_estrella = []
    for i in range(5):
        aux = ParteA.generar_cadenas(lenguajes[0], i)
        lista_estrella.append(aux)
    return lista_estrella


def operacion_conjuntos(lenguajes: []):
    lista = []
    opcion: int = int(input("Elija 1 opcion:\n1. union\2. concatenación\n3. estrella"))
    if opcion == 1:
        lista = (unir_lenguajes(lenguajes))
    elif opcion == 2:
        lista = concatenar_lenguajes(lenguajes)
    elif opcion == 3:
        lista = generar_estrella(lenguajes)
    else:
        print("Opcion invalida")

    return lista


# Implementar una o varias funciones para generar palíndromos


def generar_palindromos(alfabeto):
    lista_palindromas = []
    cantidad_palabras_lenguaje_palindromos: int = random.randint(1, 10)
    for i in range(cantidad_palabras_lenguaje_palindromos):
        longitud_palabra: int = random.randint(1, 10)
        palabra = crear_palindromo(alfabeto, "", longitud_palabra)
        lista_palindromas.append(palabra)
    print(lista_palindromas)


def crear_palindromo(alfabeto, palabra, longitud):
    """
    Algoritmo recursivo que crea una palabra palindroma aleatoriamente
    :param alfabeto: alfabeto del cual se sacarán los simbolos aleatoriamente
    :param palabra: este parametro sirve para almacenar la palabra en todo el metodo recursivo
    :param longitud: longitud de la palabra
    :return: palabra recursiva
    """
    if longitud > 0:
        simbolo_aleatorio = random.choice(alfabeto)
        if longitud >= 2:
            palabra = simbolo_aleatorio + crear_palindromo(alfabeto, palabra, longitud - 2) + simbolo_aleatorio
        else:
                palabra = simbolo_aleatorio + crear_palindromo(alfabeto, palabra, longitud - 1)
    return palabra


def es_palindromo(secuencia, alfabeto):
    # Convertir la secuencia en una lista de símbolos basada en el alfabeto
    simbolos = []
    i = 0
    while i < len(secuencia):
        # Recorremos el alfabeto para ver si algún símbolo coincide con la secuencia
        for simbolo in alfabeto:
            if secuencia[i:i + len(simbolo)] == simbolo:
                simbolos.append(simbolo)
                i += len(simbolo)
                break
        else:
            # Si no se encuentra ningún símbolo, hay un error en la secuencia
            raise ValueError(f"Símbolo desconocido en la secuencia: {secuencia[i]}")

    # Verificar si la lista de símbolos es un palíndromo
    return simbolos == simbolos[::-1]


if __name__ == '__main__':
    # Se le pide al usuario la cantidad y los elementos del alfabeto
    alfabeto = parteA.crear_alfabeto()
    generar_palindromos(alfabeto)

    print(es_palindromo("ANNANANA",alfabeto))
    """
    lenguajes: [] = definir_lenguajes(alfabeto)
    print(lenguajes)
    lista = operacion_conjuntos(lenguajes)


    print(lista)
    print(es_palindroma("ama"))
    print(es_palindroma("lola"))
    print(es_palindroma("reconocer"))
    
    """
