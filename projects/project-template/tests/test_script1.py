# pytest projects\project-template\tests\test_script1.py

import pytest
from src import script1 as function

def test_add():
    assert function.add(1, 2) == 3

def test_subtract():
    assert function.subtract(1, 2) == -1

def test_divide():
    # Test for division by zero (returns true if ZeroDivisionError is raised)
    with pytest.raises(ZeroDivisionError, match='You cant divide by zero!'):
        assert function.divide(1, 0)

#! Test will fail if the custom message is not raised
def test_custom_message():
    with pytest.raises(ZeroDivisionError, match='You cant divide by zero!'):
        assert function.divide(1, 1)

#! Test will fail
def test_try_except():
    try:
        # Code that might raise an exception
        #assert my_function.divide(1, 0)
        my_list = [1, 2, 3]
        print(my_list[5])
    except ZeroDivisionError:
        # Code to run if a ZeroDivisionError is raised
        raise AssertionError("You can't divide by zero!")
    except Exception as e:
        # Code to run for any other type of exception
        raise AssertionError(f"An error occurred: {e}")