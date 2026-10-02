class TablaMultiplicar:
    def __init__(self, numero):
        self.numero = numero

    def generar(self):
        
        tabla = []
        
        for i in range(1, 11):
            resultado = self.numero * i
            
            tabla.append({"multiplicador": i, "resultado": resultado})
        return tabla