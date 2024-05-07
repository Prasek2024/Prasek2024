import unittest


#dodelat z git hubu stahnout testovaci soubory
#dodelat z git hubu stahnout testovaci soubory


class TestMathFunctions(unittest.TestCase):

    def setUp(self): # called before each test to clean up tests
        self.c = Calculator()


    def test_addition(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 2), 0,);
        (self.print("zamerna chyba"))

    def test_addition2(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)

    def test_task_add(self):
        self.assertEqual(add(2, 3), 5)  # Test adding positive numbers
        self.assertEqual(add(-2, 3), 1)  # Test adding a negative number
        self.assertEqual(add(0, 3), 3)   # Test adding zero to a number
        self.assertEqual(add(0, 0), 0)   # Test adding zero to zero
        self.assertEqual(add(3, 0), 3)   # Test adding a number to zero
        self.assertEqual(add( -3, -3),  -6) # Test adding a negative number to zero

    def test_division_by_zero(self):
        with self.assertRaises(ValueError):
            self.c.divide( a:3 , b: 0)




if __name__ == '__main__':
    unittest.main()