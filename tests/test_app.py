from app import index
from app import sub
from app import mul
from app import power
from app import exp

def test_index():
    assert index() == '5'
def test_sub():
    assert sub() == '-1'
def test_mul():
    assert mul() == '6'
def test_power():
    assert power() == '8'
def test_exp():
    assert exp() == '22'

#from app import index


#def test_index():
#    assert index() != "Hello world!"

