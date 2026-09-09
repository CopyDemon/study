import fs from "fs";
import path from "path";

import { clean_pool } from "../db_utility/db_c";

const create_db_query = fs.readFileSync(path.join(__dirname, "clean_db_query", "create_db.sql"), "utf8");
const create_db = () => {
    clean_pool.query(create_db_query, (err, result) => {
        if(err){
            console.error("Error creating database:", err);
            return;
        }
        console.log("Database created successfully");
    });
}

export default create_db;