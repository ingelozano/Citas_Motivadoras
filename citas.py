import random

# Lista de citas
citas = [
    "El éxito es la suma de pequeños esfuerzos repetidos día tras día.",
    "La única forma de hacer un gran trabajo es amar lo que haces.",
    "El momento es ahora.",
    "No importa lo lento que vayas, siempre y cuando no te detengas.",
    "La vida es lo que pasa mientras estás ocupado haciendo otros planes.",
    "La creatividad es la inteligencia divirtiéndose.",
    "El único modo de hacer un gran trabajo es amar lo que haces.",
    "La mejor manera de predecir el futuro es crearlo.",
    "El éxito no es definitivo, el fracaso no es fatal: lo que cuenta es el coraje para continuar.",
    "La vida es cambio, crecimiento y movimiento constantes.",
    "No cuentes los días, haz que los días cuenten.",
    "La única forma de hacer un gran trabajo es amar lo que haces.",
    "No hay atajos para llegar a un lugar que vale la pena.",
    "La confianza en uno mismo es el primer secreto del éxito.",
    "El mayor error es no intentarlo.",
    "La clave del éxito está en hacer las cosas con pasión.",
    "La perseverancia es la llave que abre todas las puertas.",
    "Nunca es tarde para ser lo que podrías haber sido.",
    "La única manera de hacer un gran trabajo es amar lo que haces.",
    "No temas fracasar, teme no intentarlo.",
    "La vida es un camino que debes recorrer con una sonrisa.",
    "Cada día es una nueva oportunidad para cambiar tu vida.",
    "Los sueños no funcionan a menos que tú lo hagas.",
    "La actitud es la diferencia entre un día bueno y un día malo.",
    "La disciplina es el puente entre metas y logros.",
]

# Función para generar una cita aleatoria
def generar_cita_aleatoria(citas):
    cita_aleatoria = random.choice(citas)
    return cita_aleatoria

# Programa principal
print("¡Bienvenido al Generador de Citas!")
while True:
    input("Presiona Enter para ver una cita motivadora...")
    cita = generar_cita_aleatoria(citas)
    print(cita)
    continuar = input("¿Deseas ver otra cita? (s/n): ")
    if continuar.lower() != "s":
        print("¡Hasta luego!")
        break

