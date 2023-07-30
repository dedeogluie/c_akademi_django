const express = require("express");

const app = express();

require("dotenv").config();
const port = process.env.PORT || 5001;
console.log(process.env.PORT);

const todoRouter = require("./src/routes/todoRouter");

app.use(express.json());

app.use("/api", todoRouter);

app.get("/", (req, res) => {
  res.send("Hoşgeldiniz Node.js'e");
});

app.listen(port, () => {
  console.log(`Server: ${port} portumda çalışıyor`);
});
