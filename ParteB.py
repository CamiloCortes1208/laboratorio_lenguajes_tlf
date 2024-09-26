import random

import ParteA
import ParteA as parteA

"""
    HECHO POR:
        SEBASTIÁN JARAMILLO CARDONA
        JUAN CAMILO CORTÉS DÁVILA
        VALENTINA CASTAÑO ZULUAGA
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
    for i in range(3):
        aux = ParteA.generar_cadenas(lenguajes[0], i)
        lista_estrella.append(aux)
    lista_plana = [elemento for sublista in lista_estrella for elemento in sublista]
    lista_plana.append("...")
    return lista_plana

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
    return lista_palindromas

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
    palabra_convertida_a_lista: [] = separar_cadena_por_alfabeto(secuencia,alfabeto)
    print(palabra_convertida_a_lista)
    if len(palabra_convertida_a_lista) == 0: return False
    for i in range(len(palabra_convertida_a_lista)):
        if palabra_convertida_a_lista[i] != palabra_convertida_a_lista[len(palabra_convertida_a_lista)-1-i]:
            return False
    return True
def separar_cadena_por_alfabeto(secuencia, alfabeto):
    resultado = []
    i = 0

    while i < len(secuencia):
        for patron in alfabeto:
            # Si el patrón coincide con una parte de la cadena
            if secuencia[i:i + len(patron)] == patron:
                resultado.append(patron)
                i += len(patron)  # Avanzar en la cadena según el patrón encontrado
                break
        else:
            # Si ningún patrón coincide, avanzamos uno
            i += 1

    return resultado

# Se definió como regla que todas las letras a, pasan a ser letras o
def transformar_cadenas_lenguajes(lenguajes: []):
    lista_lenguajes_modificados = []
    for lenguaje in lenguajes:
        lenguaje_modificado = []
        for palabra in lenguaje:
            palabra_modificada = reemplazar_letra(palabra, "a", "o")
            lenguaje_modificado.append(palabra_modificada)
        lista_lenguajes_modificados.append(lenguaje_modificado)
    return lista_lenguajes_modificados

def reemplazar_letra(palabra, letra_vieja, letra_nueva):
    nueva_palabra = ""
    for i in palabra:  # Iterar sobre cada carácter en la palabra
        if i == letra_vieja:
            nueva_palabra += letra_nueva  # Reemplazar si es la letra vieja
        else:
            nueva_palabra += i  # Mantener el carácter si no es la letra vieja
    return nueva_palabra


if __name__ == '__main__':

    # Se le pide al usuario la cantidad y los elementos del alfabeto
    alfabeto = parteA.crear_alfabeto()
    print(es_palindromo("adjasdkljashjdkas",alfabeto))

    #print(es_palindromo("ANNANANA", alfabeto))


    """
    lenguajes: [] = definir_lenguajes(alfabeto)
    print(lenguajes)
    lista = operacion_conjuntos(lenguajes)


    print(lista)
    print(es_palindroma("ama"))
    print(es_palindroma("lola"))
    print(es_palindroma("reconocer"))
    
    """
