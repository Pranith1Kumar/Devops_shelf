# *Hello Docker*

## Project Explaniation

Lightweight Python/Flask web app containerized with Docker for portable, consistent deployment across environments. Includes app code, dependency definition, Dockerfile creation, image building, and isolated container execution accessible via web browser.

## Terminology
**Docker:** A platform that allows you to package, ship, and run applications in lightweight containers for consistent environments across development and production.

**Dockerfile:** A script file with a set of instructions to build a Docker image for your application.

**Docker Image:** A read-only template created from the Dockerfile that includes everything needed to run the app (code, dependencies, runtime).

**Docker Container:** A running instance of a Docker image that executes the application in an isolated environment.

## Step 1: Install Docker using below link
Install docker: [Click here to Install](https://docs.docker.com/get-docker/)

## Step 2: Create Your App
```bash
mkdir helloapp
cd helloapp
```

![Create a new directory](https://github.com/user-attachments/assets/eaa4673b-6bc1-4590-a9b0-57b1c26bc2b7)

- Create a name called app.py
- Write the pyhton flask code to deploy a Hello App

```python
# app.py
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Docker!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

- Create a  `requirements.txt` file:
```nginx
flask
```

## Step 3: Create a Dockerfile
Create a file named Dockerfile (no extension) in the project folder:


**FROM:** Specifies the base image (e.g., Python) used to build your custom image.

**WORKDIR:** Sets the working directory inside the container where commands will run.

**COPY:** Copies files from your local machine into the Docker image.

**RUN:** Executes commands (e.g., installing dependencies) while building the Docker image.

**CMD:** Defines the default command to run when the container starts.

**EXPOSE:** Informs Docker which port the application will listen to inside the container.

```Dockerfile
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
```

## Step 4: Build the Docker Image

**Docker Image:** A read-only template created from the Dockerfile that includes everything needed to run the app (code, dependencies, runtime).

Run the following in the terminal inside your project folder:

**docker build**: Command to build a Docker image from the Dockerfile.

**docker run:** Command to run a container based on the Docker image.

**-p flag:** Maps a container port to a host port, enabling external access to the app.

```bash
docker build -t helloapp:latest .
```

![Docker build](https://github.com/user-attachments/assets/d1405140-60b2-4284-94b8-681eb45e1816)


- `helloapp` is the name of the image.
- `.` refers to the current directory where Dockerfile is located.

## Step 5: Run the Docker Container

**Docker Container:** A running instance of a Docker image that executes the application in an isolated environment.

Run the app:

```bash
docker run -d -p 5000:5000 helloapp
```

![Run Container](https://github.com/user-attachments/assets/ebdb452b-d9af-4596-818d-fa41c2dc4ee1)

- `-d` runs the container in the background.

- `-p` 5000:5000 maps container port to your host.

- Visit: [http://localhost:5000](http://localhost:5000)
- 
![hello docker](https://github.com/user-attachments/assets/7de1e17a-f3de-430c-8682-3389bc3e498d)

You should see: Hello, Docker!

## Step 6: Check Running Containers

```bash
docker ps
```

![Expose](https://github.com/user-attachments/assets/dd589a9a-5b3d-4932-aa72-9720ca3609c1)

To stop the container:
```bash
docker stop <container_id>
```
![stop container](https://github.com/user-attachments/assets/f1ba5736-39cb-432b-99fa-485b240ed2c5)

Now let's remove the contianer using `rm` command:
```bash
docker rm <conatinerid>
```
To remove image use `docker rmi <image name>`.

To list all running containers  `docker ps`

To list all containers `docker ps -a`.

![remove container](https://github.com/user-attachments/assets/6e6064a0-9ed5-4ab6-9db4-a0bfc96d917d)

