#1. Concatene la cadena 'Treinta', 'Días', 'De', 'Python' en una sola cadena, 'Treinta días de Python'.
txt_treinta = 'Treinta'
txt_dias = 'dias'
txt_de = 'de'
txt_python = 'python'
print(txt_treinta + ' ' + txt_dias + ' ' + txt_de + ' ' + txt_python )

#2. Concatene la cadena 'Codificación', 'Para', 'Todos' en una sola cadena, 'Codificación para todos'.

txt_codificacion = 'Codificacion'
txt_para = 'Para'
txt_todos = 'Todos'
print(txt_codificacion + ' ' + txt_para + ' ' + txt_todos)

#3 Declare una variable llamada empresa y asígnele un valor inicial "Codificación para todos".
empresa = 'Codificacion para todos'

#4 Imprime la empresa variable usando print() .
print(empresa)

#5 Imprima la longitud de la cadena de caracteres de la empresa utilizando el método len() e print() .
print(len(empresa))

#6 Cambie todos los caracteres a letras mayúsculas usando el método upper() .
print(empresa.upper())

#7 Cambie todos los caracteres a letras minúsculas usando el método lower() .
print(empresa.lower())

#8 Use los métodos capitalize(), title(), swapcase() para formatear el valor de la cadena Coding For All .
print(empresa.capitalize())
print(empresa.title())
print(empresa.swapcase())

#9 Corte (corte) la primera palabra de la cadena Coding For All .
corte = empresa[13::]
print(corte)

