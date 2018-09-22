# -*- coding: utf-8 -*-

# @Author  : xwlan
# @Time    : 2018/9/22 22:09

import unittest
from test_math_func import *
from test_math_func2 import *
from test_math_func3 import *

####################################################################################################################
# 添加单个testCase
####################################################################################################################
tsuit = unittest.TestSuite()
tsuit.addTest(TestMathFunc("test_add"))
runner = unittest.TextTestRunner(verbosity=2)
runner.run(tsuit)


####################################################################################################################
# 添加testCase列表
####################################################################################################################
tsuit = unittest.TestSuite()
cases = [TestMathFunc("test_add"), TestMathFunc("test_minus"), TestMathFunc("test_multi"), TestMathFunc("test_divide")]
tsuit.addTests(cases)

runner = unittest.TextTestRunner(verbosity=2)
runner.run(tsuit)


####################################################################################################################
#
####################################################################################################################
tsuit = unittest.TestSuite()
tsuit.addTests(unittest.TestLoader().loadTestsFromName("test_math_func.TestMathFunc"))
runner = unittest.TextTestRunner( verbosity=2)
runner.run(tsuit)


####################################################################################################################
#
####################################################################################################################
tsuit = unittest.TestSuite()
tsuit.addTests(unittest.TestLoader().loadTestsFromNames(["test_math_func.TestMathFunc", "test_math_func2.TestMathFunc2", "test_math_func3.TestMathFunc3"]))
runner = unittest.TextTestRunner(verbosity=2)
runner.run(tsuit)