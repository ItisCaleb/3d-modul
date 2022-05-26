const express = require('express');
const path = require('path');
const app = express();
const http = require('http');
const server = http.createServer(app);

const api = require('./api.js')(server);


app.set('trust proxy', true);
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'ejs');

app.get('/', (req, res) => {
    res.render('index');
});
app.use('/assets', express.static(path.join(__dirname, 'assets')));
app.use(api);
const port = 7122
server.listen(port, () => {
    console.log(`server start at port ${port}`);
});
