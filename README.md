# Sistema de Gestión de Áreas Protegidas de Colombia
Proyecto en proceso de entega por LUIS MUÑOZ estudiante de Ingeniería de Sistemas(4to semestre) en la asignatura de Desarrollo de Aplicaciones con Acceso a Datos el cual su version actual se encuentra realizando la entrega 3


## Objetivo del Proyecto Principal 
Analizar datos de areas protegidas reales que han sido invadidas en colombia por las civilaciones que buscan establecer construciones sin importr la ecologia y el medio ambiente, esto se realiza con el fin de alertar a quienes protegen las areas de posibles construciones urbanas que llevarian a dañar o quitar la flora y fauna en areas naturales mediante el crecimiento de futuras ciudades.  


## Dataset Seleccionado
Se eligió el dataset público llamado Áreas protegidas de Colombia.

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
├── app/
    ├── controllers/datos_controller.py
    ├── models/datos_model.py
    ├── views/view.py
    ├── main.py
├── config/settings.py
├── database/conexion.py
├── test/test_modelo.py
├── requirements.txt
└── README.md


### Descripción de cada carpeta
- `controllers/`: Coordinan vista y modelo
- `models/`: Logica de acceso a datos (DAO)
- `views/`: Interfaz CLI (entrada/salida)
- `main/`: Punto de entrada
- `config/`: Configuración DB y URL del dataset
- `database/`: Conexión a MySQL
- `tests/`: Pruebas unitarias


### Requisitos
- `Python 3.8+`
- `MySQL`
- `requests`
- `unittest`


### Instruccion de instalacion
Crea la base de datos en MySQL:

sql
CREATE DATABASE areas_protegidas;

USE areas_protegidas;

CREATE TABLE areas_protegidas (
    no INT PRIMARY KEY,
    area_protegida VARCHAR(255),
    tipo_area VARCHAR(100),
    ubicacion_latitud_longitud VARCHAR(50),
    invasiones_previas INT,
    año_ultima_invasion YEAR,
    proximidad_urbana VARCHAR(20),
    nivel_alerta VARCHAR(20)
);


### Instalar dependencias:
- pip install -r requirements.txt

- Verifica tu configuración en config/settings.py:

DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'areas_protegidas'
}

API_URL = 'https://raw.githubusercontent.com/luissm4/datos-areas-protegidas/refs/heads/main/areas_protegidas.json'

### Ejecución del Proyecto
Desde la raíz del proyecto:

- python -m app.main

Pruebas Unitarias
- python -m unittest discover tests