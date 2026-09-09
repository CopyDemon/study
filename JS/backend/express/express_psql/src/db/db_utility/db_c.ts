import { Pool } from "pg";
import dotenv from "dotenv";
dotenv.config();

// clean pool is linked to the postgres db.
// reason: when make clean db we need to switch to another db then we can destroy the current db
const clean_pool = new Pool({
    user: process.env.DB_USER,
    host: process.env.DB_HOST,
    database: "postgres",
    password: process.env.DB_PASSWORD,
    port: Number(process.env.DB_PORT),
});

// pool is the current working db.
const pool = new Pool({
    user: process.env.DB_USER,
    host: process.env.DB_HOST,
    database: process.env.DB,
    password: process.env.DB_PASSWORD,
    port: Number(process.env.DB_PORT),
});


export { clean_pool, pool };