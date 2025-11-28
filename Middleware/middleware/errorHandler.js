const fs = require('fs');

const path = require('path');

function errorHandler(err, req, res, next) {
  const file = path.join(__dirname, '..', 'logs', 'error.log');

  const entry = {
        timestamp: new Date().toISOString(),
        requestId: req.id,
        error: err.message,
        stack: err.stack
    }

    fs.appendFileSync(file, JSON.stringify(entry) + '\n');

    console.log(`Error logged: ${req.id} - ${err.message}`);

    res.status(500).json({
        error: 'Internal Server Error',
        requestId: req.id
    });
}

module.exports = errorHandler;