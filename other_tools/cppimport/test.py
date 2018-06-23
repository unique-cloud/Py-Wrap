# -*- coding: utf-8 -*-

import cppimport.import_hook
import example
import unittest

class TestExample(unittest.TestCase):
    
    def test_square(self):
        self.assertEqual(25, example.square(5))
        self.assertEqual(20, example.square(2))

if __name__ == '__main__':
    unittest.main()

