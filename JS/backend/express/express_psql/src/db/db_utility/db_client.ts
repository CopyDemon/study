import { Client } from "pg";
import dotenv from "dotenv";

dotenv.config();

export abstract class DB_Client {
    public client: Client;

    constructor() {
        this.client = this.create_client();
        this.connect();
        // doing query
        this.disconnect();
    }

    abstract query(query: string, params: any[]): Promise<any>;

    /**
     * description: create a db client and return it
     * @returns db client
     */
    create_client() {
        const client = new Client({
            user: process.env.DB_USER,
            host: process.env.DB_HOST,
            database: process.env.DB_NAME,
            password: process.env.DB_PASSWORD,
            port: Number(process.env.DB_PORT),
        });

        return client;
    }
    
    /**
     * description: connect to the db
     * @returns void
     */
    async connect() {
        try{
            await this.client.connect();
        }catch(err){
            console.error("Error connecting to the db:", err);
            throw err;
        }
    }

    /**
     * description: disconnect from the db
     * @returns void
     */
    async disconnect() {
        try{
            await this.client.end();
        }catch(err){
            console.error("Error disconnecting from the db:", err);
            throw err;
        }
    }
}

export default DB_Client;