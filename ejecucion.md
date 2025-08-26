# Guía de Ejecución

Esta guía explica cómo poner en marcha el proyecto localmente utilizando Docker.

## Requisitos previos

- [Docker](https://docs.docker.com/get-docker/) 24 o superior
- [docker compose](https://docs.docker.com/compose/) plugin

## Pasos

1. **Clonar el repositorio**
   ```bash
   git clone https://example.com/cgic-mapas.git
   cd cgic-mapas
   ```
2. **Configurar variables de entorno**
   Copiar el archivo de ejemplo y ajustarlo según sea necesario.
   ```bash
   cp infrastructure/.env.example .env
   ```
3. **Construir y levantar los servicios**
   ```bash
   docker compose -f infrastructure/docker-compose.yml up --build
   ```
   Esto ejecutará PostGIS, la aplicación Django y el worker para tareas asíncronas. El entrypoint aplica migraciones y carga datos de ejemplo.
4. **Acceder a la aplicación**
   Abrir un navegador en [http://localhost:8000/map/](http://localhost:8000/map/) para ver el mapa interactivo.
5. **(Opcional) Ejecutar comandos de gestión**
   Para re‑calcular el índice de exposición u otros comandos:
   ```bash
   docker compose -f infrastructure/docker-compose.yml run --rm web python manage.py compute_index
   ```
6. **(Opcional) Ejecutar pruebas**
   ```bash
   docker compose -f infrastructure/docker-compose.yml run --rm web pytest -q
   ```
7. **Detener los servicios**
   ```bash
   docker compose -f infrastructure/docker-compose.yml down
   ```

## Notas
- Todos los datos y tiles utilizados son de fuentes abiertas (OpenStreetMap, etc.).
- El mapa muestra una demo con datos sintéticos incluidos en `data/sample/`.

