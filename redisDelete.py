
def eliminar(clave: str, r):
    print("Borrando en Redis...")
    try:
        r.delete(clave)
        print("Borrado exitosa")
    except:
        print("Error de borrado")
