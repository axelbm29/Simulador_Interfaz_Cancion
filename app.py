# Función para convertir una palabra a su representación ASCII
def palabra_a_ascii(palabra):
    ascii_values = [str(ord(caracter)) for caracter in palabra]
    return "".join(ascii_values)

# Función para convertir un número entero a representación binaria
def decimal_a_binario(decimal):
    if decimal <= 0:
        return "0"
    # Aquí almacenamos el resultado
    binario = ""
    # Mientras se pueda dividir...
    while decimal > 0:
        # Saber si es 1 o 0
        residuo = int(decimal % 2)
        # E ir dividiendo el decimal
        decimal = int(decimal / 2)
        # Ir agregando el número (1 o 0) a la izquierda del resultado
        binario = str(residuo) + binario
    return binario

# Inicializar las variables fuera de los bucles
TOTALCPU = 0
TOTALCiclos = 0

# Leer la canción desde un archivo de texto
with open("cancion.txt", "r") as archivo:
    canciones = archivo.readlines()

# Medir el tiempo de CPU y los ciclos de reloj
for cancion in canciones:
    palabras = cancion.split()
    for palabra in palabras:
        TCPU = len(palabra) * 2
        CRELOJ = 4 * TCPU
        TOTALCPU += TCPU
        TOTALCiclos += CRELOJ

        ascii_values = palabra_a_ascii(palabra)
        binario_values = decimal_a_binario(int(ascii_values))

        print(f"Unidad de analisis: {palabra}")
        print(f"ASCII: {ascii_values}")
        print(f"BINARIO: {binario_values}")
        print(f"Tiempo CPUS: {TCPU}")
        print(f"CICLOS RELOJ: {CRELOJ}")
        print("*" * 50)

# Imprimir los totales al final
print(f"Total CPU: {TOTALCPU}")
print(f"Total CICLOS RELOJ: {TOTALCiclos}")
