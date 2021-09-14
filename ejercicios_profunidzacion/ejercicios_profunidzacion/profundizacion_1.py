# Tipos de variables [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con números
'''
Enunciado:
Realice un calculadora, se ingresará por línea de comando dos
números reales y se deberá calcular todas las operaciones entre ellos:
A) Suma
B) Resta
C) Multiplicación
D) División
E) Exponente/Potencia

- Para todos los casos se debe imprimir en pantalla el resultado aclarando
  la operación realizada en cada caso y con que números
  se ha realizado la operación
  ej: La suma entre 4.2 y 6.5 es 10.7
'''

print('¡Nuestra primera calculadora!')
# Empezar aquí la resolución del ejercicio

print("************")
print("*Caculadora*")
print("************")

primer_numero = int(input("Introduce el primer numero a calcular: "))

segundo_numero = int(input("Introduce el segundo numero a calcular: "))

suma = primer_numero + segundo_numero
print("La suma entre", primer_numero, "y", segundo_numero, "es: ",suma)
resta = primer_numero - segundo_numero
print("La resta entre", primer_numero, "y", segundo_numero, "es: ",resta)
multiplicacion = primer_numero * segundo_numero
print("La multiplicacion entre", primer_numero, "y", segundo_numero, "es: ",multiplicacion)
division = primer_numero / segundo_numero
print("La division entre", primer_numero, "y", segundo_numero, "es: ",division)
exponente = primer_numero ** segundo_numero
print("El exponente de", primer_numero, "a la", segundo_numero, "potencia es: ",exponente)


