
class Asset: 
    """ A non current asset can be depleted, depreciated or amortized, what type for each?
    An asset can also appreciate? Factor this in
    Assets can be tangible, intangible, Natural Resources 
    Intangible Exs-  Intellectual property, goodwill, patents, copyrights, trademarks, etc.

    original worth, depreciation amount, revaluation and disposable value of assets in question.
    """
    def __init__(self, id, name, acquisDate, lifeSpan, valueAtCost):
        self.id = id
        self.name = name
        self.acquisDate = acquisDate
        self.lifeSpan = lifeSpan
        self.assetValue = assetValue

    def __repr__(self):
        return '<Asset "{}" "{}">'.format(self.id, self.name)

class NCAsset(Asset): 

    def __init__(self, accumDep, depType, disposalAmt ):
        super().__init__()
        
        """ DepType - straight line method, double declining, units of production, sum of years digits
        assetCost- the current value of the asset - Depreciation is applied on a continual basis so
        each year it is subtracted from the previous year value. 
        """

        """
        Prob do this decision in the route and not class 
        def depreciationCalc(self, depType, assetName,assetCost):
            if depType == "Straight-Line Method": 
                dep_expense = straightLineDep(assetCost, salvageVal, lifeSpan)
            elif depType == "Double Decline Method":
                dep_expense = DDMethod()
            elif depType == "Units of Production":
                dep_expense = UnitsOfProd()
            elif depType = "Sum of Years Digits": 
                dep_expense = SumYearDigits()

            assetCost -= dep_expense
        """

        def straightLineDep(self, assetCost, salvageVal, lifeSpan):
            return (assetCost - salvageVal)/lifeSpan
        
        def DDMethod(self,assetCost,lifeSpan):
            dep_rate = (1/lifeSpan)*2
            return assetCost*dep_rate

        def UnitsOfProd(self, unitsProduced, lifeSpanInUnits, assetCost, salvageVal):
            dep_expense = (unitsProduced / lifeSpanInUnits) * (assetCost - salvageVal)
            return dep_expense

        def SumYearDigits(self):
            pass
        
class CAsset(Asset): 
    def ___init__(self):
        super().__init__() 
