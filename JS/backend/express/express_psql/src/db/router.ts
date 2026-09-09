import { Router } from "express";
import { pool } from "./db_utility/db_c";

const db_router = Router();

// list of available routers
const router_list = [
    "/db-test"
]   

db_router.get(`/db-test`, async (req, res) => {
    try{
        const result = await pool.query("SELECT * FROM user");
        res.status(200).json(result.rows);
    }catch(error){
        res.status(500).json({error: error});
    }
});

export default db_router;