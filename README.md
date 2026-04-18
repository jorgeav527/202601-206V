# 202601-206V

1. Convertir count.txt → usuarios.csv
El archivo ahora se llamará usuarios.csv.
Cada fila tendrá:
nombre, edad, casado

El checkbox se maneja así:
 Si está marcado → Flask recibe "on" 
 Si NO está marcado → Flask no recibe el campo
 Por eso usamos:

`casado = "Sí" if "casado" in request.form else "No"`

2. En la función count:
Cuando sea POST:
Tomar nombre, edad y casado del formulario
Guardar una nueva línea en usuarios.csv
Leer todos los usuarios
Contarlos
Renderizar una tabla o simple mente contar todos los usuarios y enviar esa resuesta.
Cuando sea GET:
Mostrar el formulario