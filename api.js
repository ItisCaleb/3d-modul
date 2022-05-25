const router = require('express').Router();
const mysql = require('mysql2');
const {spawn} = require("child_process");
require('dotenv').config();
const SocketServer = require('ws').WebSocketServer;

module.exports = (server) =>{
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

    const path = spawn('./tools/path');

    const wss = new SocketServer({server});

    wss.on('connection',(ws,req)=>{
        this.ip = req.socket.remoteAddress;
        ws.on('message', data=>{
            path.stdin.write(`${this.ip} 30 86\n`,'utf8')
        })
        path.stdout.on("data", data=>{
            if(data.toString().split(" ")[0] === this.ip){
                ws.send(data.toString())
            }
        })
    })

    router.get("/get_ip",(req, res) => {
        res.send(req.ip)
    })

    return router;
}




