const express = require('express')
const bodyParser = require('body-parser');
const app = express()
const mysql = require('mysql')
//const spawn = require("child_process").spawn;
app.use(express.static('public'));
app.use(bodyParser.urlencoded({ extended: true }));
app.set('view engine', 'ejs')
//const pythonProcess = spawn('python',["sql_functions.py", 'tortoise', 'tortoise_data.csv']);




var con = mysql.createConnection({
  host: "localhost",
  user: "root",
  password: "",
  database: "galactic"
});

con.connect(function(err) {
  if (err) throw err;
  console.log("Connected to mysql");
});


app.get('/', function (req, res) {
	
	 con.query("SELECT * FROM tortoise", function (err, result, fields) {
    if (err) throw err;
	console.log(result);
	res.render('index',{results: result});
  });
	
	
	
})

app.post('/', function (req, res) {
	var tableName = req.body.dataset;
	con.query("SELECT * FROM "+tableName, function (err, result, fields) {
    if (err) throw err;
	console.log(result);
	res.render('index',{results: result});
  });
})

app.listen(3000, function () {
  console.log('Example app listening on port 3000!')
})

/*
pythonProcess.stdout.on('data', (data) => {
	pythonData += data.toString();
	});
*/