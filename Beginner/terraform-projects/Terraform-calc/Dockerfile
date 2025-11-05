# Use a lightweight Python base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the Python script into the container
COPY main.py /app/

# Install any required dependencies (optional, if needed)
# RUN pip install some_dependency

# Set the command to run the Python script using the Python interpreter
CMD ["python", "main.py"]
