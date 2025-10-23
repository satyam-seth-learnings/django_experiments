- [Offical Doc](https://django-parler.readthedocs.io/en/stable/)

# How to run the project

- Create virtual environment

    ```sh
    python3 -m venv .venv
    ```

- Activate virtual environment

    ```sh
    source .venv/bin/activate
    ```

- Install dependencies

    ```sh
    pip install -r requirements.txt
    ```

- Apply migrations:

    ```sh
    python3 manage.py migrate
    ```

- Load products fixtures:

    ```sh
    python3 manage.py loaddata products_fixture.json
    ```

- Load translations fixtures:

    ```sh
    python3 manage.py loaddata translations_fixture.json
    ```

- Run the development server:

    ```sh
    python3 manage.py runserver
    ```

- See translations in action by visiting:

    ```sh
    http://127.0.0.1:8000/product/1/?lang=hi
    ```