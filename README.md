# examen-final-api

## Parte Teorica

### 1. Para qué se puede usar Python en lo que respecta a datos. Dar 5 casos y explicar brevemente
Python es un lenguaje de programacion muy versatil en el cual se puede utilizar en analisis de datos, desarrollo de aplicaciones web, machine learning, visualizacion de datos y desarrollo de videojuego.
- Analisis de datos:
Python proporiciona una variedad en sus librerias en la cuales nos muestra una coleccion de modulos adicionales para este fin. Sus librerias mas usadas son pandas, numpy, etc. Estas permiten manipular, recopilar, limpiar datos ocultos y analizar datos relevantes.

- Desarrollo de aplicaciones web:
Python en este caso Tiene 2 Frameworks muy poderosos para crear APIS y compartir datos con servidores, procesar informacion, acceder a las BD y mantener la seguridad en los sitios web. Los mas utilizados son Django y Flask. El nuevo framework que esta sorprendiendo y se puede consolidar es el entorno de FastAPI.

- Machine learning:
En este caso python lo representa como un campo de la Inteligenci Artifical en la cual se encarga de usar algoritmos los cuales estos pueden aprender patrones de datos para realizar predicciones. Las predicciones mas comunes en este campo son indicar la pocision de los taxis, estimar riesgo de enfermedades, etc. Sus librerias mas usadas son scikit-learn, PyTorch, TensorFlow y Keras.

- Visualizacion de datos:
Python nos permite representar estos datos manipulados de manera grafica. Sus librerias mas usadas son matplotlib que se utiliza con datos de numpy y seaborn que trabaja con datos de pandas. Con ellas se pueden hacer diferentes tipos de graficos estadisticos ya sea grafico de lineas, barras, histogramas, etc.

- Automatizar Tareas:
Python tambien tiene esa funcion mediante el metodo llamado scripting. Su automatizacion se puede usar para buscar, descargar informacion de internet, llenar y enviar informacion online. Se usan scripts para realizar estas acciones en minutos lo cual aumenta tu eficacia y te ahorra tiempo.

### 2. ¿Cómo se diferencian Flask de Django? Argumentar.
Flask es un framework de python que permite desarrollar aplicaciones web mas sencillas, flexibles y rapido mientras que django trabaja con paginas web mas complejas mediante su patron MVC (Modelo, Vista, Controlador). Su entorno maneja controladores reusables y esta consolidado en las grandes empresas. Con respecto al manejo de APIS, Django las convierte en paginas HTML como puntos finales mientras que Flask esta mas condicionado excepto por su velocidad  que es rapido debido a que es pequeño su estructura.

### 3. ¿Qué es un API? Explicar en sus propias palabras
La API es una interfaz que conecta aplicaciones para que compartan informacion como youtube, whatsapp, etc. Ademas, estas son creadas mediante el HTTP segun quiera utilizar los metodos el programador ya sea crear, actualizar, listar o eliminar.


### 4. ¿Cuál es la principal diferencia entre REST y WebSockets?
La principal diferencia entre REST y WebSockets es que uno no es un protocolo y el otro si lo es. Es decir, REST es una forma para crear API mediante HTTP segun las necesidades de un programador. Tambien puede reutilizar tecnologias ya usadas en la web.
WebSockets produce un canal de comunicacion bidireccional bajo en licencia. Es decir, se utiliza para aplicaciones en tiempo real como los chats, juegos online o transmisiones en vivo.

### 5. Describir un ejemplo de API comercial y como funciona – usar otros ejemplos no vistos
### en el curso.
Un ejemplo de API comercial podria se PayPal. Esta API permite integrar funciones de pago en linea facilitando la compra y envio de dinero.
- Paso 1 - Registro y Autenticacion:
El usuario se debe registrar en la pagina de PayPal y esto permitira crearse una cuenta dentro de esta aplicacion. Estas credenciales autentica la solicitud del usuario a la aplicacion lo cual esta envia a su API.

- Paso 2 - Integrar la aplicacion:
Los programadores usan las librerias de PayPal para facilitar el uso de su API. Esta integracion debe tener botones de pago y procesar pagos directos.

- Paso 3 - Realizacion de un Pago:
Cuando el usuario decida realizar un pago, la aplicacion enviara un metodo POST a la API de PayPal con los detalles solicitados. La API generara un enlace unico en la cual el usuario es redirigido para completar el proceso.

- Paso 4 - Autorizar y Confirmar:
El usuario ingresa sus datos de pago(Estos pueden ser una tarjeta de credito, su cuenta de paypal, etc) y autoriza el pago. 
Despues de completar el pago, PayPal redirige al usuario de vuelta a la aplicacion con un codigo de autorizacion.

- Paso 5 - Finalizar el pago:
La aplicacion usa el codigo de autorizacion para hacer una llamada a la API PayPal, la cual esta confirma el pago. 
La API devuelve un mensaje indicando si el pago fue todo un exito o si hubo algun problema.


### 1. Crear un Entorno Virtual, activar el Entorno Virtual com git-bash, instalar las dependencias del requirements.txt y por último ejecutar la API FastAPI

```bash
virtualenv .venv
source .venv/Scripts/activate
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

### *Para desactivar el entorno virtual* `deactivate`