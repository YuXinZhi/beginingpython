import unittest,my_math1

def product(x,y):
    return x*y

class ProductTestCase(unittest.TestCase):

    def testIntegers(self):
        for x in range(-10,10):
            for y in range(-10,10):
                p = my_math1.product(x,y)
                self.assertTrue(p==x*y,'Integer mutiplication failed')

    def testFloats(self):
        for x in range(-10,10):
            for y in range(-10,10):
                x = x/10.0
                y = y/10.0
                p = my_math1.product(x,y)
                self.assertTrue(p == x * y, 'Float mutiplication failed')

if __name__ == '__main__':
    unittest.main()