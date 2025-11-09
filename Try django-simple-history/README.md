[Offical Doc Link](https://django-simple-history.readthedocs.io/en/latest/)

# How to run

1. Create a virtual environment:

    ```bash
    python -m venv .venv
    ```

2. Activate the virtual environment:

    ```bash
    source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Apply migrations to set up the database:

    ```bash
    python manage.py migrate
    ```

5. Run the development server:

    ```bash
    python manage.py runserver
    ```

6. Open your web browser and navigate to `http://127.0.0.1:8000/` to see the application running.
