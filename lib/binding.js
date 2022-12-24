process.env.PREBUILDS_ONLY = true;

const binding = require('node-gyp-build')(__dirname)
module.exports = binding.ffmpeg;
