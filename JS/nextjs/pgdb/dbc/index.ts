/**
 * @warning All rights reserved please contact Sheng Pang for more information. 
 * @description Connect to PG db
 * @note Do you have PG docker running?
 * @author Sheng Pang
 * @status Development
 * @tags database, postgresql, setup
 * @copyright (c) 2024 Sheng Pang
 */

import { Pool } from "pg";
import { env } from "@/.env";

import { logger } from "@/utility/logger/index";
const log = logger(module);

export class pgdb {
    constructor() {}

    async connect() {
        const pool = new Pool({
            host: env.DB_HOST,
            user: env.DB_USER,
            password: env.DB_PASSWORD,
        });
    }
}