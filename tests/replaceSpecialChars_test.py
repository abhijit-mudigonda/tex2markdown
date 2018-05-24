#!/usr/bin/env python

import unittest
from replaceSpecialChars import replaceSpecialChars
from typing import Any, Dict, List, Tuple

class replaceSpecialChars_test(unittest.TestCase): 
    def replaceSpecialChars_test(self):
        test_input = "We know that $||A^*|| = ||A||$, and also that $$(A^*)^* = A$$"
        test_output = "We know that $\|\|A^\*\|\| = \|\|A\|\|$, and also that $$(A^\*)^\* = A$$"

        print("Input was", test_input)
        print("Output was", test_output)
        self.assertEqual(replaceSpecialChars.replaceSpecialChars(test_input), test_output)

