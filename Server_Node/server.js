//using the express js framework
var express = require("express");
var app = express();

//using the built-in os module
//for providing the system information
var os = require('os');

/*** Write functions here, to be used as Express middleware ***/
function logreq (req, res, next) {
  console.log("New request: " + req.method + req.url);
  next();
}

function sendData (req, res, next) {
  res.writeHead(200, {'Content-Type': 'text/plain; charset=UTF-8'});
  res.end("login_successful\n");
  return;
}

/*** Define routes here ***/
app.use(express.static(__dirname));
app.post("/login", logreq, sendData);
app.post("/logout", logreq, sendData);
app.post("/register", logreq, sendData);
app.post("/SQL", logreq, sendData);

/*** Listen on a port here ***/
app.listen(8080, systemStart(os));

function systemStart() {
  console.log("Server is up");
  console.log("Listening on port 8080...");
  console.log("Hostname: " + os.hostname());
  console.log("OS: " + os.type());
  console.log("OS release: " + os.release());
  console.log("Platform: " + os.platform());
  console.log("Architecture: " + os.arch());
  console.log("CPU:");
  var cpuCount = os.cpus().length;
  for (var i=0; i<cpuCount; i++){
    console.log(JSON.stringify(os.cpus()[i]));
  }
  console.log("Free memory: " + (os.freemem()*1.0/1048576).toFixed(3) + " MB");
  console.log("Total memory: " + (os.totalmem()*1.0/1048576).toFixed(3) + " MB");
  console.log("Network interfaces: " + JSON.stringify(os.networkInterfaces()));
}
