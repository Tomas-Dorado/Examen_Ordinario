import numpy as np
from EstadoCuantico import EstadoCuantico
class OperadorCuantico:
    def __init__(self, nombre, matriz):
        self.nombre = nombre
        self.matriz = matriz

    def aplicar(self, estado):
        nuevo_vector = [float(x) for x in np.dot(self.matriz, estado.vector)]
        nuevo_id = f"{estado.id}_{self.nombre}"
        return estado.__class__(id=nuevo_id, vector=nuevo_vector, base=estado.base)
    
    



# Ejemplo de uso:
if __name__ == "__main__":

    # Estado |0>
    estado = EstadoCuantico("q0", [1.00, 0.00], "computacional")
    # Operador X (puerta NOT cuántica)
    opX = OperadorCuantico("X", np.array([[0, 1], [1, 0]]))
    # Aplicar operador
    nuevo_estado = opX.aplicar(estado)
    print(nuevo_estado)           # Debería representar |1> = [0, 1] en base computacional
    print(nuevo_estado.vector)    # Esperado: [0, 1]
    

    
