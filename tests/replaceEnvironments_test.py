#!/usr/bin/env python

import unittest
from replaceEnvironments import replaceEnvironments
from typing import Any, Dict, List, Tuple

class replaceEnvironments_test(unittest.TestCase): 
    def boxString_test(self):
        test_env = {
                "env_type": "example",
                "env_name": "proposition",
                "thm_counter": 4,
                "thm_txt": "Converting LaTeX to Markdown is NP-Hard",
                "test_output": "{% include exbox.html thmname='Proposition' thmnum=4 thmtxt=\"Converting LaTeX to Markdown is NP-Hard\" %} <br />"
                }
        self.assertEqual(replaceEnvironments.boxString(test_env["env_type"], test_env["env_name"], test_env["thm_txt"], test_env["thm_counter"]), test_env["test_output"])
        
    def itemize_test(self):
        test_input = "\item maka\n \item soul\n"
        test_output = "- maka\n - soul\n"

        self.assertEqual(replaceEnvironments.replaceEnvironments("itemize", test_input), test_output)
    """
    def align_test(self):
        test_input = "x^2 + 5 & = x*x + 5 \\\\ \n & = x*x + 3 + 2"
        test_output = "x^2 + 5 & = x*x + 5 \\\\\\\\ \n & = x*x + 3 + 2"

        self.assertEqual(replaceEnvironments.replaceEnvironments("align", test_input, 1), test_output)
    """

    def proof_test(self):
        test_input = "blah blah"
        test_output = "*Proof*: blah blah"

        self.assertEqual(replaceEnvironments.replaceEnvironments("proof", test_input), test_output)

        







