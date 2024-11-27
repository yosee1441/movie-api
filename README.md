# Movie API

**Movie API** es una aplicación web que permite gestionar tus **películas favoritas** a través de un API RESTful. Puedes realizar operaciones CRUD (Crear, Leer, Actualizar y Eliminar) sobre una base de datos de películas. La API está construida utilizando **FastAPI**, un moderno framework web para la creación de APIs en Python.

Este proyecto permite a los usuarios almacenar, actualizar y eliminar información sobre sus películas favoritas, como el título, la descripción, la fecha de lanzamiento y el género.

## Requisitos

Antes de comenzar, asegúrate de tener instalado lo siguiente:

- **Python 3.7+**
- **pip** (gestor de paquetes de Python)

## Instalación

```bash
pip install -r requirements.txt
```

Sigue estos pasos para configurar y ejecutar el proyecto en tu entorno local.

1. **Clona el repositorio**:

   ```bash
   git clone https://github.com/tu_usuario/movie-api.git
   cd movie-api
   ```
   
## Configuración del entorno

1. **En Windows
   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   ```
   
2. **En macOS/Linux:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

## Ejecutar la aplicación
   ```bash
   uvicorn main:app --reload
   ```
