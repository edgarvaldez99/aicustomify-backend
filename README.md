# AICustomify

AICustomify es una solución avanzada que automatiza la atención al cliente a través de chat y teléfono utilizando inteligencia artificial. Este backend es el núcleo del sistema, encargado de gestionar las interacciones entre los usuarios y la inteligencia artificial, asegurando una experiencia de soporte eficiente y personalizada.

## Requisitos

- Python 3.11
- [Poetry](https://python-poetry.org)
- [Docker](https://www.docker.com)

## Instalación

### Clonar el repositorio

```
git clone https://github.com/edgarvaldez99/aicustomify-backend.git
cd aicustomify-backend
```

### Configuración del entorno virtual y dependencias

- Instalar [Poetry](https://python-poetry.org/docs/#installation) y [Docker](https://docs.docker.com/engine/install)

- Instalar dependencias: Una vez dentro del directorio del proyecto, ejecuta:
  ```
  poetry install
  ```
  Esto instalará todas las dependencias necesarias para el proyecto en un entorno virtual administrado por Poetry.

### Crear entorno virtual

```sh
virtualenv --python="/usr/bin/python3.11" .venv
```

o

```dat
py -m venv .venv
```

### Acceder al entorno virtual

```
poetry shell
```

## Ejecutar la aplicación localmente

Puedes ejecutar la aplicación localmente:

```sh
poetry run fastapi dev app/main.py
```

o (con entorno virtual activado)

```sh
fastapi dev app/main.py
```

Esto iniciará un servidor local en http://127.0.0.1:8000.

## Docker

Levantar con Docker

```
docker-compose up --build -d
```

## Estructura del proyecto

```plaintext
aicustomify-backend/
├── aicustomify_backend/
│   ├── main.py          # Archivo principal de FastAPI
│   ├── routers/         # Aquí van las rutas de la API
│   ├── models/          # Definición de modelos de datos
│   ├── repositories/    # Definición de la lógica de acceso a BD
│   ├── schemas/         # Definición de los DTOs del API
│   ├── services/        # Definición de la lógica de negocio
│   └── ...
├── tests/               # Tests del proyecto
├── pyproject.toml       # Archivo de configuración de Poetry
├── docker-compose.yml   # Archivo Docker para manejar servicios
├── docker-entrypoint.sh # Archivo Docker para inicializar la API
├── Dockerfile           # Archivo Docker para crear la imagen
├── poetry.lock          # Archivo de Poetry para las dependencias
├── pyproject.toml       # Archivo de Poetry de configuración
└── README.md            # Este archivo
```

## Pruebas

Puedes ejecutar las pruebas con pytest utilizando Poetry:

```
poetry run pytest
```

## Despliegue

Para desplegar la aplicación, puedes seguir el mismo procedimiento que para Docker, asegurándote de configurar las variables de entorno adecuadas en el servidor de producción.
