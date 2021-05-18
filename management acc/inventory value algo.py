
'''
Inventory valuation is basically where you find out the cost of overall inventory items.
Can either be done item by item or by category. I believe item by item would be more accurate
but based on the example the figures changed so idk but seeing that we are
dealing with small businesses i went with item by item

So thats number of items x the cost
The cost can either be the market price of the cost price of the company but it must be the lower value.
eg buying 50 shirts for $100 vs the market price being $200 for them, use cost price

Different methods of calculating inventory value FIFO, LIFO and WAC
FIFO: items are sold based on what was manufactured or bought first
LIFO: most recently purchased or manufactured item should be sold first
WAC(weighted average): average cost of all items are used, little to no variation
in inventory. i belive this is better for the categorizing.
COGS = cost of goods sold 
'''
#Assuming the database looks sumn like this 
inventory={
    'shirt': {
        'shirt1':{
            'id':'shirt1',
           'quantity':5,
           'cost':500,
           'market-p':2500
           },
        "shirt2":{
            'id':'shirt2',
           'quantity':10,
           'cost':1000,
           'market-p':5000}
        },
    'skirt':{
       'skirt1':{
           'id':'skirt1',
           'quantity':9,
           'cost':1200,
           'market-p':4200
           },
        'skirt2':{
            'id':'skirt2',
           'quantity':6,
           'cost':1000,
           'market-p':4000
           }
        }
}
shirts_sold = 4
skirts_sold = 8

for category, products in inventory.items():
    for items in products:
        
        #my attempt at separating by categories, not efficient ik
        if "shirt" in products['item']['id']:
            
            #couldnt figure out how to add the two consecutive numbers properly eg. 5 and 10
            t_quantity = value[key]['quantity'] + value[key]['quantity']  #total number of items in that category
            if value[key]['cost'] < value[key]['market-p']:
                t_paid = value[key]['quantity'] * value[key]['cost']          #total cost of items in that category

            if value[key]['cost'] > value[key]['market-p']:
                t_paid = value[key]['quantity'] * value[key]['market-p']

            #this gives the value per item for that category
            wac = t_paid / t_quantity 
            #after selling a certain amount from 
            cogs = shirts_sold * wac
            #value of other similar items in inventory still
            remaining_sh = (t_quantity - shirts_sold)* wac 
       
        if "skirt" in products[item]['id']:
            t_quantity = value[key]['quantity'] + value[key]['quantity']
            
            if value[key]['cost'] < value[key]['market-p']:
                t_paid = value[key]['quantity'] * value[key]['cost']       

            if value[key]['cost'] > value[key]['market-p']:
                t_paid = value[key]['quantity'] * value[key]['market-p']
                
            #this gives the value per item for that category
            wac = t_paid / t_quantity 
            #after selling a certain amount from 
            cogs = shirts_sold * wac
            #value of other similar items in inventory still
            remaining_sk = (t_quantity - skirts_sold)* wac 
     
#value of inventory overall
inventory_value = remaining_sk + remaining_sh
