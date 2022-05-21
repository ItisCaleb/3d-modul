const express = require('express');
const path = require('path');
const app = express();
const mysql = require('mysql2')
require('dotenv').config();
const connection = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: process.env.MYSQL_ROOT_PASSWORD,
    database: 'ap'
})
connection.connect((err)=>{
    if(err) console.log(err)
    console.log('sql connect success')
    connection.query(`
        CREATE TABLE IF NOT EXISTS ap
        (ap  VARCHAR(30), stamac VARCHAR(20), srcip VARCHAR(20), time TIMESTAMP);
    `)
    /***
    #insert data
    connection.query(`
    insert into ap (ap, stamac, srcip, time) VALUES (?,?,?,?)`,
     ['cgshtea','6e:9d:dd:16:1a:f1','127.0.0.1',new Date().toISOString().slice(0, 19).replace('T', ' ')]
     ,err=>{
        if(err) console.log(err)
    })

    #find data
    connection.query('select * from ap where stamac=?',['6e:9d:dd:16:1a:f1'],(err,result)=>{
        if(err) console.log(err)
        console.log(result)
    })
    ***/

})

app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'ejs');
app.get('/', (req, res) => {
    res.render('index');
});
app.use('/assets', express.static(path.join(__dirname, 'assets')));
const port = 7122
app.listen(port,()=>{
    console.log(`server start at port ${port}`)
});
