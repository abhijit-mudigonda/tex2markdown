#!/usr/bin/env python

import sys
import re, string

if __name__ == "__main__": 
    
    #Reads the entire input TeX file as a single string. Not great, but 
    #good enough for now
    #TODO is there a less bad way?  
    tex_contents = sys.stdin.read()

    #Special characters that need to be doubly escaped in markdown (so markdown
    #know that they aren't supposed to make tables or bold text or w/e)
    special_chars = [
            '*',
            '|',
            ]

    for char in special_chars: 
        #Because markdown and regex are weird in their own distinct ways
        c = "\\" + char
        d = "\\\\" + c
        tex_contents = re.sub(c, d, tex_contents)

    tex_contents = re.sub(r'\*', r'\\\\\*', tex_contents)
    tex_contents = re.sub(r'|', r'\\|', tex_contents)

    #Replacing sections and subsections with markdown headers
    sectioning_dict = {
            r'\\section{(.+?)}': '## \\1',
            r'\\subsection{(.+?)}': '# \\1',
            }

    for key,value in sectioning_dict.items():
        tex_contents = re.sub(key, value, tex_contents)

    #Replacing in-text formatting like bolds and italics
    text_format_dict = {
            r'\\textbf{(.+?)}': '**\\1**',
            r'\\textit{(.+?)}': '*\\1*',
            }

    for key,value in text_format_dict.items():
        tex_contents = re.sub('{}'.format(key), r'{}'.format(value), tex_contents)

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

    #Basically, we want to find every instance of a begin-end block, and decide
    #what to do with it. For align, this is nothing. For itemize, and enumerate,
    #make the items lists. For 

    begin_length = len("\\begin{")
    end_length = len("\\end{") 

    env_begins = [(thm.start(), 0) for thm in re.finditer(r'\\begin{', tex_contents)]
    env_ends = [(thm.end(), 1) for thm in re.finditer(r'\\end{', tex_contents)]

    assert (len(env_begins) == len(env_ends)), "Numbers of \\begin and \\end environments inequal"
    env_endpoints = sorted(env_begins + env_ends)

    begin_stack = []
    envs = []
    for (x,y) in env_endpoints:
        if y == 0:
            begin_stack.append(x)
        else:
            envs.append((begin_stack.pop(), x))

    #cool now we have a paired list of envs
    thmcounter = 0
    for (a,b) in envs:
        env_type = tex_contents[a+len("\\begin{"):b].split('}')[0]

        begin_length = len("\\begin{}") + len(env_type)
        end_length = len("\\end{}") + len(env_type)

        env_content = tex_contents[a+begin_length:b].strip()

        if env_type in thmbox_envs:
            thmcounter += 1
            env_output = "{{% include {0} thmnum={1} thmtxt=\"{2}\" %}}".format("thmbox.html", thmcounter, env_content)

        elif env_type in defbox_envs:
            thmcounter += 1
            thm_txt = tex_contents[a+begin_length:b-end_length]
            env_output = "{{% include {0} thmnum={1} thmtxt=\"{2}\" %}}".format("defbox.html", thmcounter, env_content)

        elif env_type in exbox_envs:
            thmcounter += 1
            thm_txt = tex_contents[a+begin_length:b-end_length]
            env_output = "{{% include {0} thmnum={1} thmtxt=\"{2}\" %}}".format("defbox.html", thmcounter, env_content)

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
            tex_contents = tex_contents[:a] + env_output + tex_contents[b+end_length:]

        elif env_type == "proof":
            env_output = "*Proof*:".append(env_content)
            tex_contents = tex_contents[:a] + env_output + tex_contents[b+end_length:]

        else:
            #Envtype isn't a known type
            #Remove the environment delimiters and 

        tex_contents = tex_contents[:a] + env_output + tex_contents[b+end_length:]

        sys.stdout.write(tex_contents)
