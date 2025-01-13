# Devops_self
This repositry consists of all devops projects from scratch in detail with step by step guide.

## Project Overview
You will create a simple To-Do List API, containerize it using Docker, and push the code to a GitHub repository.


# Steps to Follow
1. Install Prerequisites
Ensure you have the following installed:

- Docker
- Git
- Node.js (latest LTS version)
- A code editor like Visual Studio Code

2. Set Up the Project
- Open a terminal and create a project folder
`mkdir todo-docker-project`
`cd todo-docker-project`
- Initialize a new Node.js project
`npm init -y`
- Install Express.js
`npm install express`

3. Write the Application Code
- Create a file index.js in the project folder.
- Add the following code to index.js

```
const express = require('express');
const app = express();

// Middleware to parse JSON
app.use(express.json());

let todos = [];

// Add a new task
app.post('/todos', (req, res) => {
    const { task } = req.body;
    if (task) {
        todos.push(task);
        res.status(201).json({ message: 'Task added successfully!', todos });
    } else {
        res.status(400).json({ error: 'Task is required!' });
    }
});

// Get all tasks
app.get('/todos', (req, res) => {
    res.json(todos);
});

// Delete all tasks
app.delete('/todos', (req, res) => {
    todos = [];
    res.json({ message: 'All tasks deleted!' });
});

const PORT = 3000;
app.listen(PORT, () => {
    console.log(`Server running at http://localhost:${PORT}`);
});
```
4. Create a Dockerfile
- In the same folder, create a file named Dockerfile.
- Add the following content

```
# Use Node.js base image
FROM node:18

# Set the working directory
WORKDIR /app

# Copy package.json and package-lock.json
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the application code
COPY . .

# Expose the application port
EXPOSE 3000

# Command to run the application
CMD ["node", "index.js"]
```

5. Create a .dockerignore File
- In the project folder, create a file .dockerignore.
- Add the following content to avoid unnecessary files in the Docker image:
`node_modules`
`npm-debug.log`

6. Build the Docker Image
- Open the terminal in the project folder.
- Build the image:
`docker build -t todo-app .`

7. Run the Application in Docker
- Start a container:
`docker run -p 3000:3000 todo-app`

- Open a browser or Postman to test:
`http://localhost:3000/todos` → Fetch all tasks.
You see the empty [] now you need to add tasks

- Run the following command in powershell or cmd to add a task to the To-Do list
`curl -X POST -H "Content-Type: application/json" -d "{\"task\":\"Learn Docker\"}" http://localhost:3000/todos`


You will noice a output is updated with task added
```
{
    "todos": ["Learn Docker"]
}
```
