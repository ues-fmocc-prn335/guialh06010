
# primero le pedimos al usuario que ingrese las tres notas
x = float(input("ingese la primer nota: "))

y = float(input("ingrese la segunda nota: "))

z = float(input("ingrese la tercer nota: "))

# luego sacamos el promedio mediante la siguiente formula
promedio = (x+y+z)/3

#obtenemos el resultado
print("el resultado es:" +str(promedio))

#luego para la mediana primero sacamos el valor minimo
a = min(x,y,z)
#sacamos el valor maximo
c = max(x,y,z)
#luego sumamos las tres notas y le restamos el minimo y el maximo asi obtndremos el valor central
b = (x+y+z)-a-c

print("la mediana es:" + str(b))