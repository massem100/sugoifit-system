def prof_margin(sales, expenses):
    """ The percentage of sales revenue that is
        profit."""      
    return ((sales - expenses) / sales ) * 100

def op_margin(sales, op_expenses):
    """ The percentage of profit a company produces 
        from its operations """
    return ((sales - op_expenses) / sales ) * 100

def break_even(fixed_cost, unit_price, var_cost):
    """ The point at which there is neither profit nor loss /
        where income and expenditure are equal"""

    #The value is the minimum units you need to avoid profit loss
    return (fixed_cost / (unit_price - var_cost))

if __name__ == "__main__":
    prof_margin()