from EstadoCuantico import EstadoCuantico

class RepositorioDeEstados:
    def __init__(self):
        self.estados = {}

    def listar_estados(self):
        if not self.estados:
            return []
        return [str(estado) for estado in self.estados.values()]
    
    def agregar_estado(self, id, vector, base):
        if id in self.estados:
            raise ValueError(f"Error: ya existe un estado con identificador '{id}'")
        estado = EstadoCuantico(id, vector, base)
        self.estados[id] = estado

    def obtener_estado(self, id):
        try:
            return self.estados[id]
        except KeyError:
            raise ValueError(f"Error: no existe un estado con identificador '{id}'")
        
    def eliminar_estado(self, id):
        if id not in self.estados:
            raise ValueError(f"Error: no existe un estado con identificador '{id}'")
        del self.estados[id]

if __name__ == "__main__":
    repo = RepositorioDeEstados()
    # Agregar estados
    repo.agregar_estado("q1", [1.0, 0.0], "computacional")
    repo.agregar_estado("q2", [0.0, 1.0], "computacional")
    # Listar estados
    print("Estados en el repositorio:")
    print(repo.listar_estados())
    # Obtener un estado
    estado = repo.obtener_estado("q1")
    print("Estado obtenido:", estado)
    # Eliminar un estado
    repo.eliminar_estado("q2")
    print("Estados después de eliminar q2:")
    print(repo.listar_estados())

