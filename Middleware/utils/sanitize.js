const SENSITIVE_FIELDS = ["password", "token", "secret", "authorization"];

function sanitize(data) {
    try {
        const clone = JSON.parse(JSON.stringify(data));
        for (const key of Object.keys(clone)) {
            if (SENSITIVE_FIELDS.includes(key.toLowerCase())) {
                clone[key] = "***REDACTED***";
            }
        }
        return clone;
    } catch {
        return data;
    }
}

module.exports = sanitize;
