import os
import sys

# CODIGO TRADUCIDO DESDE C# DESDE UN PROYECTO QUE HICE EN EL C2

def limpiar_pantalla():
    """Equivalente a Console.Clear()"""
    os.system('cls' if os.name == 'nt' else 'clear')

def dibujar_menu(opciones: list[str], titulo: str):
    """
    Equivalente a Herramientas.DibujarMenu(string[] Menu, string Titulo).
    Calcula el ancho dinámico y centra el título dentro de bordes con caracteres ASCII.
    """
    longitud_max = len(titulo)
    for linea in opciones:
        if len(linea) > longitud_max:
            longitud_max = len(linea)

    espacios_titulo = longitud_max - len(titulo)
    espacios_izq = espacios_titulo // 2
    espacios_der = espacios_titulo - espacios_izq

    # Marco superior y título
    print("++" + ("-" * longitud_max) + "++")
    print("||" + (" " * espacios_izq) + titulo + (" " * espacios_der) + "||")
    print("++" + ("-" * longitud_max) + "++")

    # Filas de opciones
    for linea in opciones:
        espacios_relleno = longitud_max - len(linea)
        print("||" + linea + (" " * espacios_relleno) + "||")

    # Marco inferior
    print("++" + ("-" * longitud_max) + "++")
    print("++" + ("-" * longitud_max) + "++")

def dibujar_inputs(mensaje: str):
    """Equivalente a Herramientas.DibujarInputs(string Mensaje)."""
    longitud = len(mensaje)
    borde = "++" + ("-" * longitud) + "++" + ("-" * longitud) + "++"
    print(borde)
    espacios_izq = longitud // 2
    espacios_der = longitud - espacios_izq
    print("|| " + (" " * espacios_izq) + mensaje + (" " * espacios_der) + " ||")
    print(borde)

def capturar_opcion(min_opc: int, max_opc: int, mensaje_prompt: str = "> ") -> int:
    """
    Equivalente al bucle int.TryParse(Console.ReadLine(), out opcion) 
    y a la validación de rangos del código original en C#.
    """
    while True:
        entrada = input(mensaje_prompt).strip()
        try:
            opcion = int(entrada)
            if min_opc <= opcion <= max_opc:
                return opcion
            print(f"Introduzca una opcion valida (entre {min_opc} y {max_opc})!")
        except ValueError:
            print("Introduzca una opcion valida!")