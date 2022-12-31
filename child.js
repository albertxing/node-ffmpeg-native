const ffmpeg = require('./binding');

const args = process.argv.slice(2);
ffmpeg(...args);
