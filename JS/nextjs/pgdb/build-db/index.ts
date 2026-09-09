/**
 * @warning All rights reserved please contact Sheng Pang for more information. 
 * @description Build PG db, create table and insert data
 * @note Do you have PG docker running?
 * @author Sheng Pang
 * @status Development
 * @tags database, postgresql, setup
 * @copyright (c) 2024 Sheng
 */

import { pgdb } from "../dbc/index";
console.log(`Start build db`);

const db = new pgdb();