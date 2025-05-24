## Automated Dockerized Python Calculator Deployment with Terraform


1. Prerequisites
- Install Terraform based on your operating system ([Terraform download](https://developer.hashicorp.com/terraform/install)).
- Install Docker ([docker download](https://www.docker.com/products/docker-desktop/)).
- Docker desktop should be running in the background when you are strating this project.
Basic knowledge of Python, Powershell, Docker, and Terraform.

2. Project Structure
Create the following directory structure:

```
terraform-docker-calculator/
├── main.py          # Python calculator application
├── Dockerfile       # Docker image definition
├── terraform/
│   ├── main.tf      # Terraform main configuration
│   ├── variables.tf # Terraform variables
│   ├── outputs.tf   # Outputs file
```
3. Step 1: Create a Basic Python Calculator Application `main.py`

```
def calculator():
    print("Welcome to the Calculator!")
    print("Options: 1-Add 2-Subtract 3-Multiply 4-Divide")
    try:
        choice = int(input("Enter choice: "))
        if choice in [1, 2, 3, 4]:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            if choice == 1:
                print(f"Result: {num1 + num2}")
            elif choice == 2:
                print(f"Result: {num1 - num2}")
            elif choice == 3:
                print(f"Result: {num1 * num2}")
            elif choice == 4:
                if num2 != 0:
                    print(f"Result: {num1 / num2}")
                else:
                    print("Division by zero is not allowed!")
        else:
            print("Invalid choice!")
    except ValueError:
        print("Please enter valid inputs.")

if __name__ == "__main__":
    calculator()
```

Step 2: Create a Dockerfile `Dockerfile`
```
# Use a lightweight Python base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy the application code
COPY main.py /app/

# Define the command to run the app
CMD ["python", "main.py"]
```

Step 3: Build and Test the Docker Image
Build the image:
```docker build -t python-calculator .```

Run the container:
```docker run -it python-calculator```

![Docker build](https://github.com/Pranith1Kumar/Devops_shelf/blob/49a22059c298fa2579e55662deb2b984998c701a/Beginner/terraform-projects/Terraform-calc/Terraform-calc-imgs/docker%20build.png)

Now you have checked the container is runnning successfully using `docker ps`.

Step 4: Configure Terraform for Docker Deployment
Navigate to the terraform/ directory. 
`main.tf`
```
terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0"
    }
  }
}

provider "docker" {}

resource "docker_image" "python_calculator" {
  name = var.image_name
  build {
    context    = var.build_context
    dockerfile = var.dockerfile_path
  }
}

resource "docker_container" "dreamy_stonebraker" {
  image    = docker_image.python_calculator.name
  name     = var.container_name
  must_run = true
  command  = ["tail","-f","python","main.py"]  # Keeps the container running
}
```
`variables.tf`

```
variable "image_name" {
  default = "python-calculator"
}

variable "container_name" {
  default = "python-calculator-app"
}

variable "build_context" {
  default = "../"
}

variable "dockerfile_path" {
  default = "../Dockerfile"
}
```

`outputs.tf`
```
output "container_name" {
  value = docker_container.dreamy_stonebraker.name
}

output "image_name" {
  value = docker_image.python_calculator.name
}
```

Step 5: Initialize and Apply Terraform
Initialize Terraform:
```terraform init```

![tf init](https://github.com/Pranith1Kumar/Devops_shelf/blob/49a22059c298fa2579e55662deb2b984998c701a/Beginner/terraform-projects/Terraform-calc/Terraform-calc-imgs/init.png)

Validate the configuration:
```terraform validate```

![tf validate](https://github.com/Pranith1Kumar/Devops_shelf/blob/49a22059c298fa2579e55662deb2b984998c701a/Beginner/terraform-projects/Terraform-calc/Terraform-calc-imgs/validate.png).

Apply the Terraform configuration:
```terraform apply```

![tf apply](https://github.com/Pranith1Kumar/Devops_shelf/blob/49a22059c298fa2579e55662deb2b984998c701a/Beginner/terraform-projects/Terraform-calc/Terraform-calc-imgs/apply.png).

Step 6: Verify Deployment
List running containers:
```docker ps```
Attach to the container to interact with the calculator:
```docker attach python-calculator-app```

![docker exec](https://github.com/Pranith1Kumar/Devops_shelf/blob/49a22059c298fa2579e55662deb2b984998c701a/Beginner/terraform-projects/Terraform-calc/Terraform-calc-imgs/attach-exec.png).


4. Push to docker hub.
Create a Docker Hub Account
- If you don’t already have a Docker Hub account, follow these steps:
- Go to Docker Hub.
- Click Sign Up and create an account.
- Log in to Docker Hub from the Command Line

Open your terminal.
Log in to Docker Hub using your Docker Hub credentials:
```docker login```

- Tag Your Docker Image
- Before you can push the image to Docker Hub, you need to tag it with your Docker Hub username and a repository name.
- If your image is named todo-app, you will tag it with the format username/repository-name:tag. For example:
```docker tag todo-app <your-dockerhub-username>/todo-app```

![docker tag](https://github.com/Pranith1Kumar/Devops_shelf/blob/49a22059c298fa2579e55662deb2b984998c701a/Beginner/terraform-projects/Terraform-calc/Terraform-calc-imgs/docker%20hub1.png).

Replace <your-dockerhub-username> with your Docker Hub username.

Push the Docker Image to Docker Hub

After tagging the image, push it to your Docker Hub repository:
```docker push <your-dockerhub-username>/todo-app```
Docker will start uploading the image to Docker Hub. It may take some time depending on the image size and your internet speed.

![successfully uploaded to docker hub](https://github.com/Pranith1Kumar/Devops_shelf/blob/49a22059c298fa2579e55662deb2b984998c701a/Beginner/terraform-projects/Terraform-calc/Terraform-calc-imgs/docker%20hub%202.png).

5. Cleanup
- Cleanup
To stop and remove the container and image:

- Destroy Terraform-managed resources:
```terraform destroy```

![tf destroy](https://github.com/Pranith1Kumar/Devops_shelf/blob/e1e8c4e11e04b7ab59c85d2f8097ede0a99d3e87/Beginner/terraform-projects/Terraform-calc/Terraform-calc-imgs/destroy%201.png).

- Verify that resources are cleaned:
```docker ps -a```
![tf check](https://github.com/Pranith1Kumar/Devops_shelf/blob/e1e8c4e11e04b7ab59c85d2f8097ede0a99d3e87/Beginner/terraform-projects/Terraform-calc/Terraform-calc-imgs/destroy%202.png).
