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
for _ in range(1,11):
    first_name = fake.first_name()
    last_name = fake.last_name()
    user["userID"].append("user"+str(_))
    user["first_name"].append( first_name )
    user["last_name"].append( last_name )
    user["user_address"].append( fake.address() )
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

# # Use the sqlalchemy engine to connect to the db. 
# engine = create_engine('mysql://root:SQLpass@localhost/mybook', echo=False)

# # Add the pandas dataframe to the database
# df_user_table.to_sql('test', con=engine,index=False)


# sqlacodegen 
# sqlacodegen mysql://root:SQLpass@localhost/sugoifit > generatedModels.py

if __name__ == '__main__':
    # print (user)
    # print (credentials)
    print(FinancialStmt)
    print (FinancialStmtDesc)
    print(Order)
    print(Business)
    print(AccountType)
    print(Account)
    print(Customer)
    print(Invoice)

