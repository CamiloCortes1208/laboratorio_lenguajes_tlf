import flet as ft

from ParteB import obtener_alfabeto
from ParteB import definir_lenguajes
from ParteB import unir_lenguajes
from ParteB import concatenar_lenguajes
from ParteB import generar_estrella


def main(page: ft.Page):
    # Título de la aplicación
    page.title = "Laboratorio lenguajes"

    # Se definen las variables
    txt_opcion = ft.TextField(label="Opción")
    simbolos = ft.TextField(
        label="Ingrese el alfabeto (los elementos deben tener espacios)",
        hint_text="a b c d e"
    )

    # Definición de etiquetas
    label_alfabeto = ft.Text(value="", size=20, color="blue")
    label_lenguajes = ft.Text(value="", size=20, color="blue")
    label_union = ft.Text(value="", size=20, color="blue")
    label_concatenacion = ft.Text(value="", size=20, color="blue")
    label_estrella = ft.Text(value="", size=20, color="blue")

    # Métodos que se ejecutan al dar clic en los botones
    def mostrar_simbolos_click(e):
        alfabeto = obtener_alfabeto(simbolos.value)
        label_alfabeto.value = f"El alfabeto es: {alfabeto}"
        page.update()

    def generar_lenguajes_click(e):
        alfabeto = obtener_alfabeto(simbolos.value)
        lenguajes = definir_lenguajes(alfabeto)
        label_lenguajes.value = f"Los lenguajes son: {lenguajes}"
        page.update()

    def realizar_union_click(e):
        alfabeto = obtener_alfabeto(simbolos.value)
        lenguajes = definir_lenguajes(alfabeto)
        union = unir_lenguajes(lenguajes)
        label_union.value = f"La unión de los lenguajes es: {union}"
        page.update()

    def realizar_concatenacion_click(e):
        alfabeto = obtener_alfabeto(simbolos.value)
        lenguajes = definir_lenguajes(alfabeto)
        concatenacion = concatenar_lenguajes(lenguajes)
        label_concatenacion.value = f"La concatenación es: {concatenacion}"
        page.update()

    def realizar_estrella_click(e):
        alfabeto = obtener_alfabeto(simbolos.value)
        lenguajes = definir_lenguajes(alfabeto)
        estrella = generar_estrella(lenguajes)
        label_estrella.value = f"La estrella del lenguaje es: {estrella}"
        page.update()

    # DEFINICIÓN DE BOTONES
    mostrar_resultados_btn = ft.ElevatedButton(text="Mostrar alfabeto", on_click=mostrar_simbolos_click)
    generar_lenguajes_btn = ft.ElevatedButton(text="Generar lenguajes", on_click=generar_lenguajes_click)
    realizar_union_btn = ft.ElevatedButton(text="Unir lenguajes", on_click=realizar_union_click)
    concatenar_lenguajes_btn = ft.ElevatedButton(text="Concatenar lenguajes", on_click=realizar_concatenacion_click)
    realizar_estrella_btn = ft.ElevatedButton(text="Realizar estrella", on_click=realizar_estrella_click)

    # Añadir los componentes a la página
    page.add(simbolos, mostrar_resultados_btn, generar_lenguajes_btn, realizar_union_btn, concatenar_lenguajes_btn,
             realizar_estrella_btn, label_alfabeto, label_lenguajes, label_union, label_concatenacion, label_estrella)


# Ejecutar la aplicación Flet
if __name__ == "__main__":
    ft.app(target=main)
