#!/usr/bin/env python

import sys, re
from operator import itemgetter
from typing import Any, Dict, List, Tuple

from replaceEnvironments import replaceEnvironments
from replaceSpecialChars import replaceSpecialChars
from replaceTextModifiers import replaceTextModifiers

class tex2markdown:
    def pairDelimiters(
            starts: List[int], 
            ends: List[int]
            ) -> List[Tuple[int, int]]:

        """
            starts: a sorted list of positions where starting delimiters occur
            ends: a sorted list of positions where starting delimiters occur
            returns: a list of (start, end) pairs, corresponding to delimiters
                that are paired
        """
        
        assert (len(starts) == len(ends)), "Numbers of start \
        and end delimiters inequal"


        starts = [x for x in zip(starts, [0] * len(starts))]
        ends = [x for x in zip(ends, [1] * len(ends))]

        delimiters = sorted(starts + ends, key=itemgetter(0))
        
        begin_stack = []
        paired_delimiters = []
        for (x,y) in delimiters:
            if y == 0:
                begin_stack.append(x)
            else:
                paired_delimiters.append((begin_stack.pop(), x))

        return paired_delimiters

    def getEnvs(input_text: str) -> List[int, int]:
        """
            input_text: LaTeX text
            output: A list of pairs of indices (index of start of \begin  
            and index of end of \end) of environments
        """
        env_starts = [thm.start() for thm in re.finditer(r'\\begin{', input_text)]
        env_ends = [thm.end() for thm in re.finditer(r'\\end{', input_text)]
        envs = tex2markdown.pairDelimiters(env_starts, env_ends)
        return envs
 
    def tex2markdown(tex_contents: str) -> str:
        """
            input_text: A LaTeX string
            returns: a markdown-compatible string
        """

        tex_contents = replaceSpecialChars.replaceSpecialChars(tex_contents)
        tex_contents = replaceTextModifiers.replaceTextModifiers(tex_contents)
        thmcounter = 0
        envs = getEnvs(tex_contents)

        #Initialize output to the portion up until the first 
        #environment, which is (hopefully) all done
        output = tex_contents[0:envs[0][0]]

        for (start_idx,end_idx) in envs:
            env_type = tex_contents[start_idx+len("\\begin{"):end_idx].split('}')[0]
            print("Processing an environment with type", env_type)
            begin_length = len("\\begin{}") + len(env_type)
            end_length = len("\\end{}") + len(env_type)
            env_content = tex_contents[start_idx+begin_length:end_idx-len("\\end{")].strip()
            environment_markdown = replaceEnvironments.replaceEnvironments(env_type, thmcounter, env_content)
            output += environment_markdown 
        #TODO need to put it back together correctly! This means... 
        #at each point, 


if __name__ == "__main__":
    input_text = sys.stdin.read()
    sys.stdout.write(tex2markdown.tex2markdown(input_text))

