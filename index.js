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
