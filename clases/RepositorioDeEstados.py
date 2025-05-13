from EstadoCuantico import EstadoCuantico
from OperadorCuantico import OperadorCuantico

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

    def aplicar_operador(self, id_estado: str, operador: OperadorCuantico, nuevo_id: str = None):
        estado_original = self.obtener_estado(id_estado)
        estado_transformado = operador.aplicar(estado_original)
        
        if nuevo_id is not None:
            estado_transformado.id = nuevo_id
            self.estados[nuevo_id] = estado_transformado
        else:
            # Generar un nuevo id si no se quiere sobrescribir el original
            nuevo_id_generado = f"{id_estado}_{getattr(operador, 'nombre', 'op')}"
            # Si el id generado ya existe, agregar un sufijo numérico
            contador = 1
            id_final = nuevo_id_generado
            while id_final in self.estados:
                id_final = f"{nuevo_id_generado}_{contador}"
                contador += 1
            estado_transformado.id = id_final
            self.estados[id_final] = estado_transformado

        # Si el id generado es igual al id original, actualizar el vector del estado existente
        if id_final == id_estado:
            self.estados[id_estado].vector = estado_transformado.vector
        else:
            self.agregar_estado(id_final, estado_transformado.vector, estado_transformado.base)



