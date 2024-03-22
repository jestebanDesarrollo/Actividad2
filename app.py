#Ingresando variables tipo string, int, float
materia = "Matematicas"
año = int(input("Ingrese su año de nacimiento sin puntos ni comas: "))
nota_final = 4.5
autoevalua = float(input("Inglese la nota del estudiante: "))

#Operaciones matematicas
resta = 2024 - año
suma = nota_final + autoevalua
division = suma / 2
multiplicacion = 5 * 30

#Ahora por ultimo vamos a imprimir el los datos.
        
print("Tu naciste en: ", año, " Asi que tienes ", resta)
print("Nota final de: ", materia)
print("Lo muestro porque toca hacer una multiflicacion: ", multiplicacion)
print("Tu nota del promedio es: " , nota_final , " tu auto evaluacion es: " , autoevalua , " Asi que tu promedio te queda en: ", division)

#aqui voy a hacer la condiciones de  if,else y elif

if division > 5.00:
    print("hiciste trampa")

elif division > 4.00:
    print("Felicidades te esforzaste mucho")

elif division > 3.00:
    print("Pasaste por poco")

else: 
    print("Perdiste")

# Voy a elaborar el blucle con for usando la clase ranger 

for i in range (5):
    print(i)









