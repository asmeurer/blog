Title: Update
Date: 2009-07-06 18:12
Author: asmeurer
Category: Uncategorized
Slug: update

It's been a while since I've posted here, so I figured an update was in
order. Here is a list of stuff that I have done since my last post.

- I recovered my data from my Terminal history. This wasn't too
difficult as I predicted. I just had to do some minor formatting on the
`git commit --interactive` data to make it a valid git patch file. For
whatever reason, a handful of the changes wouldn't apply because git
couldn't find where changed lines were, even though they were identical
to what was in the patch. `git apply` doesn't seem to have a merge
option, but eventually I found the `--reject` option, which puts failed
patches in .rej files, instead of just failing the whole apply.

- I got separable equations implemented in dsolve. I actually did this
on the road before I lost my data, but I failed to mention it before, so
here it is. The hardest part with that was creating a decent
`separatevars()` function that could separate just about any funciton.
As I mentioned in an [earlier post][], this involved changing the way
that SymPy handles automatic combining of exponents in the core, as well
as refactoring expand. I also had to make the function completely
independent of `match`, because `match` is too buggy to work correctly
for separable equations.

- Speaking of refactoring `expand` and combining exponents, that work
made it in! It is the first major thing that I have done that has
actually made it into the main SymPy repo. It got in just before the
release of SymPy 0.6.5-beta2, so it should be in the final release of
SymPy 0.6.5. Most likely, none of my ODE stuff will make it in until
0.7.

- I started to work on [Variation of Parameters][], but before I could
actually get to the variation of parameters part, I needed to be able to
solve a homogeneous equation \$latex
a\_ny\^{(n)}+a\_{n-1}y\^{(n-1)}+\\dots+a\_1y'+a\_0y=0\$ (\$latex a\_i\$
constant for all \$latex i\$). If you know how that works, it involves
finding the roots of the polynomial given by \$latex
a\_nr\^n+a\_{n-1}r\^{n-1}+\\dots+a\_1r+a\_0=0\$. Depending on whether
these roots are real, imaginary, or complex, you have different
solutions with exponentials or sin's and cos's. I had no trouble getting
the exponentials and the sin's and cos's to work correctly (SymPy
already has a root finder that I put to work), but I did have a problem
getting the arbitrary constants to work correcty. It turns out that the
code for that would be much simpler if I had an arbitrary constant type
that automatically "absorbed" other constants. Since I had planned on
doing that anyway, I decided to put the rest of variation of parameters
on hold and begin work on that.

- We had a Documentation day on June 30, and I decided to write up a
document that would help people new to SymPy and Python with some of the
gotchas and pitfalls. For example, unlike most other independent CAS's
like Maple, you can't just type `1/2` in SymPy to get \$latex
\\frac{1}{2}\$. That is because Python evaluates it numerically. You
have to do `S(1)/2` or `Rational(1,2)` to get the Rational class. It's
all things like that. It's taken me a while to get it together, not
because it took me long to write it, but because it has to be in the
Sphinx documentation format, which I have had to learn. I am just
finishing it up now.

- I met with Ondrej on Saturday. He went down from Los Alamos to
Carlsbad with a friend to see the caverns, and they stopped here in
Albuquerque on the way back up. He came just in time to see the
fireworks, and after that got some dinner. We weren't able to do any
coding, but hopefully we will be able to meet up again later this summer
to do some of that.

  [earlier post]: http://asmeurersympy.wordpress.com/2009/06/21/refactoring-expand/
  [Variation of Parameters]: http://en.wikipedia.org/wiki/Variation_of_parameters
