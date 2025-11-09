FROM python:3.9

WORKDIR /app

COPY requirements.txt .

RUN pip install gunicorn==23.0.0

RUN pip install -r requirements.txt --no-cache-dir

COPY . .

CMD ["gunicorn", "--bind", "0.0.0.0:9000", "backend.wsgi"]
