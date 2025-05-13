import numpy as np

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

        self.id = id
        self.vector= self.normalizar(np.array(vector, dtype=complex))
        self.base = base

    @staticmethod
    def normalizar(vector):
        """Normaliza el vector de estado."""
        norma = np.linalg.norm(vector)
        if norma == 0:
            raise ValueError("El vector no puede ser cero")
        return vector / norma
    
    def medir(self):
        probabilidades = np.abs(self.vector)**2
        probabilidades /= np.sum(probabilidades)
        return list(zip(self.base, probabilidades))

    def __str__(self):
        return f"{self.id}: vector={self.vector} en base {self.base}"

