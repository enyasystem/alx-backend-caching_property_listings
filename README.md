# alx-backend-caching_property_listings

Django project with Dockerized PostgreSQL and Redis for caching.

Quick start

1. Build and start services with Docker Compose:

```powershell
cd alx-backend-caching_property_listings
docker-compose up -d
```

2. Install Python deps in a virtualenv:

```powershell
pip install -r requirements.txt
```

3. Run migrations (Django will connect to the Postgres container):

```powershell
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver 0.0.0.0:8000
```

Notes
- Database settings in `alx_backend_caching_property_listings/settings.py` read from environment variables and default to the docker-compose service names (`postgres` and `redis`).
- Redis is configured as the cache backend using `django-redis` at `redis://redis:6379/1`.
