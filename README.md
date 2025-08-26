# CGIC Fire Exposure Map

Open source demo web application for fire exposure mapping in Luján de Cuyo, Mendoza (Argentina). It uses Django 5 with GeoDjango, PostGIS and a MapLibre GL JS frontend. The application demonstrates weighting, classification and polygonization of synthetic layers.

## Development

Requirements: Docker & docker compose.

```bash
docker compose -f infrastructure/docker-compose.yml up --build
```

Then browse to <http://localhost:8000/map/>.

### Management commands

```
python manage.py ingest_osm    # stub
python manage.py ingest_local  # stub
python manage.py compute_index # runs analysis with synthetic data
```

### Tests

Run tests with `pytest`:

```
pytest
```

## License

MIT. Uses OpenStreetMap tiles (© OpenStreetMap contributors).
