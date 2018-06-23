import cmake_example as m
import unittest

class TestPybind11(unittest.TestCase):
    
    def test_func(self):
        self.assertEqual(m.__version__, '0.0.1')
        self.assertEqual(m.add(1, 2), 3)
        self.assertEqual(m.subtract(1, 2), -3)

if __name__ == '__main__':
    unittest.main()
