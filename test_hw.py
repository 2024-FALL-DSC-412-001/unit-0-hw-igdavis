'''





Do NOT edit this file unless told to do so by your instructor.









'''


import random

import string
import statistics
import sys

import test_utils
sys.meta_path.append(test_utils.NotebookFinder())
loaded = test_utils.NotebookLoader("./unit_0_hw.ipynb")
loaded.load_module("unit_0_hw")

import unit_0_hw


# This file is used to grade functions created in jupyter notebooks!
print(unit_0_hw.add_3(3))
def test_add_3():
    assert unit_0_hw.add_3(3) == 6

def test_add_5():
    assert unit_0_hw.add_5(4) == 9

def test_a_string():
    the_string = ''.join(random.choices(string.ascii_uppercase +
                             string.digits, k=10))
    smile_string = unit_0_hw.append_smiley_face(the_string)
    assert smile_string is not None
    assert smile_string[-3:] == " :)"

def test_average():
    list_1 = list(range(random.randint(-99, 0), random.randint(3, 99), random.randint(1, 5)))
    if(len(list_1) == 0): # Not impossible to get an empty list
        list_1 = [1, 2, 3]

    assert unit_0_hw.average(list_1) == statistics.mean(list_1)