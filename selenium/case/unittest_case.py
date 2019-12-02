#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
class FirstCase01(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("所有的case执行前的前置")

    @classmethod
    def tearDownClass(cls):
        print("所有的case执行后的后置")

    def setUp(self):
        print("这是case的前置条件")

    def tearDown(self):
        print("这是case的后置条件")

    def testfirst01(self):
        print("第一个case")
   # @unittest.skip("不执行第2条")
    def testfirst02(self):
        print("第二个case")

    def testfirst03(self):
        print("第三个case")

if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(FirstCase01('testfirst01'))
    suite.addTest(FirstCase01('testfirst02'))
    suite.addTest(FirstCase01('testfirst03'))
    unittest.TextTestRunner().run(suite)
