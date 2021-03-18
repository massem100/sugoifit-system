from sqlalchemy import Column, DECIMAL, Date, DateTime, Enum, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata

class Accounttype(Base):
    __tablename__ = 'accounttype'

    typeID = Column(String(10), primary_key=True)
    accountCategory = Column(String(100))


class Busines(Base):
    __tablename__ = 'business'

    busID = Column(Integer, primary_key=True, unique=True)
    busName = Column(String(100))
    busemail = Column(String(255))
    busaddress = Column(String(100))
    telephone = Column(String(100))


class Customer(Base):
    __tablename__ = 'customer'

    custID = Column(String(10), primary_key=True)
    fname = Column(String(100))
    lname = Column(String(100))
    trn = Column(Integer)
    email = Column(String(255))


class Expense(Base):
    __tablename__ = 'expense'

    expenseID = Column(String(10), primary_key=True, unique=True)
    extype = Column(String(100))
    exname = Column(String(100))
    DATEIncurred = Column(Date)
    expenseAmt = Column(DECIMAL(10, 2))
""" 
""" 
class Financialstmt(Base):
    __tablename__ = 'financialstmt'

    stmtID = Column(String(10), primary_key=True, unique=True)
    fs_name = Column(String(50))
 """ """

class Financialstmtline(Base):
    __tablename__ = 'financialstmtline'

    lineID = Column(Integer, primary_key=True, unique=True)
    line_name = Column(String(50))
    lineDesc = Column(String(50))


class Product(Base):
    __tablename__ = 'product'

    prodID = Column(String(10), primary_key=True)
    prodName = Column(String(100))
    unit_price = Column(DECIMAL(10, 2))
    baseUnit = Column(DECIMAL(10, 2))
    limitedTime = Column(DateTime)
    taxPercent = Column(DECIMAL(3, 2))
    prodStatus = Column(String(25))


class Stock(Product):
    __tablename__ = 'stock'

    prodID = Column(ForeignKey('product.prodID', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True)
    inStock = Column(String(10))
    lastUpdateTime = Column(DateTime)
    quantity = Column(Integer)
    threshold = Column(Integer)


class Service(Base):
    __tablename__ = 'service'

    serviceID = Column(String(11), primary_key=True)
    serv_name = Column(String(11))
    serv_price = Column(Integer)
    taxPercent = Column(DECIMAL(3, 2))
    in_season = Column(String(11))


class ServiceSaleItem(Service):
    __tablename__ = 'service_sale_item'

    ssiID = Column(ForeignKey('service.serviceID', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True)
    serv_price = Column(Integer)
    taxAmt = Column(Integer)
    serviceID = Column(String(11))
    userID = Column(ForeignKey('user.userID', ondelete='CASCADE', onupdate='CASCADE'), index=True)

    user = relationship('User')


class User(Base):
    __tablename__ = 'user'

    userID = Column(String(5), primary_key=True, unique=True)
    fname = Column(String(25))
    lname = Column(String(25))
    user_address = Column(String(50))
    phone = Column(String(10))
 

class Account(Base):
    __tablename__ = 'account'

    accountID = Column(String(10), primary_key=True)
    accountName = Column(String(100))
    typeID = Column(ForeignKey('accounttype.typeID', ondelete='CASCADE', onupdate='CASCADE'), index=True)

    accounttype = relationship('Accounttype')


class Asset(Base):
    __tablename__ = 'asset'

    asset_id = Column(String(10), primary_key=True)
    a_name = Column(String(100))
    lifeSpan = Column(Integer)
    a_type = Column(String(100))
    acquisDATE = Column(Date)
    a_value = Column(DECIMAL(10, 0))
    busID = Column(ForeignKey('business.busID', ondelete='CASCADE', onupdate='CASCADE'), index=True)

    busines = relationship('Busines')


class ConServiceSaleItem(Base):
    __tablename__ = 'con_service_sale_item'

    cssiID = Column(String(11), primary_key=True)
    quantitySold = Column(Integer)
    unit_price = Column(Integer)
    serv_price = Column(Integer)
    taxAmt = Column(Integer)
    serviceID = Column(ForeignKey('service.serviceID', ondelete='CASCADE', onupdate='CASCADE'), index=True)
    starttime = Column(DateTime)
    endtime = Column(DateTime)
    prolong_period = Column(DateTime)

    service = relationship('Service')


class Credential(Base):
    __tablename__ = 'credentials'

    userID = Column(ForeignKey('user.userID', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, unique=True)
    role = Column(String(10))
    email = Column(String(50), primary_key=True)
    user_password = Column(String(255))
    pass_salt = Column(String(50))

    user = relationship('User')


class Financialstmtdesc(Base):
    __tablename__ = 'financialstmtdesc'

    fStmtDescID = Column(Integer, primary_key=True, nullable=False, unique=True)
    companyID = Column(ForeignKey('business.busID', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True, nullable=False, unique=True)
    fsLineID = Column(ForeignKey('financialstmtline.lineID', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True, nullable=False, unique=True)
    fiscalPeriod = Column(Date)
    fillingDATE = Column(Date)
    fiscalYear = Column(Integer)
    startDATE = Column(Date)
    endDATE = Column(Date)
    unit = Column(DECIMAL(10, 2))

    busines = relationship('Busines')
    financialstmtline = relationship('Financialstmtline')


class Financialstmtlinealia(Base):
    __tablename__ = 'financialstmtlinealias'

    lineID = Column(ForeignKey('financialstmtline.lineID', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True, nullable=False, unique=True)
    fsStmtID = Column(ForeignKey('financialstmt.stmtID', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)
    aliasID = Column(Integer, primary_key=True, nullable=False, unique=True)
    lineAlias = Column(String(50))

    financialstmt = relationship('Financialstmt')
    financialstmtline = relationship('Financialstmtline')


class Financialstmtlineseq(Base):
    __tablename__ = 'financialstmtlineseq'

    lineSeqID = Column(Integer, primary_key=True, nullable=False)
    fsStmtID = Column(ForeignKey('financialstmt.stmtID', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True, nullable=False, index=True)
    fsStmtLineID = Column(ForeignKey('financialstmtline.lineID', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True, nullable=False, index=True)
    sequence = Column(Integer)

    financialstmt = relationship('Financialstmt')
    financialstmtline = relationship('Financialstmtline')


class Invoice(Base):
    __tablename__ = 'invoice'

    invoiceID = Column(String(10), primary_key=True)
    custID = Column(ForeignKey('customer.custID', ondelete='CASCADE', onupdate='CASCADE'), index=True)
    invoice_DATE = Column(Date)
    tax_tot = Column(DECIMAL(10, 2))

    customer = relationship('Customer')


class Liability(Base):
    __tablename__ = 'liability'

    liab_id = Column(String(5), primary_key=True, unique=True)
    liab_type = Column(String(100))
    liab_name = Column(String(100))
    Amt_owed = Column(DECIMAL(10, 2))
    borw_DATE = Column(Date)
    loan_period = Column(Integer)
    busID = Column(ForeignKey('business.busID', ondelete='CASCADE', onupdate='CASCADE'), index=True)

    busines = relationship('Busines')


class ProductSaleItem(Base):
    __tablename__ = 'product_sale_item'

    psiID = Column(Integer, primary_key=True)
    customerID = Column(ForeignKey('customer.custID', ondelete='CASCADE', onupdate='CASCADE'), index=True)
    timePaid = Column(DateTime)
    timeCreated = Column(DateTime)
    saleAmt = Column(DECIMAL(10, 2))
    saleAmtPaid = Column(DECIMAL(10, 2))
    SaleStatus = Column(String(25))
    quantitySold = Column(DECIMAL(10, 2))
    unit_price = Column(DECIMAL(10, 2))
    prodID = Column(ForeignKey('product.prodID', ondelete='CASCADE', onupdate='CASCADE'), index=True)
    taxAmt = Column(DECIMAL(10, 2))

    customer = relationship('Customer')
    product = relationship('Product')


class Purchase(Base):
    __tablename__ = 'purchase'

    purchaseID = Column(String(10), primary_key=True, unique=True)
    p_DATE = Column(Date)
    p_item = Column(String(100))
    p_quantity = Column(Integer)
    p_price = Column(DECIMAL(10, 2))
    busID = Column(ForeignKey('business.busID'), index=True)
    stmtID = Column(ForeignKey('financialstmt.stmtID'), index=True)

    busines = relationship('Busines')
    financialstmt = relationship('Financialstmt')


class ConService(Base):
    __tablename__ = 'con_service'

    serviceID = Column(String(11), primary_key=True)
    serv_name = Column(String(11))
    serv_uprice = Column(Integer)
    basic_unit = Column(DECIMAL(10, 2))
    d_prolongperiod = Column(DateTime)
    taxPercent = Column(DECIMAL(3, 2))
    in_season = Column(String(11))
    cssiID = Column(ForeignKey('con_service_sale_item.cssiID', ondelete='CASCADE', onupdate='CASCADE'), index=True)

    con_service_sale_item = relationship('ConServiceSaleItem')


class Currentasset(Base):
    __tablename__ = 'currentasset'

    asset_id = Column(ForeignKey('asset.asset_id', ondelete='CASCADE', onupdate='CASCADE'), index=True)
    a_name = Column(String(100))
    lifeSpan = Column(Integer)
    a_type = Column(String(100))
    acquisDATE = Column(Date)
    a_value = Column(DECIMAL(10, 2))
    ca_id = Column(String(10), primary_key=True)
    busID = Column(ForeignKey('business.busID', ondelete='CASCADE', onupdate='CASCADE'), index=True)

    asset = relationship('Asset')
    busines = relationship('Busines')


class Currentliability(Base):
    __tablename__ = 'currentliability'

    liab_id = Column(ForeignKey('liability.liab_id', ondelete='CASCADE', onupdate='CASCADE'), index=True)
    cliab_id = Column(String(10), primary_key=True, unique=True)
    liab_type = Column(String(100))
    liab_name = Column(String(100))
    Amt_owed = Column(DECIMAL(10, 2))
    borw_DATE = Column(Date)
    loan_period = Column(Integer)
    busID = Column(ForeignKey('business.busID', ondelete='CASCADE', onupdate='CASCADE'), index=True)

    busines = relationship('Busines')
    liab = relationship('Liability')


class Longtermliability(Base):
    __tablename__ = 'longtermliability'

    liab_id = Column(ForeignKey('liability.liab_id', ondelete='CASCADE', onupdate='CASCADE'), index=True)
    Itliab_id = Column(String(10), primary_key=True, unique=True)
    liab_type = Column(String(100))
    liab_name = Column(String(100))
    Amt_owed = Column(DECIMAL(10, 2))
    borw_DATE = Column(Date)
    loan_period = Column(Integer)
    busID = Column(ForeignKey('business.busID', ondelete='CASCADE', onupdate='CASCADE'), index=True)

    busines = relationship('Busines')
    liab = relationship('Liability')


class Noncurrentasset(Base):
    __tablename__ = 'noncurrentasset'

    asset_id = Column(ForeignKey('asset.asset_id', ondelete='CASCADE', onupdate='CASCADE'), index=True)
    a_name = Column(String(100))
    lifeSpan = Column(Integer)
    a_type = Column(String(100))
    acquisDATE = Column(Date)
    a_value = Column(DECIMAL(10, 2))
    nca_id = Column(String(10), primary_key=True)
    AccumDep = Column(DECIMAL(10, 2))
    disposalAmt = Column(DECIMAL(10, 2))
    depType = Column(String(100))
    busID = Column(ForeignKey('business.busID', ondelete='CASCADE', onupdate='CASCADE'), index=True)

    asset = relationship('Asset')
    busines = relationship('Busines')


class Order(Base):
    __tablename__ = 'order'

    orderID = Column(String(10), primary_key=True)
    order_tot = Column(DECIMAL(10, 2))
    order_DATE = Column(Date)
    custID = Column(ForeignKey('customer.custID', ondelete='CASCADE', onupdate='CASCADE'), index=True)
    invoiceID = Column(ForeignKey('invoice.custID', ondelete='CASCADE', onupdate='CASCADE'), index=True)
    busID = Column(ForeignKey('business.busID', ondelete='CASCADE', onupdate='CASCADE'), index=True)
    status = Column(String(20))

    busines = relationship('Busines')
    customer = relationship('Customer')
    invoice = relationship('Invoice')


class Voucher(Base):
    __tablename__ = 'voucher'

    vouchID = Column(String(5), primary_key=True, unique=True)
    accountID = Column(ForeignKey('account.accountID', ondelete='CASCADE', onupdate='CASCADE'), index=True)
    vType = Column(Enum('creditVoucher', 'debitVoucher'))
    vDATE = Column(Date)
    authBy = Column(ForeignKey('user.userID', ondelete='CASCADE', onupdate='CASCADE'), index=True)
    prepBy = Column(ForeignKey('user.userID', ondelete='CASCADE', onupdate='CASCADE'), index=True)

    account = relationship('Account')
    user = relationship('User', primaryjoin='Voucher.authBy == User.userID')
    user1 = relationship('User', primaryjoin='Voucher.prepBy == User.userID')


class Credit(Voucher):
    __tablename__ = 'credit'

    vouchID = Column(ForeignKey('voucher.vouchID'), primary_key=True)
    accountID = Column(ForeignKey('account.accountID'), nullable=False, index=True)
    sourceNo = Column(Integer)
    Amount = Column(DECIMAL(10, 2))
    Narration = Column(String(100))

    account = relationship('Account')


class Creditvoucher(Voucher):
    __tablename__ = 'creditvoucher'

    vouchID = Column(ForeignKey('voucher.vouchID'), primary_key=True)
    vDATE = Column(Date)
    credit = Column(DECIMAL(10, 2))
    authBy = Column(ForeignKey('user.userID'), index=True)
    prepBy = Column(ForeignKey('user.userID'), index=True)

    user = relationship('User', primaryjoin='Creditvoucher.authBy == User.userID')
    user1 = relationship('User', primaryjoin='Creditvoucher.prepBy == User.userID')


class Debit(Voucher):
    __tablename__ = 'debit'

    vouchID = Column(ForeignKey('voucher.vouchID'), primary_key=True)
    accountID = Column(ForeignKey('account.accountID'), nullable=False, index=True)
    sourceNo = Column(Integer)
    Amount = Column(DECIMAL(10, 2))
    Narration = Column(String(100))

    account = relationship('Account')


class Debitvoucher(Voucher):
    __tablename__ = 'debitvoucher'

    vouchID = Column(ForeignKey('voucher.vouchID'), primary_key=True)
    vDATE = Column(Date)
    debit = Column(DECIMAL(10, 2))
    authBy = Column(String(100))
    prepBy = Column(String(100))


class Voucherdetail(Voucher):
    __tablename__ = 'voucherdetails'

    vouchID = Column(ForeignKey('voucher.vouchID', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True)
    sourceNo = Column(Integer)
    Amount = Column(DECIMAL(10, 2))
    Narration = Column(String(100))


class Orderdetail(Base):
    __tablename__ = 'orderdetails'

    orderID = Column(ForeignKey('order.orderID', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True, nullable=False)
    detailsID = Column(String(10), primary_key=True, nullable=False)
    prodID = Column(String(10))
    serviceID = Column(String(10))
    quantity = Column(Integer)
    order_tot = Column(DECIMAL(10, 2))

    order = relationship('Order')


class Receipt(Base):
    __tablename__ = 'receipt'

    receiptID = Column(String(10), primary_key=True)
    orderID = Column(ForeignKey('order.orderID', ondelete='CASCADE', onupdate='CASCADE'), index=True)
    busID = Column(ForeignKey('business.busID', ondelete='CASCADE', onupdate='CASCADE'), index=True)
    DATE_issued = Column(Date)

    busines = relationship('Busines')
    order = relationship('Order')


class Supportdoc(Base):
    __tablename__ = 'supportdoc'

    vouchID = Column(ForeignKey('voucher.vouchID', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True, nullable=False)
    sourceNo = Column(Integer, primary_key=True, nullable=False, unique=True)
    docName = Column(String(100))
    docDATE = Column(Date)

    voucher = relationship('Voucher')


class Receiptdetail(Base):
    __tablename__ = 'receiptdetails'

    receiptID = Column(ForeignKey('receipt.receiptID', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, unique=True)
    rdetailsID = Column(String(10), primary_key=True)
    orderID = Column(ForeignKey('order.orderID', ondelete='CASCADE', onupdate='CASCADE'), index=True)
    prodID = Column(ForeignKey('product.prodID', ondelete='CASCADE', onupdate='CASCADE'), index=True)
    serviceID = Column(ForeignKey('service.serviceID', ondelete='CASCADE', onupdate='CASCADE'), index=True)
    quantity = Column(Integer)
    order_tot = Column(DECIMAL(10, 2))

    order = relationship('Order')
    product = relationship('Product')
    receipt = relationship('Receipt')
    service = relationship('Service')


class Sale(Base):
    __tablename__ = 'sale'

    saleID = Column(String(11), primary_key=True)
    customerID = Column(ForeignKey('customer.custID', ondelete='CASCADE', onupdate='CASCADE'), index=True)
    timePaid = Column(DateTime)
    timeCreated = Column(DateTime)
    saleAmt = Column(Integer)
    saleAmtPaid = Column(Integer)
    SaleStatus = Column(String(11))
    receiptID = Column(ForeignKey('receipt.receiptID', ondelete='CASCADE', onupdate='CASCADE'), index=True)

    customer = relationship('Customer')
    receipt = relationship('Receipt')

