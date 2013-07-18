The Risch Algorithm: Part 3, Liouville's Theorem
################################################
:date: 2010-08-14 02:55
:author: asmeurer
:category: Uncategorized
:slug: the-risch-algorithm-part-3-liouvilles-theorem

So this is the last official week of the Summer of Code program, and my
work is mostly consisting of removing ``NotImplementedError``\ s (i.e.,
implementing stuff), and fixing bugs. None of this is particularly
interesting, so instead of talking about that, I figured I would produce
another one of my Risch Algorithm blog posts. It is recommended that you
read parts `1`_ and `2`_ first, as well as my post on `rational function
integration`_, which could be considered part 0.

| **Liouville's Theorem**
|  Anyone who's taken calculus intuitively knows that integration is
hard, while differentiation is easy. For differentiation, we can produce
the derivative of any elementary function, and we can do so easily,
using a simple algorithm consisting of the sum and product rules, the
chain rule, and the rules for the derivative of all the various
elementary functions. But for integration, we have to try to work
backwards.

There are two things that make integration difficult. First is the
existence of functions that simply do not have any elementary
antiderivative. $latex e^{-x^2}$ is perhaps the most famous example of
such a function, since it arises from the normal distribution in
statistics. But there are many others. $latex \\sin{(x^2)}$, $latex
\\frac{1}{\\log{(x)}}$, and $latex x^x$ are some other examples of
famous non-integrable functions.

The second problem is that no one single simple rule for working
backwards will always be applicable. We know that u-substitution and
integration by parts are the reverse of the chain rule and the product
rule, respectively. But those methods will only work if those rules were
the ones that were applied originally, and then only if you chose the
right $latex u$ and $latex dv$.

But there is a much simpler example that gets right down to the point
with Liouville's theorem. The power rule, which is that $latex
\\frac{d}{dx}x^n=nx^{n-1}$ is easily reversed for integration. Given the
power rule for differentiation, it's easy to see that the reverse rule
should be $latex \\int{x^ndx}=\\frac{x^{n+1}}{n+1}$. This works fine,
except that were are dividing something, $latex n+1$. In mathematics,
whenever we do that, we have to ensure that whatever we divide by is not
0. In this case, it means that we must assert $latex n\\neq -1$. This
excludes $latex \\int{\\frac{1}{x}dx}$. We know from calculus that this
integral requires us to introduce a special function, the natural
logarithm.

But we see that $latex n=-1$ is the only exception to the power rule, so
that the integral of any (`Laurent`_) polynomial is again a (Laurent)
polynomial, plus a logarithm. Recall from part 0 (`Rational Function
Integration`_) that the same thing is true for any rational function:
the integral is again a rational function, plus a logarithm (we can
combine multiple logarithms into one using the logarithmic identities,
so assume for simplicity that there is just one). The argument is very
similar, too. Assume that we have split the denominator rational
function into linear factors in the `algebraic splitting field`_ (such
as the complex numbers). Then perform a partial fractions decomposition
on the rational function. Each term in the decomposition will be either
a polynomial, or of the form $latex \\frac{a}{(x - b)^n}$. The
integration of these terms is the same as with the power rule, making
the substitution $latex u = x - b$. When $latex n\\geq 2$, the integral
will be $latex \\frac{-1}{n - 1}\\frac{a}{(x - b)^{n - 1}}$; when $latex
n = 1$, the integral will be $latex a\\log{(x - b)}$. Now
computationally, we don't want to work with the algebraic splitting
field, but it turns out that we don't need to actually compute it to
find the integral. But theory is what we are dealing with here, so don't
worry about that.

Now the key observation about differentiation, as I have pointed out in
the earlier parts of this blog post series, is that the derivative of an
elementary function can be expressed in terms of itself, in particular,
as a polynomial in itself. To put it another way, functions like $latex
e^x$, $latex \\tan{(x)}$, and $latex \\log{(x)}$ all satisfy linear
differential equations with rational coefficients (e.g., for these,
$latex y'=y$, $latex y'=1 + y^2$, and $latex y'=\\frac{1}{x}$).

Now, the theory gets more complicated, but it turns out that, using a
careful analysis of this fact, we can prove a similar result to the one
about rational functions to any elementary function. In a nutshell,
Liouville's Theorem says this: if an elementary function has an
elementary integral, then that integral is a composed only of functions
from the original integrand, plus a finite number of logarithms of
functions from the integrand, which can be considered one logarithm, as
mentioned above ("functions from" more specifically means a rational
function in the terms from our elementary extension). Here is the formal
statement of the theorem.

| **Theorem (Liouville's Theorem - Strong version)**
|  Let $latex K$ be a differential field, $latex C=\\mathrm{Const}(K)$,
and $latex f\\in K$. If there exist an elementary extension $latex E$ of
$latex K$ and $latex g \\in E$ such that $latex Dg =f$, then there are
$latex v \\in K$, $latex c\_1, \\dots, c\_n\\in \\bar{C}$, and $latex
u\_1, \\dots,u\_n\\in K(c\_1,\\dots,c\_n)^\*$ such that

$latex f = Dv + \\sum\_{i=1}^n c\_i\\frac{Du\_i}{u\_i}$.
========================================================

| 
|  Looking closely at the formal statement of the theorem, we can see
that it says the same thing as my "in a nutshell" statement. $latex K$
is the differential extension, say of $latex \\mathbb{Q}(x)$, that
contains all of our elementary functions (see `part 2`_). $latex E$ is
an extension of $latex K$. The whole statement of the theorem is that
$latex E$ need not be extended from $latex K$ by anything more than some
logarithms. $latex f$ is our original function and $latex g=\\int f$.
Recall from `part 1`_ that $latex Dg = \\frac{Du}{u}$ is just another
way of saying that $latex g = \\log{(u)}$. The rest of the formal
statement is some specifics dealing with the constant field, which
assure us that we do not need to introduce any new constants in the
integration. This fact is actually important to the decidability of the
Risch Algorithm, because many problems about constants are either
unknown or undecidable (such as the transcendence degree of $latex
\\mathbb{Q}(e, \\pi)$). But this ensures us that as long as we start
with a constant field that is computable, our constant field for our
antiderivative will also be computable, and will in fact be the same
field, except for some possible algebraic extensions (the $latex c\_i$).

At this point, I want to point out that even though my work this summer
has been only on the purely transcendental case of the Risch Algorithm,
Liouville's Theorem is true for all elementary functions, which includes
algebraic functions. However, if you review the proof of the theorem,
the proof of the algebraic part is completely different from the proof
of the transcendental part, which is the first clue that the algebraic
part of the algorithm is completely different from the transcendental
part (and also a clue that it is harder).

Liouville's Theorem is what allows us to prove that a given function
does not have an elementary antiderivative, by giving us the form that
any antiderivative must have. We first perform the same Hermite
Reduction from the `rational integration case`_. Then, a generalization
of the same Lazard-Rioboo-Trager Algorithm due to Rothstein allows us to
find the logarithmic part of any integral (the $latex \\sum\_{i=1}^n
c\_i\\frac{Du\_i}{u\_i}$ from Liouville's Theorem).

Now a difference here is that sometimes, the part of the integrand that
corresponds to the $latex \\frac{a}{x - b}$ for general functions
doesn't always have an elementary integral (these are called *simple*
functions. I think I will talk about them in more detail in a future
post in this series). An example of this is $latex
\\frac{1}{\\log{(x)}}$. Suffice it to say that any elementary integral
of $latex \\frac{1}{\\log{(x)}}$ must be part of some log-extension of
$latex \\mathbb{Q}(x, \\log{(x)})$, and that we can prove that no such
logarithmic extension exists in the course of trying to compute it with
the Lazard-Rioboo-Rothstein-Trager Algorithm.

In the rational function case, after we found the rational part and the
logarithmic part, we were practically done, because the only remaining
part was a polynomial. Well, for the general transcendental function
case, we are left with an analogue, which are called *reduced*
functions, and we are far from done. This is the hardest part of the
integration algorithm. This will also be the topic of a future post in
this series. Suffice it to say that this is where most of the proofs of
non-integrability come from, including the other integrals than $latex
\\frac{1}{\\log{(x)}}$ that I gave above.

| **Conclusion**
|  That's it for now. Originally, I was also going to include a bit on
the structure theorems too, but I think I am going to save that for part
4 instead. I may or may not have another post ready before the official
end of coding date for Google Summer of Code, which is Monday (three
days from now). I want to make a post with some nice graphs comparing
the timings of the new ``risch_integrate()`` and the old ``heurisch()``
(what is currently behind SymPy's ``integrate()``). But as I have said
before, I plan on continuing coding the integration algorithm beyond the
program until I finish it, and even beyond that (there are lots of cool
ways that the algorithm can be extended to work with special functions,
there's definite integration with Meijer-G functions, and there's of
course the algebraic part of the algorithm, which is a much larger
challenge). And along with it, I plan to continue keeping you updated
with blog posts, including at least all the Risch Algorithm series posts
that I have promised (I have counted at least three topics that I have
explicitly promised but haven't done yet). And of course, there will be
the mandatory GSoC wrap-up blog post, detailing my work for the summer.

Please continue to test my prototype ```risch_integrate()```_ function
in my `integration3`_ branch, and tell me what you think (or if you find
a bug).

.. _1: http://asmeurersympy.wordpress.com/2010/06/30/the-risch-algorithm-part-1/
.. _2: http://asmeurersympy.wordpress.com/2010/07/24/the-risch-algorithm-part-2-elementary-functions/
.. _rational function integration: http://asmeurersympy.wordpress.com/2010/06/11/integration-of-rational-functions/
.. _Laurent: http://en.wikipedia.org/wiki/Laurent_polynomial
.. _Rational Function Integration: http://asmeurersympy.wordpress.com/2010/06/11/integration-of-rational-functions/
.. _algebraic splitting field: http://en.wikipedia.org/wiki/Algebraic_splitting_field
.. _part 2: http://asmeurersympy.wordpress.com/2010/07/24/the-risch-algorithm-part-2-elementary-functions/
.. _part 1: http://asmeurersympy.wordpress.com/2010/06/30/the-risch-algorithm-part-1/
.. _rational integration case: http://asmeurersympy.wordpress.com/2010/06/11/integration-of-rational-functions/
.. _``risch_integrate()``: http://asmeurersympy.wordpress.com/2010/08/05/prototype-risch_integrate-function-ready-for-testing/
.. _integration3: http://github.com/asmeurer/sympy/tree/integration3
