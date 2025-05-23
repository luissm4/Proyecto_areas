# Sistema de Gestión de Áreas Protegidas de Colombia

Proyecto realizado por: Luis Muñoz
Ingeniería de Sistemas — tercer corte
Asignatura - Desarrollo de Aplicaciones con Acceso a Datos
Versión actual: Entrega 3 (configuración inicial)

## Objetivo del Proyecto Principal 
Construir una aplicación en Python que consuma datos abiertos de Colombia desde una API pública, los procese y los guarde en una base de datos relacional. Todo esto aplicando el patrón de diseño **MVC**.

## Objetivo de la entrega 2

Implementar una solución funcional que:

- Consuma datos desde el dataset abierto de Áreas Protegidas.
- Guarde estos datos en una base de datos **MySQL**.
- Permita al usuario listar la información almacenada mediante un menú interactivo.
- Use una arquitectura clara, modular y mantenible, aplicando el patrón **Modelo–Vista–Controlador (MVC)**.

Esta es solo la primera etapa. Más adelante se incorporarán operaciones CRUD y almacenamiento en base de datos.


## Dataset Seleccionado
Se eligió el dataset público llamado **Áreas protegidas de Colombia**, disponible en el portal oficial de datos abiertos del gobierno:

[https://www.datos.gov.co/resource/xpgq-dbtk.json](https://www.datos.gov.co/resource/xpgq-dbtk.json)

Este recurso contiene información sobre áreas naturales protegidas

- Nombre del área protegida
- Municipio
- Área declarada en la jurisdicción
- Área total (ha)
- Año de declaratoria
- Información sobre plan de manejo y acuerdos

  
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
- `models/`: defina la estructura de los datos.
- `views/`: Muestra los datos de forma legible para el usuario.
- `services/`: Consume los datos de la API externa.
- `config/`: Contiene configuración de conexión a la base de datos
- `database/`: Implementa la conexión a MySQL.
- `tests/`: Archivo `test_api.py` que actúa como punto de entrada con menú CLI.


## Configuración del entorno


### Requisitos
- Python 3.8+
- MySql


### Instalación
pip install -r requirements.txt


##  Prueba inicial del API(test_api.py)
En esta primera entrega se implementó un archivo de prueba llamado `test_api.py`. Al ejecutarlo, se hace una solicitud a la API de datos abiertos y se muestra por consola cuántos registros se obtuvieron y un ejemplo del contenido.


### Resultado esperado
Se obtuvieron 58 registros.
{'no': '50', 'area_protegida': 'RNSC EL MONTE', 'municipio': 'Guasca', 'area_declarada_en_la_jurisdiccion': '0.300', ... }
