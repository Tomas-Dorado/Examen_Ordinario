import math

class EstadoCuantico:
    def __init__(self, id: str, vector, base: str):
        if not isinstance(id, str) or not id:
            raise ValueError("El id debe ser una cadena no vacía.")
        if not isinstance(vector, list) or len(vector) == 0:
            raise ValueError("El vector debe ser una lista no vacía.")
        if not all(isinstance(x, (float, complex)) for x in vector):
            raise ValueError("Todos los elementos del vector deben ser float o complex.")
        if not isinstance(base, str) or not base:
            raise ValueError("La base debe ser una cadena no vacía.")

        norm = sum(abs(x)**2 for x in vector)
        if not abs(norm - 1.0) < 1e-8:
            raise ValueError("El vector debe estar normalizado (suma de |componentes|^2 debe ser 1).")

        self.id = id
        self.vector = vector
        self.base = base

    def medir(self):
        probabilidades = [abs(amplitud)**2 for amplitud in self.vector]
        return probabilidades
    
    def __str__(self):
        return f"{self.id}: vector={self.vector} en base {self.base}"

