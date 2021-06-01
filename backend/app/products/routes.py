import os, sys
from app import db, login_manager, csrf_, principal
from app.forms import orderForm, NewProductForm
from app.model.sales import Product, ProductSaleItem, Customer, Invoice, Order
from app.schema.sales import product_schema, products_schema
from app.views import form_errors
from sqlalchemy import func, inspection, event, desc
from datetime import datetime
from flask import  Blueprint, current_app,  request, jsonify, flash, session,  _request_ctx_stack, g
from flask_login import current_user
from werkzeug.utils import secure_filename
import os


product = Blueprint('product', __name__)


"""
--------------------------------------- Product/Services Routes ----------------------------------------------------------
"""


# @app.route('/dev/<int:id>/', methods=['PUT'])
# def update_dev(id):
#     dev = Developer.query.get(id)
#     dev.name = request.json.get('name', dev.name)
#     db.session.commit()
#     return jsonify({'dev': dev.serialize()})


@product.route('/api/<busID>/products/<prodID>', methods = ['PUT', 'DELETE'])
def delete_product(busID, prodID):
    if request.method == 'DELETE': 
        product = db.session.query(Product).filter_by(busID =busID, prodID = prodID).first()
        print(product)
        if product is not None:

            db.session.delete(product)
            db.session.commit() 
            return jsonify({'message': 'Product {} has been deleted.'.format(prodID)})
        else: 
            return jsonify({'message': 'No product found'})

    if request.method == 'PUT': 
        pass

@product.route('/api/<busID>/products', methods = ["GET", "POST"])
def aproduct(busID):
    form = NewProductForm(request.form)

    if request.method == "POST":
        if form.validate_on_submit():
            product_name = form.product_name.data
            image_file = request.files["image"]
            prod_desc = form.desc.data
            quantity = form.quantity.data
            prod_size = form.size.data
            man_units = form.man_units.data
            unit_price = form.unit_price.data
            status = form.status.data
            tax = form.tax.data 
            

            if image_file is not None:
                basedir = os.path.abspath(os.path.dirname(__file__))
                sec_filename = secure_filename(image_file.filename)
                image_file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], sec_filename))

                try:
                    newProduct = Product(prodID=None, busID=busID, prodName=product_name, prodType="None", 
                                prodDesc=prod_desc, prodQuantity=quantity, prodSize=prod_size, unit_price=unit_price, 
                                    Unit=man_units, limitedTime=datetime.now(), taxPercent=tax, grade="", 
                                    prodStatus=status, image=sec_filename)

                    db.session.add(newProduct)
                    db.session.commit()
                except Exception as e:
                    error = str(e)
                    print(error)

                return jsonify({"message":"New product added successfully"})
        else: 
            errors = form_errors(form) 
            return jsonify(erorrs=errors)

    if request.method == "GET": 
        products = []
        product_list = db.session.query(Product).filter_by(busID=busID).order_by(desc(Product.prodID)).all()
        product_dump = products_schema.dump(product_list)
    
        # QUERY THE SERVICES TABLE TOO
        return jsonify(product_dump)

   

#@app.route('/api/product/classify', methods = ['GET', 'POST'])
@product.route('/api/classify', methods = ['GET', 'POST'])
def product_classify():
    #safety stock = (max daily sales x max lead time in days) - (average daily sales x average lead time in days)
    annual_consum_val = []
    total_consum_val = 0
    total_units_sold = 0
    product_sales = db.session.query(ProductSaleItem).all()

    today = datetime.today()
    today = today.strftime(date_format)
    today = datetime.strptime(today, date_format)

    for product in product_sales: 
        consum_val = product.quantitySold * product.unit_price
        pDateAdded = db.session.query(Stock).filter_by(prodID = product.psiID)
        pDateAdded = pDateAdded[0].lastUpdateTime
        pDateAdded = pDateAdded.strftime(date_format)
        pDateAdded = datetime.strptime(pDateAdded, date_format)

        daysPassed = today - pDateAdded
        daysPassed = daysPassed.days
        
        if daysPassed >=28:    
            annual_consum_val.append([product.psiID, consum_val, 'C', 0]) #Set them as C by default
            total_consum_val += consum_val
            total_units_sold += product.quantitySold
        else:
            notApplicable.append([product.psiID, consum_val, 'N/A', 'N/A'])

    
    #Sort consumption list in descending order
    annual_consum_val.sort(key= lambda x: x[1], reverse = True)

    total_valA = 0
    total_valB = 0
    index = None
    #Check for A products
    for product in annual_consum_val:
        total_valA+= product[1]
        product[2]= 'A'
        percentage = (total_valA / total_consum_val) * 100
        product[3] = (product[1] / total_consum_val ) *100
        if percentage >=80:
            index = annual_consum_val.index(product)
            break

    #Check for B products
    for product in annual_consum_val[index + 1:]:
        total_valB+= product[1]
        product[2]= 'B'
        percentage = (total_valB / total_consum_val) * 100
        product[3] = (product[1] / total_consum_val ) *100
        
        if percentage >=15:
            break
    
    try:
        for product in annual_consum_val[index + 1:]:
            product[3] = (product[1] / total_consum_val ) *100     
    except LookupError:
        print("Out of bounds")
    else:
        print("complete")

    
    data = []
    #Convert to dict
    for product in annual_consum_val:

        prod = db.session.query(Product).filter_by(prodID = product[0])
        
        """ Date fetching """
        prodDate = db.session.query(Stock).filter_by(prodID = product[0])
        updatedDate = prodDate[0].lastUpdateTime
        updatedDate = updatedDate.strftime(date_format)

        product[1] = "{:.2f}".format(product[1])
        product[3] = "{:.2f}".format(product[3])
        data.append({'prodID':prod[0].prodName, 'con_val': "$"+product[1], 'grade':product[2], 'stock': prod[0].prodStatus, 
            'dateAdded':updatedDate, 'percent':product[3]})

    for naItem in notApplicable:
        prod = db.session.query(Product).filter_by(prodID = naItem[0])

        """ Date Fetching """
        prodDate = db.session.query(Stock).filter_by(prodID = naItem[0])
        updatedDate = prodDate[0].lastUpdateTime
        updatedDate = updatedDate.strftime(date_format)

        naItem[1] = "{:.2f}".format(naItem[1]) #consumption val
        data.append({'prodID':prod[0].prodName, 'con_val': "$"+naItem[1], 'grade':naItem[2], 'stock': prod[0].prodStatus, 
            'dateAdded':updatedDate, 'percent':naItem[3]})

    
    return jsonify({'products': data})

