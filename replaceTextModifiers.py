#!/usr/bin/env python

import re
from typing import Any, Dict, List, Tuple

class replaceTextModifiers:
    def replaceTextModifiers(
            input_text: str
            ) -> str:
        """ 
            input_text: Mostly LaTeX ext
            output: Replaces LaTeX modified text like headings and 
                emphasis with appropriate markdown equivalents
        """
        text_mods = {
                r"\\section{(.+?)}": '## \\1',
                r"\\subsection{(.+?)}": '# \\1',
                r"\\strong{(.+?)}": '**\\1**',
                r"\\emph{(.+?)}": '*\\1*',
                }

        output = input_text
        for key,value in text_mods.items():
            output = re.sub(key, value, output)

        return output


