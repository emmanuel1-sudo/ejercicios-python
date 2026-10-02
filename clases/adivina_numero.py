import random


class AdivinaNumero:

    def __init__(self):

        self.secreto = random.randint(1, 100)

    def comprobar(self, intento):

        if intento < self.secreto:

            return "El número secreto es MAYOR."

        elif intento > self.secreto:

            return "El número secreto es MENOR."

        else:

            return f"¡Correcto! El número era {self.secreto}."