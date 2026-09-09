import express from "express"; // express
import cors from "cors"; // CORS
import bodyParser from "body-parser"; //body parser for request body, or express will auto ignore body.
import findFreePort from "./utility/findFreePort.js"; // function to find a free port on this computer.

const app = express(); // Express server
app.use(cors());
app.use(bodyParser.json());

const port = findFreePort(); //port

app.get("/", (req, res)=>{
    res.status(200).send(`app works`)
})

app.listen(port, ()=>{
    console.log(`app is running on port: ${port}`)
})
