# from app import db

# class Accounttype(db.Model):
#     __tablename__ = 'accounttype'

#     typeID = db.Column(db.String(10), primary_key=True)
#     accountCategory = db.Column(db.String(100)) 


# class Busines(db.Model):
#     __tablename__ = 'business'

#     busID = db.Column(db.Integer, primary_key=True, unique=True)
#     busName = db.Column(db.String(100))
#     busemail = db.Column(db.String(255))
#     busaddress = db.Column(db.String(100))
#     telephone = db.Column(db.String(100))


# class Customer(db.Model):
#     __tablename__ = 'customer'

#     custID = db.Column(db.String(10), primary_key=True)
#     fname = db.Column(db.String(100))
#     lname = db.Column(db.String(100))
#     trn = db.Column(db.Integer)
#     email = db.Column(db.String(255))


# class Expense(db.Model):
#     __tablename__ = 'expense'

#     expenseID = db.Column(db.String(10), primary_key=True, unique=True)
#     extype = db.Column(db.String(100))
#     exname = db.Column(db.String(100))
#     DATEIncurred = db.Column(db.Date())
#     expenseAmt = db.Column(db.DECIMAL(10, 2))

# class Financialstmt(db.Model):
#     __tablename__ = 'financialstmt'

#     stmtID = db.Column(db.String(10), primary_key=True, unique=True)
#     fs_name = db.Column(db.String(50))


# class Financialstmtline(db.Model):
#     __tablename__ = 'financialstmtline'

#     lineID = db.Column(db.Integer, primary_key=True, unique=True)
#     line_name = db.Column(db.String(50))
#     lineDesc = db.Column(db.String(50))


# class Product(db.Model):
#     __tablename__ = 'product'

#     prodID = db.Column(db.String(10), primary_key=True)
#     prodName = db.Column(db.String(100))
#     unit_price = db.Column(db.DECIMAL(10, 2))
#     db.ModelUnit = db.Column(db.DECIMAL(10, 2))
#     limitedTime = db.Column(db.DateTime())
#     taxPercent = db.Column(db.DECIMAL(3, 2))
#     prodStatus = db.Column(db.String(25))


# class Stock(Product):
#     __tablename__ = 'stock'

#     prodID = db.Column(db.ForeignKey('product.prodID', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True)
#     inStock = db.Column(db.String(10))
#     lastUpdateTime = db.Column(db.DateTime())
#     quantity = db.Column(db.Integer)
#     threshold = db.Column(db.Integer)


# class Service(db.Model):
#     __tablename__ = 'service'

#     serviceID = db.Column(db.String(11), primary_key=True)
#     serv_name = db.Column(db.String(11))
#     serv_cost = db.Column(db.Integer)
#     taxPercent = db.Column(db.DECIMAL(3, 2))
#     in_season = db.Column(db.String(11))


# class ServiceSaleItem(Service):
#     __tablename__ = 'service_sale_item'

#     ssiID = db.Column(db.ForeignKey('service.serviceID', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True)
#     serv_price = db.Column(db.Integer)
#     taxAmt = db.Column(db.Integer)
#     serviceID = db.Column(db.String(11))
#     userID = db.Column(db.ForeignKey('user.userID', ondelete='CASCADE', onupdate='CASCADE'), index=True)

#     user = db.relationship('User')


# class User(db.Model):
#     __tablename__ = 'user'

#     userID = db.Column(db.String(5), primary_key=True, unique=True)
#     fname = db.Column(db.String(25))
#     lname = db.Column(db.String(25))
#     user_address = db.Column(db.String(50))
#     phone = db.Column(db.String(10))
 

# class Account(db.Model):
#     __tablename__ = 'account'

#     accountID = db.Column(db.String(10), primary_key=True)
#     accountName = db.Column(db.String(100))
#     typeID = db.Column(db.ForeignKey('accounttype.typeID', ondelete='CASCADE', onupdate='CASCADE'), index=True)

#     accounttype = db.relationship('Accounttype')


# class Asset(db.Model):
#     __tablename__ = 'asset'

#     asset_id = db.Column(db.String(10), primary_key=True)
#     a_name = db.Column(db.String(100))
#     lifeSpan = db.Column(db.Integer)
#     a_type = db.Column(db.String(100))
#     acquisDATE = db.Column(db.Date)
#     a_value = db.Column(db.DECIMAL(10, 0))
#     busID = db.Column(db.ForeignKey('business.busID', ondelete='CASCADE', onupdate='CASCADE'), index=True)

#     busines = db.relationship('Busines')


# class ConServiceSaleItem(db.Model):
#     __tablename__ = 'con_service_sale_item'

#     cssiID = db.Column(db.String(11), primary_key=True)
#     quantitySold = db.Column(db.Integer)
#     unit_price = db.Column(db.Integer)
#     serv_price = db.Column(db.Integer)
#     taxAmt = db.Column(db.Integer)
#     serviceID = db.Column(db.ForeignKey('service.serviceID', ondelete='CASCADE', onupdate='CASCADE'), index=True)
#     starttime = db.Column(db.DateTime)
#     endtime = db.Column(db.DateTime)
#     prolong_period = db.Column(db.DateTime)

#     service = db.relationship('Service')


# class Credential(db.Model):
#     __tablename__ = 'credentials'

#     userID = db.Column(db.ForeignKey('user.userID', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, unique=True)
#     role = db.Column(db.String(10))
#     email = db.Column(db.String(50), primary_key=True)
#     user_password = db.Column(db.String(255))
#     pass_salt = db.Column(db.String(50))

#     user = db.relationship('User')


# class Financialstmtdesc(db.Model):
#     __tablename__ = 'financialstmtdesc'

#     fStmtDescID = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
#     companyID = db.Column(db.ForeignKey('business.busID', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True, nullable=False, unique=True)
#     fsLineID = db.Column(db.ForeignKey('financialstmtline.lineID', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True, nullable=False, unique=True)
#     fiscalPeriod = db.Column(db.Date)
#     fillingDATE = db.Column(db.Date)
#     fiscalYear = db.Column(db.Integer)
#     startDATE = db.Column(db.Date)
#     endDATE = db.Column(db.Date)
#     unit = db.Column(db.DECIMAL(10, 2))

#     busines = db.relationship('Busines')
#     financialstmtline = db.relationship('Financialstmtline')


# class Financialstmtlinealia(db.Model):
#     __tablename__ = 'financialstmtlinealias'

#     lineID = db.Column(db.ForeignKey('financialstmtline.lineID', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True, nullable=False, unique=True)
#     fsStmtID = db.Column(db.ForeignKey('financialstmt.stmtID', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)
#     aliasID = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
#     lineAlias = db.Column(db.String(50))

#     financialstmt = db.relationship('Financialstmt')
#     financialstmtline = db.relationship('Financialstmtline')


# class Financialstmtlineseq(db.Model):
#     __tablename__ = 'financialstmtlineseq'

#     lineSeqID = db.Column(db.Integer, primary_key=True, nullable=False)
#     fsStmtID = db.Column(db.ForeignKey('financialstmt.stmtID', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True, nullable=False, index=True)
#     fsStmtLineID = db.Column(db.ForeignKey('financialstmtline.lineID', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True, nullable=False, index=True)
#     sequence = db.Column(db.Integer)

#     financialstmt = db.relationship('Financialstmt')
#     financialstmtline = db.relationship('Financialstmtline')


# class Invoice(db.Model):
#     __tablename__ = 'invoice'

#     invoiceID = db.Column(db.String(10), primary_key=True)
#     custID = db.Column(db.ForeignKey('customer.custID', ondelete='CASCADE', onupdate='CASCADE'), index=True)
#     invoice_DATE = db.Column(db.Date)
#     tax_tot = db.Column(db.DECIMAL(10, 2))

#     customer = db.relationship('Customer')


# class Liability(db.Model):
#     __tablename__ = 'liability'

#     liab_id = db.Column(db.String(5), primary_key=True, unique=True)
#     liab_type = db.Column(db.String(100))
#     liab_name = db.Column(db.String(100))
#     Amt_owed = db.Column(db.DECIMAL(10, 2))
#     borw_DATE = db.Column(db.Date)
#     loan_period = db.Column(db.Integer)
#     busID = db.Column(db.ForeignKey('business.busID', ondelete='CASCADE', onupdate='CASCADE'), index=True)

#     busines = db.relationship('Busines')


# class ProductSaleItem(db.Model):
#     __tablename__ = 'product_sale_item'

#     psiID = db.Column(db.Integer, primary_key=True)
#     customerID = db.Column(db.ForeignKey('customer.custID', ondelete='CASCADE', onupdate='CASCADE'), index=True)
#     timePaid = db.Column(db.DateTime)
#     timeCreated = db.Column(db.DateTime)
#     saleAmt = db.Column(db.DECIMAL(10, 2))
#     saleAmtPaid = db.Column(db.DECIMAL(10, 2))
#     SaleStatus = db.Column(db.String(25))
#     quantitySold = db.Column(db.DECIMAL(10, 2))
#     unit_price = db.Column(db.DECIMAL(10, 2))
#     prodID = db.Column(db.ForeignKey('product.prodID', ondelete='CASCADE', onupdate='CASCADE'), index=True)
#     taxAmt = db.Column(db.DECIMAL(10, 2))

#     customer = db.relationship('Customer')
#     product = db.relationship('Product')


# class Purchase(db.Model):
#     __tablename__ = 'purchase'

#     purchaseID = db.Column(db.String(10), primary_key=True, unique=True)
#     p_DATE = db.Column(db.Date)
#     p_item = db.Column(db.String(100))
#     p_quantity = db.Column(db.Integer)
#     p_price = db.Column(db.DECIMAL(10, 2))
#     busID = db.Column(db.ForeignKey('business.busID'), index=True)
#     stmtID = db.Column(db.ForeignKey('financialstmt.stmtID'), index=True)

#     busines = db.relationship('Busines')
#     financialstmt = db.relationship('Financialstmt')


# class ConService(db.Model):
#     __tablename__ = 'con_service'

#     serviceID = db.Column(db.String(11), primary_key=True)
#     serv_name = db.Column(db.String(11))
#     serv_uprice = db.Column(db.Integer)
#     basic_unit = db.Column(db.DECIMAL(10, 2))
#     d_prolongperiod = db.Column(db.DateTime)
#     taxPercent = db.Column(db.DECIMAL(3, 2))
#     in_season = db.Column(db.String(11))
#     cssiID = db.Column(db.ForeignKey('con_service_sale_item.cssiID', ondelete='CASCADE', onupdate='CASCADE'), index=True)

#     con_service_sale_item = db.relationship('ConServiceSaleItem')


# class Currentasset(db.Model):
#     __tablename__ = 'currentasset'

#     asset_id = db.Column(db.ForeignKey('asset.asset_id', ondelete='CASCADE', onupdate='CASCADE'), index=True)
#     a_name = db.Column(db.String(100))
#     lifeSpan = db.Column(db.Integer)
#     a_type = db.Column(db.String(100))
#     acquisDATE = db.Column(db.Date)
#     a_value = db.Column(db.DECIMAL(10, 2))
#     ca_id = db.Column(db.String(10), primary_key=True)
#     busID = db.Column(db.ForeignKey('business.busID', ondelete='CASCADE', onupdate='CASCADE'), index=True)

#     asset = db.relationship('Asset')
#     busines = db.relationship('Busines')


# class Currentliability(db.Model):
#     __tablename__ = 'currentliability'

#     liab_id = db.Column(db.ForeignKey('liability.liab_id', ondelete='CASCADE', onupdate='CASCADE'), index=True)
#     cliab_id = db.Column(db.String(10), primary_key=True, unique=True)
#     liab_type = db.Column(db.String(100))
#     liab_name = db.Column(db.String(100))
#     Amt_owed = db.Column(db.DECIMAL(10, 2))
#     borw_DATE = db.Column(db.Date)
#     loan_period = db.Column(db.Integer)
#     busID = db.Column(db.ForeignKey('business.busID', ondelete='CASCADE', onupdate='CASCADE'), index=True)

#     busines = db.relationship('Busines')
#     liab = db.relationship('Liability')


# class Longtermliability(db.Model):
#     __tablename__ = 'longtermliability'

#     liab_id = db.Column(db.ForeignKey('liability.liab_id', ondelete='CASCADE', onupdate='CASCADE'), index=True)
#     Itliab_id = db.Column(db.String(10), primary_key=True, unique=True)
#     liab_type = db.Column(db.String(100))
#     liab_name = db.Column(db.String(100))
#     Amt_owed = db.Column(db.DECIMAL(10, 2))
#     borw_DATE = db.Column(db.Date)
#     loan_period = db.Column(db.Integer)
#     busID = db.Column(db.ForeignKey('business.busID', ondelete='CASCADE', onupdate='CASCADE'), index=True)

#     busines = db.relationship('Busines')
#     liab = db.relationship('Liability')


# class Noncurrentasset(db.Model):
#     __tablename__ = 'noncurrentasset'

#     asset_id = db.Column(db.ForeignKey('asset.asset_id', ondelete='CASCADE', onupdate='CASCADE'), index=True)
#     a_name = db.Column(db.String(100))
#     lifeSpan = db.Column(db.Integer)
#     a_type = db.Column(db.String(100))
#     acquisDATE = db.Column(db.Date)
#     a_value = db.Column(db.DECIMAL(10, 2))
#     nca_id = db.Column(db.String(10), primary_key=True)
#     AccumDep = db.Column(db.DECIMAL(10, 2))
#     disposalAmt = db.Column(db.DECIMAL(10, 2))
#     depType = db.Column(db.String(100))
#     busID = db.Column(db.ForeignKey('business.busID', ondelete='CASCADE', onupdate='CASCADE'), index=True)

#     asset = db.relationship('Asset')
#     busines = db.relationship('Busines')


# class Order(db.Model):
#     __tablename__ = 'order'

#     orderID = db.Column(db.String(10), primary_key=True)
#     order_tot = db.Column(db.DECIMAL(10, 2))
#     order_DATE = db.Column(db.Date)
#     custID = db.Column(db.ForeignKey('customer.custID', ondelete='CASCADE', onupdate='CASCADE'), index=True)
#     invoiceID = db.Column(db.ForeignKey('invoice.custID', ondelete='CASCADE', onupdate='CASCADE'), index=True)
#     busID = db.Column(db.ForeignKey('business.busID', ondelete='CASCADE', onupdate='CASCADE'), index=True)
#     status = db.Column(db.String(20))

#     busines = db.relationship('Busines')
#     customer = db.relationship('Customer')
#     invoice = db.relationship('Invoice')


# class Voucher(db.Model):
#     __tablename__ = 'voucher'

#     vouchID = db.Column(db.String(5), primary_key=True, unique=True)
#     accountID = db.Column(db.ForeignKey('account.accountID', ondelete='CASCADE', onupdate='CASCADE'), index=True)
#     vType = db.Column(db.Enum('creditVoucher', 'debitVoucher'))
#     vDATE = db.Column(db.Date)
#     authBy = db.Column(db.ForeignKey('user.userID', ondelete='CASCADE', onupdate='CASCADE'), index=True)
#     prepBy = db.Column(db.ForeignKey('user.userID', ondelete='CASCADE', onupdate='CASCADE'), index=True)

#     account = db.relationship('Account')
#     user = db.relationship('User', primaryjoin='Voucher.authBy == User.userID')
#     user1 = db.relationship('User', primaryjoin='Voucher.prepBy == User.userID')


# class Credit(Voucher):
#     __tablename__ = 'credit'

#     vouchID = db.Column(db.ForeignKey('voucher.vouchID'), primary_key=True)
#     accountID = db.Column(db.ForeignKey('account.accountID'), nullable=False, index=True)
#     sourceNo = db.Column(db.Integer)
#     Amount = db.Column(db.DECIMAL(10, 2))
#     Narration = db.Column(db.String(100))

#     account = db.relationship('Account')


# class Creditvoucher(Voucher):
#     __tablename__ = 'creditvoucher'

#     vouchID = db.Column(db.ForeignKey('voucher.vouchID'), primary_key=True)
#     vDATE = db.Column(db.Date)
#     credit = db.Column(db.DECIMAL(10, 2))
#     authBy = db.Column(db.ForeignKey('user.userID'), index=True)
#     prepBy = db.Column(db.ForeignKey('user.userID'), index=True)

#     user = db.relationship('User', primaryjoin='Creditvoucher.authBy == User.userID')
#     user1 = db.relationship('User', primaryjoin='Creditvoucher.prepBy == User.userID')


# class Debit(Voucher):
#     __tablename__ = 'debit'

#     vouchID = db.Column(db.ForeignKey('voucher.vouchID'), primary_key=True)
#     accountID = db.Column(db.ForeignKey('account.accountID'), nullable=False, index=True)
#     sourceNo = db.Column(db.Integer)
#     Amount = db.Column(db.DECIMAL(10, 2))
#     Narration = db.Column(db.String(100))

#     account = db.relationship('Account')


# class Debitvoucher(Voucher):
#     __tablename__ = 'debitvoucher'

#     vouchID = db.Column(db.ForeignKey('voucher.vouchID'), primary_key=True)
#     vDATE = db.Column(db.Date)
#     debit = db.Column(db.DECIMAL(10, 2))
#     authBy = db.Column(db.String(100))
#     prepBy = db.Column(db.String(100))


# class Voucherdetail(Voucher):
#     __tablename__ = 'voucherdetails'

#     vouchID = db.Column(db.ForeignKey('voucher.vouchID', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True)
#     sourceNo = db.Column(db.Integer)
#     Amount = db.Column(db.DECIMAL(10, 2))
#     Narration = db.Column(db.String(100))


# class Orderdetail(db.Model):
#     __tablename__ = 'orderdetails'

#     orderID = db.Column(db.ForeignKey('order.orderID', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True, nullable=False)
#     detailsID = db.Column(db.String(10), primary_key=True, nullable=False)
#     prodID = db.Column(db.String(10))
#     serviceID = db.Column(db.String(10))
#     quantity = db.Column(db.Integer)
#     order_tot = db.Column(db.DECIMAL(10, 2))

#     order = db.relationship('Order')


# class Receipt(db.Model):
#     __tablename__ = 'receipt'

#     receiptID = db.Column(db.String(10), primary_key=True)
#     orderID = db.Column(db.ForeignKey('order.orderID', ondelete='CASCADE', onupdate='CASCADE'), index=True)
#     busID = db.Column(db.ForeignKey('business.busID', ondelete='CASCADE', onupdate='CASCADE'), index=True)
#     DATE_issued = db.Column(db.Date)

#     busines = db.relationship('Busines')
#     order = db.relationship('Order')


# class Supportdoc(db.Model):
#     __tablename__ = 'supportdoc'

#     vouchID = db.Column(db.ForeignKey('voucher.vouchID', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True, nullable=False)
#     sourceNo = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
#     docName = db.Column(db.String(100))
#     docDATE = db.Column(db.Date)

#     voucher = db.relationship('Voucher')


# class Receiptdetail(db.Model):
#     __tablename__ = 'receiptdetails'

#     receiptID = db.Column(db.ForeignKey('receipt.receiptID', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, unique=True)
#     rdetailsID = db.Column(db.String(10), primary_key=True)
#     orderID = db.Column(db.ForeignKey('order.orderID', ondelete='CASCADE', onupdate='CASCADE'), index=True)
#     prodID = db.Column(db.ForeignKey('product.prodID', ondelete='CASCADE', onupdate='CASCADE'), index=True)
#     serviceID = db.Column(db.ForeignKey('service.serviceID', ondelete='CASCADE', onupdate='CASCADE'), index=True)
#     quantity = db.Column(db.Integer)
#     order_tot = db.Column(db.DECIMAL(10, 2))

#     order = db.relationship('Order')
#     product = db.relationship('Product')
#     receipt = db.relationship('Receipt')
#     service = db.relationship('Service')


# class Sale(db.Model):
#     __tablename__ = 'sale'

#     saleID = db.Column(db.String(11), primary_key=True)
#     customerID = db.Column(db.ForeignKey('customer.custID', ondelete='CASCADE', onupdate='CASCADE'), index=True)
#     timePaid = db.Column(db.DateTime)
#     timeCreated = db.Column(db.DateTime)
#     saleAmt = db.Column(db.Integer)
#     saleAmtPaid = db.Column(db.Integer)
#     SaleStatus = db.Column(db.String(11))
#     receiptID = db.Column(db.ForeignKey('receipt.receiptID', ondelete='CASCADE', onupdate='CASCADE'), index=True)

#     customer = db.relationship('Customer')
#     receipt = db.relationship('Receipt')

    