Undetermined Coefficients
#########################
:date: 2009-08-17 22:33
:author: asmeurer
:category: Uncategorized
:slug: undetermined-coefficients

*[Sorry for the delay in this post. I was having some difficulties
coming up with some of the rationales below. Also, classes have started,
which has made me very busy.]*

If there was one ODE solving method that I did not want to implement
this summer, it was undetermined coefficients. I didn't really like the
method too much when we did it my my ODE class (though it was not as
unenjoyable as series methods). The thing that I never really understood
very well is to what extent you have to multiply terms in the trial
function by powers of x to make them linearly independent of the
solution to the general equation. We did our ODEs homework in Maple, so
I would usually just keep trying higher powers of x until I got a
solution. But to implement it in SymPy, I had to have a much better
understanding of the exact rules for it.

From a user's point of view, the method of undetermined coefficients is
much better than the method of variation of parameters. While it is true
that variation of parameters is a general method and undetermined
coefficients only works on a special class of functions, undetermined
coefficients requires no integration or advanced simplification, so it
is fast (very fast, as well shall see below). All that the CAS has to do
is figure out what a trial function looks like, plug it into the ODE,
and solve for the coefficients, which is a system of linear equations.

On the other hand, from the programmer's point of view, `variation of
parameters`_ is much better. All you have to do is take the Wronskian of
the general solution set and use it to set up some integrals. But the
Wronskian has to be simplified, and if the general solution contains
sin's and cos's, this requires trigonometric simplification not
currently available in SymPy (although it looks like the `new Polys
module`_ will be making a big leap forward in this area). Also,
integration is slow, and in SymPy, it often fails (hangs forever).

Figuring out what the trial function should be for undetermined
coefficients is way more difficult to program, but having finnally
finished it, I can say that it is definitely worth having in the module.
Problems that it can solve can run orders of magnitude faster than the
variation of parameters, and often variation of parameters can't do the
integral or returns a less simplified result.

So what is this undetermined coefficients? Well, the idea is this: if
you knew what each linearly independent term of the particular solution
was, minus the coefficients, then you could just set each coefficient as
an unknown, plug it into the ODE, and solve for them. It turns out that
resulting system of equations is linear, so if you do the first part
right, you can always get a solution.

The key thing here is that you know what form the particular solution
will take. However, you don't really know this ahead of time. All you
have is the linear ode $latex a\_ny^{(n)}(x) + \\dots + a\_1y'(x) +
a\_0y(x) = F(x)$ (as far as I can tell, this only works in the case
where the coefficients $latex a\_i$ are constant with respect to x. I'd
be interested to learn that it works for other linear ODEs. At any rate,
that is the only one that works in my branch right now.). The solution
to the ode is $latex y(x) = y\_g(x) + y\_p(x)$, where $latex y\_g(x)$ is
the solution to the homogeneous equation $latex f(x) \\equiv 0$, and
$latex y\_p(x)$ is the particular solution that produces the $latex
F(x)$ term on the right hand side. The key here is just that. If you
plug $latex y\_p(x)$ into the left hand side of the ode, you get $latex
F(x)$.

It turns out that this method only works if the function $latex F(x)$
only has a finite number of linearly independent derivatives (I am
unsure, but this might be able to work in other cases, but it would
involve much more advanced mathematics). So what kind of functions have
a finite number of linearly independent solutions? Obviously,
polynomials do. So does $latex e^x$, $latex \\cos{x}$, and $latex
\\sin{x}$. Also, if we multiply two or more of these types together,
then we will get a finite number of linearly independent solutions after
applying the product rule. But is that all? Well, if we take the
definition of linear independence from linear algebra, we know that a
set of n vectors $latex \\{\\boldsymbol{v\_1}, \\boldsymbol{v\_2},
\\boldsymbol{v\_3}, \\dots, \\boldsymbol{v\_n}\\}$, not all zero, are
linearly independent only if $latex a\_1\\boldsymbol{v\_1} +
a\_2\\boldsymbol{v\_2} + a\_3\\boldsymbol{v\_3} + \\dots +
a\_n\\boldsymbol{v\_n}=0$ holds only when $latex a\_1 \\equiv 0, a\_2
\\equiv 0, a\_3 \\equiv 0, \\dots, a\_n \\equiv 0$, that is, the only
solution is the trivial one (remember, this is the *definition* of
linear independence). They are linearly dependent if there exist weights
$latex a\_1, a\_2, a\_3, \\dots, a\_n$, not all 0, such that the
equation $latex a\_1\\boldsymbol{v\_1} + a\_2\\boldsymbol{v\_2} +
a\_3\\boldsymbol{v\_3} + \\dots + a\_n\\boldsymbol{v\_n}=0$ is
satisfied. Using this definition, we can see that a function $latex
f(x)$ will have a finite number of linearly independent derivatives if
it satisfies $latex a\_nf^{(n)}(x) + a\_{n - 1}f^{(n - 1)}(x) + \\dots +
a\_1f'(x) + a\_0f(x) = 0$ for some $latex n$ and with $latex a\_i\\neq
0$ for some $latex i$. But this is just a `homogeneous linear ODE with
constant coefficients`_, which we know how to solve. The solutions are
all of the form $latex ax^ne^{b x}\\cos{cx}$ or $latex ax^ne^{b
x}\\sin{cx}$, where a, b, and c are real numbers and n is a non-negative
integer. We can set the various constants to 0 to get the type we want.
For example, for a polynomial term, b will be 0 and c will be 0 (use the
cos term).

So this gives us the exact form of functions that we need to look for to
apply undetermined coefficients, based on the assumption that it only
works on functions with a finite number of linearly independent
derivatives.

Well, implementing it was quite difficult. For every ODE, the first step
in implementation is matching the ODE, so the solver can know what
methods it can apply to a given ODE. To match in this case, I had to
write a function that determined if the function matched the form given
above, which was not too difficult, though not as trivial as just
grabbing the right hand side in variation of parameters. The next step
is to use the matching to format the ODE for the solver. In this case,
it means finding all of the finite linearly independent derivatives of
the ODE, so that the solver can just create a linear combination of them
solve for the coefficients. This was a little more difficult, and it
took some lateral thinking.

At this point, there is one more thing that needs to be noted. Since the
trial functions, that is, the linearly independent derivative terms of
the right hand side of the ODE, are of the same form as the solutions to
the homogeneous equation, it is possible that one of the trial function
terms will be a solution to the homogeneous equation. If this happens,
plugging it into the ODE will cause it to go to zero, which means that
we will not be able to solve for a coefficient for that term. Indeed,
that term will be of the form $latex C1\*\\textrm{term}$ in the final
solution, so even if we had a coefficient for it, it would be absorbed
into this term from the solution to the homogeneous equation. For
example, variation of parameters will give a coefficient for such terms,
even though it is unnecessary. This is a clue that Maple uses variation
of parameters for all linear constant coefficient ODE solving, because
it gives the unnecessary terms with the coefficients that would be given
by variation of parameters, instead of absorbing them into the arbitrary
constants.

We can safely ignore these terms for undetermined coefficients, because
their coefficients will not even appear in the system of linear
equations of the coefficients anyway. But, without these coefficients,
we will run into trouble. It turns out that if a term $latex
x^ne^{ax}\\sin{bx}$ or $latex x^ne^{ax}\\cos{bx}$ is repeated solution
to the homogeneous equation, and $latex x^{n + 1}e^{ax}\\sin{bx}$ or
$latex x^{n + 1}e^{ax}\\cos{bx}$ is not, so that $latex n$ is the
highest $latex x$ power that makes it a solution to the homogeneous
equation, and if the trial solution has $latex x^me^{ax}\\sin{bx}$ or
$latex x^me^{ax}\\cos{bx}$ terms, but not $latex x^{m +
1}e^{ax}\\sin{bx}$ or $latex x^{m + 1}e^{ax}\\cos{bx}$ terms, so that
$latex m$ is the highest power of $latex x$ in the the trial function
terms, then we need to multiply these trial function terms by $latex
x^{n + m}$ to make them linearly independent with the solutions of the
homogeneous equation.

Most `references`_ simply say that you need to multiply the trial
function terms by "sufficient powers of x" to make them linearly
independent with the homogeneous solution. Well, this is just fine if
you are doing it by hand or you are creating the trial function manually
in Maple and plugging it in and solving for the coefficients. You can
just keep upping the powers of x until you get a solution for the
coefficients. Creating those trial functions in Maple, plugging them
into the ODE, and solving for the coefficients is exactly what I had to
do for my homework when I took ODEs last spring, and this "upping
powers" trial and error method is exactly the method I used. But when
you are doing it in SymPy, you need to know exactly what power to
multiply it by. If it is too low, you will not get solution to the
coefficients. If it is too high, you can actually end up with too many
terms in the final solution, giving a wrong answer.

Fortunately, my excellent `ODEs textbook`_ gives the exact cases to
follow, and so I was able to implement it correctly. The textbook also
gives a whole slew of exercises, all for which the solutions are given.
As usual, this helped me to find the bugs in my very complex and
difficult to write routine. It also helped me to find a `match bug`_
that would have prevented ``dsolve()`` from being able to match certain
types of ODEs. The bug turned out to be fundamental to the way
``match()`` is written, so I had to write my own custom matching
function for linear ODEs.

The final step in solving the undetermined coefficients is of course
just creating a linear combination of the trial function terms, plugging
it into the original ODE, and setting the coefficients of each term on
each side equal to each other, which gives a linear system. SymPy can
solve these easily, and once you have the values of the coefficients,
you can use them to build your particular solution, at which point, you
are done.

The results were astounding. Variation of parameters would hang on many
simple inhomogeneous ODEs because of poor trig simplification of the
Wronsikan, but my undetermined coefficients method handles them
perfectly. Also, there is no need to worry about absorbing superfluous
terms into the arbitrary constants as with variation of parameters,
because they are removed from within the undetermined coefficients
algorithm.

.. raw:: html

   <p>

| But the biggest thing was speed. Here are some benchmarks on some
random ODEs from the test suite. WordPress code blocks are impervious to
whitespace, as I have mentioned before, so no pretty printing here.
Also, it truncates the hints. The hints used are
``'nth_linear_constant_coeff_undetermined_coefficients'`` and
``'nth_linear_constant_coeff_variation_of_parameters'``:

    | In [1]: time dsolve(f(x).diff(x, 2) - 3\*f(x).diff(x) -
    2\*exp(2\*x)\*sin(x), f(x),
    hint='nth\_linear\_constant\_coeff\_undetermined\_coefficients')
    |  CPU times: user 0.07 s, sys: 0.00 s, total: 0.08 s
    |  Wall time: 0.08 s
    |  Out[2]:
    |  f(x) == C1 + (-3\*sin(x)/5 - cos(x)/5)\*exp(2\*x) + C2\*exp(3\*x)

    | In [3]: time dsolve(f(x).diff(x, 2) - 3\*f(x).diff(x) -
    2\*exp(2\*x)\*sin(x), f(x),
    hint='nth\_linear\_constant\_coeff\_variation\_of\_parameters')
    |  CPU times: user 0.92 s, sys: 0.01 s, total: 0.93 s
    |  Wall time: 0.94 s
    |  Out[4]:
    |  f(x) == C1 + (-3\*sin(x)/5 - cos(x)/5)\*exp(2\*x) + C2\*exp(3\*x)

    | In [5]: time dsolve(f(x).diff(x, 4) - 2\*f(x).diff(x, 2) + f(x) -
    x + sin(x), f(x),
    hint='nth\_linear\_constant\_coeff\_undetermined\_coefficients')
    |  CPU times: user 0.06 s, sys: 0.00 s, total: 0.06 s
    |  Wall time: 0.06 s
    |  Out[6]:
    |  f(x) == x - sin(x)/4 + (C1 + C2\*x)\*exp(x) + (C3 +
    C4\*x)\*exp(-x)

    | In [7]: time dsolve(f(x).diff(x, 4) - 2\*f(x).diff(x, 2) + f(x) -
    x + sin(x), f(x),
    hint='nth\_linear\_constant\_coeff\_variation\_of\_parameters')
    |  CPU times: user 5.43 s, sys: 0.03 s, total: 5.46 s
    |  Wall time: 5.52 s
    |  Out[8]:
    |  f(x) == x - sin(x)/4 + (C1 + C2\*x)\*exp(x) + (C3 +
    C4\*x)\*exp(-x)

    | In [9]: time dsolve(f(x).diff(x, 5) + 2\*f(x).diff(x, 3) +
    f(x).diff(x) - 2\*x - sin(x) - cos(x), f(x),
    'nth\_linear\_constant\_coeff\_undetermined\_coefficients')
    |  CPU times: user 0.10 s, sys: 0.00 s, total: 0.10 s
    |  Wall time: 0.11 s
    |  Out[10]:
    |  f(x) == C1 + (C2 + C3\*x - x\*\*2/8)\*sin(x) + (C4 + C5\*x +
    x\*\*2/8)\*cos(x) + x\*\*2

    In [11]: time dsolve(f(x).diff(x, 5) + 2\*f(x).diff(x, 3) +
    f(x).diff(x) - 2\*x - sin(x) - cos(x), f(x),
    'nth\_linear\_constant\_coeff\_variation\_of\_parameters')

| 
|  The last one involves a particularly difficult Wronskian for SymPy
(run it with
hint='nth\_linear\_constant\_coeff\_variation\_of\_parameters\_Integral',
simplify=False).

.. raw:: html

   <p>

| Wall time comparisons reveal amazing speed differences. We're talking
orders of magnitude.

    | In [13]: 0.94/0.08
    |  Out[13]: 11.75

    | In [14]: 5.52/0.06
    |  Out[14]: 92.0

    | In [15]: oo/0.11
    |  Out[15]: +inf

.. raw:: html

   <p>

| 
|  Of course, variation of parameters has the most difficult time when
there are sin and cos terms involved, because of the poor trig
simplification in SymPy. So let's see what happens with an ODE that just
has exponentials and polynomial terms involved.

    | In [16]: time dsolve(f(x).diff(x, 2) + f(x).diff(x) - x\*\*2 -
    2\*x, f(x),
    hint='nth\_linear\_constant\_coeff\_undetermined\_coefficients')
    |  CPU times: user 0.10 s, sys: 0.00 s, total: 0.10 s
    |  Wall time: 0.10 s
    |  Out[17]:
    |  f(x) == C1 + x\*\*3/3 + C2\*exp(-x)

    | In [18]: time dsolve(f(x).diff(x, 2) + f(x).diff(x) - x\*\*2 -
    2\*x, f(x),
    hint='nth\_linear\_constant\_coeff\_variation\_of\_parameters')
    |  CPU times: user 0.19 s, sys: 0.00 s, total: 0.19 s
    |  Wall time: 0.20 s
    |  Out[19]:
    |  f(x) == C1 + x\*\*3/3 + C2\*exp(-x)

    | In [20]: time dsolve(f(x).diff(x, 3) + 3\*f(x).diff(x, 2) +
    3\*f(x).diff(x) + f(x) - 2\*exp(-x) + x\*\*2\*exp(-x), f(x),
    hint='nth\_linear\_constant\_coeff\_undetermined\_coefficients')
    |  CPU times: user 0.09 s, sys: 0.00 s, total: 0.09 s
    |  Wall time: 0.09 s
    |  Out[21]:
    |  f(x) == (C1 + C2\*x + C3\*x\*\*2 + x\*\*3/3 - x\*\*5/60)\*exp(-x)

    | In [22]: time dsolve(f(x).diff(x, 3) + 3\*f(x).diff(x, 2) +
    3\*f(x).diff(x) + f(x) - 2\*exp(-x) + x\*\*2\*exp(-x), f(x),
    hint='nth\_linear\_constant\_coeff\_variation\_of\_parameters')
    |  CPU times: user 0.29 s, sys: 0.00 s, total: 0.29 s
    |  Wall time: 0.29 s
    |  Out[23]:
    |  f(x) == (C1 + C2\*x + C3\*x\*\*2 + x\*\*3/3 - x\*\*5/60)\*exp(-x)

.. raw:: html

   <p>

| 
|  The wall time comparisons here are:

    | In [24]: 0.20/0.10
    |  Out[24]: 2.0

    | In [25]: 0.29/0.09
    |  Out[25]: 3.22222222222

So we don't have orders of magnitude anymore, but it is still 2 to 3
times faster. Of course, most ODEs of this form *will* have sin or cos
terms in them, so the order of magnitude improvement over variation of
parameters can probably be attributed to undetermined coefficients in
general.

Of course, we know that variation of parameters will still be useful,
because functions like $latex \\ln{x}$, $latex \\sec{x}$ and $latex
\\frac{1}{x}$ do not have a finite number of linearly independent
derivatives, and so you cannot apply the method of undetermined
coefficients to them.

There is one last thing I want to mention. You can indeed multiply any
polynomial, exponential, sin, or cos functions together and still get a
function that has a finite number of linearly independent solutions, but
if you multiply two or more of the trig functions, you have to apply the
`power reduction rules`_ to the resulting function to get it in terms of
sin and cos alone. Unfortunately, SymPy does not yet have a `function`_
that can do this, so to solve such a differential equation with
undetermined coefficients (recommended, see above), you will have to
apply them manually yourself. Also, just for the record, it doesn't play
well with exponentials in the form of sin's and cos's or the other way
around (complex coefficients on the arguments), so you should back
convert those first too.

Well, this concludes the first of two blog posts that I promised. I also
promised that I would write about my summer of code experiences. Not
only is this important to me, but it is a `requirement`_. I really
*hope* to get this done soon, but with classes, who knows.

.. _variation of parameters: http://asmeurersympy.wordpress.com/2009/08/01/variation-of-parameters-and-more/
.. _new Polys module: http://code.google.com/p/sympy/issues/detail?id=1598
.. _homogeneous linear ODE with constant coefficients: http://asmeurersympy.wordpress.com/2009/08/01/variation-of-parameters-and-more/
.. _references: http://en.wikipedia.org/wiki/Method_of_undetermined_coefficients
.. _ODEs textbook: http://books.google.com.np/books?id=29utVed7QMIC&lpg=PA24&ots=uxLSUKt_3P&dq=testing%20implicit%20solutions%20to%20ode&hl=en&pg=PA61#v=onepage&q=&f=false
.. _match bug: http://code.google.com/p/sympy/issues/detail?id=1601
.. _power reduction rules: http://en.wikipedia.org/wiki/Trig_identities#Power-reduction_formulas
.. _function: http://code.google.com/p/sympy/issues/detail?id=1590
.. _requirement: http://code.google.com/p/sympy/wiki/GSoC2009
