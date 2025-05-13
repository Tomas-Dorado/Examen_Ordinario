import numpy as np

class OperadorCuantico:
    def __init__(self, nombre, matriz):
        self.nombre = nombre
        self.matriz = matriz

    def aplicar(self, estado):
        nuevo_vector = np.dot(self.matriz, estado.vector)
        return estado.__class__(nuevo_vector)