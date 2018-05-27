#Until I can figure out how to deal with weird
#escapes


sed 's/\\textbf/\\strong/g' | sed 's/\\textit/\\emph/g' | sed 's/\\begin{align}/\n$$\\begin{align}/g' | sed 's/\\end{align}/\\end{align}$$\n/g'
