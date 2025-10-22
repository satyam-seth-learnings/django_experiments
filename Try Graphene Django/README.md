[Official Doc](https://docs.graphene-python.org/projects/django/en/latest/tutorial-plain/)

- Loaddata

```sh
python manage.py loaddata ingredients
```

- Try GraphQL Query

```sh
curl --location --globoff --request POST 'http://127.0.0.1:8000/graphql/' \
--header 'Content-Type: application/json' \
--header 'Cookie: csrftoken=seDqxKUUxKac2H4P3RgNwXGpFaBI4QaT' \
--data-raw '{
  "query": "{ allIngredients { id name } }"
}'
```
