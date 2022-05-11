const express = require('express');
const path = require('path');
const ejs = require('ejs');
const app = express();
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'ejs');
app.get('/', (req, res) => {
    res.render('index');
});
app.use('/assets', express.static(path.join(__dirname, 'assets')));
app.listen(7122);
console.log("server is on now");