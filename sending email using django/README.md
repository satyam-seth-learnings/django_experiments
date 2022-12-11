[Reference Doc Link](https://docs.djangoproject.com/en/4.1/topics/email/)

To run smtp server for testing purpose if we set `django.core.mail.backends.smtp.EmailBackend` as Email Backend in settings.py
then we can run smtp server using following command

```bash
python -m smtpd -n -c DebuggingServer localhost:1025
```