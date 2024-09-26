import flet as ft

from ParteB import obtener_alfabeto, es_palindromo
from ParteB import definir_lenguajes
from ParteB import unir_lenguajes
from ParteB import concatenar_lenguajes
from ParteB import generar_estrella
#from ParteB import es_palindromo
from ParteB import transformar_cadenas_lenguajes
from ParteB import generar_palindromos


def main(page: ft.Page):
    # Título de la aplicación
    page.title = "Laboratorio lenguajes"

    # Se definen las variables
    txt_simbolos = ft.TextField(
        label="Ingrese el alfabeto (los elementos deben tener espacios)",
        hint_text="a b c d e"
    )
    txt_palindromo = ft.TextField(label="Ingrese una palabra para verificar si es palindroma")
    # Definición de etiquetas
    label_resultado = ft.Text(value="", size=20, color="blue")

    # Métodos que se ejecutan al dar clic en los botones
    def mostrar_simbolos_click(e):
        alfabeto = obtener_alfabeto(txt_simbolos.value)
        label_resultado.value = f"El alfabeto es: {alfabeto}"
        page.update()

    def generar_lenguajes_click(e):
        alfabeto = obtener_alfabeto(txt_simbolos.value)
        lenguajes = definir_lenguajes(alfabeto)
        label_resultado.value = f"Los lenguajes son: {lenguajes}"
        page.update()

    def realizar_union_click(e):
        alfabeto = obtener_alfabeto(txt_simbolos.value)
        lenguajes = definir_lenguajes(alfabeto)
        union = unir_lenguajes(lenguajes)
        label_resultado.value = f"La unión de los lenguajes es: {union}"
        page.update()

    def realizar_concatenacion_click(e):
        alfabeto = obtener_alfabeto(txt_simbolos.value)
        lenguajes = definir_lenguajes(alfabeto)
        concatenacion = concatenar_lenguajes(lenguajes)
        label_resultado.value = f"La concatenación es: {concatenacion}"
        page.update()

    def realizar_estrella_click(e):
        alfabeto = obtener_alfabeto(txt_simbolos.value)
        lenguajes = definir_lenguajes(alfabeto)
        estrella = generar_estrella(lenguajes)
        label_resultado.value = (f"Como los lenguajes son aleatorios, el resultado puede variar."
                                 f" La estrella del lenguaje es: {estrella}")
        page.update()

    def generar_palindromos_click(e):
        alfabeto = obtener_alfabeto(txt_simbolos.value)
        palindromos = generar_palindromos(alfabeto)
        label_resultado.value = f"Los palindromos son: {palindromos}"
        page.update()

    def verificar_palindromo_click(e):
        alfabeto = obtener_alfabeto(txt_simbolos.value)
        palindromo = es_palindromo(txt_palindromo.value, alfabeto)
        if palindromo:
            label_resultado.value = f"La palabra ingresada es palindroma"
        else:
            label_resultado.value = f"La palabra ingresada no es palindroma"
        page.update()

    def cambiar_palabras_click(e):
        alfabeto = obtener_alfabeto(txt_simbolos.value)
        lenguajes = definir_lenguajes(alfabeto)
        lenguajes_nuevos = transformar_cadenas_lenguajes(lenguajes)
        label_resultado.value = f"Los lenguajes modificados son {lenguajes_nuevos}"
        page.update()

    # DEFINICIÓN DE BOTONES
    mostrar_resultados_btn = ft.ElevatedButton(text="Mostrar alfabeto", on_click=mostrar_simbolos_click)
    generar_lenguajes_btn = ft.ElevatedButton(text="Generar lenguajes", on_click=generar_lenguajes_click)
    realizar_union_btn = ft.ElevatedButton(text="Unir lenguajes", on_click=realizar_union_click)
    concatenar_lenguajes_btn = ft.ElevatedButton(text="Concatenar lenguajes", on_click=realizar_concatenacion_click)
    realizar_estrella_btn = ft.ElevatedButton(text="Realizar estrella", on_click=realizar_estrella_click)
    verificar_palindromo_btn = ft.ElevatedButton(text="Verificar palindromo", on_click=verificar_palindromo_click)
    cambiar_palabras_btn = ft.ElevatedButton(text="Cambiar palabra", on_click=cambiar_palabras_click)
    generar_palindromos_btn = ft.ElevatedButton(text="Generar palindromos", on_click=generar_palindromos_click)

    # Añadir los componentes a la página
    page.add(txt_simbolos, txt_palindromo, mostrar_resultados_btn, generar_lenguajes_btn,
             realizar_union_btn, concatenar_lenguajes_btn, realizar_estrella_btn, verificar_palindromo_btn,
             cambiar_palabras_btn, generar_palindromos_btn, label_resultado)


# Ejecutar la aplicación Flet
if __name__ == "__main__":
    ft.app(target=main)
