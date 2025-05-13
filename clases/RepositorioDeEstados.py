from EstadoCuantico import EstadoCuantico
from OperadorCuantico import OperadorCuantico

class RepositorioDeEstados:
    def __init__(self):
        self.estados = {}

    def listar_estados(self):
        ''' Devuelve una lista con los identificadores de los estados.'''
        if not self.estados:
            return []
        return [str(estado) for estado in self.estados.values()]
    
    def agregar_estado(self, id, vector, base):
        ''' Agrega un nuevo estado al repositorio.'''
        if id in self.estados:
            raise ValueError(f"Error: ya existe un estado con identificador '{id}'")
        estado = EstadoCuantico(id, vector, base)
        self.estados[id] = estado

    def obtener_estado(self, id):
        ''' Devuelve el estado asociado al identificador.'''
        try:
            return self.estados[id]
        except KeyError:
            raise ValueError(f"Error: no existe un estado con identificador '{id}'")
        
    def eliminar_estado(self, id):
        ''' Elimina un estado del repositorio.'''
        if id not in self.estados:
            raise ValueError(f"Error: no existe un estado con identificador '{id}'")
        del self.estados[id]

    def aplicar_operador(self, id_estado: str, operador: OperadorCuantico, nuevo_id: str = None):
        """
        Aplica un operador cuántico a un estado existente.
        - Si se proporciona 'nuevo_id', el estado transformado se guarda con ese identificador y el original permanece.
        - Si no se proporciona 'nuevo_id', se genera uno automáticamente (por ejemplo, 'q0_H'), y el original permanece.
        - En ningún caso se sobrescribe ni elimina el estado original automáticamente, permitiendo comparar antes y después.
        """
        estado_original = self.obtener_estado(id_estado)
        estado_transformado = operador.aplicar(estado_original)

        if nuevo_id is not None:
            estado_transformado.id = nuevo_id
            self.estados[nuevo_id] = estado_transformado
        else:
            # Generar un nuevo id basado en el operador
            base_id = f"{id_estado}_{getattr(operador, 'nombre', 'op')}"
            id_final = base_id
            contador = 1
            while id_final in self.estados:
                id_final = f"{base_id}_{contador}"
                contador += 1
            estado_transformado.id = id_final
            self.estados[id_final] = estado_transformado


    def medir_estado(self, id, imprimir=True):
        """
        Mide el estado cuántico y muestra/retorna las probabilidades.
        
        Args:
            id (str): ID del estado a medir
            imprimir (bool): Si True, imprime resultados formateados
            
        Returns:
            dict: Probabilidades de medición si imprimir=False
        """
        estado = self.obtener_estado(id)
        probabilidades = estado.medir()
        
        if imprimir:
            print(f"\nMedición del estado {id} en base {estado.base}:")
            for resultado, prob in probabilidades.items():
                print(f"- {resultado}: {prob*100:.2f}%")
            print(f"Suma total: {sum(probabilidades.values())*100:.2f}%")
        else:
            return probabilidades

    
if __name__ == "__main__":
    # Crear repositorio
    repo = RepositorioDeEstados()
    
    # Agregar estados de ejemplo
    repo.agregar_estado("psi_plus", [0.707, 0.707], "computacional")  # |+>
    repo.agregar_estado("psi_minus", [0.707, -0.707], "computacional") # |->
    repo.agregar_estado("ejemplo", [0.6, 0.8], "computacional")  # Estado no normalizado
    
    # Definir operador Hadamard
    H = OperadorCuantico("H", [
        [0.707, 0.707],
        [0.707, -0.707]
    ])
    
    # Aplicar operador a un estado
    repo.aplicar_operador("psi_plus", H, "psi_plus_H")
    
    # Medir diferentes estados
    print("\n=== Ejemplos de medición ===")
    repo.medir_estado("psi_plus")      # Medir estado |+>
    repo.medir_estado("psi_minus")     # Medir estado |->
    repo.medir_estado("ejemplo")       # Medir estado [0.6, 0.8]
    repo.medir_estado("psi_plus_H")    # Medir estado H|+> ≈ |0>
    
