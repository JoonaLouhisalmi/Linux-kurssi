FROM python:3.11-slim

WORKDIR /app

# Kopioi vain requirements
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Kopioi muu sovelluskoodi
COPY . /app/

EXPOSE 5000

CMD ["python", "app.py"]
