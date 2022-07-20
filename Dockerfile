FROM python:3.9.12-alpine3.14

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt
RUN chmod u+s /bin/ping

COPY . .

USER 1101

CMD ["gunicorn", "--bind", "0.0.0.0:8080", "wsgi:app"]
