#!/usr/bin/env python

import unittest
from replaceMisc import replaceMisc
from typing import Any, Dict, List, Tuple

class replaceMisc_test(unittest.TestCase): 
    def replaceMisc_test(self):
        test_input_1 = r"\begin{align} \n x^2 & = y \\ \n & = z^3 \n \end{align}"
        test_output_1 = r"\begin{align} \n x^2 & = y \\ \n & = z^3 \n \end{align}"

        self.assertEqual(replaceMisc.replaceMisc(test_input_1), test_output_1)
        self.assertEqual(replaceMisc.replaceMisc(test_input_2), test_output_2)




