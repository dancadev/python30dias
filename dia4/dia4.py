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

#saltar cadenas al cortar

pto = lenguaje[0:6:2]
print(pto)

'''

#metodos de cadena

#CAPITALIZE(): convierte el primer caracter de la letra en mayuscula

reto = 'treinta dias de python'
print(reto.capitalize())

#COUNT(): devuelve ocurrencias de subcadena en cadena, cuenta(subcadena, inicio=.., final=..). El inicio es una indexación inicial para contar y el final es el último índice para contar.

print(reto.count('i'))
print(reto.count('y', 7, 22)) #('y', 7, 22) y: caracter a buscar 7:desde esa posicion 22:hasta esa posicion 
print(reto.count('th'))#combinacion de caracteres a encontrar 

#ENDSWITH(): Termina con (): compureba siu la cadena termina copn un lugar especifico

print(reto.endswith('as'))
print(reto.endswith('on'))


#EXPANDTABS(): reemplaza el carácter de tabulación con espacios, el tamaño de tabulación predeterminado es 8. Toma el argumento de tamaño de tabulación

reto2 = 'treinta\tdias\tde\tpython'
print(reto2.expandtabs()) #tabulacion por defecto de 8
print(reto2.expandtabs(12))

#FIND(): Devuelve el índice de la primera aparición de una subcadena, si no se encuentra devuelve -1

print(reto.find('i'))
print(reto.find('th'))
print(reto.find('c'))

#RFIND(): Devuelve el índice de la última aparición de una subcadena, si no se encuentra devuelve -1

print(reto.rfind('y'))
print(reto.rfind('th'))

#FORMAT() formatea la cadena enb una salida mas agradable

first_name = 'Asabeneh'
last_name = 'Yetayeh'
age = 250
job = 'teacher'
country = 'Finland'
sentence = 'I am {} {}. I am a {}. I am {} years old. I live in {}.'.format(first_name, last_name, age, job, country)
print(sentence) # I am Asabeneh Yetayeh. I am 250 years old. I am a teacher. I live in Finland.

radius = 10
pi = 3.14
area = pi * radius ** 2
result = 'The area of a circle with radius {} is {}'.format(str(radius), str(area))
print(result) # The area of a circle with radius 10 is 314

#INDEX(): devuelve el índice más bajo de una subcadena, los argumentos adicionales indican el índice inicial y final (predeterminado 0 y longitud de cadena - 1). Si no se encuentra la subcadena, genera un valueError.

challenge = 'thirty days of python'
sub_string = 'da'
print(challenge.index(sub_string))  # 7
#print(challenge.index(sub_string, 9)) # error

#RINDEX(): Devuelve el índice más alto de una subcadena, los argumentos adicionales indican el índice inicial y final (predeterminado 0 y longitud de la cadena - 1)
print(challenge.rindex(sub_string))  # 8
#print(challenge.rindex(sub_string, 9)) # error

#ISALNUM() comprueba el caracter alfanumerico
print(reto.isalnum())
retoisa = '30diasdepython' 
print(retoisa.isalnum())

#ISALPHA() comprueba si todos los carcteres de la cadena son caracteres alfanumericos (az AZ)
print(reto.isalpha())
print(retoisa.isalpha())
retocaracteres = 'treintdiasdepython'
print(retocaracteres.isalpha())


#ISDECIMAL() Comprueba si todos los caracteres de una cadena son decimales (0-9)

print(reto.isdecimal())
entero = '358'
print(entero.isdecimal())

#ISDIGIT() Compruieba si todos los caracteres de la cadena son numeros (0-9 y algunos otros caracteres unicode para numneros )

print(entero.isdigit())
unicodigo = '\u00b2'
print(unicodigo.isdigit())

#ISNUMERIC(): comprueba si todos los caracteres de una cadena son números o están relacionados con números (al igual que isdigit(), solo acepta más símbolos, como ½)

print(entero.isnumeric())
print(unicodigo.isnumeric())
decimal = '10.5'
print(decimal.isnumeric())

#ISIDENTIFIER(): busca un identificador valido, verifica si una cadena es un nombre de variable valido

reto = '30diasdepython'
print(reto.isidentifier()) #false, porque inicia con un numero
reto = 'treinta_dias_de_python'
print(reto.isidentifier())

#ISLOWER(): comprueba si todos los caracteres de la cadena estan en minusculas
reto = 'treinta dias de python'
print(reto.islower())
reto2 = 'Treinta Dias De Python'
print(reto2.islower())

#ISUPPER(): Comprueba si todos los caracteres de la cadena estan en mayusculas
print(reto2.isupper())
reto_mayuscula = 'RETO'
print(reto_mayuscula.isupper())

#JOIN() devuelve la cadena concatenada

tecnologias = ['HTML','CSS','JAVASCRIPT']
resultado = ''.join(tecnologias)
print(resultado)
resultado = '#-'.join(tecnologias)
print(resultado)

#STRIP() elimina los caracteres indicados del principio y final de la cadena
print(reto.strip('tron'))

#REPLACE() Reemplaza la subcadena con una cadena dada
print(reto.replace('treinta','veinte'))

#SPLIT() divide la cadena utilizando la cadena dada o el espacio como separador
print(reto.split())
reto_split = 'treinta, dias, de, python'
print(reto_split.split(', '))

#TITLE() Devuelve la cadena de titulo en mayusculas
print(reto.title())

#SWAPCASE() Convierte todos los caracteres de mayusculas a minusculas y todos los caracteres en minusculas a mayusculas
print(reto.swapcase())
print(reto_mayuscula.swapcase())

#STARTSWITH() Comprueba si la cadena comienza con la cadena especificada
print(reto.startswith('tre'))
print(reto.startswith('red'))





