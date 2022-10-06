import unittest

from githubapi import githubapi

class Testgithubapi(unittest.TestCase):
    def testGithub(self):
        self.assertEqual(githubapi('?'), False)
    def testGithub2(self):
        self.assertEqual(githubapi('NehharShah'), True)

if __name__ == '__main__':
    print("Test cases are running")
    unittest.main()