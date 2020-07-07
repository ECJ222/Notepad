const express = require('express');
const path = require('path');

app = express();

if (process.env.NODE_ENV === 'production'){
	app.use(express.static('dist')); //all the static files are being served

	app.get('*', (req, res) => {
		res.sendFile(path.resolve(__dirname, 'dist', 'index.html')) //sends response data to index.html
	});
}

const port = process.env.PORT || 8080;

app.listen(port);