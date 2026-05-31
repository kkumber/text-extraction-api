FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY . .

RUN chmod +x /app/start.sh

CMD ["/app/start.sh"]