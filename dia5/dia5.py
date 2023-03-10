'''
Lista:

Hay cuatro tipos de datos de colección en Python:

Lista: es una colección ordenada y cambiable (modificable). Permite miembros duplicados.
Tupla: es una colección ordenada e inmutable o inmodificable (inmutable). Permite miembros duplicados.
Conjunto: es una colección desordenada, no indexada y no modificable, pero podemos agregar nuevos elementos al conjunto. No se permiten miembros duplicados.
Diccionario: es una colección desordenada, cambiable (modificable) e indexada. No hay miembros duplicados.
Una lista es una colección de diferentes tipos de datos ordenados y modificables (mutables). Una lista puede estar vacía o puede tener diferentes elementos de tipo de datos.
'''
'''
#como crear una lista

#forma1: uso de la funcion incorporada de lista:
lst = list()
lista_vacia = list()
print('El tamaño de la lista es: ',len(lista_vacia))

#forma2: usando corchetes:
lista= []
print('la lista tiene un tamaño de : ', len(lista))

#listas con valores iniciales
frutas = ['pera','manzana','tomate','mango','limon']
vegetales = ['choclo','repollo','tomate','zapallo']
productos_animales= ['leche','carne','mantequilla','yogurth']
tecnologias_web = ['HTML','CSS','JS','MONGODB']
ciudades = ['Pasto','Cali','Medellin','Bogota']

print(frutas)
print('Tamaño de la lista de frutas: ',len(frutas))
print(vegetales)
print('Tamaño de la lista de vegetales: ',len(vegetales))
print(productos_animales)
print('Tamaño de la lista de productos animales: ',len(productos_animales))
print(tecnologias_web)
print('Tamaño de la lista de tecnologias web: ',len(tecnologias_web))
print(ciudades)
print('Tamaño de la lista de ciudades: ',len(ciudades))

#las listas pueden contener difrentes tipos de datos:

lista_datos = ['texto',250, True, {'pais:':'Colombia','Ciudad: ':'Pasto'}]
print(lista_datos)
print('El tamaño de la lista de varios tipos de elementos es: ',len(lista_datos))
print('\n')

#acceder a los elemntos de una lista mediante indexacion positiva
print('### INDEXACION POSITIVA ###')

print('Fruta posición 0 de la lista',frutas[0])
print('Fruta posición 1 de la lista',frutas[1])
print('Fruta posición 2 de la lista',frutas[2])
print('Fruta posición 3 de la lista',frutas[3])
print('Fruta posición 4 de la lista',frutas[4])
print('\n')

#acceder a los elementos de la lista mediante indxacion negativa
print('### INDEXACION NEGATIVA ###')

print('Fruta en la posicion -1: ',frutas[-1])
print('Fruta en la posicion -2: ',frutas[-2])
print('Fruta en la posicion -3: ',frutas[-3])
print('Fruta en la posicion -4: ',frutas[-4])
print('Fruta en la posicion -5: ',frutas[-5])
print('\n')

#desempaquetar elementos de la lista:
print('### DESEMPAQUETAR ELEMENTOS DE LA LISTA ###')

primer_item,segundo_item,tercer_item,*rest = vegetales
print(primer_item)
print(segundo_item)
print(tercer_item)
print(*rest)

first, second, third,*rest, tenth = [1,2,3,4,5,6,7,8,9,10]
print(first)          # 1
print(second)         # 2
print(third)          # 3
print(rest)           # [4,5,6,7,8,9]
print(tenth)          # 10

countries = ['Germany', 'France','Belgium','Sweden','Denmark','Finland','Norway','Iceland','Estonia']
gr, fr, bg, sw, *scandic, es = countries
print(gr)
print(fr)
print(bg)
print(sw)
print(scandic)
print(es)
'''
#cortar elementos de una lista: Indexación positiva: podemos especificar un rango de índices positivos especificando el inicio, el final y el paso, el valor de retorno será una nueva lista. (valores predeterminados para inicio = 0, final = len (lst) - 1 (último elemento), paso = 1)
#listas con valores iniciales
frutas = ['pera','manzana','tomate','mango','limon']
vegetales = ['choclo','repollo','tomate','zapallo']
productos_animales= ['leche','carne','mantequilla','yogurth']
tecnologias_web = ['HTML','CSS','JS','MONGODB']
ciudades = ['Pasto','Cali','Medellin','Bogota']

todas_frutas = frutas[0:4]
print(todas_frutas)
todas_frutas = frutas[0:]
print(todas_frutas)
pera_manzana = frutas[0:2]
print(pera_manzana)
tomate_mango_limon = frutas[2:]
print(tomate_mango_limon)
menos_limon = frutas[:4]
print(menos_limon)
limon = frutas[4:5]
print(limon)
saltando_una=frutas[::2]
print(saltando_una)

#Indexación negativa: podemos especificar un rango de índices negativos especificando el inicio, el final y el paso, el valor devuelto será una nueva lista.

manzana= frutas[-4]
print(manzana)
tomate_mango = frutas[-2:-3]
print(tomate_mango)

#modificacion de las listas

frutas[0] = 'aguacate'
print(frutas)
ultimo_index = len(frutas) -1
frutas[ultimo_index] = 'uva'
print(frutas)

#comprobacion de un elemnto de la lista: Comprobación de un elemento si es miembro de una lista mediante el operador in . Vea el ejemplo a continuación.

no_existe = 'curuba' in frutas
print(no_existe)
existe = 'manzana' in frutas
print(existe)

#adicion de elemntos a una lista: Para agregar un elemento al final de una lista existente, usamos el método append() .

frutas.append('curuba')
print(frutas)
frutas.append('lima')
print(frutas)

#insertar elementos en una lista: Podemos usar el método insert() para insertar un solo elemento en un índice específico en una lista. Tenga en cuenta que otros elementos se desplazan a la derecha. Los métodos insert() toman dos argumentos: índice y un elemento para insertar.

frutas.insert(2,'pera')
print(frutas)
frutas.insert(4,'uvilla')
print(frutas)
print(len(frutas))

#eliminacion de elemntos de una lista: el metodo remove() elimina un elemnto especifico de una lista

frutas.remove('uvilla')
print(frutas)

#eliminacion de elementos mediante pop: El método pop() elimina el índice especificado (o el último elemento si no se especifica el índice):

frutas.pop()
print(frutas)
frutas.pop(3)
print(frutas)

#eliminacion de elementos mediaten del: La palabra clave del elimina el índice especificado y también se puede usar para eliminar elementos dentro del rango del índice. También puede eliminar la lista por completo.

del frutas[0]
print(frutas)
del frutas[2]
print(frutas)
#frutas = ['pera','manzana','tomate','mango','limon']
del frutas
print(frutas)