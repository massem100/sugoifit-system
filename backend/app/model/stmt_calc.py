from collections import defaultdict
""" 
# Income Statement main items
Revenue
Cost of Good Sold
Gross Profit 
Total Expenses
Operating Expenses 
Non-Operating Expenses 
Other revenue
Taxation
Net Profit

Introduction of capital 
Purchase of asset by cheque
Purchase of an asset and the incurring of a liability 
Sale of an asset on credit 
Sale of an asset immediate payment 
Payment of a liability 
Collection of an asset 

 """

Asset  = defaultdict(list)
Liability = defaultdict(list)
Expense  = defaultdict(list)
Revenue = defaultdict(list)
Equity = defaultdict(list)


for _ in range (1):
   Asset['asset_id'].append('1')
   Asset['a_name'].append('1')
   Asset['lifeSpan'].append('4')
   Asset['a_type'].append('NCA')
   Asset['acquisDate'].append('19/01/2019')
   Asset['debitVal'].append('')
   Asset['creditVal'].append('1000')
   Asset['accBal'].append('1000')
   Asset['busID'].append('78483868')


def generalLedger(Asset, Liability, Revenue, Expense, Equity): 


"""
 name=Form.data.get("transaction_name")
date=Form.data.get("date")
desc=Form.data.get("transanction_desc")
value =Form.data.get("transaction_value")
tag = Form.data.get("transaction_tag)
effect = form.data.get ("transaction_effect")

If tag == noncurrentasset and effect = bought:
   Dep =NonCurrentAsset.depreciation ()
   value = value -Dep
    Asset( name, date, desc , value, tag)

   Add new asset to the db

Add new cash to the db or update some value?

Cash decrease asset increase 
Line items to update: noncurrentasset, cash, depreciation.

Update asset amount in the financial statements.
We then know what operation to take when updating each account. 
     
else if tag == current asset: 

Line items  to update current asset, cash 

Elseif tag ==expense and expense_type =direct:

Line items, operating expense, maybe even the specific heading. Cash

"""

if __name__ == '__main__': 
   print(Asset)
