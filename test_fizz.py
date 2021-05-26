import unittest
import fizz

class TestCase(unittest.TestCase):
    def testOne(self):
        self.assertEqual(fizz.fizzBuzz(1),1)

if __name__ == '__main__':
    unittest.main()
