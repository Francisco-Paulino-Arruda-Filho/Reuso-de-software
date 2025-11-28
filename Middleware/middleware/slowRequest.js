const fs = require('fs');
const { url } = require('inspector');

const path = require('path');

const SLOW_THRESHOLD_MS = 800; // 800 milliseconds

function slowRequest(req, res, next) {
    const start = Date.now();
    res.on('finish', () => {
        const duration = Date.now() - start;
        if (duration > SLOW_THRESHOLD_MS) {
            const file = path.join(logDir, 'slow_requests.log');
            const entry = {
                timestamp: new Date().toISOString(),
                requestId: req.id,
                sessionId: req.sessionId,
                url: req.originalUrl,
                method: req.method,
                duration: duration
            }
            fs.appendFileSync(file, JSON.stringify(entry) + '\n');
            console.log(`Slow request logged: ${req.id} - ${req.method} ${req.originalUrl} took ${duration}ms`);
        }
    });

    next();
}

module.exports = slowRequest;