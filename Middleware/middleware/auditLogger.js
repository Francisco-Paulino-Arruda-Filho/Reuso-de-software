const fs = require('fs');
const path = require('path');

const sanitize = require('../utils/sanitize');

function auditLogger(req, res, next) {
  if (req.method !== 'GET') {
    const file = path.join(__dirname, '..', 'logs', 'audit.log');

    const entry = {
      timestamp: new Date().toISOString(),
      requestId: req.id,
      sessionId: req.sessionId,
      ip: req.userIp,
      action: `${req.method} ${sanitize(req.originalUrl)}`,
      payload: sanitize(req.body || {})
    };

    fs.appendFileSync(file, JSON.stringify(entry) + '\n');
  }

  next(); // sempre chamar next()
}

module.exports = auditLogger;
