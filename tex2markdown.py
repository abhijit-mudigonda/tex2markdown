#!/usr/bin/env python

import sys
import re
from operator import itemgetter
from typing import Any, Dict, List, Tuple

def box_string(
        box_type: str,
        env_name: str,
        thm_counter: int,
        thm_txt: str,
        ) -> str
    """
        box_type: The type of box we want (must be in box_files)
        env_name: The name of this environment (e.g. corollary)
        thm_counter: The theorem/definition/example number
        thm_txt: The content in the box

    """

    box_files = {
            "theorem": "thmbox.html"
            "definition": "defbox.html"
            "example": "exbox.html"
            }

    assert (box_files.contains(box_type)), "Invalid box type"
    box_string = "{{% include {0} thmname={1} thmnum={2} thmtxt=\"{3}\" %}}".format(
            box_files[box_type], 
            env_name,
            thm_counter,
            thm_txt
            )
    return box_string

def pair_delimiters(
        starts: List[int], 
        ends: List[int]
        ) -> List[Tuple[int, int]]

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

def replace_special_chars(
        input_text: str
        ) -> str: 
    """
        input_text: Mostly LaTeX text
        output: Escapes * and | appropriately for markdown
    """
    output = re.sub(r'\*', r'\\\\\*', input_text)
    output = re.sub(r'|', r'\\|', output)

    return output

def replace_text_modifiers(
        input_text: str
        ) -> str:
    """ 
        input_text: Mostly LaTeX ext
        output: Replaces LaTeX modified text like headings and 
            emphasis with appropriate markdown equivalents
    """
    text_mods = {
            r'\\section{(.+?)}': '## \\1',
            r'\\subsection{(.+?)}': '# \\1',
            r'\\textbf{(.+?)}': '**\\1**',
            r'\\textit{(.+?)}': '*\\1*',
            }

    for key,value in text_mods.items():
       tex_contents = re.sub(key, value, tex_contents)

    return output

def replace_environments(
        env_type: str
        input_text: str
        ) -> str:
    """
        env_type: Which environment is being replaced
        input_text: Text cut from between \begin{env_type} and
            \end{env_type} (but not including the delimiters
        output: Text, where the environments have been
            replaced with markdown equivalents
    """
    #Environments that should be rendered within a red box
    thmbox_envs = [
            "theorem",
            "corollary",
            "lemma",
            "claim",
            "proposition",
            "conjecture",
            ]

    #Environments that should be rendered within a blue box
    defbox_envs = [
            "definition"
            ]


    #Environments that should be rendered within a green box
    exbox_envs = [
            "example",
            "exercise",
            ]

    if env_type in thmbox_envs:
        thmcounter += 1
        env_output = box_string("theorem", env_type, thmcounter, env_content)
    elif env_type in defbox_envs:
        thmcounter += 1
        env_output = box_string("definition", env_type, thmcounter, env_content)
    elif env_type in exbox_envs:
        thmcounter += 1
        env_output = box_string("example", env_type, thmcounter, env_content)

    elif env_type == "itemize":
        #Bullet points
        env_output = re.sub(r'\\item', r'-', env_content)
    elif env_type == "enumerate":
        #TODO need to make this number each thing rather than bullet points
        env_output = re.sub(r'\\item', r'-', env_content)

    elif env_type == "align":
        #It's a quirk of mathjax that new lines don't work in align without 
        #being in math mode
        env_output = "\n$$".append(env_content.append("$$\n"))
    elif env_type == "proof":
        env_output = "*Proof*:".append(env_content)

    else:
        #TODO warn the user that they might've made a mistake or
        #be missing desired functionality
        pass

    return env_output
    


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

