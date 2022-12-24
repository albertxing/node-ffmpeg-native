process.env.PREBUILDS_ONLY = true;

const path = require('path');
const binding = require('node-gyp-build')(path.resolve(__dirname, '../'));
module.exports = binding.ffmpeg;
