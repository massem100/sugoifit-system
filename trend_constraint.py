""" 
Trend Analysis 
To aid in forecasting models 
the algorithm should isolate each item apply each technique and then apply
  the most accurate technique that is in line with past performance.
        Sales Growth Factor 
        Vertical/Horizontal Common Size Averages
        Etc. 
 


Ratio Functions
Process in English 
1.	Take as input the variables and the year. 
2.	Compute the ratio, 
3.	Output the result of the calculation and accurate interpretation.

What if the year is not yet finished? Take the sum of the months so far and then evaluate using that sum. 
Or would it be taking the most recent sum? Since that would be the value of current assets for that time…
Psuedocode:
currentRatio (cAsset, cLiabilities, year): 
cal = current asset/ liabilities 
if cal < 1: 
the business is not in  a good position of pay off debts. Seek extreme measures to rectify problems. 	
Else If cal > 1  and cal <1.5: 

This still a low margin, and the business is close to not being able to pay off its short term debts.
Else if cal in the range 1.5 -2 
         Good position to pay off its debts for the foreseeable future. 

"""
# Liquidity Ratios
def currentRatio(currentAsset,cLiabilities): 
    result = {}
    cal = currentAsset/cLiabilities
    if cal in range(0,2): 
        result.append({cal: 'interpretation'})
    return result

def acidTestRatio(currentAsset, inventories, cLiabilities): 
    return (currentAsset-inventories )/ cLiabilities
    
def cashRatio(cashequiv,cLiabilities): 
    result = {}
    cal = cashequiv/cLiabilities
    if cal in range(0,2): 
        result.append({cal: 'interpretation'})
    return result

def opcashFlowRatio(opcashflow ,cLiabilities): 
    result = {}
    cal = opcashflow /cLiabilities
    if cal in range(0,2): 
        result.append({cal: 'interpretation'})
    return result

# Leverage Financial Ratios

def debtRatio(totalLiabilities, totalAssets):
    result = {}
    cal = totalLiabilities/totalAssets
    if cal in range(0,2): 
        result.append({cal: 'interpretation'})
    return result

def debtEquityRatio(totalLiabilities,shareEquity):
    result = {}
    cal = totalLiabilities/ shareEquity
    if cal in range(0,2): 
        result.append({cal: 'interpretation'})
    return result

def interestCoverageRatio(opIncome, interestExpense): 
    result = {}
    cal = opIncome/interestExpense
    if cal in range(0,2): 
        result.append({cal: 'interpretation'})
    return result

# Efficiency Ratios 
def assetTurnoverRatio(netSales, avgTotalAssets):
    result = {}
    cal = netSales/avgTotalAssets
    if cal in range(0,2): 
        result.append({cal: 'interpretation'})
    return result

def inventoryTurnoverRatio(costOfGoodsSold, avgInventory):
    result = {}
    cal = costOfGoodsSold/avgInventory
    if cal in range(0,2): 
        result.append({cal: 'interpretation'})
    return result

def receivablesTurnoverRatio(netCreditSales, avgAccountsReceivable):
    result = {}
    cal = netCreditSales/avgAccountsReceivable
    if cal in range(0,2): 
        result.append({cal: 'interpretation'})
    return result

def daysInventoryRatio(inventoryTurnoverRatio):
    result = {}
    cal = 365/inventoryTurnoverRatio
    if cal in range(0,2): 
        result.append({cal: 'interpretation'})
    return result

"""
Profitability Ratios
Profitability ratios measure a company’s ability to generate income relative to revenue, 
balance sheet assets, operating costs, and equity.

Gross margin ratio = Gross profit / Net sales
Operating margin ratio = Operating income / Net sales
Return on assets ratio = Net income / Total assets
Return on equity ratio = Net income / Shareholder’s equity

Market Value Ratios
Earnings per share ratio = Net earnings / Total shares outstanding
Price-earnings ratio = Share price / Earnings per share



Constraint Analysis
Identify the bottlenecks and how are they hurting performance and profitability. 
suggest possible solutions.

Factors affecting Sale Performance 
Internal Factors: 
•	The product 
•	Marketing 
•	Availability of finance 
•	Technology and automation
•	Availability of suppliers 
External Factors 
•	Economic cycle
•	Consumer’s expectations 
	Laws and regulations 
	Competition.

Factors to use to determine the performance of a product
	Target Audience 
	Can we isolate salaries/ quality of living to determine if the pricing for the product is affecting its demand. 
Production time/ Turnover Rate-how is this affecting product demand 
Track products by units sold over a certain period, identify the one with the least units. 
How much resources does it take to produce that product. 
A product should at least breakeven and not cost the business. Analyze the cost for production versus sales and demand. 



"""