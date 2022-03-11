
def leer(clave: str, r):
    print("Leyendo en Redis...")
    try:
        value = r.get(clave)
        print("Lectura exitosa")
        return value
    except:
        print("Error de lectura")
        return None
    
  

