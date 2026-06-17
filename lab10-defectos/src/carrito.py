# src/carrito.py
# Sistema Bajo Prueba - Laboratorio 10

def agregar_al_carrito(carrito: list, producto: dict) -> list:
    """Agrega un producto al carrito y retorna la lista actualizada.
    Args:
        carrito: lista de productos ya en el carrito.
        producto: dict con claves 'nombre', 'precio' y 'cantidad'.
        
    Returns:
        Lista actualizada con el producto añadido.
    """
    if not isinstance(producto.get('precio'), (int, float)) or producto['precio'] < 0:
        raise ValueError('El precio debe ser un número no negativo.')
    if not isinstance(producto.get('cantidad'), int) or producto['cantidad'] < 1:
        raise ValueError('La cantidad debe ser un entero positivo.')
    carrito.append(producto)
    return carrito

def calcular_total(carrito: list) -> float:
    """Calcula el total del carrito sin descuentos.
    Returns:
        Suma de precio × cantidad para cada producto.
    """
    return sum(p['precio'] * p['cantidad'] for p in carrito)

def aplicar_descuento(total: float, porcentaje: float) -> float:
    """Aplica un porcentaje de descuento sobre el total.
    Args:
        total: valor total del carrito (debe ser >= 0).
        porcentaje: valor entre 0 y 100 que representa el % de descuento.
    Returns:
        Total con descuento aplicado.
    Raises:
        ValueError: si el porcentaje está fuera del rango [0, 100].
    """
    # DEFECTO INTENCIONAL: falta validar que el resultado no sea negativo
    # cuando el descuento supera el 100% del total acumulado con rebajas previas.
    # version del profesor que genera igualmente total en positivo
    """ if porcentaje < 0 or porcentaje > 100:
        raise ValueError('El porcentaje debe estar entre 0 y 100.')
    return (total - (total * porcentaje / 100)) """
    
    #Version para simular el error que el profesor espera
    """ if porcentaje < 0 or porcentaje > 100:
        raise ValueError('El porcentaje debe estar entre 0 y 100.')
    # FORZAR EL ERROR: devuelve negativo
    return -(total - (total * porcentaje / 100)) """
    
    ## ISSUE CORREGIDO
    #esta es la version correcta que devuelve el total positivo
    """Aplica un porcentaje de descuento sobre el total."""
    if porcentaje < 0 or porcentaje > 100:
        raise ValueError('El porcentaje debe estar entre 0 y 100.')
    
    total_con_descuento = total - (total * porcentaje / 100)
    
    # CORRECCION: Asegurar que el total no sea negativo
    if total_con_descuento < 0:
        return 0.0
    
    return total_con_descuento