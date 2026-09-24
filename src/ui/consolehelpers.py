import os
import sys

# CODIGO TRADUCIDO DESDE C# DESDE UN PROYECTO QUE HICE EN EL C2

def limpiar_pantalla():
    # limpia la pantalla
    os.system('cls' if os.name == 'nt' else 'clear')

def dibujar_menu(opciones: list[str], titulo: str):
    # calcula el ancho y centra el titulo con bordes ascii
    longitud_max = len(titulo)
    for linea in opciones:
        if len(linea) > longitud_max:
            longitud_max = len(linea)

    espacios_titulo = longitud_max - len(titulo)
    espacios_izq = espacios_titulo // 2
    espacios_der = espacios_titulo - espacios_izq

    # marco superior y titulo
    print("++" + ("-" * longitud_max) + "++")
    print("||" + (" " * espacios_izq) + titulo + (" " * espacios_der) + "||")
    print("++" + ("-" * longitud_max) + "++")

    # opciones
    for linea in opciones:
        espacios_relleno = longitud_max - len(linea)
        print("||" + linea + (" " * espacios_relleno) + "||")

    # marco inferior
    print("++" + ("-" * longitud_max) + "++")
    print("++" + ("-" * longitud_max) + "++")

def dibujar_inputs(mensaje: str):
    # marco del input
    longitud = len(mensaje)
    borde = "++" + ("-" * longitud) + "++" + ("-" * longitud) + "++"
    print(borde)
    espacios_izq = longitud // 2
    espacios_der = longitud - espacios_izq
    print("|| " + (" " * espacios_izq) + mensaje + (" " * espacios_der) + " ||")
    print(borde)

def capturar_opcion(min_opc: int, max_opc: int, mensaje_prompt: str = "> ") -> int:
    # valida que la opcion ingresada este dentro del rango permitido
    while True:
        entrada = input(mensaje_prompt).strip()
        try:
            opcion = int(entrada)
            if min_opc <= opcion <= max_opc:
                return opcion
            print(f"Introduzca una opcion valida (entre {min_opc} y {max_opc})!")
        except ValueError:
            print("Introduzca una opcion valida!")