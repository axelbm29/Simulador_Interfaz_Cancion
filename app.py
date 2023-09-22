# funcion conversion de palabra a ascii
def palabra_a_ascii(palabra):
    valor_ascii = [str(ord(caracter)) for caracter in palabra]
    return "".join(valor_ascii)

# funcion conversion de numero a binario
def decimal_a_binario(decimal):
    if decimal <= 0:
        return "0"
    binario = ""
    while decimal > 0:
        residuo = int(decimal % 2)
        decimal = int(decimal / 2)
        binario = str(residuo) + binario
    return binario

# Variables inicializadas en 0
TOTALCPU = 0
TOTALCiclos = 0

# leer cancion de un bloc de notas de nuestra carpeta
with open("cancion.txt", "r") as archivo:
    canciones = archivo.readlines()


for cancion in canciones:
    palabras = cancion.split()
    for palabra in palabras:
        # Tiempo CPUS
        TCPU = len(palabra) * 2
        #CICLOS RELOJ
        CRELOJ = 4 * TCPU
        # SUMATORIA DE TODOS LOS TIEMPOS CPU
        TOTALCPU += TCPU
        # SUMATORIA DE TODOS LOS CICLOS RELOJ
        TOTALCiclos += CRELOJ
        
        # CONVERSION PALABRA A ASCII
        valor_ascii = palabra_a_ascii(palabra)
        
        # CONVERSION DECIMAL A BINARIO
        binario = decimal_a_binario(int(valor_ascii))

        print(f"Unidad de analisis: {palabra}")
        print(f"ASCII: {valor_ascii}")
        print(f"BINARIO: {binario}")
        print(f"Tiempo CPUS: {TCPU}")
        print(f"CICLOS RELOJ: {CRELOJ}")
        print("*" * 50)

# Imprimir los totales al final
print(f"Total CPU: {TOTALCPU}")
print(f"Total CICLOS RELOJ: {TOTALCiclos}")
