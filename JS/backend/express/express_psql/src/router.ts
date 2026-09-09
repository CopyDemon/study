import { Router } from "express";
import db_router from "./db/router";

const router = Router();

router.get("/", (req, res) => {
    res.status(200).json("Sheng's express server handle with psql home page");
});

router.use("/db", db_router);

export default router;