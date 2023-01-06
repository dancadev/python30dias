'''
# OPERADORES

#BOOBLEANOS
print(True)
print(False)

#ARITMETICOS

#ENTEROS
print('Adicion o suma: ', 1+2)
print('Substracion o resta: ', 2-1)
print('Multiplicación: ', 2*3)
print('División: ', 6/2)
print('Division: ',4/2)
print('Division: ', 7/2)
print('Division sin el resto: ', 7//2)
print('Division sin el resto: ', 7//3)
print('Modulo MOD', 3%2)
print('Exponenciación: ', 2**3)

#FLOAT

print('Numero flotante PI: ', 3.14)
print('Numero flotante  de Gravedad: ', 9.81)

#COMPLEJOS

print('Numero complejo: ', 1+1j)
print('Multiplicando Numeros Complejos: ',(1+1j)*(1-1j))
'''
'''
#declaracione de variables:
#se debe declarar la variable primero:

a=3
b=2

#operaciones artimeticas y asignar resultados a la variable

suma = a+b
diferencia = a-b
multiplicacion = a*b
division = a/b
mod = a%b
floorDivision = a//b
exponencial = a**b

print('El total de la suma es: ',suma)
print('La diferencia es: ',diferencia)
print('La multiplicación es: ',multiplicacion)
print('La division es: ', division)
print('Mod es:',mod)
print('Floor Division es:',floorDivision)
print('Exponencial es: ',exponencial)

'''
'''
print('=== Suma,resta,multiplicación, división, modulo ===')
n1= 3
n2 = 4

suma = n1+n2
resta = n2-n1
multiplicacion =  n1*n2
division = n2 / n1
modulo = n2 % n1

print('El total de la suma es: ',suma)
print('La diferencia es: ',resta)
print('La multiplicación es: ',multiplicacion)
print('La division es: ', division)
print('Mod es:',modulo)

'''

'''
#calculando el area de un circulo

radio = input('Ingrese el valor de Radio: ')
print('El Radio es: ',radio)

area_circulo = 3.1416 * int(radio) ** 2
print('El area del circulo es: ',area_circulo)

#calulando el area de un rectangulo:

ancho = input('Ingrese el valor del ancho del rectangulo: ')
print('Usted ingreso como valor de ANCHO :',ancho)
alto = input('Ingrese el calor del alto del rectangulo: ')
print('Usted ingreso el valor de ALTO',alto)

area_rectangulo = float(ancho)*float(alto)
print('El area del triangulo es: ',area_rectangulo)

#calculando el peso de un objeto

masa = float(input('Cual es la masa del objeto: ')) 
gravedad = 9.81
peso = masa*gravedad
print('El peso del objeto es: ',peso)

#calulando la densidad de un liquido
masal = float(input('Cual es la masa del objeto kg: '))
volumen = float(input('Cual es volumen m^3 del objeto: ')) 
densidad = masal / volumen
print('la densidad del liguido es : ', densidad , ' Kg/m^3')


'''
'''
#operadores de comparacion

print(3>2)
print(3>=2)
print(3<2)
print(2<3)
print(2<=3)
print(3 == 2)
print(3!=2)
print(len('mango') == len('aguacate'))
print(len('mango') != len('aguacate'))
print(len('mango') < len('aguacate'))
print(len('leche') != len('carne'))
print(len('leche') == len('carne'))
print(len('tomate') == len('papa'))
print(len('python') > len('dragon'))

#comparndo valores de tru o false 

print('True == True', True == True)
print('True == False', True == False)
print('False == False', False == False)

'''
#is, is not ,in,not in

print('1 is 1', 1 is 1)                   # True - because the data values are the same
print('1 is not 2', 1 is not 2)           # True - because 1 is not 2
print('A in Asabeneh', 'A' in 'Asabeneh') # True - A found in the string
print('B in Asabeneh', 'B' in 'Asabeneh') # False - there is no uppercase B
print('coding' in 'coding for all') # True - because coding for all has the word coding
print('a in an:', 'a' in 'an')      # True
print('4 is 2 ** 2:', 4 is 2 ** 2)   # True

#operadores logicos
print(3 > 2 and 4 > 3) # True - because both statements are true
print(3 > 2 and 4 < 3) # False - because the second statement is false
print(3 < 2 and 4 < 3) # False - because both statements are false
print('True and True: ', True and True)
print(3 > 2 or 4 > 3)  # True - because both statements are true
print(3 > 2 or 4 < 3)  # True - because one of the statements is true
print(3 < 2 or 4 < 3)  # False - because both statements are false
print('True or False:', True or False)
print(not 3 > 2)     # False - because 3 > 2 is true, then not True gives False
print(not True)      # False - Negation, the not operator turns true to false
print(not False)     # True
print(not not True)  # True
print(not not False) # False

