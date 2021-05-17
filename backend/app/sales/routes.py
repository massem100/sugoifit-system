# from app import  db, login_manager, cors, csrf_, principal, jwt_token
from flask import Blueprint, request, jsonify, flash, session,  _request_ctx_stack, g
from werkzeug.utils import secure_filename
from app.forms import orderForm
from app.model.sales import Product, ProductSaleItem, Customer, Invoice, Order
 
sales= Blueprint('sales', __name__)

"""
--------------------------------------- Orders ----------------------------------------------------------
"""

@sales.route('/api/placeorder', methods = ['POST', 'GET'])
def place_order():
  #Display order based on rank
  form = orderForm(request.form)

  if request.method == "POST":
    total_price = request.form['tcost']
    fname = form.fname.data
    lname = form.lname.data
    trn = form.trn.data
    address = form.address.data
    phone = form.phone_num.data
    email = form.email.data

    customer = Customer.query.filter_by(trn = trn).first()

    if customer == None:
        # Add new customer
        new_customer = Customer(custID="c01",fname=fname, lname=lname, trn=trn, email=email)
        db.session.add(new_customer)

    date_format = "%Y-%m-%d"
    status = "Pending"
    today = datetime.now()
    todayString = today.strftime(date_format)
    dateDue = (today + timedelta(days=7)).strftime(date_format)

    new_order = Order(orderID="O1", order_tot=total_price, order_DATE=todayString, custID=customer.custID, invoiceID="", busID="", status=status)
    try:
        db.session.add(new_order)
        db.session.commit()
    except Exception as e:
        error = str(e)

    #data = {"order_tot":total_price, "order_DATE":todayString, "customer.custID":customer.custID, "invoiceID":7, "status":status}
    return jsonify({"message":"order added successfully", 'errors': error})
    
""" 
Rank based on date order should be fulfilled
 
Click manage orders
1) Pull all orders which are pending
2) compare date due, with current date. Subtract and use the value to rank
3) Sort in ascending order based on that value.

from datetime import datetime

date_format = "%Y-%m-%d"
a = datetime.strptime('2021-04-14',date_format)
b = datetime.strptime('2021-04-22',date_format)
delta = b - a
print (delta.days)

"""
@sales.route('/manage-orders')
def manageOrders():
    #Get all orders that are pending
    date_format = "%Y-%m-%d"
    allOrders = []
    ordersQuery = Order.query.filter_by(status="Pending").all()

    #Calculate days left for each record
    #Put record in tuple form and append to list
    for record in ordersQuery:
        orderID = record.orderID
        orderTotal = record.order_tot
        date = record.order_DATE
        custID = record.custID
        invoiceID = record.invoiceID
        busID = record.busIDo
        status = record.status
        dueDate = record.dueDate

        startDate = datetime.strptime(date, date_format)
        endDate = datetime.strptime(dueDate, date_format)

        daysLeft = endDate - startDate
        daysLeft = daysLeft.days()

        allOrders.append((orderID, orderTotal, date, custID, invoiceID,
        busID, status, dueDate, daysLeft))

    allOrders.sort(lambda x: x[8], reverse = False)

    #Need to print this list on the front end.
    return allOrders

@sales.route('/api/invoice', methods = ['GET', 'POST'])
def all_product():
    data_list = []
    busID = "Mon1"
    products = Product.query.filter_by(busID=busID).all()
    output = sales.products_schema.dump(products)

    for item in output:
        case = {
            "id":item['prodID'],
            "name":item['prodName'],
            "price":item['unit_price'],
            "tax":item['taxPercent'],   
            "status":item['prodStatus'],
            "image":item['image']
        }
        data_list.append(case)
        #data.update(item=item.index)

    #return jsonify(output)
    return jsonify(data_list)