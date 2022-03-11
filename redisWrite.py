
def escribir(clave: str, valor: str, r):
    print("Escribiendo en Redis...")
    try:
        r.set(clave,valor)
        print("Escritura exitosa")
    except:
        print("Error de escritura")
