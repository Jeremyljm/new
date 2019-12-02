#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
class FirstCase02(unittest.TestCase):

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

    def testfirst001(self):
        print("第0一个case")
    @unittest.skip("不执行第2条")
    def testfirst002(self):
        print("第0二个case")

    def testfirst003(self):
        print("第0三个case")

if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(FirstCase02('testfirst001'))
    suite.addTest(FirstCase02('testfirst002'))
    suite.addTest(FirstCase02('testfirst003'))
    unittest.TextTestRunner().run(suite)