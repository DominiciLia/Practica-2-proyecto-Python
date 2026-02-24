import random2

def generar_frase():
    nombre = input("¿Cómo te llamas? ")

    frases = [
        "El esfuerzo de hoy es el éxito de mañana.",
        "Nunca te rindas.",
        "Confía en ti misma.",
        "Todo es posible con dedicación.",
        "Cada día es una nueva oportunidad."
    ]

    frase_aleatoria = random2.choice(frases)

    print(f"\nHola {nombre}")
    print("Tu frase de hoy es:")
    print(frase_aleatoria)

if __name__ == "__main__":
    generar_frase()