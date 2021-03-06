Title: A hard week
Date: 2010-07-17 04:38
Author: asmeurer
Category: Uncategorized
Slug: a-hard-week

After last week's [breakthrough][], work this week has been very slow. I
started working on the Parametric Risch Differential Equation Problem,
which is almost identical to the Risch Differential Equation Problem in
how it is solved, except there are a few extra steps. Unfortunately,
because it is so similar, Bronstein breezes through the description.
This is fine for the parts that are the same, but he is a little unclear
on how some of the new parts fit in. Also, his pseudocode has a line
more or less saying

[code]  
if r1 = … = rn = 0 then  
N = -1  
else  
N = max(deg(r1), …, deg(rn))

for i from 0 to N  
for j from 1 to m  
Mij = coefficient(rj, t\^i)

[/code]

where M is a matrix. It is not very clear what this is supposed to mean
in the case where N = -1. Obviously, you can't have a a matrix with
negative dimensions. Clearly, this means that this particular function
doesn't apply somehow in this case, but I am not really even sure where
it fits in to the whole algorithm at this point in reading. After
reading a few more pages in, it gives a few hints here and there on how
it is to be used, but never is it explicitly shown, in pseudocode or
otherwise. So for now, I think my best bet is to read ahead and get a
fuller understanding of the complete function before I try implementing
anything (this is what I had been doing before, but I caught up to
myself).

Also, on an unrelated note, I just found out today that I passed my
[Google Summer of Code midterm evaluation][]. This means that I will
receive half of my stipend for the program (the other half comes after
passing the final evaluation at the end of the summer), and that I can
continue working on my project in the program.

EDIT:

Later in the text, it runs through an example and says "… \$latex dc =
-1\$, hence M and A are 0 by 0 matrices." So obviously, that is what was
meant.

  [breakthrough]: http://asmeurersympy.wordpress.com/2010/07/12/integration-of-exponential-functions/
  [Google Summer of Code midterm evaluation]: http://socghop.appspot.com/document/show/gsoc_program/google/gsoc2010/faqs#evaluations
