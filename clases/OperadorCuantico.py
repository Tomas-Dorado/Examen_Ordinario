import numpy as np
from EstadoCuantico import EstadoCuantico

class OperadorCuantico:
    def __init__(self, nombre, matriz):
        self.nombre = nombre
        self.matriz = matriz

    def aplicar(self, estado):
        '''Aplica el operador cuántico al estado cuántico dado y devuelve un nuevo estado cuántico.'''
        nuevo_vector = [float(x) for x in np.dot(self.matriz, estado.vector)]
        nuevo_id = f"{estado.id}_{self.nombre}"
        return estado.__class__(id=nuevo_id, vector=nuevo_vector, base=estado.base)
    
    




    

    
