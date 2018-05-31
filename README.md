This is designed for use on a github-pages blog using Jekyll. Math is rendered with MathJax, and I have some divs in `_includes` that make theorem boxes. 
Unless you're also forking those files, this won't work for you out of the box. 


To use, pipe your file first through `./hack.sh` and then through the python script, and you should get working markdown! You might need to unindent some lists if your Markdown automatically turns indented blocks into code blocks. 
