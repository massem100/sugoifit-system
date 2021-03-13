
class Asset: 

    def __init__(self, id, name, acquisDate, lifeSpan, assetValue):
        self.id = id
        self.name = name
        self.acquisDate = acquisDate
        self.lifeSpan = lifeSpan
        self.assetValue = assetValue

    def __repr__(self):
        return '<Asset "{}" "{}">'.format(self.id, self.name)