import numpy as np
from clases import EstadoCuantico, OperadorCuantico, RepositorioDeEstados

def ejecutar_pruebas():
    """Función principal que ejecuta todas las pruebas"""
    print("=== INICIO DE PRUEBAS DEL SISTEMA CUÁNTICO ===")
    
    # Crear repositorio
    repo = RepositorioDeEstados()
    
    # Prueba 1: Creación básica de estados
    print("\n--- Prueba 1: Creación de estados básicos ---")
    repo.agregar_estado("cero", [1.0, 0.0], "computacional")  # |0>
    repo.agregar_estado("uno", [0.0, 1.0], "computacional")   # |1>
    repo.agregar_estado("mas", [0.707, 0.707], "computacional")  # |+>
    repo.agregar_estado("menos", [0.707, -0.707], "computacional")  # |->
    
    print("Estados creados correctamente:")
    for estado_id in ["cero", "uno", "mas", "menos"]:
        print(f"- {repo.obtener_estado(estado_id)}")
    
    # Prueba 2: Operadores básicos
    print("\n--- Prueba 2: Operadores cuánticos ---")
    X = OperadorCuantico("Pauli-X", [[0, 1], [1, 0]])
    H = OperadorCuantico("Hadamard", [[0.707, 0.707], [0.707, -0.707]])
    print(X)
    print(H)
    
    # Prueba 3: Aplicación de operadores
    print("\n--- Prueba 3: Aplicación de operadores ---")
    repo.aplicar_operador("cero", X, "cero_X")  # X|0> = |1>
    repo.aplicar_operador("uno", X, "uno_X")    # X|1> = |0>
    repo.aplicar_operador("cero", H, "cero_H")  # H|0> = |+>
    repo.aplicar_operador("uno", H, "uno_H")    # H|1> = |->
    
    print("Resultados de aplicar operadores:")
    print(f"X|0> = {repo.obtener_estado('cero_X')}")
    print(f"X|1> = {repo.obtener_estado('uno_X')}")
    print(f"H|0> = {repo.obtener_estado('cero_H')}")
    print(f"H|1> = {repo.obtener_estado('uno_H')}")
    
    # Prueba 4: Mediciones
    print("\n--- Prueba 4: Mediciones de estados ---")
    print("Medición del estado |0>:")
    repo.medir_estado("cero")
    
    print("\nMedición del estado |+>:")
    repo.medir_estado("mas")
    
    print("\nMedición del estado H|0> (debería ser |+>):")
    repo.medir_estado("cero_H")
    
    # Prueba 5: Normalización automática
    print("\n--- Prueba 5: Normalización automática ---")
    repo.agregar_estado("no_normalizado", [1, 1], "computacional")
    print(f"Estado no normalizado: {repo.obtener_estado('no_normalizado')}")
    print("Probabilidades (deberían ser 50%-50%):")
    repo.medir_estado("no_normalizado")
    
    # Prueba 6: Manejo de errores
    print("\n--- Prueba 6: Manejo de errores ---")
    try:
        repo.agregar_estado("cero", [1, 0], "computacional")  # ID repetido
    except ValueError as e:
        print(f"Error correctamente capturado: {e}")
    
    try:
        repo.obtener_estado("no_existe")
    except ValueError as e:
        print(f"Error correctamente capturado: {e}")
    
    try:
        op_dim_err = OperadorCuantico("Mal", [[1, 0, 0], [0, 1, 0]])
        repo.aplicar_operador("cero", op_dim_err, "error")
    except ValueError as e:
        print(f"Error correctamente capturado: {e}")
    
    print("\n=== TODAS LAS PRUEBAS COMPLETADAS CON ÉXITO ===")

