mensaje="GANASTE UN PREMIO"

convierto_mensaje=mensaje.lower()

print(convierto_mensaje)
if "premio" in mensaje:
    print("Es SPAM")
else:
    print("No es SPAM")
