import pandas as pd
from faker import Faker
from collections import defaultdict
from sqlalchemy import create_engine
# from numpy import random
from datetime import datetime
import random
# from sqlacodegen import sqlacodegen

# Initialize the faker instance
fake = Faker() 


# DATA FOR USER TABLE
# Declare and assign dictionary to store data 
user = defaultdict(list)


# Populate dictionary 
for _ in range(1,30):
    first_name = fake.first_name()
    last_name = fake.last_name()
    user["userID"].append("u"+str(_))
    user["fname"].append( first_name )
    user["lname"].append( last_name )
    user["user_address"].append( fake.country() )
    # user_table["phone"].append( fake.phone_number_with_country_code())
    

# packaging data into pandas data frame
df_user_table = pd.DataFrame(user)

# DATA FOR CREDENTIALS 

credentials = defaultdict(list)
role_enum = ["employee", "owner", "finmanager"]


for _ in range(1,11): 
    credentials["userid"].append("user"+ str(_))
    roleindex = random.randint(0, 2) 
    credentials["role"].append(role_enum[roleindex])
    credentials["email"].append(fake.email())
    credentials["user_password"].append("password")
    credentials["pass_salt"].append("salt1244#")


df_credentials_table = pd.DataFrame(credentials)


# DATA FOR FINANCIAL STATEMENTS

FinancialStmt = defaultdict(list)


for _ in range(1,4):
    FinancialStmt["stmtID"].append("stmt" + str(_))
    # FinancialStmt["lineID"].append()
    # FinancialStmt["fs_name"].append()
    # FinancialStmt["fStmtDescID"].append()

df_financialstmt_table = pd.DataFrame(FinancialStmt)

# DATA FOR FINANCIAL STATEMENTS DESC

FinancialStmtDesc = defaultdict(list)


for _ in range(1,2):
    FinancialStmtDesc["fStmtDescID"].append("stmt" + str(_))
    FinancialStmtDesc["companyID"].append("bus" + str(_))
    # FinancialStmtDesc["fsLineID"].append()
    # FinancialStmtDesc["fiscalPeriod"].append()
    FinancialStmtDesc["fillingDATE"].append(datetime.today().strftime('%Y-%m-%d'))
    FinancialStmtDesc["fiscalYear"].append(2020)
    start_date = fake.date()
    FinancialStmtDesc["startDATE"].append('2020-01-01')
    # print (str(start_date).split('-')[0])
    FinancialStmtDesc["endDATE"].append('2020-12-31')
   

df_financialstmt_table = pd.DataFrame(FinancialStmtDesc)

#DATA FOR BUSINESS TABLE

Business = defaultdict(list)

for _ in range(1,6):
    Business["busID"].append("business" + str(_))
    Business["busName"].append("Business "+ str(_))
    Business["busemail"].append(fake.email())
    Business["busaddress"].append(fake.address())
    # Business["telephone"].append(fake.phone())

df_business_table = pd.DataFrame(Business)

#DATA FOR AccountType TABLE

AccountType = defaultdict(list)


for _ in range(1,3):
    AccountType["typeID"].append("type" + str(_))
    AccountType["accountCategory"].append("category" + str(_))

df_accounttype_table = pd.DataFrame(AccountType)

#DATA FOR Account TABLE

Account = defaultdict(list)

for _ in range(1,6):
    Account["accountID"].append("acc" + str(_))
    Account["accountName"].append("name" + str(_))
    Account["typeID"].append("type" + str(random.randint(1,3)))

df_account_table = pd.DataFrame(Account)

#DATA FOR Customer TABLE

Customer = defaultdict(list)

for _ in range(1,6):
    Customer["custID"].append("cust" + str(_))
    Customer["fname"].append(fake.first_name())
    Customer["lname"].append(fake.last_name())
    Customer["trn"].append(117111220 + _ )
    Customer["email"].append(fake.email())

df_customer_table = pd.DataFrame(Customer)

#DATA FOR Invoice TABLE

Invoice = defaultdict(list)

for _ in range(1,6):
    Invoice["invoiceID"].append("invoice" + str(_))
    Invoice["custID"].append("cust" + str(random.randint(1,5)))
    Invoice["invoice_DATE"].append(fake.date_this_year())
    Invoice["tax_tot"].append(45.56 + (3 * _ ))

df_invoice_table = pd.DataFrame(Invoice)


#DATA FOR Order TABLE

Order = defaultdict(list)

for _ in range(1,6):
    Order["orderID"].append("order" + str(_))
    Order["order_tot"].append(67.89 + ( 4 * _ ))
    Order["order_DATE"].append(fake.date_this_year())
    Order["custID"].append("cust" + str(random.randint(1,5)))
    Order["invoiceID"].append("invoice" + str(random.randint(1,5)))
    Order["busID"].append("business" + str(random.randint(1,5)))

df_order_table = pd.DataFrame(Order)

#DATA FOR OrderDetails TABLE

OrderDetails = defaultdict(list)

for _ in range(1,6):
    OrderDetails["orderID"].append("order" + str(random.randint(1,5)))
    OrderDetails["detailsID"].append("detail" + str(_))
    OrderDetails["prodID"].append("prod" + str(random.randint(1,5)))
    OrderDetails["serviceID"].append("service" + str(random.randint(1,5)))
    OrderDetails["quantity"].append(random.randint(1,10))
    OrderDetails["order_tot"].append(123.33 + (2 * _ ))

df_orderdetails_table = pd.DataFrame(OrderDetails)


""" 
    Todo: Expense, Purchase, Product, stock, receipt etc
"""
#Data for Expense

Expense = defaultdict(list)

expenseTypes = ["Bills", "Wages", 
"Purchases"]

for _ in range(1,6):
    Expense["expenseID"].append("expense"+ str(_))
    Expense["extype"].append(expenseTypes[random.randint(0,2)])
    Expense["exname"].append("ExpenseName" + str(_))
    Expense["dateIncurred"].append("03-19-2021")
    Expense["expenseAmt"].append(1632.56 * _ )

df_expense_table = pd.DataFrame(Expense)

#Data for Purchase

Purchase = defaultdict(list)

for _ in range(1,6):
    Purchase["purchaseID"].append("Pch" + str(_))
    Purchase["p_date"].append("10-2-2021")
    Purchase["p_item"].append("Item" + str(_))
    Purchase["p_quantity"].append(( _ * 2) + 1)
    Purchase["p_price"].append(2652.33 + (1200 / _ ))
    Purchase["busID"].append("business" + str(random.randint(1,5)))
    Purchase["stmtID"].append("stmt" + str(random.randint(1,5)))

df_purchase_table = pd.DataFrame(Purchase)

#Date for Product

Product = defaultdict(list)

products = ["Shoes", "Slipper", "Dress", "Skirt", "Pants"]

for _ in range(1,6):
    Product["prodID"].append("Prod" + str(_))
    Product["prodName"].append(products[( _ - 1)])
    Product["unit_price"].append(67.36 * 1.5 * _ )
    Product["baseUnit"].append("None")
    Product["limitedTime"].append("05-10-202" + str( _ - 1))
    Product["taxPercent"].append((12.3 * 1.7) / _ )
    Product["prodStatus"].append("In Stock")


df_product_table = pd.DataFrame(Product)

#Data for stock

stock = defaultdict(list)

for _ in range(1,6):
    stock["prodID"].append("Prod" + str(_))
    stock["inStock"].append("Yes")
    stock["lastUpdateTime"].append("02-01-2021 13:23:44")
    stock["quantity"].append(100)
    stock["quantity"].append(25)

df_stock_table = defaultdict(list)

#Data for Receipt

Receipt = defaultdict(list)

for _ in range(1,6):
    Receipt["receiptID"].append("Recp" + str(_))
    Receipt["orderID"].append("order" + str(_))
    Receipt["busID"].append("business" + str(_))
    Receipt["date_issued"].append("23-03-2021")

df_receipt_table = defaultdict(list)

#Data for Service

Service = defaultdict(list)

servicename = ["Painting", "Plumbing", "Transporation", "Catering"]
season = ["Summer", "Winter", "Fall", "Spring"]

for _ in range(1,6):
    Service["serviceID"].append("service" + str(_))
    Service["serv_name"].append(servicename[random.randint(0,2)])
    Service["serv_price"].append((326.56 + 4.3) * _ )
    Service["taxPercent"].append(5.3)
    Service["in_season"].append(season[random.randint(0,3)])

df_service_table = defaultdict(list)



# commercial_income_statement = Financialstmt('CIS1',fs_name='Commercial Income Statement')
# commercial_balance_sheet = Financialstmt('CBS2',fs_name='Commercial Balance Sheet Statement')
# commercial_cash_flow_statement = Financialstmt('CCF3',fs_name='Commercial Cash Flow Statement')

# financial_income_statement = Financialstmt('FIS1',fs_name='Financial Income Statement')
# financial_balance_sheet = Financialstmt('FBS2',fs_name='Financial Balance Sheet Statement')
# financial_cash_flow_statement = Financialstmt('FCF3', fs_name='Financial Cash Flow Statement')

# print('woo')
# db.session.add(commercial_income_statement)
# db.session.add(commercial_balance_sheet)
# db.session.add(commercial_cash_flow_statement)
# db.session.add(financial_income_statement)
# db.session.add(financial_balance_sheet)
# db.session.add(financial_cash_flow_statement)
# db.session.commit()
    
    

# financial_statement_lines = pd.read_csv(r"C:\Users\Masse\Desktop\Files\sugoifit-system\backend\app\financial_statements_lines.csv")
# print (financial_statement_lines)
# financial_statement_lines = financial_statement_lines[['tag', 'name']].drop_duplicates('tag')

# for index, line in financial_statement_lines.iterrows():
#     db.session.add(Financialstmtline(tag=line['tag'], line_name=line['name']))
#     db.session.commit()        

# financial_statement_lines = pd.read_csv(r"C:\Users\Masse\Desktop\Files\sugoifit-system\backend\app\financial_statements_lines.csv")
# statement_types = ['commercial', 'financial']
# statement_codes = ['income_statement', 'balance_sheet_statement', 'cash_flow_statement']

# for statement_type in statement_types:
#     for statement_code in statement_codes:
#         statement_name = (statement_type + ' ' + statement_code.replace('_',' ')).title()
#         statement = db.session.query(Financialstmt) \
#             .filter(Financialstmt.fs_name == statement_name).one()
#         financial_statement_sequence = financial_statement_lines[
#             (financial_statement_lines['statement_type'] == statement_type) & \
#             (financial_statement_lines['statement_code'] == statement_code)]
        
#         for index, row in financial_statement_sequence.iterrows():
#             line = db.session.query(Financialstmtline) \
#                 .filter(Financialstmtline.tag == row['tag']).one()
#             db.session.add(Financialstmtlineseq(sequence=row['sequence'],
#                                                     fsStmtID =statement.stmtID,
#                                                     fsStmtLineID=line.lineID))
#     db.session.commit()


# # Use the sqlalchemy engine to connect to the db. 
# engine = create_engine('mysql://root:SQLpass@localhost/sugoifit', echo=False)

# # Add the pandas dataframe to the database
# df_user_table.to_sql('test', con=engine,index=False)
df_user_table.to_sql('user', con=engine, index=False, if_exists = "append")


# sqlacodegen 
# sqlacodegen mysql://root:SQLpass@localhost/sugoifit > generatedModels.py

result = pd.read_excel('Financial STatement.xls', index_col=0, sheet_name= 'Commercial Income Statement')


if __name__ == '__main__':
    print (user)
    # print (credentials)
    # print(FinancialStmt)
    # print (FinancialStmtDesc)
    # print(Order)
    # print(Business)
    # print(AccountType)
    # print(Account)
    # print(Customer)
    # print(Invoice)

    # print(result)
