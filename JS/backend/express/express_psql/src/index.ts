import express from "express";
import dotenv from "dotenv";
import corsMiddleware from "./cors";
import router from "./router";
dotenv.config();

const port = process.env.APP_PORT || 3008;
const app = express();

// CORS
app.use(corsMiddleware);
// Router
app.use("/", router);

// App start
app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});