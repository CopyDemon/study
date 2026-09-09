import cors from "cors";
import dotenv from "dotenv";
dotenv.config();

const currentEnvironment = process.env.ENVIRONMENT;

let corsMiddleware: any  = undefined;

if(currentEnvironment === "development"){
    corsMiddleware = cors({
        origin: "http://localhost:5173",
        methods: ["GET", "POST", "PUT", "DELETE"],
        allowedHeaders: ["Content-Type", "Authorization"],
      });
}else{
    throw new Error("CORS is not supported in prod environment, please check the file and update the cors options");
}

export default corsMiddleware;