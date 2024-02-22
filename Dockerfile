FROM python:3.11.7
COPY . .
RUN pip install -r requirements.py

ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0"]
