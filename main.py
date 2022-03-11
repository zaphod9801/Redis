from redis import StrictRedis
import sys
from redisDelete import eliminar
from redisRead import leer
from redisUpdate import Actualizar
from redisWrite import escribir


def selector(r):
    print("Interfaz para Redis desde Python")
    while(True):
        print("")
        opcion = input('Seleccione una opciòn por favor: \n 1 Leer \n 2 Escribir \n 3 Actualizar \n 4 Eliminar  \n 5 Salir \n')
        print("")
        validador = 0
        while validador == 0:
            try:
                opcion = int(opcion)
            except:
                print("Opciòn no valida")
                validador = 1
            
            if (opcion < 1 or opcion > 5):
                print("Opciòn no valida")
                validador = 1
            
            if opcion == 1:
                print("Lectura")
                clave = input('clave: ')
                valor = leer(clave, r)
                print("Valor: "+str(valor))
                validador = 1
            
            if opcion == 2:
                print("Escritura")
                clave = input('clave: ')
                valor = input('valor: ')
                escribir(clave,valor, r)
                validador = 1

            if opcion == 3:
                print("Actualizaciòn")
                clave = input('clave: ')
                valor = input('valor: ')
                Actualizar(clave, valor, r)
                validador = 1

            if opcion == 4:
                print("Borrado")
                clave = input('clave: ')
                eliminar(clave, r)
                validador = 1

            if opcion == 5:
                print("Gracias")
                sys.exit()

if __name__ == '__main__':
    hostname=sys.argv[1]
    password=sys.argv[2]

    r = StrictRedis(host=hostname,port=6379,password=password,db=0)

    selector(r)




