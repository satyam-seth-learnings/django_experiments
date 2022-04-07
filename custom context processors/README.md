[Reference Link](https://docs.djangoproject.com/en/4.0/ref/templates/api/#s-writing-your-own-context-processors)

## Writing your own context processors
A context processor has a simple interface: It’s a Python function that takes one argument, an HttpRequest object, and returns a dictionary that gets added to the template context.

For example, to add the **test_value** to every context:

- app_name/context_processors.py

    ```python

    def demo_context_processor(request):
        return {
            "test_value": "this is demo",
        }
    ```

- Custom context processors can live anywhere in your code base. All Django cares about is that your custom context processors are pointed to by the 'context_processors' option in your TEMPLATES setting — or the context_processors argument of Engine if you’re using it directly.

    ```python
    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                    'app_name.context_processors.demo_context_processor',
                ],
            },
        },
    ]
    ```