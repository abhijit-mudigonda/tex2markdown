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

    def getEnvs(input_text: str) -> List[Tuple[int, int]]:
        """
            input_text: LaTeX text
            output: A list of pairs of indices (index of start of \begin  
            and index of end of \end) of environments
        """
        skip_envs = [
                "align",
                ]

        env_starts = [thm.start() for thm in re.finditer(r'\\begin{', input_text)]
        env_ends = [thm.end() for thm in re.finditer(r'\\end{', input_text)]
        envs = tex2markdown.pairDelimiters(env_starts, env_ends)

        for start_idx, end_idx in envs: 
            env_type = input_text[start_idx+len("\\begin{"):end_idx].split('}')[0]
            if env_type in skip_envs:
                envs.remove((start_idx, end_idx))

        return envs

        
    def tex2markdown(tex_contents: str) -> str:
        """
            input_text: A LaTeX string
            returns: a markdown-compatible string
        """


        tex_contents = replaceSpecialChars.replaceSpecialChars(tex_contents)
        tex_contents = replaceTextModifiers.replaceTextModifiers(tex_contents)
        thmcounter = 0


        #This block is presently really inefficient, since it works with each 
        #environment and recomputes the indices every time (because the changes
        #will usually change the indices). Probably the right way to do this is
        #to compute all the changes and then stitch it all together, but there 
        #seemed to be some annoyances with nested environments and I got bored
        #of coding

        output = tex_contents
        envs = tex2markdown.getEnvs(output)
        while len(envs) != 0:
            start_idx, end_idx = envs[0]
            env_type = output[start_idx+len("\\begin{"):end_idx].split('}')[0]
            begin_length = len("\\begin{}") + len(env_type)
            end_length = len("\\end{}") + len(env_type)
            env_content = output[start_idx+begin_length:end_idx-len("\\end{")]
            environment_markdown = replaceEnvironments.replaceEnvironments(env_type, env_content, thmcounter)
            output = output[0:start_idx]+environment_markdown+output[end_idx+len(env_type)+1:]
            envs = tex2markdown.getEnvs(output)
        return output


if __name__ == "__main__":
    input_text = sys.stdin.read()
    sys.stdout.write(tex2markdown.tex2markdown(input_text))

