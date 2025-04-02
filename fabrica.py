# Una fabrica de productos ceramicos
# Elabora 10 productos para CORONA
# Cada producto esta identidicado por:
# id, referencia (8 caracteres), descripción,
# precio de fabricacion individual,
# numero de piezas fabricadas,
# numero de piezas defectuosas
# fecha de envio de las piezas

# construya una función para agregar piezas la pedido
# construya una funcion para ver el pedido

def agregarPieza(lista, pieza):
    lista.append(pieza)
    return lista

def crearPieza(id, referencia, descripcion, precio,
               numeroFabricadas, numeroDefectuosas, fechaEnvio):
    pieza={
        "id":id,
        "referencia":referencia,
        "descripcion":descripcion,
        "precio":precio,
        "numeroFabricadas":numeroFabricadas,
        "numeroDefectuosas":numeroDefectuosas,
        "fechaEnvio":fechaEnvio
    }
    return pieza

def mostrarPedido(lista):
    for pieza in lista:
        print(lista)