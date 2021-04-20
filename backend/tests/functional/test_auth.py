import pytest
# from app import add_twoN
from app import views



# print(app)



# def add_twoN(a,b): 
#     return a+b

def test_add1():
    assert add_twoN(2,5) ==7

def test_add2():
    assert add_twoN(2,5) !=7