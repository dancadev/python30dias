#strings

'''
letra = 'A'
print(letra)
print(len(letra))

saludo = 'Hola bienvenido siga asi!!!'
print(saludo)
print(len(saludo))

sentencia = "Tambien se puede colocar con comillas dobles"
print(sentencia)

cadena_multilinea = """Esta es una cadena multilinea
todo aqui se imprime hasta 
los
espacios
""" 
print(cadena_multilinea)

#concatenacion de cadenas

nombre = 'Johana'
apellido = 'Enriquez'
espacio = ' '
nombre_completo = nombre + espacio + apellido
print(nombre_completo)

print(len(nombre))
print(len(apellido))
print(len(espacio))
print(len(nombre_completo))

#secuentcia de escape de cadenas

print('Fuerza y \nFe') #salto de linea
print('Dias\tTopics\tEjercicios') #agregando tab de 4 espacios
print('Dia 1\t3\t5')
print('Dia 2\t3\t5')
print('Dia 3\t3\t5')
print('Dia 4\t3\t5')
print('Este es el simbolo de backslash (\\)')
print('todos los lenguajes de programacion inician con \"Hola mundo\"')

#formato de cadena

# %s %d %f %.number of digitsf

# solamente cadenas
primer_nombre = 'David'
primer_apellido = 'Calvache'
lenguaje = 'Python'
cadena_formateada = 'Mi nombre es %s %s y estoy estudiando %s'%(primer_nombre,primer_apellido,lenguaje)
print(cadena_formateada)

#cadenas y numeros

radio = 10
pi = 3.1416
area = pi * radio **2
Cadena_formateada2 = 'el area del circulo con radio %d es %.2f'%(radio,area)
print(Cadena_formateada2)

librerias_python = ['Django','Flask','NumPy','Matplotlib','Pandas']
cadformat = 'Estas son algunas de las librerias de python: %s'%(librerias_python)
print(cadformat)

'''
'''
#Nuevo formato de estilo de cadena str.format

nombre = 'Johana'
apellido = 'Enriquez'
lenguaje = 'Python'
cadenafomato1 = '{} {} es mencionada en lenguaje de programacion {}'.format(nombre,apellido,lenguaje)
print(cadenafomato1)

a = 4 
b = 3

print('{} + {} = {}'.format(a,b,a+b))
print('{} - {} = {}'.format(a,b,a-b))
print('{} * {} = {}'.format(a,b,a*b))
print('{} / {} = {:.2f}'.format(a,b,a/b))
print('{} % {} = {}'.format(a,b,a%b))
print('{} // {} = {}'.format(a,b,a//b))
print('{} ** {} = {}'.format(a,b,a**b))

#nuevo formato para cadenas y numeros

radio = 10
pi = 3.1416
area = pi * radio **2
cadena_formato2 = 'El area de un circulo con radio {} es {:.2f}'.format(radio,area)
print(cadena_formato2)

'''

#interpolacion de cadenas / cadenas f

a = 4
b = 3
print(f'{a} + {b} = {a+b}')
print(f'{a} - {b} = {a-b}')
print(f'{a} * {b} = {a*b}')
print(f'{a} / {b} = {a/b:.2f}')
print(f'{a} % {b} = {a%b}')
print(f'{a} // {b} = {a//b}')
print(f'{a} ** {b} = {a**b}')

#cadenas de python como secuencias de caracteres

lenguaje = 'python'
a,b,c,d,e,f = lenguaje #edsempaquetando secuencia de caracteres dentro de variables
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

#acediendo a caracteres de cadenas por indices

lenguaje = 'python'
primera_letra = lenguaje[0]
segunda_letra = lenguaje[1]
tercera_letra = lenguaje[2]
cuarta_letra = lenguaje[3]
quinta_letra = lenguaje[4]
sexta_letra = lenguaje[5]
print(primera_letra)
print(segunda_letra)
print(tercera_letra)
print(cuarta_letra)
print(quinta_letra)
print(sexta_letra)

#cortar cadenas en python: se pueden dividir cadenas en subcadenas

primeras_tres = lenguaje[0:3]
print(primeras_tres)
ultimas_tres = lenguaje[3:6]
print(ultimas_tres)
# de otra manera:
primeras_tresB = lenguaje[-3:]
print('ultimas tres de otra manera: ',primeras_tresB)
primeras_tresC = lenguaje[3:]
print('Ultimas tres de otra manera más: ',primeras_tresC)

#invertir una cadena

cadena = 'Hola David Continua asi.'
print(cadena[::-1])





