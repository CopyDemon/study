const fs = require("fs");
const path = require("path");
const XLSX = require("xlsx");

// const file = path.join(__dirname, "stmt.csv");
const filePath = "/Users/shengpang/Downloads/stmt.csv";

if (!filePath) {
    console.error(`File not found: ${filePath}`);
    process.exit(1);
}

const workbook = XLSX.readFile(filePath);
const sheetName = workbook.SheetNames[0];
const worksheet = workbook.Sheets[sheetName];
const data = XLSX.utils.sheet_to_json(worksheet, { range: 6 });

const discription = [];

// get all discription
data.forEach((item) => {
    const descriptionTitle = item.Description.split(" ")[0];
    if (!discription.includes(descriptionTitle)) {
        discription.push(descriptionTitle);
    }
});

// from description create a map
const dataMap = new Map();
discription.forEach((item) => {
    dataMap.set(item, []);
});

// fill map
data.forEach((item) => {
    const itemTitle = item.Description.split(" ")[0];
    const mapItem = dataMap.get(itemTitle);
    const newItem = {
        Date: item.Date,
        Description: item.Description,
        Amount: item.Amount,
    };
    mapItem.push(newItem);
});

const totalDisplayObj = {};
discription.forEach((item) => {
    totalDisplayObj[item] = dataMap.get(item).reduce((acc, item) => acc + item.Amount, 0);
});

console.log(totalDisplayObj);

const totalSpend = Object.values(totalDisplayObj).reduce((acc, item) => {
    if (!isNaN(item) && item < 0) {
        return acc + Math.abs(item);
    }
    return acc;
}, 0);
console.log(`total spend: ${totalSpend}`);
