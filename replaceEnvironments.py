#!/usr/bin/env python 

import re
from typing import Any, Dict, List, Tuple

class replaceEnvironments:
    def boxString(
            box_type: str,
            env_name: str,
            thm_counter: int,
            thm_txt: str,
            ) -> str:
        """
            box_type: The type of box we want (must be in box_files)
            env_name: The name of this environment (e.g. corollary)
            thm_counter: The theorem/definition/example number
            thm_txt: The content in the box

        """

        box_files = {
                "theorem": "thmbox.html",
                "definition": "defbox.html",
                "example": "exbox.html"
                }

        assert (box_type in box_files), "Invalid box type"
        box_string = "{{% include {0} thmname='{1}' thmnum={2} thmtxt='{3}' %}}".format(
                box_files[box_type], 
                env_name,
                thm_counter,
                thm_txt
                )
        return box_string


    def replaceEnvironments(
            env_type: str,
            input_text: str,
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
            env_output = box_string("theorem", env_type, thmcounter, input_text)
        elif env_type in defbox_envs:
            thmcounter += 1
            env_output = box_string("definition", env_type, thmcounter, input_text)
        elif env_type in exbox_envs:
            thmcounter += 1
            env_output = box_string("example", env_type, thmcounter, input_text)

        elif env_type == "itemize":
            #Bullet points
            env_output = re.sub(r'\\item', r'-', input_text)
        elif env_type == "enumerate":
            #TODO need to make this number each thing rather than bullet points
            env_output = re.sub(r'\\item', r'-', input_text)

        elif env_type == "align":
            #It's a quirk of mathjax that new lines don't work in align without 
            #being in math mode
            env_output = "\n$$".append(input_text.append("$$\n"))
        elif env_type == "proof":
            env_output = "*Proof*:".append(input_text)

        else:
            #TODO warn the user that they might've made a mistake or
            #be missing desired functionality
            pass

        return env_output
        


