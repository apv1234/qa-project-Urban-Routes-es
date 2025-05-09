Nombre del proyecto:
Proyecto Sprint 8 - Andrea Ponce Vera cohort_27

Descripcion del proyecto:

El objetivo del proyecto es automatizar uno de los happy paths de la aplicacion Urban Routes, la cual consiste en ordenar un taxi con la tarifa comfort de manera satisfactoria, los pasos de la prueba se describiran mas especificos mas adelante.

Descripción de las tecnologías:
Se hizo uso de las librerias pytest (para ejecutar las pruebas) y selenium (como lenguaje de programacion)

Comando de ejecucion:
- Tener instalado Python. Al tiempo de creación del proyecto se utilizó la versión 3.13
- Un entorno base funcional
- Instalar las dependencias, Utilizar el siguiente comando desde la raíz del proyecto: pip install -r requirements
- Instalar pytest: pip install pytest
- En el archivo configuration.py cambiar la variable URL_SERVICE por la URL del servidor actual y activo de Urban Routes
- Ejecutar desde consola, donde "root" es la carpeta base donde se encuentra el proyecto: pytest root/main.py

Instrucciones sobre cómo ejecutar las pruebas y técnicas utilizadas:

Para ejecutar las pruebas se hara uso de dos principales archivos (data.py y main.py);
En data.py se encontraran los datos o las entradas necesarias para ejecutar las pruebas, por ejemplo la URL del servidor de la aplicacion, los datos de la ruta from y to, datos de la tarjeta, numero de telefono y mensaje al conductor, estos datos pueden ser modificados como se requieran.
En el archivo main.py se encuentran las librerias definidas, los localizadores y elementos que se utilizan para ejecutar las pruebas.
Los localizadores y elementos se encuentran agrupados en la clase "UrbanRoutesPage".
Los hooks de entrada y salida (setup_class y teardown_class) asi como los casos de prueba estan agrupados en la clase "TestUrbanRoutes".
Los casos de prueba se encuentran en orden conforme a la ejecucion de las acciones necesarias para ordenar un taxi con la tarifa Confort, los pasos son los siguientes:

1.Agregar ruta from y to - test_set_route
2.Seleccionar la tarifa - test_select_comfort_tariff
3.Ingresar numero de telefono - test_ingresar_num_telef
4.Ingrsar codigo de verificacion - test_ingresar_codigo_SMS
5.Agregar tarjeta y CVV - test_agregar_tarjeta
6.Agregar mensaje al conducto - test_mensaje_conductor
7.Activar switch para pedir manta y panuelos - test_pedir_manta_panuelos
8.Ordenar helados - test_pedir_dos_helados
9.Confirmar orden y reservar taxi - test_reservar_taxi

