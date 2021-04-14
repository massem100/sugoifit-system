from app import db 
from app.model.auth import Busines

class Customer(db.Model):
    __tablename__ = 'customer'

    custID = db.Column(db.String(10), primary_key=True)
    fname = db.Column(db.String(100))
    lname = db.Column(db.String(100))
    trn = db.Column(db.Integer)
    email = db.Column(db.String(255))

class Sale(db.Model):
    __tablename__ = 'sale'

    saleID = db.Column(db.String(11), primary_key=True)
    customerID = db.Column(db.ForeignKey('customer.custID', ondelete='CASCADE', onupdate='CASCADE'), index=True)
    timePaid = db.Column(db.DateTime)
    timeCreated = db.Column(db.DateTime)
    saleAmt = db.Column(db.Integer)
    saleAmtPaid = db.Column(db.Integer)
    SaleStatus = db.Column(db.String(11))
    receiptID = db.Column(db.ForeignKey('receipt.receiptID', ondelete='CASCADE', onupdate='CASCADE'), index=True)

    customer = db.relationship('Customer')
    receipt = db.relationship('Receipt')


class Product(db.Model):
    __tablename__ = 'product'

    prodID = db.Column(db.String(10), primary_key=True)
    prodName = db.Column(db.String(100))
    unit_price = db.Column(db.DECIMAL(10, 2))
    Unit = db.Column(db.DECIMAL(10, 2))
    limitedTime = db.Column(db.DateTime())
    taxPercent = db.Column(db.DECIMAL(3, 2))
    prodStatus = db.Column(db.String(25))


class Stock(Product):
    __tablename__ = 'stock'

    prodID = db.Column(db.ForeignKey('product.prodID', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True)
    inStock = db.Column(db.String(10))
    lastUpdateTime = db.Column(db.DateTime())
    quantity = db.Column(db.Integer)
    threshold = db.Column(db.Integer)


class Service(db.Model):
    __tablename__ = 'service'

    serviceID = db.Column(db.String(11), primary_key=True)
    serv_name = db.Column(db.String(11))
    serv_cost = db.Column(db.Integer)
    taxPercent = db.Column(db.DECIMAL(3, 2))
    in_season = db.Column(db.String(11))


class ServiceSaleItem(Service):
    __tablename__ = 'service_sale_item'

    ssiID = db.Column(db.String(11), primary_key=True)
    serv_price = db.Column(db.Integer)
    taxAmt = db.Column(db.Integer)
    serviceID = db.Column(db.ForeignKey('service.serviceID', ondelete='CASCADE', onupdate='CASCADE'), index=True)
    userID = db.Column(db.ForeignKey('user.userID', ondelete='CASCADE', onupdate='CASCADE'), index=True)

    user = db.relationship('User')



class ConServiceSaleItem(db.Model):
    __tablename__ = 'con_service_sale_item'

    cssiID = db.Column(db.String(11), primary_key=True)
    quantitySold = db.Column(db.Integer)
    unit_price = db.Column(db.Integer)
    serv_price = db.Column(db.Integer)
    taxAmt = db.Column(db.Integer)
    serviceID = db.Column(db.ForeignKey('service.serviceID', ondelete='CASCADE', onupdate='CASCADE'), index=True)
    starttime = db.Column(db.DateTime)
    endtime = db.Column(db.DateTime)
    prolong_period = db.Column(db.DateTime)

    service = db.relationship('Service')


class Invoice(db.Model):
    __tablename__ = 'invoice'

    invoiceID = db.Column(db.String(10), primary_key=True)
    custID = db.Column(db.ForeignKey('customer.custID', ondelete='CASCADE', onupdate='CASCADE'), index=True)
    invoice_DATE = db.Column(db.Date)
    tax_tot = db.Column(db.DECIMAL(10, 2))

    customer = db.relationship('Customer')


class ProductSaleItem(db.Model):
    __tablename__ = 'product_sale_item'

    psiID = db.Column(db.Integer, primary_key=True)
    customerID = db.Column(db.ForeignKey('customer.custID', ondelete='CASCADE', onupdate='CASCADE'), index=True)
    timePaid = db.Column(db.DateTime)
    timeCreated = db.Column(db.DateTime)
    saleAmt = db.Column(db.DECIMAL(10, 2))
    saleAmtPaid = db.Column(db.DECIMAL(10, 2))
    SaleStatus = db.Column(db.String(25))
    quantitySold = db.Column(db.DECIMAL(10, 2))
    unit_price = db.Column(db.DECIMAL(10, 2))
    prodID = db.Column(db.ForeignKey('product.prodID', ondelete='CASCADE', onupdate='CASCADE'), index=True)
    taxAmt = db.Column(db.DECIMAL(10, 2))

    customer = db.relationship('Customer')
    product = db.relationship('Product')


class ConService(db.Model):
    __tablename__ = 'con_service'

    serviceID = db.Column(db.String(11), primary_key=True)
    serv_name = db.Column(db.String(11))
    serv_uprice = db.Column(db.Integer)
    basic_unit = db.Column(db.DECIMAL(10, 2))
    d_prolongperiod = db.Column(db.DateTime)
    taxPercent = db.Column(db.DECIMAL(3, 2))
    in_season = db.Column(db.String(11))
    cssiID = db.Column(db.ForeignKey('con_service_sale_item.cssiID', ondelete='CASCADE', onupdate='CASCADE'), index=True)

    con_service_sale_item = db.relationship('ConServiceSaleItem')



class Order(db.Model):
    __tablename__ = 'order'

    orderID = db.Column(db.String(10), primary_key=True)
    order_tot = db.Column(db.DECIMAL(10, 2))
    order_DATE = db.Column(db.Date)
    custID = db.Column(db.ForeignKey('customer.custID', ondelete='CASCADE', onupdate='CASCADE'), index=True)
    invoiceID = db.Column(db.ForeignKey('invoice.custID', ondelete='CASCADE', onupdate='CASCADE'), index=True)
    busID = db.Column(db.ForeignKey('business.busID', ondelete='CASCADE', onupdate='CASCADE'), index=True)
    status = db.Column(db.String(20))

    busines = db.relationship('Busines')
    customer = db.relationship('Customer')
    invoice = db.relationship('Invoice')



class Orderdetail(db.Model):
    __tablename__ = 'orderdetails'

    orderID = db.Column(db.ForeignKey('order.orderID', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True, nullable=False)
    detailsID = db.Column(db.String(10), primary_key=True, nullable=False)
    prodID = db.Column(db.String(10))
    serviceID = db.Column(db.String(10))
    quantity = db.Column(db.Integer)
    order_tot = db.Column(db.DECIMAL(10, 2))

    order = db.relationship('Order')


class Receipt(db.Model):
    __tablename__ = 'receipt'

    receiptID = db.Column(db.String(10), primary_key=True)
    orderID = db.Column(db.ForeignKey('order.orderID', ondelete='CASCADE', onupdate='CASCADE'), index=True)
    busID = db.Column(db.ForeignKey('business.busID', ondelete='CASCADE', onupdate='CASCADE'), index=True)
    DATE_issued = db.Column(db.Date)

    busines = db.relationship('Busines')
    order = db.relationship('Order')


class Receiptdetail(db.Model):
    __tablename__ = 'receiptdetails'

    receiptID = db.Column(db.ForeignKey('receipt.receiptID', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, unique=True)
    rdetailsID = db.Column(db.String(10), primary_key=True)
    orderID = db.Column(db.ForeignKey('order.orderID', ondelete='CASCADE', onupdate='CASCADE'), index=True)
    prodID = db.Column(db.ForeignKey('product.prodID', ondelete='CASCADE', onupdate='CASCADE'), index=True)
    serviceID = db.Column(db.ForeignKey('service.serviceID', ondelete='CASCADE', onupdate='CASCADE'), index=True)
    quantity = db.Column(db.Integer)
    order_tot = db.Column(db.DECIMAL(10, 2))

    order = db.relationship('Order')
    product = db.relationship('Product')
    receipt = db.relationship('Receipt')
    service = db.relationship('Service')


class Websitedetails(db.Model):
    __tablename__ = 'websitedetails'
    
    section_detail = db.Column(db.String(10), primary_key=True, unique=True) 
    sec_header = db.Column(db.String(50)) 
    sec_message = db.Column(db.String(50))

    websitedrag = db.relationship("Websitedrag", uselist=False, backref= db.backref("websitedetails", uselist=False))

    def __init__(self, section_detail, sec_header, sec_message): 
        self.section_detail = section_detail
        self.sec_header = sec_header
        self.sec_message = sec_message

class Websitedrag(db.Model):
    __tablename__ = 'websitedrag'

    sectionID = db.Column(db.Integer, primary_key=True, unique=True)
    positionID = db.Column(db.String(50)) 
    sectionName = db.Column(db.String(50)) 
    section_detail = db.Column(db.String(50), db.ForeignKey('websitedetails.section_detail', ondelete='CASCADE', onupdate='CASCADE'))
    
    def __init__(self,  sectionID, positionID, sectionName, section_detail):
        self.sectionID = sectionID
        self.positionID = positionID
        self.sectionName = sectionName
        self.section_detail = section_detail
