import pytest
from app import init_app, db
from datetime import datetime
from app.model import auth


@pytest.fixture(scope='module')
def new_business_owner():
    print("-------------Setup---------------")
    business = auth.Busines("Joh1", "John Doe Bakery", datetime.now())
    user = auth.User('1', 'John', 'Doe' , '1723 Iron Bauxite Place, JA', '876-555-9028')
    usercred = auth.UserCredential('1', 'Pan1', True, 'johndoe@gmail.com', 'doe123', )
    yield [business, user, usercred]
    print("-------------Tear Down---------------")


@pytest.fixture(scope='module')
def test_client():
    flask_app = init_app('flask_test.cfg')

    # Create a test client using the Flask application configured for testing
    with flask_app.test_client() as testing_client:
        # Establish an application context
        with flask_app.app_context():
            yield testing_client  # this is where the testing happens!


@pytest.fixture(scope='module')
def init_database(test_client):
    # Create the database and the database table
    db.create_all()

    # Insert user data
    # User 1 
    u1_business = auth.Busines("Joh1", "John Doe Bakery", datetime.now())
    user_1 = auth.User('1', 'John', 'Doe' , '1723 Iron Bauxite Place, JA', '876-555-9028')
    usercred_1 = auth.UserCredential('1', 'Pan1', True, 'johndoe@gmail.com', 'doe123', )
    db.session.add(u1_business)
    db.session.add(user_1)
    db.session.add(usercred_1)

    # User 1 
    u1_business = auth.Busines("Pan2", "Peter Pan Shoes", datetime.now())
    user_1 = auth.User('2', 'Peter', 'Pan' , '1723 Iron Magnesium Silver, JA', '876-554-9328')
    usercred_1 = auth.UserCredential('2', 'Pan1', True, 'peterpan@gmail.com', 'pan123', )
    db.session.add(u1_business)
    db.session.add(user_1)
    db.session.add(usercred_1)

    # Commit the changes for the users
    db.session.commit()

    yield  # this is where the testing happens!

    db.drop_all()


@pytest.fixture(scope='function')
def login_default_user(test_client):
    test_client.post('/login',
                     data=dict(email='patkennedy79@gmail.com', password='FlaskIsAwesome'),
                     follow_redirects=True)

    yield  # this is where the testing happens!

    test_client.get('/logout', follow_redirects=True)
