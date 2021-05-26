import unittest
import fizz

class TestCase(unittest.TestCase):
    def testOne(self):
        self.assertEqual(fizz.fizzBuzz(1),1)

    def testTwo(self):
        self.assertEqual(fizz.fizzBuzz(3),"fizz")

    def testThree(self):
        self.assertEqual(fizz.fizzBuzz(5),"buzz")

if __name__ == '__main__':
    unittest.main()
