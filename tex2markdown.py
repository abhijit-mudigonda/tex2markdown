#!/usr/bin/env python

import sys
import re
from operator import itemgetter
from typing import Any, Dict, List, Tuple

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


    starts = zip(starts, [0] * len(starts))
    ends = zip(ends, [1] * len(ends))

    delimiters = sorted(starts + ends, key=itemgetter(0))
    
    begin_stack = []
    paired_delimiters = []
    for (x,y) in delimiters:
        if y == 0:
            begin_stack.append(x)
        else:
            paired_delimiters.append((begin_stack.pop(), x))

    return paired_delimiters

def tex2markdown(input_text: str) -> str:
    """
        input_text: A LaTeX string
        returns: a markdown-compatible string
    """

    tex_contents = replace_special_chars(tex_contents)
    tex_contents = replace_text_modifiers(tex_contents)
    
    env_starts = [thm.start() for thm in re.finditer(r'\\begin{', tex_contents)]
    env_ends = [thm.end() for thm in re.finditer(r'\\end{', tex_contents)]
    pair_delimiters(env_starts, env_ends)
    thmcounter = 0
    for (start_idx,end_idx) in envs:
        env_type = tex_contents[start_idx+len("\\begin{"):end_idx].split('}')[0]
        begin_length = len("\\begin{}") + len(env_type)
        end_length = len("\\end{}") + len(env_type)
        env_content = tex_contents[start_idx+begin_length:end_idx-end_length].strip()

        tex_contents = tex_contents[:start_idx] + replace_environment(env_type, env_content) + tex_contents[end_idx:]
    return tex_contents

