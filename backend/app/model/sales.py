from app import db 
from app.model.auth import Busines
from xlrd.timemachine import unicode

class Customer(db.Model):
    __tablename__ = 'customer'

    custID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fname = db.Column(db.String(100))
    lname = db.Column(db.String(100))
    trn = db.Column(db.Integer)
    email = db.Column(db.String(255))

    def ___init__(self, custID, fname, lname, trn, email):
        self.custID = custID
        self.fname = fname
        self.lname = lname 
        self.trn = trn 
        self.email = email 
    
    def get_id(self):
        try:
            return unicode(self.custID)  # python 2 support
        except NameError:
            return str(self.custID)  # python 3 support       
    
    def __repr__(self):
        name = self.fname + "" + self.lname
        return "<Customer {}, {}".format(self.custID, name)

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

    def __init__(self, saleID, customerID, timePaid, timeCreated, saleAmt, saleAmtPaid, SaleStatus, receiptID): 
        self.saleID = saleID
        self.customerID = customerID
        self.timePaid = timePaid
        self.timeCreate =timeCreated
        self.saleAmt = saleAmt
        self.saleAmtPaid = saleAmtPaid
        self.SaleStatus = SaleStatus
        self.receiptID = receiptID
    
    def get_id(self):
        try:
            return unicode(self.saleID)  # python 2 support
        except NameError:
            return str(self.saleID)  # python 3 support       
    
    def __repr__(self):
        return "<Sale {}, {}".format(self.saleID, self.customerID)



class Product(db.Model):
    __tablename__ = 'product'

    prodID = db.Column(db.String(10), primary_key=True)
    busID = db.Column(db.ForeignKey('business.busID', ondelete='CASCADE', onupdate='CASCADE'), index=True)
    prodName = db.Column(db.String(100))
    unit_price = db.Column(db.DECIMAL(10, 2))
    Unit = db.Column(db.DECIMAL(10, 2))
    limitedTime = db.Column(db.DateTime())
    taxPercent = db.Column(db.DECIMAL(3, 2))
    #grade = db.Column(db.String(5))
    prodStatus = db.Column(db.String(25))
    image = db.Column(db.String(50))

    def ___init__(self, prodID, prodName, unit_price, Unit, limitedTime, taxPercent, prodStatus): 
        self.prodID = prodID 
        self.prodName = prodName 
        self.unit_price = unit_price
        self.Unit = Unit 
        self.limitedTime = limitedTime
        self.taxPercent = taxPercent
        self.prodStatus = prodStatus
    
    def get_id(self):
        try:
            return unicode(self.prodID)  # python 2 support
        except NameError:
            return str(self.prodID)  # python 3 support       
    
    def __repr__(self):
        return "<Product {}, {}".format(self.prodID, self.prodName)



class Stock(Product):
    __tablename__ = 'stock'

    prodID = db.Column(db.ForeignKey('product.prodID', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True)
    inStock = db.Column(db.String(10))
    lastUpdateTime = db.Column(db.DateTime())
    quantity = db.Column(db.Integer)
    threshold = db.Column(db.Integer)

    def __init__(self, prodID, inStock, lastUpdateTime, quantity, threshold): 
        self.prodID = prodID 
        self.inStock = inStock
        self.lastUpdateTime = lastUpdateTime
        self.quantity = quantity
        self.threshold = threshold

    def get_id(self):
        try:
            return unicode(self.prodID)  # python 2 support
        except NameError:
            return str(self.prodID)  # python 3 support       
    
    def __repr__(self):
        return "<Stock {}".format(self.prodID)


class Service(db.Model):
    __tablename__ = 'service'

    serviceID = db.Column(db.String(11), primary_key=True)
    busID = db.Column(db.ForeignKey('business.busID', ondelete='CASCADE', onupdate='CASCADE'), index=True)
    serv_name = db.Column(db.String(11))
    serv_cost = db.Column(db.Integer)
    taxPercent = db.Column(db.DECIMAL(3, 2))
    in_season = db.Column(db.String(11))
    image = db.Column(db.String(50))

    def __init__(self, serviceID, serv_name, serv_cost, taxPercent, in_season): 
        self.serviceID = serviceID 
        self.serv_name = serv_name
        self.serv_cost = serv_cost
        self.taxPercent = taxPercent
        self.in_season = in_season

    def get_id(self):
        try:
            return unicode(self.serviceID)  # python 2 support
        except NameError:
            return str(self.serviceID)  # python 3 support       
    
    def __repr__(self):
        return "<Service {}, {}".format(self.serviceID, self.serv_name)

class ServiceSaleItem(Service):
    __tablename__ = 'service_sale_item'

    ssiID = db.Column(db.String(11), primary_key=True)
    serv_price = db.Column(db.Integer)
    taxAmt = db.Column(db.Integer)
    serviceID = db.Column(db.ForeignKey('service.serviceID', ondelete='CASCADE', onupdate='CASCADE'), index=True)
    userID = db.Column(db.ForeignKey('user.userID', ondelete='CASCADE', onupdate='CASCADE'), index=True)

    user = db.relationship('User')

    def ___init__(self, ssiID, serv_price, taxAmt, serviceID, userID): 
        self.ssiID = ssiID
        self.serv_price = serv_price 
        self.taxAmt = taxAmt 
        self.serviceID = serviceID 
        self.userID = userID

    def get_id(self):
        try:
            return unicode(self.ssiID)  # python 2 support
        except NameError:
            return str(self.ssiID)  # python 3 support       
    
    def __repr__(self):
        return "<Service Sale Item {}".format(self.ssiID)



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

    def ___init__(self, cssiID, quantitySold, unit_price, serv_price, taxAmt, serviceID, startTime, endtime, prolong_period):
        self.cssiID = cssiID
        self.quantitySold = quantitySold
        self.unit_price = unit_price
        self.serv_price = serv_price 
        self.taxAmt = taxAmt 
        self.serviceID = serviceID 
        self.starttime = startTime
        self.endtime = endtime
        self.prolong_period = prolong_period

        def get_id(self):
            try:
                return unicode(self.cssiID)  # python 2 support
            except NameError:
                return str(self.cssiID)  # python 3 support       
    
    def __repr__(self):
        return "<Continous Service Sale {}".format(self.cssiID)


class Invoice(db.Model):
    __tablename__ = 'invoice'

    invoiceID = db.Column(db.String(10), primary_key=True)
    busID = db.Column(db.ForeignKey('business.busID', ondelete='CASCADE', onupdate='CASCADE'), index=True)
    custID = db.Column(db.ForeignKey('customer.custID', ondelete='CASCADE', onupdate='CASCADE'), index=True)
    invoice_DATE = db.Column(db.Date)
    tax_tot = db.Column(db.DECIMAL(10, 2))

    customer = db.relationship('Customer')

    def __init__(self, invoiceID, custID, invoice_DATE, tax_total): 
        self.invoiceID = invoiceID 
        self.custID = custID 
        self.invoice_DATE = invoice_DATE
        self.tax_tot = tax_total
    
    def get_id(self):
        try:
            return unicode(self.invoiceID)  # python 2 support
        except NameError:
            return str(self.invoiceID)  # python 3 support       
    
    def __repr__(self):
        return "<Invoice Inovoice ID: {}, Invoice Date: {}".format(self.invoiceID, self.invoice_DATE)

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

    def __init__(self, psiID, customerID, timePaid, timeCreated, saleAmt, saleAmtPaid, status, qSold, uPrice, prodID,taxAmt): 
        self.psiID = psiID
        self.customerID = customerID 
        self.timePaid = timePaid
        self.timeCreated = timeCreated
        self.saleAmt = saleAmt 
        self.saleAmtPaid = saleAmtPaid
        self.SaleStatus = status 
        self.quantitySold = qSold
        self.unit_price =uPrice
        self.prodID = prodID
        self.taxAmt = taxAmt 
    
    def get_id(self):
        try:
            return unicode(self.psiID)  # python 2 support
        except NameError:
            return str(self.psiID)  # python 3 support       
    
    def __repr__(self):
        return "<Product Sale Item, PSaleID: {}, Product ID: {}".format(self.psiID, self.prodID)
        
class ConService(db.Model):
    __tablename__ = 'con_service'

    serviceID = db.Column(db.String(11), primary_key=True)
    busID = db.Column(db.ForeignKey('business.busID', ondelete='CASCADE', onupdate='CASCADE'), index=True)
    serv_name = db.Column(db.String(11))
    serv_uprice = db.Column(db.Integer)
    basic_unit = db.Column(db.DECIMAL(10, 2))
    d_prolongperiod = db.Column(db.DateTime)
    taxPercent = db.Column(db.DECIMAL(3, 2))
    in_season = db.Column(db.String(11))
    image = db.Column(db.String(50))
    cssiID = db.Column(db.ForeignKey('con_service_sale_item.cssiID', ondelete='CASCADE', onupdate='CASCADE'), index=True)

    con_service_sale_item = db.relationship('ConServiceSaleItem')

    def __init__(self, serviceID, serv_name, serv_uprice, basic_unit, 
                d_prolongperiod, taxPercent, in_season, cssiID):
        self.serviceID = serviceID 
        self.serv_name = serv_name
        self.serv_uprice = serv_uprice
        self.basic_unit = basic_unit
        self.d_prolongperiod = d_prolongperiod
        self.taxPercent = taxPercent
        self.in_season = in_season
        self.cssiID = cssiID
    

    def get_id(self):
        try:
            return unicode(self.serviceID)  # python 2 support
        except NameError:
            return str(self.serviceID)  # python 3 support       
    
    def __repr__(self):
        return "<Continous Service, CServID: {}, Service ID: {}".format(self.cssiID, self.serviceID)
        


class Order(db.Model):
    __tablename__ = 'custorder'

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


    def ___init__(self, orderID, order_tot,order_DATE, custID, invoiceID, busID, status): 
        self.orderID = orderID 
        self.order_tot = order_tot
        self.order_DATE = order_DATE
        self.custID = custID
        self.invoiceID = invoiceID 
        self.busID = busID 
        self.status = status 
    

    def get_id(self): 
        try: 
            return unicode(self.orderID) # python 2 code
        except NameError: 
            return str(self.orderID) #python 3 code
    
    def __repr__(self):
        return "<Order {}>".format(self.orderID)


class Orderdetail(db.Model):
    __tablename__ = 'orderdetails'

    orderID = db.Column(db.ForeignKey('custorder.orderID', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True, nullable=False)
    detailsID = db.Column(db.String(10), primary_key=True, nullable=False)
    prodID = db.Column(db.String(10))
    serviceID = db.Column(db.String(10))
    quantity = db.Column(db.Integer)
    order_tot = db.Column(db.DECIMAL(10, 2))

    order = db.relationship('Order')

    def __init__(self, orderID, detailsID, prodID, serviceID, quantity, order_tot): 
        self.orderID = orderID 
        self.detailsID = detailsID
        self.prodID = prodID 
        self.serviceID = serviceID 
        self.quantity = quantity
        self.order_tot = order_tot

    # def get_id(self):
    #     try:
    #         return unicode(self.saleID)  # python 2 support
    #     except NameError:
    #         return str(self.saleID)  # python 3 support       
    
    def __repr__(self):
        return "<Order Detail {}, Order: {}".format(self.orderID, self.detailsID)

class Receipt(db.Model):
    __tablename__ = 'receipt'

    receiptID = db.Column(db.String(10), primary_key=True)
    orderID = db.Column(db.ForeignKey('custorder.orderID', ondelete='CASCADE', onupdate='CASCADE'), index=True)
    busID = db.Column(db.ForeignKey('business.busID', ondelete='CASCADE', onupdate='CASCADE'), index=True)
    DATE_issued = db.Column(db.Date)

    busines = db.relationship('Busines')
    order = db.relationship('Order')

    def __init__(self, receiptID, orderID, busID, date_issued): 
        self.receiptID = receiptID
        self.orderID = orderID 
        self.busID = busID 
        self.DATE_issued = date_issued
    

    def get_id(self):
        try:
            return unicode(self.receiptID)  # python 2 support
        except NameError:
            return str(self.receiptID)  # python 3 support       
    
    def __repr__(self):
        return "<Receipt {}, Order ID: {}".format(self.receiptID, self.orderID)

class Receiptdetail(db.Model):
    __tablename__ = 'receiptdetails'

    receiptID = db.Column(db.ForeignKey('receipt.receiptID', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, unique=True)
    rdetailsID = db.Column(db.String(10), primary_key=True)
    orderID = db.Column(db.ForeignKey('custorder.orderID', ondelete='CASCADE', onupdate='CASCADE'), index=True)
    prodID = db.Column(db.ForeignKey('product.prodID', ondelete='CASCADE', onupdate='CASCADE'), index=True)
    serviceID = db.Column(db.ForeignKey('service.serviceID', ondelete='CASCADE', onupdate='CASCADE'), index=True)
    quantity = db.Column(db.Integer)
    order_tot = db.Column(db.DECIMAL(10, 2))

    order = db.relationship('Order')
    product = db.relationship('Product')
    receipt = db.relationship('Receipt')
    service = db.relationship('Service')

    def ___init__(self, receiptID, rdetailsID, orderID, prodID, serviceID, quantity, order_tot):
        self.receiptID = receiptID
        self.rdetailsID = rdetailsID
        self.orderID = orderID 
        self.prodID = prodID 
        self.serviceID = serviceID 
        self.quantity = quantity
        self.order_tot = order_tot
    
    def get_id(self):
        try:
            return unicode(self.rdetailsID)  # python 2 support
        except NameError:
            return str(self.rdetailsID)  # python 3 support       
    
    def __repr__(self):
        return "<Receipt Details ID {}, Receipt ID:{}".format(self.rdetailsID, self.receiptID)

class Websitedetails(db.Model):
    _tablename_ = 'websitedetails'
    
    section_detail = db.Column(db.String(10), primary_key=True, unique=True) 
    sec_header = db.Column(db.String(50)) 
    sec_message = db.Column(db.String(50))

    websitedrag = db.relationship("Websitedrag", uselist=False, backref= db.backref("websitedetails", uselist=False))

    def _init_(self, section_detail, sec_header, sec_message): 
        self.section_detail = section_detail
        self.sec_header = sec_header
        self.sec_message = sec_message

    def get_id(self):
        try:
            return unicode(self.section_detail)  # python 2 support
        except NameError:
            return str(self.section_detail)  # python 3 support       
    
    def __repr__(self):
        return "<Website Details {} ".format(self.section_detail)

class Websitedrag(db.Model):
    _tablename_ = 'websitedrag'

    sectionID = db.Column(db.Integer, primary_key=True, unique=True)
    positionID = db.Column(db.String(50)) 
    sectionName = db.Column(db.String(50)) 
    section_detail = db.Column(db.String(50), db.ForeignKey('websitedetails.section_detail', ondelete='CASCADE', onupdate='CASCADE'))
    
    def _init_(self,  sectionID, positionID, sectionName, section_detail):
        self.sectionID = sectionID
        self.positionID = positionID
        self.sectionName = sectionName
        self.section_detail = section_detail
    
    def get_id(self):
        try:
            return unicode(self.sectionID)  # python 2 support
        except NameError:
            return str(self.sectionID)  # python 3 support       
    
    def __repr__(self):
        return "<WebsiteDrag {}, {}, {}".format(self.sectionID, self.positionID, self.sectionName)

