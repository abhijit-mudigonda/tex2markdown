#!/usr/bin/env python

import unittest
from replaceTextModifiers import replaceTextModifiers
from typing import Any, Dict, List, Tuple

class replaceTextModifiers_test(unittest.TestCase): 
    def replaceTextModifiers_test(self):
        test_input_1 = "\section{Subsections} \n \strong{emphasis} can be hard sometimes"
        test_input_2 = "\subsection{Sections} \n \emph{And} sometimes it's even harder"
        test_output_1 = "## Subsections \n **emphasis** can be hard sometimes"
        test_output_2 = "# Sections \n *And* sometimes it's even harder"

        self.assertEqual(replaceTextModifiers.replaceTextModifiers(test_input_1), test_output_1)
        self.assertEqual(replaceTextModifiers.replaceTextModifiers(test_input_2), test_output_2)



