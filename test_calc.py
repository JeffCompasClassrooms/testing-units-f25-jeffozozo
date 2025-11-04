from calc import Calc
import pytest

my_calc = Calc()

def test_the_calc():

	assert my_calc.add(0,0) == 0
	assert my_calc.add(1,1) == 2
	assert my_calc.add(-1,1) == 0

	assert my_calc.mul(0,0) == 0
	assert my_calc.mul(1,1) == 1
	assert my_calc.mul(-1,1) == -1

	with pytest.raises(ZeroDivisionError):
		my_calc.div(1,0)

	assert my_calc.div(10,5) == 2
	assert my_calc.div(-1,-1) == 1



