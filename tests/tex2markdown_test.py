#!/usr/bin/env python

import unittest
from tex2markdown import tex2markdown
from typing import Any, Dict, List, Tuple

class tex2markdown_test(unittest.TestCase):
    def pairDelimiters_test(self):
        starts_test = [1, 4, 5, 8]
        ends_test = [2, 6, 7, 10]
        output_test = [(1, 2), (5, 6), (4, 7), (8, 10)]

        self.assertEqual(tex2markdown.pairDelimiters(starts_test, ends_test), output_test)




    



        




