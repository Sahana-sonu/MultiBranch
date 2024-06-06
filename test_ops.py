from ops import *

def test_add():
    if add(2, 3) != 5:
        print("test_add failed: add(2, 3) did not return 5")

def test_subtract():
    if subtract(2, 3) != -1:
        print("test_subtract failed: subtract(2, 3) did not return -1")

def test_multiply():
    if multiply(2, 3) != 6:
        print("test_multiply failed: multiply(2, 3) did not return 6")

def test_divide():
    if divide(10, 5) != 2:
        print("test_divide failed: divide(10, 5) did not return 2")
