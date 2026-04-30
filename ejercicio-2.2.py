#creando un funcion que nos devuelva los numeros primos
#entre 0 y el argumento que pasemos

#crear una funcion que verifique si un numero es primo
def es_primo(num):
    #v
    for i in range(2,num-1):
        if num%i==0: return False
    return True

def primos_hasta(num):
    primos = []
    for i in range(3,num+1):
         resultado = es_primo(i)
         if resultado == True: primos.append(i)
    return primos

resultado = primos_hasta(99)
print (resultado)