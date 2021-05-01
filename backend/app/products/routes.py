from app import  db, login_manager, csrf_, principal
from app.forms import orderForm
from app.model.sales import Product, ProductSaleItem, Customer, Invoice, Order
from sqlalchemy import func, inspection, event
from flask import  Blueprint,  request, jsonify, flash, session,  _request_ctx_stack, g
from werkzeug.utils import secure_filename


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
            basedir = os.path.abspath(os.path.dirname(__file__))
            filename = secure_filename(image_file.filename)
            image_file.save(os.path.join(basedir, current_app.config['UPLOAD_FOLDER'], filename))

        last_product = db.session.query(sales.Product).order_by(sales.Product.prodID.desc()).first()
        if last_product is None: 
            prod_int = 1
        else:
                
            # Get the numeric part of the last User ID and increment by 1
            last_pID = last_product.prodID
            prod_int = int(last_pID[1:])
            prod_int +=1

        # ADD QUANTITY TO DATABASE
        newProdID = 'P' + str(prod_int)
        newProduct = Product(prodID=newProdID, busID="Mon2", prodName=product_name, unit_price=unit_price, 
                            Unit="", limitedTime="", taxPercent=tax, prodStatus=status, image=filename)
        print(last_pID)
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
    busID = "Mon2"
    products = Product.query.filter_by(busID=busID).all()
    output = products_schema.dump(products)
    
    
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


    '''
    data = {}
    products = [
        {
            "id":1,
            "name":"Black Dress",
            "price":6000,
            "tax":15,
            "status":"active",
            "image":"dress1.jpg"
        },
        {
            "id":2,
            "name":"White Skirt",
            "price":1000,
            "tax":15,
            "status":"active",
            "image":"skirt1.jpg"
        },
        {
            "id":3,
            "name":"Plaid top",
            "price":500,
            "tax":15,
            "status":"active",
            "image":"top1.jpg"
        },
    ]
    data['products'] = products
    '''
    #return jsonify(output)
    return jsonify(data_list)


@product.route('/api/product/classify', methods = ['GET', 'POST'])
def product_classify():
    product_list = defaultdict(list)
    annual_consum_val = []
    total_consum_val = 0
    total_units_sold = 0
    product_sales = db.session.query(ProductSaleItem).all()

    for product in product_sales: 
        consum_val = product.quantitySold * product.unit_price
        annual_consum_val.append([product.psiID, consum_val])
        total_consum_val += consum_val
        total_units_sold += product.quantitySold

    # Find Percentage of Annual Units Sold 
    for product in product_sales: 
        desc_consum_val = sorted(annual_consum_val, reverse=True) # List of Annual Consumption Values (Descending Order)
        percent_units_sold = (product.quantitySold/total_units_sold)*100.0  # % of Annual Units Sold
        for val in desc_con_val: 
            percent_consum_val = (val/total_consum_val)*100.0  # % of Total Annual Consumption Value

            # Split Data ito 80/15/5
            # get length of product_list then divide by percentage
            # Assign Grades to products based on products in each percentile


    # Find Percentage of Annual Consumption Value

    return jsonify({'products': products})
