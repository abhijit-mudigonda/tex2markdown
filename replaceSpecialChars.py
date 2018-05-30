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

        input_text = input_text.split()
        for idx, char in enumerate(input_text):
            if char == '$':
                #Current char is a $
                if last_char == '$':
                    #At a $ and the last char was also $
                    doubledollar_mode = not doubledollar_mode
            else:
                if last_char == '$' and doubledollar_mode is False:
                    #Current char isn't a $ and there was a single $ before current char
                    singledollar_mode = not singledollar_mode
                elif char in specialchars:
                    if singledollar_mode is True:
                        input_text[idx] = "\\"+char
                    elif doubledollar_mode is True:
                        pass
                    else:
                        pass
                elif char == '|':
                    print("Sadness")
                    if singledollar_mode is True:
                        input_text[idx] = r'\|'
                    elif doubledollar_mode is True:
                        pass
                    else:
                        pass
                elif char == '*':
                    print("Sadness")
                    if singledollar_mode is True:
                        input_text[idx] = r'\*'
                    elif doubledollar_mode is True:
                        pass
                    else:
                        pass
                else:
                    pass

            assert (not (singledollar_mode and doubledollar_mode))
            last_char = char

            return ''.join(input_text)



                    



        
