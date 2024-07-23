# How to run

- Create virtual enticement

    ```sh
    python -m venv .venv
    ```

- Activate virtual environment

    ```sh
    source .venv/bin/active
    ```

- Install require dependencies

    ```sh
    pip install -r requirements.txt
    ```

- Run the Django server

    ```sh
    python manage.py runserver 0.0.0.0:8000
    ```

- Prometheus metrics are exposed at `http://<private_ip>:8000/metrics`. "You have to set your private IP hostname in the `prometheus-config.yml` file's targets list. For example, if your private IP is `192.168.1.5`, then your resulting hostname should be `192.168.1.5:8000`. (Note: your Django server is running on port `8000`.)

- Visit the Django app at `http://127.0.0.1:8000/`

- Run the Prometheus server

    ```sh
    docker compose up
    ```

- Visit prometheus at `http://127.0.0.1:9090/`

- Run the Grafana server

    ```sh
    docker run -d -p 3000:3000 --name=grafana grafana/grafana-oss
    ```

- Visit the Grafana at `http://127.0.0.1:3000/`


# Reference Links

- [YouTube Video Link](https://youtu.be/ddZjhv66o_o?si=C_21jIsQ9QHII00X)

- [Prometheus Official Docs](https://prometheus.io/docs)

- [Grafana Official Docs](https://grafana.com/)

- [Prometheus Python Client Official Docs](https://prometheus.github.io/client_python/)

- [Django Grafana Dashboard Example](https://grafana.com/grafana/dashboards/9528-django-prometheus/)

- [GitHub Gist Link](https://gist.github.com/piyushgarg-dev/7c4016b12301552b628bbac21a11e6ab)