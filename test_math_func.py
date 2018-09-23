# -*- coding: utf-8 -*-

# @Author  : xwlan
# @Time    : 2018/9/22 14:07

import unittest
from math_func import *
from socket_util import *

class TestMathFunc(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print "setUpClass ..."
        cls._conn = SocketUtil()

    def setUp(self):
        print "start test {0}...".format(self._testMethodName)

    def test_add(self):
        self.assertEqual(3, add(1, 2))

    def test_minus(self):
        self.assertEqual(10, minus(20, 10))

    def test_multi(self):
        self.assertEqual(4, multi(2, 2))

    def test_divide(self):
        self.assertEqual(3, divide(7, 2))

    def tearDown(self):
        print "finish test."

    @classmethod
    def tearDownClass(cls):
        print "tearDownClass ..."
        cls._conn.close_sock()


if __name__ == "__main__":
    unittest.main(verbosity=2)




















