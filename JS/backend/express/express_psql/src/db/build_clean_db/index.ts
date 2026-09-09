/**
 * Description: this file is used to build a clean db.
 */
console.log(`building clean db...`);

import fs from "fs";
import path from "path";

import dotenv from "dotenv";

import destroy_db from "./destroy_db";
import create_db from "./create_db";

dotenv.config();

// destroy current browser db.
// destroy_db();
// create new browser db.
// create_db();
console.log("clean db build finished");

