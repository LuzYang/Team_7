const express = require("express");
const app = express();
const port = process.env.PORT || 3080;
require("dotenv").config();
const cors = require("cors");
const sql = require("mssql");

const config = {
  user: process.env.user,
  password: process.env.password,
  server: process.env.host,
  database: process.env.database,
};

const allowedIPs = process.env.ALLOWED_IPS.split(",");

sql.connect(config, (err) => {
  if (err) {
    console.error("Error connecting to the SQL server:", err);
    return;
  }
  console.log("Connected to the SQL server.");
});

app.use(cors());
app.use(express.json());

app.use((req, res, next) => {
  const clientIP = req.headers["x-forwarded-for"]?.split(",")[0] || req.ip;
  console.log(`[${new Date().toISOString()}] 访问IP: ${clientIP}`);

  if (allowedIPs.includes("*")) {
    next();
  }
});

app.use((req, res, next) => {
  res.setHeader("Access-Control-Allow-Origin", "*");
  next();
});

app.get("/", (req, res) => {
  res.send("Hello, World!");
});

app.get("/users", (req, res) => {
  const request = new sql.Request();
  request.query("SELECT * FROM Users", (err, result) => {
    if (err) {
      console.error("Error executing query:", err);
      res.status(500).send("Server error");
      return;
    }
    res.json(result.recordset);
  });
});

app.get("/get_temp", (req, res) => {
  const request = new sql.Request();
  request.query("SELECT * FROM Temperature", (err, result) => {
    if (err) {
      console.error("Error executing query:", err);
      res.status(500).send("Server error");
      return;
    }
    res.json(result.recordset);
  });
});

app.listen(port, "0.0.0.0", () => {
  console.log(`Server is running at http://0.0.0.0:${port}`);
  console.log(`允许访问的IP列表: ${allowedIPs}`);
});
