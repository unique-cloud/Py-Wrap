import example
import unittest

class TestSwig(unittest.TestCase):
    
    def test_func(self):
        self.assertEqual(1, example.my_mod(7,3))
        self.assertEqual(120, example.fact(5))

if __name__ == '__main__':
    unittest.main()
