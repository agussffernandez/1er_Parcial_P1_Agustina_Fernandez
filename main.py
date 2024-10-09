def mostrar_opciones():
    """ 
    Muestra las opciones disponibles
    """
    print(
        """ 
        1. Cargar pacientes
        2. Mostrar la lista de pacientes
        3. Busqueda de pacientes
        4. Ordenamiento de pacientes
        5. Determinar el paciente con más dias de internación
        6. Determinar el paciente con menos dias de internación
        7. Cantidad de pacientes con días de internación mayor a 5 días
        8. Promedio de días de internación de todos los pacientes
        9. Salir
        """
    )


def cargar_pacientes(lista_pacientes: list) -> list[list]:
    """ 
    Carga a un nuevo paciente con los datos ingresados por el usuario
    
    Args:
        lista_pacientes(list): la lista de pacientes a agregar uno nuevo
    
    Return:
        (list): La lista de pacientes actuallizada con el nuevo paciente
    """
    num_de_historia_clinica = int(input("Ingrese el número de historia clinica: "))
    nombre_paciente = str(input("Ingrese el nombre del paciente: ")).capitalize()
    edad_paciente = int(input("Ingrese la edad del paciente: "))
    diagnostico = str(input("Ingrese el diagnostico del paciente: ")).capitalize()
    cantidad_dias_internacion = int(input("Ingrese la cantidad de dias de internacion: "))
    
    datos_nuevo_paciente = [num_de_historia_clinica, nombre_paciente, edad_paciente, diagnostico, cantidad_dias_internacion]
    
    lista_pacientes.append(datos_nuevo_paciente)
    
    return lista_pacientes


def mostrar_lista_de_pacientes(lista_pacientes: list) -> None:
    """ 
    Muestra todos los datos de los pacientes almacenados
    
    Args:
        lista_pacientes(list): lista de pacientes almacenador a mostrar
    
    Return:
        (None): Imprime por pantalla la lista de pacientes almacenados
    """
    if not lista_pacientes:
        print("No hay pacientes registrados.")
        return 
    
    print(lista_pacientes)
    return 


def buscar_paciente(lista_pacientes: list):
    """ 
    Busca a un paciente por el número de historia clinica y muestra sus datos
    
    Args:
        lista_pacientes(list): la lista de pacientes en donde buscar al paciente por nro de clinica.
    
    Return:
        (list): Muestra los datos del paciente búscado si es que esta
        (None|str): Imprime paciente no encontrado
    """
    if not lista_pacientes:
        print("No hay pacientes registrados.")
        return 
    
    nro_clinica_a_buscar = int(input("Ingrese el numero de clinica del paciente a buscar: "))
    
    for i in range(len(lista_pacientes)):
        if lista_pacientes[i][0] == nro_clinica_a_buscar:
            print(lista_pacientes[i])
            return 
    
    print("Paciente no encontrado")
    return


def ord_burbuja(array: list):
    longitud = len(array)
    
    for i in range(longitud):
        for j in range(longitud - 1 - i): # Ponemos el -1 para dejar el último número fijo (ya que el ordenamiento burbuja es así). La i hace que el algoritmo no de vueltas de más al pedo.
            if array[j][0] > array[j+1][0]: # compara [j][0] el siguiente elemento de de la lista que sigue [j+1][0]
                # Intercambio los elementos
                temporal = array[j+1] #guarda el número sig al actual, para no pisarlo
                array[j+1] = array[j] # A la posición del núm sig, le guardo la posición j
                array[j] = temporal # A la posición j, le dejo el núm que estaba en j+1 (que para no pisarlo lo guarde en temporal)


def ordenamiento_de_pacientes(lista_pacientes: list) :
    """ 
    Ordena a los pacientes por su numero de historia clinica
    
    Args:
        lista_pacientes(list): lista de pacientes a ordenar por nro de historia clinica.
    
    Return:
        (None|list): lista de pacientes ordenados por nro de historia clinica
        (None|str): Imprime que no hay pacientes registrados
    """
    if not lista_pacientes:
        return print("No hay pacientes registrados.")
    # ordenamiento burbuja para ordenar 
    ord_burbuja(lista_pacientes)
    print(lista_pacientes)
    return 


def determinar_paciente_con_mayor_dias_de_internacion(lista_pacientes: list):
    """ 
    Determina el paciente con más días de internación, mostrando sus datos completos 
    
    Args:
        lista_pacientes(list): la lista de pacientes a determinar paciente con más días de internación
    
    Return:
        (None|list): La lista del paciente con más días de internación
        (None|str): Imprime que no hay pacientes registrados
    """
    if not lista_pacientes:
        print("No hay pacientes registrados.")
        return 
    
    paciente_mayor_internacion = lista_pacientes[0]
    for i in range(1, len(lista_pacientes)):
        if lista_pacientes[i][4] > paciente_mayor_internacion[4]: 
            paciente_mayor_internacion = lista_pacientes[i]
    
    print(paciente_mayor_internacion)
    return



def determinar_paciente_con_menor_dias_de_internacion(lista_pacientes: list) -> list|None:
    """ 
    Determina el paciente con menos días de internación, mostrando sus datos completos 
    
    Args:
        lista_pacientes(list): la lista de pacientes a determinar paciente con menos días de internación
    
    Return:
        (None|list): La lista del paciente con menos días de internación
        (None|str): Imprime que no hay pacientes registrados
    """
    if not lista_pacientes:
        print("No hay pacientes registrados.")
        return 
    
    paciente_menor_internacion = lista_pacientes[0]
    for i in range(1, len(lista_pacientes)):
        if lista_pacientes[i][4] < paciente_menor_internacion[4]: 
            paciente_menor_internacion = lista_pacientes[i]
    
    print(paciente_menor_internacion)
    return