Variation of Parameters and More
################################
:date: 2009-08-01 17:39
:author: asmeurer
:category: Uncategorized
:slug: variation-of-parameters-and-more

Well, the last time I posted a project update, I had resigned myself to
writing a constant simplifying function and putting the Constant class
on the shelf. Well, just as I suspected, it was hell writing it, but I
eventually got it working. Already, what I have in dsolve() benefits
from it. I had many solutions with things like $latex \\frac{x}{C\_1}$
or $latex -C\_1x$ in them, and they are now automatically reduced to
just $latex C\_1x$. Of course, the disadvantage to this, as I mentioned
in the other post, is that it will only simplify once. Also, I wrote the
function very specifically for expressions returned by dsolve. It only
works, for example, with constants named sequentially like C1, C2, C3
and so on. Even with making it specialized, it was still hell to write.
I was also able to get it to renumber the constants, so something like
``C2*sin(x) + C1*cos(x)`` would get transfered to
``C1*sin(x) + C2*cos(x)``. It uses ``Basic._compare_pretty()`` (thanks
to Andy for that tip), so it will always number the constants in the
order they are printed.

Once I got that working, it was just little work to finish up what I had
already started with solving general linear homogeneous odes ($latex
a\_ny^{(n)} + a\_{n-1}y^{(n-1)} + \\dots + a\_2y'' + a\_1y' + a\_0y = 0$
with $latex a\_i$ constant for all $latex i$). Solving these equations
is easy. You just set up a polynomial of the form $latex a\_nm^n +
a\_{n-1}m^{n-1} + \\cdots + a\_2m^2 + a\_1m + a\_0 = 0$ and find the
roots of it. Then you plug the roots into an exponential times $latex
x^i$ for i from 1 to the multiplicity of the root (as in $latex
Cx^ie^{root \\cdot x}$). You usually expand the real and complex parts
of the root using Euler's Formula, and, once you simplify the constants,
you get something like $latex x^ie^{realpart \\cdot x}(C\_1\\sin{(impart
\\cdot x)} + C\_2\\cos{(impart \\cdot x)})$ for each i from 1 to the
multiplicity of the root. Anyway, with the new constantsimp() routine, I
was able to set this whole thing up as one step, because if the
imaginary part is 0, then the two constants will be simplified into each
other. Also, SymPy has some good polynomial solving, so I didn't have
any problems there. I even made good use of the collect() function to
factor out common terms, so you get something like $latex (C\_1 +
C\_2x)e^{x}$ instead of $latex C\_1e^{x} + C\_2xe^{x}$, which for larger
order solutions, can make the solution much easier to read (compare for
example, $latex ((C\_1 + C\_2x)\\sin{x} + (C\_3 + C\_4x)\\cos{x})e^{x}$
with the expanded form, $latex C\_1e^{x}\\sin{x} + C\_2xe^{x}\\sin{x} +
C\_3\\cos{x}e^{x} + C\_4x\\cos{x}{e^x}$ as the solution to $latex
{\\frac {d^{4}}{d{x}^{4}}}f \\left( x \\right) -4\\,{\\frac
{d^{3}}{d{x}^{3}}}f \\left( x \\right) +8\\,{\\frac {d^{2}}{d{x}^{2}}}f
\\left( x \\right) -8\\,{\\frac {d}{dx}}f \\left( x \\right) +4\\,f
\\left( x \\right) =0$).

I entered all 30 examples from the relevant chapter of my text (Ordinary
Differential Equations by Morris Tenenbaum and Harry Pollard), and the
whole thing runs in under 2 seconds on my machine. So it is fast, though
that is mostly due to fast polynomial solving in SymPy.

So once I got that working well, I started implementing variation of
parameters, which is a general method for solving all equations of form
$latex a\_ny^{(n)} + a\_{n-1}y^{(n-1)} + \\dots + a\_2y'' + a\_1y' +
a\_0y = F(x)$. The method will set up an integral to represent the
particular solution to any equation of this form, assuming that you have
all $latex n$ linearly independent solutions to the homogeneous equation
$latex a\_ny^{(n)} + a\_{n-1}y^{(n-1)} + \\dots + a\_2y'' + a\_1y' +
a\_0y = 0$. The coefficients $latex a\_i$ do not even have to be
constant for this method to work, although they do have to be in my
implantation because otherwise it will not be able to find general
solution to the homogeneous equation.

So, aside from doing my GSoC project this summer, I am also learning
Linear Algebra, because I could not fit it in to my schedule next
semester and I need to know it for my Knot Theory class. It turns out
that it was very useful in learning the method of variation of
parameters. I will explain how the method works below, but first I have
a little rant.

Why is the Wikipedia article on `variation of parameters`_ the only
website anywhere that covers variation of parameters in the general
case? Every other site that I could find only covers 2nd order
equations, which I understand is what is taught in most courses because
applying it to anything higher can be tedious and deriving the nth order
case requires knowledge of Cramer's Rule, which many students may not
know. But you would think that there would at least be sites that
discuss what I am about to discuss below, namely, applying it to the
general case of an nth order inhomogeneous linear ode. Even the
`Wolphram MathWorld article`_ only explains the derivation for a second
order linear ODE, mentioning at the bottom that it can be applied to nth
order linear ODEs. I did find a website called `Planet Math`_ that
covers the general case, but it wasn't on the top of the Google results
list and took some digging to find. It also has problems of its own,
like being on a very slow server and some of the LaTeX on the page not
rendering among them.

This partially annoys me because the Wikipedia article is not very well
written. You have to read through it several times to understand the
derivation (I will try to be better below). The Planet Math site is a
little better, but like I said, it took some digging to find, and I
actually found it after I had written up half of this post already.

But it is also part of a larger attitude that I am finding more and more
of where anything that is not likely to be directly applied is not worth
knowing and thus not worth teaching. Sure, it is not likely that any
person doing hand calculations will ever attempt variation of parameters
on an ode of order higher than 2 or 3, but that is what computer algebra
systems like SymPy are for. Unfortunately, it seems that they are also
in a large part for allowing you to not know how or why something
mathematically is true. What difference does it make if variation of
parameters can be applied to a 5th order ODE if I have to use Maple to
do actually do it anyway. As long as the makers of Maple know how to
apply variation of parameters to a nth order ODE, I can get along just
fine. At least with SymPy, the source is freely available, so anyone who
does desire to know how things are working can easily see. Anyway, I am
done ranting now, so if you were skipping that part, this would be the
point to start reading again.

| So you have your linear inhomogeneous ODE: $latex a\_ny^{(n)} +
a\_{n-1}y^{(n-1)} + \\dots + a\_2y'' + a\_1y' + a\_0y = F(x)$. $latex
a\_n$ cannot be zero (otherwise it would be a n-1 order ODE), so we can
and should divide through by it. Lets pretend that we already did that,
and just use the same letters. Also, I will rewrite $latex a\_n$ as
$latex a\_n(x)$ to emphasize that the coefficients do not have to be
constants for this to work. So you have your linear inhomogeneous ODE:
$latex y^{(n)} + a\_{n-1}(x)y^{(n-1)} + \\dots + a\_2(x)y'' + a\_1(x)y'
+ a\_0(x)y = F(x)$. So, as I mentioned above, we need n linearly
independent solutions to the homogeneous equation $latex y^{(n)} +
a\_{n-1}(x)y^{(n-1)} + \\dots + a\_2(x)y'' + a\_1(x)y' + a\_0(x)y = 0$
to use this method. Let us call those solutions $latex y\_1(x), y\_2(x),
\\dots, y\_n(x)$. Now let us write our particular solution as $latex
y\_p(x) = c\_1(x)y\_1(x) + c\_2(x)y\_2(x) + \\dots + c\_n(x)y\_n(x)$.
Now, if we substitute our particular solution in to the left hand side
of our ODE, we should get $latex F(x)$ back. So we have $latex
(y\_p)^{(n)} + a\_{n-1}(x)(y\_p)^{(n-1)} + \\dots + a\_2(x)y\_p'' +
a\_1(x)y\_p' + a\_0(x)y\_p =$ $latex F(x)$. Now, let me rewrite $latex
y\_p$ as a summation to help keep things from getting too messy. I am
also going to write $latex c\_i$ instead of $latex c\_i(x)$ on terms for
additional sanity. Every variable is a function of x. $latex y\_p(x) =
\\sum\_{i=1}^{n} c\_i y\_i$. The particular solution should satisfy the
condition of the ODE, so
|  $latex y\_p^{(n)} + a\_{n-1}y\_p^{(n-1)} + \\dots + a\_2y\_p'' +
a\_1y\_p' + a\_0y\_p = F(x)$.

| $latex (\\sum\_{i=1}^{n} c\_i y\_i)^{(n)} + a\_{n-1}(\\sum\_{i=1}^{n}
c\_i y\_i)^{(n-1)} + \\dots + a\_2(\\sum\_{i=1}^{n} c\_i y\_i)^{(2)} + $
|  $latex a\_1(\\sum\_{i=1}^{n} c\_i y\_i)^{(1)} + a\_0\\sum\_{i=1}^{n}
c\_i y\_i = F(x)$.

Now, if we apply the product rule to this, things will get ugly really
fast, because we have to apply the product rule on each term as many
times as the order of that term (the first term would have to be applied
n times, the second, n-1 times, and so on). But there is a trick that we
can use. In the homogeneous case, there is no particular solution, so in
that case the $latex c\_i$ terms must all vanish identically because the
solutions are linearly independent of one another. Thus, if we plug the
particular solution into the homogeneous case, we get

| $latex (\\sum\_{i=1}^{n} c\_i y\_i)^{(n)} + a\_{n-1}(\\sum\_{i=1}^{n}
c\_i y\_i)^{(n-1)} + \\dots + a\_2(\\sum\_{i=1}^{n} c\_i y\_i)^{(2)} + $
|  $latex a\_1(\\sum\_{i=1}^{n} c\_i y\_i)^{(1)} + a\_0\\sum\_{i=1}^{n}
c\_i y\_i = 0$.

| We already know that if we plug the $latex y\_i$ terms in individually
of the $latex c\_i$ terms, that the expression will vanish identically
because the $latex y\_i$ terms are solutions to the homogeneous
equation. The product rule on each term will be evaluated according to
the `Leibniz Rule`_, which is that $latex (c\_i \\cdot
f\_i)^{(n)}=\\sum\_{k=0}^n {n \\choose k} c\_i^{(k)} y\_i(x)^{(n-k)}$.
Now the $latex c\_i y\_i^{(n)}$ terms will vanish because we can factor
out a $latex c\_i$ and they will be exactly the homogeneous solution.
Because the expression is identically equal to zero, the remaining terms
must vanish as well. If we assume that each $latex \\sum\_{i=1}^n c\_i'
y\_i^{(j)}=0$ for each j from 0 to n-2, then this will take care of
this; the terms with higher derivatives on $latex c\_i$ will also be 0,
if this is true, then we do not need them for our derivation. In other
words,
|  $latex c\_1' y\_1 + c\_2' y\_2 + \\cdots + c\_n' y\_n = 0 $
|  $latex c\_n' y\_1' + c\_n' y\_2' + \\cdots + c\_n' y\_n' = 0 $
|  $latex \\vdots $
|  $latex c\_n' y\_1^{(n-2)} + c\_n' y\_2^{(n-2)} + \\cdots + c\_n'
y\_n^{(n-2)} = 0$.

| So, turning back to our original ODE with the particular solution
substituted in, we have
|  $latex (\\sum\_{i=1}^{n} c\_i y\_i)^{(n)} + a\_{n-1}(\\sum\_{i=1}^{n}
c\_i y\_i)^{(n-1)} + \\dots + a\_2(\\sum\_{i=1}^{n} c\_i y\_i)^{(2)} + $
|  $latex a\_1(\\sum\_{i=1}^{n} c\_i y\_i)^{(1)} + a\_0\\sum\_{i=1}^{n}
c\_i y\_i = F(x)$.
|  But we know that most of the terms of this will vanish, from our
assumption above. If we remove those terms, what remains is $latex
\\sum\_{i=1}^{n} c\_i' y\_i^{(n-1)} = F(x)$. So this is where it is nice
that I learned `Cramer's Rule`_ literally days before learning how to do
Variation of Parameters in the general case. We have a system of n
equations (the n-1 from above, plus the one we just derived), of n
unknowns (the $latex c\_i$ terms). The determinant that we use here is
used often enough to warrant a name: the `Wronskian`_. We have that
$latex c\_i' = \\frac{W\_i(x)}{W(x)}$, or $latex c\_i = \\int
\\frac{W\_i(x)}{W(x)}$, where $latex W\_i(x)$ is the Wronskian of the
fundamental system with the ith column replaced with $latex
\\begin{bmatrix} 0 \\\\ 0 \\\\ \\vdots \\\\ 0 \\\\ F(x) \\end{bmatrix}$.
So we finally have $latex y\_p = \\sum\_{i=1}^n \\int
\\frac{W\_i(x)}{W(x)} y\_i$.

| Well, that's the theory, but as always here, that is only half of the
story. A Wronskian function is already implemented in SymPy, and finding
$latex W\_i(x)$ simply amounts to $latex F(x)$ times the Wronskian of
the system without the ith equation, all times $latex (-1)^i$. So
implementing it was easy enough. But it soon became clear that there
would be some problems with this method. Sometimes, the SymPy would
return a really simple Wronskian, something like $latex -4e^{2x}$, but
other times, it would return something crazy. For example, consider the
expression that I reported in `SymPy issue 1562`_. The expression is
(thanks to SymPy's ``latex()`` command, no thanks to WordPress's stupid
auto line breaks that have forced me to upload my own image. If it
wasn't such a pain, I would do it for every equation, because it looks
much nicer.):
|  |Crazy Trig Wronskian (SymPy)|.
|  This is the Wronskian, as calculated by SymPy's ``wronskian()``
function, of
|  $latex \\begin{bmatrix}x \\sin{x}, & \\sin{x}, & 1, & x \\cos{x}, &
\\cos{x}\\end{bmatrix}$, which is the set of linearly independent
solutions to the ODE $latex {\\frac {d^{5}}{d{x}^{5}}}f \\left( x
\\right) +2\\,{\\frac {d^{3}}{d{x}^{3}}}f \\left( x \\right) +{\\frac
{d}{dx}}f \\left( x \\right) -1$. Well, the problem here is that, as
verified by Maple, that complex Wronskian above is identically equal to
$latex -4$. SymPy's ``simplify()`` and ``trigsimp()`` functions are not
advanced enough to handle it. It turns out that in this case, the
problem is that SymPy's ``cancel()`` and ``factor()`` routines do not
work unless the expression has only symbols in it, and that expression
requires you to cancel and factor to find the $latex \\cos^2{x} +
\\sin^2{x}$ (see the issue page for more information on this).
Unfortunately, SymPy's ``integrate()`` cannot handle that unsimplified
expression in the denominator of something, as you could imagine, and it
seems like almost every time that sin's and cos's are part of the
solution to the homogeneous equation, the Wronskian becomes too
difficult for SymPy to simplify. So, while I was hoping to slip along
with only variation of parameters, which technically solves every linear
inhomogeneous ODE, it looks like I am going to have to implement the
method of undetermined coefficients. Variation of parameters will still
be useful, as undetermined coefficients only works if the expression on
the right hand side of the equation, $latex F(x)$ has a finite set of
linearly independent derivatives (such as sin, cos, exp, polynomial
terms, and combinations of them (I'll talk more about this whenever I
implement it).

| The good news here is that I discovered that I was wrong. I had
previously believed that among the second order special cases were cases
that could only be handled by variation of parameters or undetermined
coefficients, but it turns out I was wrong. All that was implemented
were the homogeneous cases for second order linear with constant
coefficients. In addition to this, there was one very special case ODE
that Ondrej had implemented for an example
(examples/advanced/relativity.py). The ODE is
|  $latex
-2({\\frac{d}{dx}}f(x)){e^{-f(x)}}+x({\\frac{d}{dx}}f(x))^{2}{e^{-f(x)}}-x({\\frac{d^{2}}{d{x}^{2}}}f(x)){e^{-f(x)}}$,
which is the second derivative of $latex xe^{-f(x)}$ with respect to x.
According to the example file, it is know as Einstein's equations. Maple
has a nice ``odeadvisor()`` function similar to the ``classify_ode()``
function I am writing for SymPy that tells you all of the different ways
that an ODE can be solved. So, I plugged that ODE into it and got a few
possible methods out that I could potentially implement in SymPy to
maintain compatibility with the example equation. The chief one is that
the lowest order of f in the ODE is 1 (assuming you divide out the
$latex e^{-f(x)}$ term, which is perfectly reasonable as that term will
never be 0. You can then make the substitution $latex u = f'(x)$, and
you will reduce the order of the ODE to first order, which in this case
would be a Bernoulli equation, the first thing that I ever implemented
in SymPy.

| But I didn't do that. Reduction of order methods would be great to
have for ``dsolve()``, but that is a project for another summer. Aside
from that method, Maple's ``odeadvisor()`` also told me that it was a
Liouville ODE. I had never heard of that method, and neither it seems
has Wikipedia or "Uncle Google" (as Ondrej calls it). Fortunately,
Maple's Documentation has a nice page for each type of ODE returned by
``odeadvisor()``, so I was able to learn the method. The method relies
on Lie Symmetries and exact second order equations, neither of which I
am actually familiar with, so I will not attempt to prove anything here.
Suffice it to say that if an ODE has the form
|  $latex
{\\frac{d^{2}}{d{x}^{2}}}y(x)+g(y(x))({\\frac{d}{dx}}y(x))^{2}+f(x){\\frac{d}{dx}}y(x)=0$,
then the solution to the ODE is
|  $latex \\int^{y(x)}{e^{\\int g(a){da}}}{da}+C1\\int{e^{-\\int
f(x){dx}}}{dx}+C2=0$
|  You could probably verify this by substituting the solution into the
original ODE. See the `Maple Documentation page on Liouville ODEs`_, as
well as the `paper they reference`_ (Goldstein and Braun, "Advanced
Methods for the Solution of Differential Equations", see pg. 98).

The solution is very straight forward--as much so as first order linear
or Bernoulli equations, so it was a cinch to implement it. It looks like
quite a few differential equations generated by doing $latex F''(y(x),
x)$ for some function or x and y $latex F(y(x), x)$ generates equations
of that type, so it could be actually useful for solving other things.

Before I sign off, I just want to mention one other thing that I
implemented. I wanted my linear homogeneous constant coefficient ODE
solver to be able to handle ODEs for which SymPy can't solve the
characteristic equation, for whatever reason. SymPy has ``RootOf()``
objects similar to Maple that let you represent the roots of a
polynomial without actually solving it, or even being able to solve it,
but a you can only use RootOf's if you know that none of the roots are
repeated. Otherwise, you would have to know which terms require an
additional $latex x^i$ to preserve linear independence. Well, it turns
out that there is a way to tell if a polynomial has repeated roots
without solving for them. There is a number associated with every
polynomial of one variable called the `discriminant`_. For example, the
discriminant of the common quadratic polynomial $latex ax^2 + bx + c$ is
the term under the square root of the famous solution $latex b^2 - 4ac$.
It is clear that a quadratic has repeated roots if and only if the
discriminant is 0. Well, the same is true for the discriminant of any
polynomial. I am not highly familiar with this (ask me again after I
have taken my abstract algebra class next semester), but apparently
there is something called the resultant, which is the product of the
differences of roots between two polynomials and which can also be
calculated without explicitly finding the roots of the polynomials.
Clearly, this will be 0 if and only if the two polynomials share a root.
So the discriminant is built from the fact that a polynomial has a
repeated root iff it shares a root with its resultant. So it is
basically the resultant of a polynomial and its derativave, times an
extra factor. It is 0 if and only if the polynomial has a repeated root.

Fortunately, SymPy's excelent Polys module already had resultants
implemented (quite efficiently too, I might add), so it was easy to
implement the discriminant. I added it as `issue 1555`_. If you are a
SymPy developer and you have somehow managed to make yourself read this
far (bless your heart), please review that patch.

Well, this has turned out to be one hella long blog post. But what can I
say. You don't have to read this thing (except for possibly my mentor.
Sorry Andy). And I haven't been quite updating weekly like I am supposed
to be, so this compensates. If you happened upon this blog post because,
like me, you were looking for a general treatment of variation of
parameters, I hope you found my little write up helpful. And if you did,
and you now understand it, could you go ahead and improve the Wikipedia
article. I'm not up to it?

.. _variation of parameters: http://en.wikipedia.org/wiki/Variation_of_parameters
.. _Wolphram MathWorld article: http://mathworld.wolfram.com/VariationofParameters.html
.. _Planet Math: http://planetmath.org/encyclopedia/VariationOfParameters.html
.. _Leibniz Rule: http://en.wikipedia.org/wiki/Leibniz_rule_(generalized_product_rule)
.. _Cramer's Rule: http://en.wikipedia.org/wiki/Cramer%27s_rule
.. _Wronskian: http://en.wikipedia.org/wiki/Wronskian
.. _SymPy issue 1562: http://code.google.com/p/sympy/issues/detail?id=1562
.. _Maple Documentation page on Liouville ODEs: http://www.maplesoft.com/support/help/view.aspx?path=odeadvisor/Liouville
.. _paper they reference: http://eric.ed.gov:80/ERICWebPortal/custom/portlets/recordDetails/detailmini.jsp?_nfpb=true&_&ERICExtSearch_SearchValue_0=ED089982&ERICExtSearch_SearchType_0=no&accno=ED089982
.. _discriminant: http://en.wikipedia.org/wiki/Discriminant
.. _issue 1555: http://code.google.com/p/sympy/issues/detail?id=1555&q=discriminant

.. |Crazy Trig Wronskian (SymPy)| image:: http://asmeurersympy.files.wordpress.com/2009/08/crazy-trig-wronskian-sympy.png
