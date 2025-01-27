import unittest
from sort import sort

class TestSort(unittest.TestCase):
    def test_standard(self):
        self.assertEqual(sort(10, 10, 10, 10), "STANDARD")
    def test_bulky(self):
        self.assertEqual(sort(100, 100, 100, 10), "SPECIAL")
    def test_heavy(self):
        self.assertEqual(sort(10, 10, 10, 20), "SPECIAL")
    def test_rejected(self):
        self.assertEqual(sort(150, 150, 150, 25), "REJECTED")

if __name__ == "__main__":
    unittest.main()