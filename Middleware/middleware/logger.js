const fs = require('fs');

const path = require('path');

const sanitize = require('../utils/sanitize');

function rotateLogs(filePath) {
    const maxSize = 5 * 1024 * 1024; // 5MB

    if (fs.existsSync(filePath)) {
        const stats = fs.statSync(filePath);
        if (stats.size >= maxSize) {
            const backupPath = filePath + '.' + Date.now() 
            fs.renameSync(filePath, backupPath);
        }
    }
}

function logger(req, res, next) {
    const start = Date.now();
    const logDir = path.join(__dirname, '..', 'logs');
    const file = path.join(logDir, 'access.log');

    if (!fs.existsSync(logDir)){
        fs.mkdirSync(logDir);
    }

    res.on('finish', () => {
        rotateLogs(file);
        const duration = Date.now() - start;
        const entry = {
            timestamp: new Date().toISOString(),
            requestId: req.id,
            sessionId: req.sessionId,
            ip: req.userIp,
            method: req.method,
            url: sanitize(req.originalUrl),
            status: res.statusCode,
            responseTime: duration,
            params: sanitize(req.params),
            query: sanitize(req.query),
            body: sanitize(req.body || {})
        };
        fs.appendFileSync(file, JSON.stringify(entry) + '\n');

        console.log(`Request logged: ${req.id} - ${req.method} ${req.originalUrl}`);
    });

    next();
}

module.exports = logger;