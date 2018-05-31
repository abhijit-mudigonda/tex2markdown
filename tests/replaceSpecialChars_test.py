#!/usr/bin/env python

import unittest
from replaceSpecialChars import replaceSpecialChars
from typing import Any, Dict, List, Tuple

class replaceSpecialChars_test(unittest.TestCase): 
    def replaceSpecialChars_test(self):
        input_1 = "We know that $||A^*|| = ||A||$, and also that $$||A^*|| = ||A||$$"
        output_1 = "We know that $||A^*|| = ||A||$, and also that $$\|\|A^\*\|\| = \|\|A\|\|$$"

        self.assertEqual(replaceSpecialChars.replaceSpecialChars(input_1), output_1)

