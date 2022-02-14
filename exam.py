"Degree function"
import unittest
import math

MORE90 = "More 90 degree"
LESS90 = "Less 90 degree"
INV = "invalid input"

def results(x):
    "results"
    print("input:",x)
    result = ""
    if (type(x) == int or type(x) == float):
        num = math.degrees(x)
        if num> 90:
            result = MORE90
        else:
            result = LESS90
    else:
        result = INV
    print(result,"\n")
    return result


class Test(unittest.TestCase):
    "testcase"
    def test_more90(self):
        "more than 90 degree"
        self.assertEqual(results(2.3), MORE90)

    def test_less90(self):
        "more less 90 degree"
        self.assertEqual(results(1.2), LESS90)

    def test_invalid(self):
        "invalid input"
        self.assertEqual(results("abc"), INV)

if __name__ == '__main__':
    unittest.main()
