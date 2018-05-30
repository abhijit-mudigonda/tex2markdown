#!/usr/bin/env python

import re
from typing import Any, Dict, List, Tuple

class replaceMisc:
    def replaceMisc(
            input_text: str
            ) -> str:
        """
            input_text: Mostly LaTeX text
            output: Replaces miscellaneous things
                after all other processing has happened
        """

        output = re.sub('\\begin{align}', '\n$$\\begin{align}', input_text)
        output = re.sub('\\end{align}', '\\end{align}$$\n', output)

        return output


