import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class CompoundInterestCalculator:
    def __init__(self, price_per_share=0, initial_investment=0, daily_invest_amount=0, apy=0, years=0):
        self.price_per_share = price_per_share
        self.initial_investment = initial_investment
        self.daily_invest_amount = daily_invest_amount
        self.apy = apy
        self.years = years
        
        # total trading days in a year could be 250 or 252, depends on if holiday is land on trading day or not
        self.yearly_total_days_of_investment = 250 # rough estimate, later may replace with total trading days calculator
        logger.info("Total days of investment: %s, this is a rough estimate, later may replace with total trading days calculator", self.yearly_total_days_of_investment) 
        
        if self.years == 0:
            logger.error("Years is 0, please set years to a positive number")
        
    def total_out_of_pocket_investment(self):
        logger.info("calculating total out of pocket investment... ...")
        total_invest_days = self.yearly_total_days_of_investment * self.years
        total_out_of_pocket_investment = self.initial_investment + self.daily_invest_amount * total_invest_days
        logger.info("Total out of pocket investment: %s", total_out_of_pocket_investment)
        return total_out_of_pocket_investment

if __name__ == "__main__":
    # SCHD
    CompoundInterestCalculator(price_per_share=27.01, initial_investment=1000, daily_invest_amount=10, apy=0.038, years=1).total_out_of_pocket_investment()