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

        env_names = {
                "theorem": "Theorem",
                "corollary": "Corollary",
                "lemma": "Lemma",
                "claim": "Claim",
                "proposition": "Proposition",
                "conjecture": "Conjecture",
                "definition": "Definition",
                "example": "Example",
                "exercise": "Exercise",
                "problem": "Problem",
                "question": "Question",
                "remark": "Remark",
                }


        assert (box_type in box_files), "Invalid box type"
        box_string = "{{% include {0} thmname='{1}' thmnum={2} thmtxt=\"{3}\" %}} <br \>".format(
                box_files[box_type], 
                env_names[env_name],
                thm_counter,
                thm_txt
                )
        return box_string


    def replaceEnvironments(
            env_type: str,
            thmcounter: int,
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
                "problem",
                "question",
                "remark",
                ]

        if env_type in thmbox_envs:
            thmcounter += 1
            input_text = input_text.strip()
            env_output = replaceEnvironments.boxString("theorem", env_type, thmcounter, input_text)
        elif env_type in defbox_envs:
            input_text = input_text.strip()
            thmcounter += 1
            env_output = replaceEnvironments.boxString("definition", env_type, thmcounter, input_text)
        elif env_type in exbox_envs:
            input_text = input_text.strip()
            thmcounter += 1
            env_output = replaceEnvironments.boxString("example", env_type, thmcounter, input_text)
        elif env_type == "itemize":
            #Bullet points
            env_output = re.sub(r'\\item', r'-', input_text)

        elif env_type == "enumerate":
            #TODO need to make this number each thing rather than bullet points
            env_output = re.sub(r'\\item', r'-', input_text)

        elif env_type == "proof":
            env_output = "*Proof*: "+input_text

        else:
            #TODO warn the user that they might've made a mistake or
            #be missing desired functionality
            print("I don't recognize the environment", env_type)
            env_output = input_text

        return env_output
        


