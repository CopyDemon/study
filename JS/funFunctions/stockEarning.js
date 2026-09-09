console.clear();
console.log(`
    This is a simple script to calculate the earning of stock base on 
        1. initial investment
        2. earning percentage rate
        3. how many times to tread
    Draw back is winning rate is 100%
`);
let treadTimes = 200;
let earningPercentage = 0.02;
let initialInvestment = 100;
let displayStartMoney = initialInvestment;

for (let i = 0; i < treadTimes; i++) {
    let currentEarning = initialInvestment * earningPercentage;
    initialInvestment += currentEarning;
}

console.log(`
    Result:
        Initial investment: ${displayStartMoney}
        Tread times: ${treadTimes}
        Earning percentage for each tread: ${earningPercentage}
        Now the initial investment is: ${initialInvestment}
`);
