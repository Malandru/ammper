FROM python:3.11.7
COPY . .
RUN pip install --upgrade pip && pip install -r requirements.txt

ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0"]
