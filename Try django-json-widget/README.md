# `django-json-widget` [Official Doc](django-json-widget)

1. Set up the environment

```sh
docker-compose up --build -d
```

2. Apply migrations:

```sh
docker-compose exec web python manage.py migrate
```

3. Apply fixtures:

```sh
docker-compose exec web python manage.py loaddata inventory/fixtures/items.json inventory/fixtures/products.json
```

4. Create a superuser:

```sh
docker-compose exec web python manage.py createsuperuser
```

5. Access the admin interface by visiting [`http://localhost:8000/admin/`](http://localhost:8000/admin/) in your web browser.
