FROM python:3.11.7
VOLUME /tmp
COPY . /tmp

ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0"]
