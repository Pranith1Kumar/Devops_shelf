# Use official Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy files to container
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

# Expose port
EXPOSE 5000

# Start the app
CMD ["python", "app.py"]
