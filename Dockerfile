FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY weather_reviewer.py .

CMD ["python", "weather_reviewer.py"]