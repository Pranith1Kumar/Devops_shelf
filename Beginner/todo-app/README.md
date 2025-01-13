**Docker**
# What is Docker?
Docker is a platform for building, delivering, and managing containerized applications. A container is a small, independent, executable software package that contains everything required to run a program (code, libraries, and dependencies). It encapsulates your program and its dependencies, ensuring that it works reliably across many environments (development, testing, and production).
- Containerization: Docker allows you to bundle the To-Do application and its dependencies (such as the Node.js runtime and libraries) into a container.
- Portability: If Docker is installed, the application may operate anywhere (for example, on the local machine or in the cloud).
- Ease of Deployment: You may build and deploy the application container with one easy command.

**Git**
# What is git?
Git is a version control system that developers use to monitor code changes, communicate with others, and manage numerous project versions. It allows you to efficiently manage your project's code, revert to prior versions if needed, and interact with others via platforms such as GitHub.
- Version Control: Keeps track of code modifications.
- Collaboration: You may share the project with others or your future self by submitting it to a GitHub repository.
- Backup: Your code is safely stored in a remote repository (GitHub).
- Commands used: `git init`, `git add`, `git commit`, and `git push`.

**Node.js**
# What is Node.js?
Node.js is a JavaScript runtime based on Chrome's V8 engine. It allows you to execute JavaScript code on the server side (backend). Node.js enables you to develop scalable and efficient server-side applications in JavaScript, a client-side language.
- Backend Development: Node.js runs the Express.js framework, which powers the To-Do app's RESTful API.
- Dependency Management: Node.js ships with npm (Node Package Manager), which is used to install project dependencies such as Express.js.
- Commands used include npm init and npm install.



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
```
mkdir todo-docker-project
cd todo-docker-project
```

![Dir creation](https://github.com/Pranith1Kumar/Devops_self/blob/852597cfcee0939961aea2aea01a9be40ecdfe0d/Beginner/todo-app/directory%20flow.png)

- Initialize a new `Node.js` project
```
npm init -y
```
- Install `Express.js`
```
npm install express
```

3. Write the Application Code
- Create a file index.js in the project folder.
- Add the following code to `index.js`

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
4. Create a `Dockerfile`
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

5. Create a `.dockerignore` File
- In the project folder, create a file .dockerignore.
- Add the following content to avoid unnecessary files in the Docker image:
```
node_modules
npm-debug.log
```

6. Build the Docker Image
- Open the terminal in the project folder.
- Build the image:
```
docker build -t todo-app .
```

![Docker build success](https://github.com/Pranith1Kumar/Devops_self/blob/852597cfcee0939961aea2aea01a9be40ecdfe0d/Beginner/todo-app/Docker%20build.png)

7. Run the Application in Docker
- Start a container:
```
docker run -p 3000:3000 todo-app
```
![run container](https://github.com/Pranith1Kumar/Devops_self/blob/26540cbd77fe662130f257c2f7b48cd7b3efdeae/Beginner/todo-app/docker%20container%20start.png)

- Open a browser:
```
http://localhost:3000/todos
```
→ Fetch all tasks.
You see the empty `[]` now you need to add tasks

8. Push the Code to GitHub
- Initialize a Git repository
```
git init
```
![Intialized git](https://github.com/Pranith1Kumar/Devops_self/blob/852597cfcee0939961aea2aea01a9be40ecdfe0d/Beginner/todo-app/git-init.png)
- Add a .gitignore file and include:
```
node_modules/
```
- Stage and commit the code:
```
git add .
```
```
git commit -m "Initial commit - To-Do List App"
```
![adding git to current dir](https://github.com/Pranith1Kumar/Devops_self/blob/852597cfcee0939961aea2aea01a9be40ecdfe0d/Beginner/todo-app/git-add.png)
- Create a new repository on GitHub and link it to your local repository:
```
git remote add origin <your-github-repo-url>
```
Ex: 
```
git remote add origin https://github.com/Pranith1Kumar/Devops_self
```
```
git branch -M main
```
![Intailized remote to git](https://github.com/Pranith1Kumar/Devops_self/blob/852597cfcee0939961aea2aea01a9be40ecdfe0d/Beginner/todo-app/remote.png)
```
git push -u origin main
```
![Push to git](https://github.com/Pranith1Kumar/Devops_self/blob/852597cfcee0939961aea2aea01a9be40ecdfe0d/Beginner/todo-app/git-push.png)

Successfully addeed to git
![Successfully added to git](https://github.com/Pranith1Kumar/Devops_self/blob/852597cfcee0939961aea2aea01a9be40ecdfe0d/Beginner/todo-app/succ%20to%20github.png)

9. Run the following command in powershell or cmd to add a task to the To-Do list
```
curl -X POST -H "Content-Type: application/json" -d "{\"task\":\"Learn Docker\"}" http://localhost:3000/todos
```

![Task added](https://github.com/Pranith1Kumar/Devops_self/blob/852597cfcee0939961aea2aea01a9be40ecdfe0d/Beginner/todo-app/task%20added%20succ.png)

You will noice a output is updated with task added
```
{
    "todos": ["Learn Docker"]
}
```

or 

![Final Output](https://github.com/Pranith1Kumar/Devops_self/blob/852597cfcee0939961aea2aea01a9be40ecdfe0d/Beginner/todo-app/final%20output.png)

10. Remove all the tasks
- Run the cURL Command Open your terminal and use the following command
```
curl -X DELETE http://localhost:3000/todos
```
View the Response if successful, you will see a response like this
```
{"message": "All tasks deleted!" }
```
![Successfull deletion of all tasks](https://github.com/Pranith1Kumar/Devops_shelf/blob/4aacc729a67becce223ece18fd43d6a1eda60f1a/Beginner/todo-app/delete%20todo.png)

- Verify All Tasks Are Deleted
- You can confirm by fetching the list of tasks with a GET request
```
curl -X GET http://localhost:3000/todo
```
![Verify all tasks are deleted](https://github.com/Pranith1Kumar/Devops_shelf/blob/4aacc729a67becce223ece18fd43d6a1eda60f1a/Beginner/todo-app/verify%20taskes%20are%20deleted.png)

`curl`: The command-line tool for HTTP requests.
`-X DELETE`: Specifies the HTTP method as DELETE.
`http://localhost:3000/todos`: The endpoint to send the DELETE request to.
