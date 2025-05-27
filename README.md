# Sistema de Gestión de Áreas Protegidas de Colombia
Proyecto en proceso por LUIS MUÑOZ estudiante de Ingeniería de Sistemas(4to semestre) en la asignatura de Desarrollo de Aplicaciones con Acceso a Datos el cual su version actual se encuentra realizando la entrega 3


## Objetivo del Proyecto Principal 
Analizar datos de areas protegidas reales que han sido invadidas en colombia por las civilaciones que buscan establecer construciones sin importr la ecologia y el medio ambiente, esto se realiza con el fin de alertar a quienes protegen las areas de posibles construciones urbanas que llevarian a dañar o quitar la flora y fauna en areas naturales mediante el crecimiento de futuras ciudades.  


## Dataset Seleccionado
Se eligió el dataset público llamado **Áreas protegidas de Colombia**, disponible en el portal oficial de datos abiertos del gobierno:

(https://raw.githubusercontent.com/luissm4/datos-areas-protegidas/refs/heads/main/areas_protegidas.json)

Este recurso contiene campos de información:

- Nombre del área protegida.
- Tipo de area, este campo muestra de que area se habla ya sea una reserva, un santuario, un parque, etc.
- Ubicacion, la cual se agrega la coordenada para saber con precision que zona de dicha area puede estar vulnerable los proximos años.
- Invasiones previas, este campo informa cuantas veces invadieron el area de algun tipo de area.
- Año de la ultima invasion.
- Proximidad urbana, este campo segun las veces de invasion y el ultimo año, advierte la probabilidad de acercamiento urbano
- Nivel de alerta, esta opcion indica que tan alto es el riesgo de invasion.

  
## Estructura del Proyecto
El proyecto se organiza de la siguiente manera, cumpliendo con las indicaciones:

proyecto_areas/

├──app/
    ├── controllers/
    │   └── datos_controller.py
    ├── models/
    │   └── datos_model.py
    ├── views/
    │   └── view.py
    ├── services/
        └── api_service.py
├── config/
    └── settings.py
├── database/
│   └── conexion.py
├── test/
    └── test_api.py
├── requirements.txt
└── README.md


### Descripción breve de cada carpeta
- `controllers/`: Coordinan la lógica entre vista y modelo.
- `models/`: define la estructura de los datos.
- `views/`: Muestra los datos de forma legible para el usuario.
- `services/`: Consume los datos de la API externa.
- `config/`: Contiene configuración de conexión a la base de datos.
- `database/`: Implementa la conexión a MySQL.
- `tests/`: este archivo que actúa como punto de entrada con menú CLI.


### Requisitos
- Python 3.8+
- MySql


### Instalación
pip install -r requirements.txt


##  Pruebas realizadas(test_api.py)
Al ejecutarlo, hace el uso correcto de CRUD permitiendo al usuario interactuar para que pueda elegirr una opcion dentro de los campos que se observan en pantalla. 
 
===== Sistema de Áreas Protegidas =====
1. Cargar datos desde la API           <--esta opcion uno hace un llamado a la base de datos abierta y la guarda en MySql.
2. Listar datos                        <--esta opcion permite visualisar en consonsola la lista de los datos.
3. Crear nuevo dato                    <--esta opcion te permite crear un nuevo dato llenando los campos. 
4. Actualizar dato                     <--esta opcion te permite reemplazar el valor de un campo.
5. Eliminar dato                       <--esta opcion te permite eliminar cualquier dato.
6. Salir                               <--salimos
   
================================ ===

Seleccione una opción:                 <--esta opcion es para abrir la opcion que el usuario desee.

================================ ===

NOTA: Respecto a la opcion podra realizar lo que necesita.
