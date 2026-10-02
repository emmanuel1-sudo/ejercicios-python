class ParImpar:

    def __init__(self, numero):
        self.numero = numero

    def comprobar(self):

        if self.numero % 2 == 0:
            return f"El número {self.numero} es PAR."
        else:
            return f"El número {self.numero} es IMPAR."