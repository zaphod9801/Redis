
def Actualizar(clave: str, valor: str, r):
    print("Actualizando en Redis...")
    try:
        r.set(clave,valor)
        print("Actualizacion exitosa")
    except:
        print("Error de actualizaciòn")
