const { randomUUID } = require('crypto');

function requestId(req, res, next) {
    req.id = randomUUID()
    req.sessionId = req.headers['x-session-id'] || null;
    req.userIp = req.headers['x-forwarded-for'] || req.socket.remoteAddress;
    req.setHeader('X-Request-Id', req.id);
    req.setHeader('X-Session-Id', req.sessionId);

    next();
}

module.exports = requestId;