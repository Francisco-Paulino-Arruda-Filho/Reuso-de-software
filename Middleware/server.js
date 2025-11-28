const express = require('express');
const requestId = require('./middleware/requestId');
const auditLogger = require('./middleware/auditLogger');
const slowRequest = require('./middleware/slowRequest');
const errorHandler = require('./middleware/errorHandler');
const logger = require('./middleware/logger');
const fs = require('fs');
const path = require('path');

const app = express();

const logDir = path.join(__dirname, 'logs');

if (!fs.existsSync(logDir)){
    fs.mkdirSync(logDir);
}

app.use(requestId);
app.use(express.json());
app.use(slowRequest);
app.use(logger);
app.use(auditLogger);

// Sample route
app.get('/', (req, res) => {
    res.send('Hello, World!');
});

app.post('/login', (req, res) => {
    res.json({ message: 'Login successful' });
});

app.get('/error', (req, res) => {
    throw new Error('Simulated server error');
});

app.use(errorHandler);

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});