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


            In particular, * and | don't need to be escaped in
            $$ -- $$ mode but need to be escaped in $ -- $ (inline)
            mode
        """

        dollar_count = 0
        last_char = ''

        singledollar_mode = False
        doubledollar_mode = False

        specialchars = [
                r'*',
                r'|'
                ]

        char_list = list(input_text)
        for idx, char in enumerate(char_list):
            if char == '$' and last_char == '$':
                #At a $ and the last char was also $
                doubledollar_mode = not doubledollar_mode
            else:
                if last_char == '$' and doubledollar_mode is False:
                    #Current char isn't a $ and there was a single $ before current char
                    singledollar_mode = not singledollar_mode
                if char in specialchars and doubledollar_mode is True:
                    char_list[idx] = "\\"+char

            assert (not (singledollar_mode and doubledollar_mode))
            last_char = char

        return ''.join(char_list)



                    



        
