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
 """


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