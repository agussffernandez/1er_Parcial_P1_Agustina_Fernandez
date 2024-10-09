def mostrar_opciones():
    """ 
    Muestra las opciones disponibles
    """
    print(
        """ 
        1. Cargar pacientes
        2. Mostrar la lista de pacientes
        3. Busqueda de pacientes
        5. Ordenamiento de pacientes
        6. Determinar el paciente con más dias de internación
        7. Determinar el paciente con menos dias de internación
        8. Cantidad de pacientes con días de internación mayor a 5 días
        9. Promedio de días de internación de todos los pacientes
        10. Salir
        """
    )



def cargar_pacientes(lista_pacientes: list) -> list:
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
    print(lista_pacientes)

