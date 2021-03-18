import pandas as pd
from faker import Faker
from collections import defaultdict
from sqlalchemy import create_engine
# from numpy import random
from datetime import datetime
import random
from sqlacodegen import sqlacodegen
from

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
