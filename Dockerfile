FROM python:3.11-alpine

WORKDIR /app

COPY requirements.txt /app

RUN pip install -r requirements.txt

COPY . /app

ENV PORT=8000

CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0"]

# docker build -t mercado:0.1 . && docker run -dit -v .:/app -p 5000:8000 mercado:0.1