import unittest
from easy_1 import longestCommonPrefix

class TestStringMethods(unittest.TestCase):

    def test_empty(self):
        s = [""]
        self.assertEqual(longestCommonPrefix(s), "")
   
    def test_str1(self):
        s = ["aa", "ab"]
        self.assertEqual(longestCommonPrefix(s), "a")
        
    def test_str2(self):
        s = ["aa", "bb"]
        self.assertEqual(longestCommonPrefix(s), "")
        
    def test_str3(self):
        s = ["aa", "aa"]
        self.assertEqual(longestCommonPrefix(s), "aa")

    def test_str4(self):
        s = ["aa", "aab", "aac", "aad"]
        self.assertEqual(longestCommonPrefix(s), "aa")

if __name__ == '__main__':
    unittest.main()