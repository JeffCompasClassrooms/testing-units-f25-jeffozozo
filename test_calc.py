from calc import Calc
import pytest

my_calc = Calc()

def test_add_works_with_good_numbers():

	assert my_calc.add(0,0) == 0
	assert my_calc.add(1,1) == 2
	assert my_calc.add(-1,1) == 0

def test_mult_works_with_good_numbers():
	assert my_calc.mul(0,0) == 0
	assert my_calc.mul(1,1) == 1
	assert my_calc.mul(-1,1) == -1

def test_div_by_zero_throws_exception():    
	with pytest.raises(ZeroDivisionError):
		my_calc.div(1,0)

def test_div_works_with_good_numbers():    
	assert my_calc.div(10,5) == 2
	assert my_calc.div(-1,-1) == 1

def test_it_fails():
    assert 1 == 0
