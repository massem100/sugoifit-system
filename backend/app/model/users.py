# from . import user
from werkzeug.security import generate_password_hash
from datetime import date
from flask_login._compat import unicode
from datetime import datetime
from flask_login import UserMixin



class User(UserMixin):
            
    def __init__(self,id, username, f_name, l_name, gender, dateOfBirth, hireDate):
        self.id= id
        self.f_name = f_name
        self.username = username
        self.l_name = l_name
        self.gender = gender
        self.dateOfBirth = dateOfBirth
        
       
        
    def test(self, set):
        return set

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User "{}">'.format(self.id)
    
class Owner(User, UserMixin): 

    def __init__(self, id, role, username):
        self.id = id
        self.username = username
        self.role = role


class Employee(User):
    def __init__(self, id, hireDate):
        self.id = id
        self.hireDate = hireDate


if __name__ == '__main__':    
    Pat = User('0019', 'Patty', 'Pat', 'Lazarus', 'female' )
    Bob = Owner('high','bob')
    print (Bob)
    print (Pat)
    result = Bob.test('child working')
    print (result)

    result = Pat.test('parent working')
    print (result)
    print (Bob.is_authenticated)