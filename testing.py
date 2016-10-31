import unittest
import os
import requests


from pe import add, get, delete


class MyTestCase(unittest.TestCase):

    def setUp(self):
        print ("setup")
        r = requests.post("http:127.0.0.1:5000/api/users/add?user_name=bavly")
    def testAdd(self):
        print(" - run testAdd")
        #self.assertEqual(adding(1,2),3,"unexpected addition result!")
        self.assertTrue(os.path.isfile("bavly"),"Error, file bavly is not found")
    def testGet(self):
        print(" - run testGet")

    def testDelete(self):
        print(" - run testDelete")

    def tearDown(self):
        print("teardown")