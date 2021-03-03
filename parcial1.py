# En una llantera se ha establecido una promoción de las llantas marca
# Ponchadas, dicha promoción consiste en lo siguiente: Si se compran menos
# de cinco llantas el precio es de $300 cada una, de $250 si se compran de
# cinco a 10 y de $200 si se compran más de 10. Obtener la cantidad de dinero
# que una persona tiene que pagar por cada una de las llantas que compra y la
# que tiene que pagar por el total de la compra.

n_llantas = int(input('diga el numero de llantas a comprar: '))

if (n_llantas < 5):
    
    prom_1 = n_llantas * 300
    
    print(f'por usar la promocion 1 cada llanta sale en $300 y el total a pagar es: ${prom_1: ,}')

elif (n_llantas >= 5 and n_llantas < 10):
     
    prom_2 = n_llantas * 250
    
    print(f'por usar la promocion 2 cada llanta sale en $250 y el total a pagar es:  ${prom_2 :,}')

else:
     prom_3 = n_llantas * 200
     print(f'por usar la promocion 3 cada llanta sale en $200 y el total a pagar es:  ${prom_3: ,}')
     
     

# Hacer algoritmo que de el valor final por la compra de televisores. El
# descuento lo hace basado en los dos numeros finales a la cédula, si
# termina en 01 el descuento es del 10% y si termina en 25 el descuento es
# del 20%, si termina en 44 el descuento es 35% y si es 57 el 50%


u_digito = int(input('diga los ultimos 2 digitos de su cedula: '))
v_tele = int(input('diga el valor del tv: $'))
if (u_digito == 0o1):
    
    desc_1 = v_tele * 0.90
    
    print(f'el valor del tv: ${desc_1: ,}')

elif (u_digito == 25):
     
    desc_2 = v_tele * 0.80
    
    print(f'el valor del tv: ${desc_2: ,}')

elif (u_digito == 44):
     
    desc_3 = v_tele * 0.65
    
    print(f'el valor del tv: ${desc_3: ,}')
    
elif (u_digito == 57):
     
    desc_4 = v_tele * 0.50
    
    print(f'el valor del tv: ${desc_4: ,}')

else:
     
     print(f'por sus ultimos digitos no aplica a los descuentos el valor del tv es: {v_tele: ,}')
     

# calcular el valor a pagar por los colchones dependiendo de la cantidad

n_colchones = int(input('diga cuantos colchones desea comprar: '))
v_colchones = int(input('diga el valor del colchon: $'))
if (n_colchones >= 3 and n_colchones < 6):
    
    v_pagar1 = (v_colchones * n_colchones) * 0.80
    
    print(f'el valor total a pagar es: ${v_pagar1: ,}')

elif (n_colchones >= 6 and n_colchones < 8):
    
    v_pagar2 = (v_colchones * n_colchones) * 0.75
    
    print(f'el valor total a pagar es: ${v_pagar2: ,}')

elif (n_colchones >= 8):
    
    v_pagar3 = (v_colchones * n_colchones) * 0.70
    
    print(f'el valor total a pagar es: ${v_pagar3: ,}')
    


else:
    v_pagar4 = v_colchones * n_colchones
    
    print(f'el valor total a pagar es: ${v_pagar4: ,}')
    

# Una universidad desea seleccionar una muestra de estudiantes para
# realizar una encuesta. Si el número de estudiantes es menor que 20 se
# tomará el 50%, si el salón tiene entre 20 y 30 estudiantes se tomará 60%,
# si la cantidad es mayor a 30 tomará 70%. ¿Que cantidad de estudiantes
# serán seleccionados para la encuesta?.    
    
    


n_estudiantes = int(input('diga el numero de estudiantes: '))

if (n_estudiantes < 20):
    
    enc_1 = int(n_estudiantes * 0.5)
    
    print(f'el numero de estudiantes a usar en la encuesta es: {enc_1}')

elif (n_estudiantes >= 20 and n_estudiantes <30):
    
    enc_2 = int(n_estudiantes * 0.6)
    
    print(f'el numero de estudiantes a usar en la encuesta es: {enc_2}')


else:
    enc_3 = int(n_estudiantes * 0.7)
    
    print(f'el numero de estudiantes a usar en la encuesta es: {enc_3}')
     








     