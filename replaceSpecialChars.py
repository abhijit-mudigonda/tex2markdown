#!/usr/bin/env python

import re
from typing import Any, Dict, List, Tuple

class replaceSpecialChars:
    def replaceSpecialChars(
            input_text: str
            ) -> str: 
        """
            input_text: Mostly LaTeX text
            output: Escapes * and | appropriately for markdown
        """
        #output = re.sub('\*', '\\\*', input_text)
        output = re.sub('\|', '\\|', output)

        return output
