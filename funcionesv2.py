print("Mas sobre funciones")
# aqui se escriben las funciones
def suma_ab(a,b):
    s=a+b 
    return s

def resta_ab(a,b):
    r=a-b 
    return r

def multi_ab(a,b):
    m=a*b 
    return m

def division_ab(a,b):
    d=a/b 
    return d
#Llamadas a funciones
print("----calculando suma----")
n1=int(input("Ingresa el primer numero "))
n2=int(input("Ingresa el segundo numero "))
suma=suma_ab(n1,n2)
print(f"La suma de {n1} + {n2} es {suma}")

print("----calculando resta----")
r1=int(input("Ingresa el primer numero "))
r2=int(input("Ingresa el segundo numero "))
resta=resta_ab(r1,r2)
print(f"La resta de {r1} - {r2} es {resta}")

print("----calculando multiplicacion----")
m1=int(input("Ingresa el primer numero "))
m2=int(input("Ingresa el segundo numero "))
multi=multi_ab(m1,m2)
print(f"La multiplicacion de {m1} * {m2} es {multi}")

print("----calculando division----")
d1=int(input("Ingresa el primer numero "))
d2=int(input("Ingresa el segundo numero "))
division=division_ab(d1,d2)
print(f"La division de {d1} / {d2} es {division}")