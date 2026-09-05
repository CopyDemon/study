/**
 * @warning All rights reserved please contact Sheng Pang for more information. 
 * @description use to define environment variables. this use NextJS default env.
 * @note Do you have your .env file configured in the root directory?
 * @author Sheng Pang
 * @status Development
 * @tags database, postgresql, setup
 * @copyright (c) 2024 Sheng Pang
 */

// load sequence: 
// from file import {env} from env.ts then use env.VARIABLE_NAME to access the variable
// this env.ts auto load the variable from .env file

// to define env variable, you need to edit .env file

export const env = {
    // db
    PORT: process.env.PORT,
    DB_HOST: process.env.DB_HOST,
    DB_USER: process.env.DB_USER,
    DB_PASSWORD: process.env.DB_PASSWORD,
}