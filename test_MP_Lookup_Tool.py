import unittest
from MP_Lookup_Tool import fetch_data

class Testlookup(unittest.TestCase):
    
    def test_int(self):
        self.assertEqual(fetch_data(20), 20)
        
    def test_float(self):
        with self.assertRaises(TypeError):
            fetch_data(20.5)
    
    def test_str(self):
        with self.assertRaises(TypeError):
            fetch_data('apple')