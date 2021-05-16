from app import  db, login_manager, csrf_, principal, ma
from app.forms import orderForm, newProductForm
from app.model.sales import Product, ProductSaleItem, Customer, Invoice, Order
from app.schema import sales
from sqlalchemy import func, inspection, event
from flask import  Blueprint, current_app, request, jsonify, flash, session,  _request_ctx_stack, g
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

@product.route('/api/product/<prodID>', methods =['PUT'])
def update_product(prodID):
    product = Product.query.get(prodID)
    # What parts to
    return 1

@product.route('/api/product/<prodID>', methods = ['DELETE'])
def delete_product(prodID): 
    product = Product.query.get(prodID)
    db.session.delete(product)
    db.session.commit() 
    return jsonify({'message': 'Product {} has been deleted.'}.format(prodID))

@product.route('/api/newproduct', methods = ['GET', 'POST'])
def new_product():
    form = newProductForm(request.form)

    if request.method == "POST":
        product_name = form.product_name.data
        quantity = form.quantity.data
        uom = form.uom.data
        unit_price = form.unit_price.data
        status = form.status.data
        tax = form.tax.data

        image_file = request.files['image']
        if image_file:
            filename = secure_filename(image_file.filename)
            image_file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))

       
        newProduct = Product(prodID=None, busID="Mon1", prodName=product_name, unit_price=unit_price, 
                            Unit="", limitedTime="", taxPercent=tax, prodStatus=status, image=filename)
    
        try:
            db.session.add(newProduct)
            db.session.commit()
        except Exception as e:
            error = str(e)

        flash('New product added successfully')
    return jsonify({"message":"New product added successfully"})

@product.route('/api/products', methods = ['GET', 'POST'])
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
        
    return jsonify(data_list)

#@app.route('/api/product/classify', methods = ['GET', 'POST'])
@product.route('/api/classify', methods = ['GET', 'POST'])

#safety stock = (max daily sales x max lead time in days) - (average daily sales x average lead time in days)

def product_classify():
    #product_list = defaultdict(list)
    annual_consum_val = []
    total_consum_val = 0
    total_units_sold = 0
    product_sales = db.session.query(ProductSaleItem).all()

    for product in product_sales: 
        consum_val = product.quantitySold * product.unit_price
        annual_consum_val.append([product.psiID, consum_val, 'C']) #Set them as C by default
        total_consum_val += consum_val
        total_units_sold += product.quantitySold

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
        if percentage >=80:
            index = annual_consum_val.index(product)
            break

    #Check for B products
    for product in annual_consum_val[index + 1:]:
        total_valB+= product[1]
        product[2]= 'B'
        percentage = (total_valB / total_consum_val) * 100
        if percentage >=15:
            break

    data = []
    #Convert to dict
    for product in annual_consum_val:
        data.append({'prodID':product[0], 'con_val': str(product[1]), 'grade':product[2]})
    
    return jsonify({'products': data})

    # Find Percentage of Annual Units Sold 
    # for product in product_sales: 
    #     desc_consum_val = sorted(annual_consum_val, reverse=True) # List of Annual Consumption Values (Descending Order)
    #     percent_units_sold = (product.quantitySold/total_units_sold)*100.0  # % of Annual Units Sold
    #     for val in desc_con_val: 
    #         percent_consum_val = (val/total_consum_val)*100.0  # % of Total Annual Consumption Value

            # Split Data ito 80/15/5
            # get length of product_list then divide by percentage
            # Assign Grades to products based on products in each percentile


    # Find Percentage of Annual Consumption Value



@product.route('/api/checkout-products', methods = ['GET'])
def checkoutproducts():
    message = {}
    data = {}
    tprice = 0
    deliver = 500

    transaction_inputs = [
            {
                'id': 1,
                'img': "https://5.imimg.com/data5/RU/WI/MY-46283651/school-skirts-500x500.jpg",
                'name': 'skirt',
                'quantity': '1',
                'size': 'L',
                'colour': 'black',
                'price': "500"
            },
            {
                'id': 2,
                'img': "https://slimages.macysassets.com/is/image/MCY/products/2/optimized/17864922_fpx.tif?$browse$&wid=170&fmt=jpeg",
                'name': 'pants',
                'quantity': '1',
                'size': 'medium',
                'colour': 'white',
                'price': '1000'
            },
            {
                'id': 3,
                'img': "https://di2ponv0v5otw.cloudfront.net/posts/2018/03/24/5ab6a736077b9758675a91e5/m_5ab6c769c9fcdfbadf53cd14.jpeg",
                'name': 'top',
                'quantity': '1',
                'size': 'medium',
                'colour': 'white',
                'price': '800'
            }
        ]

    for card in transaction_inputs:
        tprice = tprice + int(card['price'])

    tcost = tprice + deliver

    return jsonify(data)
