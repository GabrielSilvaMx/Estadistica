from collections import defaultdict
from prettytable import PrettyTable
import math

def frecuencia(serie:list) -> dict:
    # crear un diccionario con los valores únicos de la serie y su frecuencia
    frecuencia = defaultdict(int)
    for i in serie:
        frecuencia[i] += 1
    return frecuencia

def distribucion_frecuencia(serie:list, min=0, max=10, incr=10) -> dict:
    # crear un diccionario con indice de min a max con incrementos de incr
    distribucion = defaultdict(int)
    for i in range(min, max, incr):
        distribucion[f'{i} a menos de {( i + incr )}'] = 0
        # sumar los valores de la serie que cumplan con la condición
        distribucion[f'{i} a menos de {( i + incr )}'] = sum(map(lambda x: i <= x < i + incr, serie))
    return distribucion  

def distribucion_relativa(serie:dict) -> dict:
    valor_previo = 0
    distribucion = defaultdict(dict)

    for variable_x, frecuencia in serie.items():
        tabla_frec = defaultdict(lambda: [0, 0, 0, 0])    
        tabla_frec[variable_x][0] = frecuencia
        tabla_frec[variable_x][1] = tabla_frec[variable_x][0] + valor_previo
        tabla_frec[variable_x][2] = tabla_frec[variable_x][0] / sum(serie.values())
        tabla_frec[variable_x][3] = int( tabla_frec[variable_x][2] * 100)
        distribucion[variable_x] = tabla_frec[variable_x]
        valor_previo = tabla_frec[variable_x][1]
    return distribucion 

def pretty_table(data=dict, varX="x", frecuencia="f"):
    table = PrettyTable()
    #table.add_row(f'Min: {min(data.keys())} Max: {max(data.keys())}',divider=True)
    table.field_names = [varX, frecuencia]
    for key, value in data.items():
        table.add_row([key, value])
    return table

def pretty_table_frec_relativa(data=dict, field_names=list):
    table = PrettyTable()
    table.field_names = field_names
    # reduce column width
    table.max = 5
    for key, value in data.items():
        table.add_row([key, value[0], value[1], value[2], value[3]])
    table.add_divider()
    table.add_row(["Total", sum([value[0] for value in data.values()]), "", '{0:.2f}'.format(sum([value[2] for value in data.values()])), f'{int(sum([value[3] for value in data.values()]))} %'])
    return table

def reglaSturges(datos):
     # Determinar el número de clases o intervalos utilizando la raíz cuadrada del número de elementos de la serie.
     intervalos = math.ceil(math.sqrt(len(datos)))
     # Establecer el rango de los datos: máximo – mínimo
     rango = max(datos) - min(datos)
     # Dividir el rango entre el número de clases para determinar los intervalos de clase 
     # (este paso normalmente requiere de redondeos y ajustes para llegar, de preferencia, 
     # a valores enteros y gruesos, como decenas, por ejemplo)
     amplitud_clase = rango / intervalos
     # Determinar cuántos de los datos caen dentro de cada clase     
     return amplitud_clase