from app import db 
#from app.model.auth import Busines

class Website_details(db.Model):
    __tablename__ = 'websiteDetails'
    
    section_detail = db.Column(db.String(10), primary_key=True, unique=True) 
    sec_header = db.Column(db.String(50)) 
    sec_message = db.Column(db.String(50))

    def __init__(self, section_detail, sec_header, sec_message): 
        self.section_detail = section_detail
        self.sec_header = sec_header
        self.sec_message = sec_message

    def __repr__(self):
        return 'Website Details {} {} {}'.format(self.section_detail, self.sec_header, self.sec_message)
    

class Website_drag(db.Model):
    __tablename__ = 'websiteDrag'

    sectionID = db.Column(db.Integer, primary_key=True, unique=True, default = 0)
    positionID = db.Column(db.String(50)) 
    sectionName = db.Column(db.String(50)) 
    section_detail = db.Column(db.ForeignKey('websiteDetails.section_detail', ondelete='CASCADE', onupdate='CASCADE'))
    
    def __init__(self,  sectionID, positionID, sectionName, section_detail):
        self.sectionID = sectionID
        self.positionID = positionID
        self.sectionName = sectionName
        self.section_detail = section_detail

    def __repr__(self):
        return 'Website Sections {} {} {}'.format(self.sectionID, self.positionID, self.sectionName, self.section_detail)