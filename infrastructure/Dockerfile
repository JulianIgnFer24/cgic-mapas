FROM python:3.12-slim
RUN apt-get update && apt-get install -y binutils libproj-dev gdal-bin && rm -rf /var/lib/apt/lists/*
WORKDIR /app
COPY backend /app
RUN pip install django==5.0 djangorestframework django-rest-framework-gis drf-spectacular psycopg2-binary shapely numpy
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
