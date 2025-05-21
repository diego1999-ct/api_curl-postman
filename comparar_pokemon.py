import requests

def obtener_estadisticas(pokemon):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon.lower()}"
    respuesta = requests.get(url)

    if respuesta.status_code == 200:
        datos = respuesta.json()
        stats = {stat["stat"]["name"]: stat["base_stat"] for stat in datos["stats"]}
        return stats
    else:
        return None

def solicitar_pokemon(numero):
    while True:
        nombre = input(f"Ingrese el nombre del Pokémon #{numero}: ").strip()
        stats = obtener_estadisticas(nombre)
        if stats:
            return nombre.capitalize(), stats
        else:
            print(f"❌ El Pokémon '{nombre}' no fue encontrado. Intenta nuevamente.\n")

def imprimir_comparacion(stats1, stats2, nombre1, nombre2):
    print(f"\n{'Estadística':<17} | {nombre1:<12} | {nombre2:<12}")
    print("-" * 45)
    for stat in stats1:
        valor1 = stats1.get(stat, "N/A")
        valor2 = stats2.get(stat, "N/A")
        print(f"{stat:<17} | {valor1:<12} | {valor2:<12}")

# Solicitar Pokémon válidos
nombre1, stats1 = solicitar_pokemon(1)
nombre2, stats2 = solicitar_pokemon(2)

# Mostrar comparación
imprimir_comparacion(stats1, stats2, nombre1, nombre2)
