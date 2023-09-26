# tercera-pre-entrega-silvetti

primero:
-crear Proyecto.
-crear App.
-crear models.
-crear views.
-vincular views a urls.
-crear templates.
-crear un templates padre para vincular con los hijos.
-vincular templates a urls.
-extraer de start bootstrap.
-de la carpeta index, copiar a padre.
-en carpeta padre, colocar los elementos {% load static %}.
-Realizar los bloques para modificar estetica.
-manage.makemigrations
-manage.migrations

segundo:
-Crear un archivo forms
-Segun los models, realizar los forms (forms.Form)
-Hacer los formularios, para colocarlos en los nuevos templates, uno para crear y otro para buscar


La pagina de inicio muestra la botonera en gral: 
Inicio
Jugadores 
Futbol
Basquet
Rugby

Cada boton al ingresar devuelve 3 opciones
Inicio -- Al presionarlo siempre accedera a la pagina principal
Jugadores---(Crear jugador, Buscar Jugador)
Futbol---(Crear jugador de futbol, buscar jugador de futbol)
Basquet---(Crear jugador de basquet, buscar jugador de basquet)
Rugby---(Crear jugador de rugby, buscar jugador de rugby)

Al hacer Click en inicio es estar en la pagina principal
Al hacer click en Crear----nos envia a una pagina con un formulario para Crear (jugadores, futbol, basquet, rugby)---cuando enviamos los datos, nos devuelve a la pagina de inicio.
Al hacer click en Buscar---nos envia a una pagina para buscar los elementos cargados con el botón crear.
En caso de encontrar la busqueda, nos enviara a una nueva pagina donde mostrará los resultados. (resultados.....)
Todas las opciones nos dan los resultados en caso de encontrarlos, en caso de que "no", mostrará el mensaje de que no existe en la base de datos. 
