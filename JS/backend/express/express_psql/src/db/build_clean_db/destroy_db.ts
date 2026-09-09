import fs from "fs";
import path from "path";

import { clean_pool } from "../db_utility/db_c";
import { DB_Client } from "../db_utility/db_client";

class Destroy_DB extends DB_Client {
    private queryFilePath: string;
    
    constructor(queryFilePath: string) {
        super();
        this.queryFilePath = queryFilePath;
    }
    
    // abs function override query db
    async query(query: string, params: any[]): Promise<any> {
        return await this.client.query(query, params);
    }

    async run(){
        try{
            const destroy_db = new Destroy_DB(this.queryFilePath);
            await destroy_db.run();
        }catch(err){
            console.error("Error destroying database:", err);
            throw err;
        }
    }
}

/**
 * 这个文件适用于，创建新数据库的第一步：删除现有数据库
 */

// // read destroy_db.sql

// // destroy_db function
// /**
//  * description: 删除现有数据库
//  * @param none
//  * @returns void
//  */
// export const destroy_db = () => {
//     clean_pool.query(destroy_db_query, (err, result) => {
//         if(err){
//             console.error("Error destroying database:", err);
//             return;
//         }
//         console.log("Database destroyed successfully");
//     });
// }

export default Destroy_DB;
