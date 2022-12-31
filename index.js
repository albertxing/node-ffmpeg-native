const path = require('path');
const { fork } = require('child_process');

module.exports = (args) => (
	new Promise((resolve, reject) => {
		const child = fork(path.resolve(__dirname, 'child.js'), args);
		child.on('exit', (code) => {
			if (code === 0) {
				resolve();
			} else {
				reject(code);
			}
		});
	})
);
