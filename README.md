# Sistema de Gestión de Áreas Protegidas de Colombia

Proyecto realizado por: Luis Muñoz
Ingeniería de Sistemas — Segundo corte
Asignatura - Desarrollo de Aplicaciones con Acceso a Datos
Versión actual: Entrega 1 (configuración inicial)

## Objetivo del Proyecto Principal 
Construir una aplicación en Python que consuma datos abiertos de Colombia desde una API pública, los procese y los guarde en una base de datos relacional. Todo esto aplicando el patrón de diseño **MVC**.

## Objetivo del Proyecto
Crear un sistema de gestión que permita consultar, almacenar y trabajar con los datos de las **Áreas Protegidas de Colombia** utilizando Python. Para esta Entrega 1, se añade:

- La configuración básica del entorno.
- La conexión a la API.
- La obtención y visualización de los datos.
- La organización del proyecto bajo la estructura MVC indicadas.

Esta es solo la primera etapa. Más adelante se incorporarán operaciones CRUD y almacenamiento en base de datos.


## Dataset Seleccionado
Se eligió el dataset público llamado **Áreas protegidas de Colombia**, disponible en el portal oficial de datos abiertos del gobierno:

[https://www.datos.gov.co/resource/xpgq-dbtk.json](https://www.datos.gov.co/resource/xpgq-dbtk.json)

Este recurso contiene información sobre áreas naturales protegidas, incluyendo nombre del área, municipio, año de declaratoria, área total en hectáreas, entre otros.


## Estructura del Proyecto
El proyecto se organiza de la siguiente manera, cumpliendo con la indicacion modular requerida:

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
- `models/`: Lógica de los datos.
- `views/`: Encargada de mostrar información.
- `services/`: Donde se encuentra el `APIClient`, encargado de consumir la API.
- `config/`: Configuracion DB
- `database/`: Carpeta donde estará la base de datos SQLite.
- `tests/`: Script de prueba inicial para comprobar conexión con la API.


## Configuración del entorno
Para poder correr el proyecto, se deben instalar las dependencias listadas en el archivo `requirements.txt`.


### Requisitos
- Python 3.8+


### Instalación
pip install -r requirements.txt


##  Prueba inicial del API(test_api.py)
En esta primera entrega se implementó un archivo de prueba llamado `test_api.py`. Al ejecutarlo, se hace una solicitud a la API de datos abiertos y se muestra por consola cuántos registros se obtuvieron y un ejemplo del contenido.


### Resultado esperado
Se obtuvieron 58 registros.
{'no': '50', 'area_protegida': 'RNSC EL MONTE', 'municipio': 'Guasca', 'area_declarada_en_la_jurisdiccion': '0.300', ... }