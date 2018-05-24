#!/usr/bin/env python

import unittest
from replaceEnvironments import replaceEnvironments
from typing import Any, Dict, List, Tuple

class replaceEnvironments_test(unittest.TestCase): 
    def boxString_test(self):
        test_env = {
                "env_type": "example",
                "env_name": "superdupercoroloposition",
                "thm_counter": 4,
                "thm_txt": "Converting LaTeX to Markdown is NP-Hard",
                "test_output": "{% include exbox.html thmname='superdupercoroloposition' thmnum=4 thmtxt='Converting LaTeX to Markdown is NP-Hard' %}"
                }
        self.assertEqual(replaceEnvironments.boxString(test_env["env_type"], test_env["env_name"], test_env["thm_counter"], test_env["thm_txt"]), test_env["test_output"])
        
    def itemize_test(self):
        test_input = " \
        \\begin{itemize} \n \
            \item maka \n \
            \item soul \n \
            \item medusa \n \
            \item kid \n \
        \\end{itemize}"

        test_output = " \
            - maka \n \
            - soul \n \
            - medusa \n \
            - kid \n \
            "

        self.assertEqual(replaceEnvironments.replaceEnvironments("itemize", test_input), test_output)






