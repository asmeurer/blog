Title: Integration of rational functions
Date: 2010-06-11 19:39
Author: asmeurer
Category: Uncategorized
Slug: integration-of-rational-functions

So for this week's blog post I will try to explain how the general
algorithm for integrating rational functions works. Recall that a
[rational function][] is the quotient of two polynomials. We know that
using common denominators, we can convert the sum of any number of
rational functions into a single quotient, \$latex \\frac{a\_nx\^n +
a\_{n-1}x\^{n-1} + \\cdots + a\_2x\^2 + a\_1x + a\_0}{b\_nx\^n +
b\_{n-1}x\^{n-1} + \\cdots + b\_2x\^2 + a\_1x + a\_0}\$. Also, using
[polynomial division][] we can rewrite any rational function as the sum
of a polynomial and the quotient of two polynomials such that the degree
of the numerator is less than the degree of the denominator (\$latex
F(x) = \\frac{b(x)}{c(x)} = p(x) + \\frac{r(x)}{g(x)}\$, with \$latex
deg(r) \< deg(g)\$). Furthermore, we know that the representation of a
rational function is not unique. For example, \$latex \\frac{(x + 1)(x -
1)}{(x + 2)(x - 1)}\$ is the same as \$latex \\frac{x + 1}{x + 2}\$
except at the point \$latex x = 1\$, and \$latex \\frac{(x - 1)\^2}{x -
1}\$ is the same as \$latex x - 1\$ everywhere. But by using [Euclid's
algorithm][] for finding the GCD of polynomials on the numerator and the
denominator, along with polynomial division on each, we can cancel all
common factors to get a representation that is unique (assuming we
expand all factors into one polynomial). Finally, using polynomial
division with remainder, we can rewrite any rational function \$latex
F(x)\$ as \$latex \\frac{a(x)}{b(x)} = p(x) + \\frac{a(x)}{d(x)}\$,
where \$latex a(x)\$, \$latex b(x)\$, \$latex c(x)\$, \$latex d(x)\$,
and \$latex p(x)\$ are all polynomials, and the degree of \$latex a\$ is
less than the degree of \$latex d\$.

We know from calculus that the integral of any rational function
consists of three parts: the polynomial part, the rational part, and the
logarithmic part (consider arctangents as complex logarithms). The
polynomial part is just the integral of \$latex p(x)\$ above. The
rational part is another rational function, and the logarithmic part,
which is a sum of logarithms of the form \$latex a\\log{s(x)}\$, where
\$latex a\$ is an algebraic constant and \$latex s(x)\$ is a polynomial
(note that if \$latex s(x)\$ is a rational function, we can split it
into two logarithms of polynomials using the log identities).

To find the rational part, we first need to know about square-free
factorizations. An important result in algebra is that any polynomial
with rational coefficients can be factored uniquely into irreducible
polynomials with rational coefficients, up to multiplication of a
non-zero constant and reordering of factors, similar to how any integer
can be factored uniquely into primes up to multiplication of 1 and -1
and reordering of factors (technically, it is with coefficients from a
unique factorization domain, for which the rationals is a special case,
and up to multiplication of a unit, which for rationals is every
non-zero constant). A polynomial is square-free if this unique
factorization does not have any polynomials with powers greater than 1.
Another theorem from algebra tells us that irreducible polynomials over
the rationals do not have any repeated roots, and so given this, it is
not hard to see that a polynomial being square-free is equivalent to it
not having repeated roots.

A [square-free factorization][] of a polynomial is a list of
polynomials, \$latex P\_1P\_2\^2 \\cdots P\_n\^n\$, where each \$latex
P\_i\$ is square-free (in other words, \$latex P\_1\$ is the product of
all the factors of degree 1, \$latex P\_2\$ is the product of all the
factors of degree 2, and so on). There is a relatively simple algorithm
to compute the square-free factorization of a polynomial, which is based
on the fact that \$latex gcd(P, \\frac{dp}{dx})\$ reduces the power of
each irreducible factor by 1. For example:  
[![][]][]  
(Sorry for the picture. WordPress code blocks do not work)

It is not too hard to prove this using the product rule on the
factorization of P. So you can see that by computing \$latex
\\frac{P}{gcd(P, \\frac{dP}{dx})}\$, you can obtain \$latex
P\_1P\_2\\cdots P\_n\$. Then, by recursively computing \$latex A\_0 =
P\$, \$latex A\_1 = gcd(A\_0, \\frac{dA\_0}{dx})\$, \$latex A2 =
gcd(A\_1, \\frac{dA\_1}{dx})\$, … and taking the quotient each time as
above, we can find the square-free factors of P.

OK, so we know from partial fraction decompositions we learned in
calculus that if we have a rational function of the form \$latex
\\frac{Q(x)}{V(x)\^n}\$ , where \$latex V(x)\$ is square-free, the
integral will be a rational function if \$latex n \> 1\$ and a logarithm
if \$latex n = 1\$. We can use the partial fraction decomposition that
is easy to find once we have the square-free factorization of the
denominator to rewrite the remaining rational function as a sum of terms
of the form \$latex \\frac{Q}{V\_k\^k}\$, where \$latex V\_i\$ is
square-free. Because \$latex V\$ is square-free, \$latex gcd(V, V')=1\$,
so the [Extended Euclidean Algorithm][] gives us \$latex B\_0\$ and
\$latex C\_0\$ such that \$latex B\_0V + C\_0V'=1\$ (recall that \$latex
g\$ is the gcd of \$latex p\$ and \$latex q\$ if and only if there exist
\$latex a\$ and \$latex b\$ relatively prime to \$latex g\$ such that
\$latex ap+bq=g\$. This holds true for integers as well as polynomials).
Thus we can find \$latex B\$ and \$latex C\$ such that \$latex BV + CV'=
\\frac{Q}{1-k}\$. Multiplying through by \$latex \\frac{1-k}{V\^k}\$,
\$latex \\frac{Q}{V\^k}=-\\frac{(k-1)BV'}{V\^k} +
\\frac{(1-k)C}{V\^{k-1}}\$, which is equal to \$latex \\frac{Q}{V\^k} =
(\\frac{B'}{V\^{k-1}} - \\frac{(k-1)BV'}{V\^k}) +
\\frac{(1-k)C-B'}{V\^{k-1}}\$. You may notice that the term in the
parenthesis is just the derivative of \$latex \\frac{B}{V\^{k-1}}\$, so
we get \$latex \\int\\frac{Q}{V\^k}=\\frac{B}{V\^{k-1}} +
\\int\\frac{(1-k)C - B'}{V\^{k-1}}\$. This is called Hermite Reduction.
We can recursively reduce the integral on the right hand side until the
\$latex k=1\$. Note that there are more efficient ways of doing this
that do not actually require us to compute the partial fraction
decomposition, and there is also a linear version due to Mack (this one
is quadratic), and an even more efficient algorithm called the
Horowitz-Ostrogradsky Algorithm, that doesn't even require a square-free
decomposition.

So when we have finished the Hermite Reduction, we are left with
integrating rational functions with purely square-free denominators. We
know from calculus that these will have logarithmic integrals, so this
is the logarithmic part.

First, we need to look at resultants and PRSs. The [resultant][] of two
polynomials is defined as differences of the roots of the two
polynomials, i.e., \$latex resultant(A, B) =
\\prod\_{i=1}\^n\\prod\_{j=1}\^m (\\alpha\_i - \\beta\_j)\$, where
\$latex A = (x - \\alpha\_1)\\cdots(x - \\alpha\_n)\$ and \$latex B = (x
- \\beta\_1)\\cdots(x - \\beta\_m)\$ are monic polynomials split into
linear factors. Clearly, the resultant of two polynomials is 0 if and
only if the two polynomials share a root. It is an important result that
the resultant of two polynomials can be computed from only their
coefficients by taking the determinant of the [Sylvester Matrix][] of
the two polynomials. However, it is more efficiently calculated using a
polynomial remainder sequence (PRS) (sorry, there doesn't seem to be a
Wikipedia article), which in addition to giving the resultant of A and
B, also gives a sequence of polynomials with some useful properties that
I will discuss below. A polynomial remainder sequence is a
generalization of the Euclidian algorithm where in each step, the
remainder \$latex R\_i\$ is multiplied by a constant \$latex
\\beta\_i\$. The Fundamental PRS Theorem shows how to compute specific
\$latex \\beta\_i\$ such that the resultant can be calculated from the
polynomials in the sequence.

Then, if we have \$latex \\frac{A}{D}\$, left over from the Hermite
Reduction (so \$latex D\$ square-free), let \$latex
R=resultant\_t(A-t\\frac{dD}{dx}, D)\$, where \$latex t\$ is a new
variable, and \$latex \\alpha\_i\$ be the distinct roots of R. Let
\$latex p\_i=\\gcd(A - \\alpha\_i\\frac{dD}{dx}, D)\$. Then it turns out
that the logarithmic part of the integral is just \$latex
\\alpha\_1\\log{p\_1} + \\alpha\_2\\log{p\_2} + \\cdots
\\alpha\_n\\log{p\_n}\$. This is called the Rothstein-Trager Algorithm.

However, this requires finding the prime factorization of the resultant,
which can be avoided if a more efficient algorithm called the
Lazard-Rioboo-Trager Algorithm is used. I will talk a little bit about
it. It works by using subresultant polynomial reminder sequences.

It turns out that the above \$latex gcd(A-\\alpha\\frac{dD}{dx}, D)\$
will appear in the PRS of \$latex D\$ and \$latex A-t\\frac{dD}{dx}\$.
Furthermore, we can use the PRS to immediately find the resultant
\$latex R=resultant\_t(A-t\\frac{dD}{dx}, D)\$, which as we saw, is all
we need to compute the logarithmic part.

So that's rational integration. I hope I haven't bored you too much, and
that this made at least a little sense. I also hope that it was all
correct. Note that this entire algorithm has already been implemented in
SymPy, so if you plug a rational function in to `integrate()`, you
should get back a solution. However, I describe it here because the
transcendental case of the Risch Algorithm is just a generalization of
rational function integration.

As for work updates, I found that the Poly version of the heursitic
Risch algorithm was considerably slower than the original version, due
to inefficiencies in the way the polynomials are currently represented
in SymPy. So I have put that aside, and I have started implementing
algorithms from the full algorithm. There's not much to say on that
front. It's tedious work. I copy the algorithm from Bronstein's book,
then try make sure that it is correct based on the few examples given
and from the mathematical background given, and when I'm satisfied, I
move on to the next one. Follow my [integration][] branch if you are
interested.

In my next post, I'll try to define some terms, like "elementary
function," and introduce a little differential algebra, so you can
understand a little bit of the nature of the general integration
algorithm.

  [rational function]: http://en.wikipedia.org/wiki/Rational_function
  [polynomial division]: http://en.wikipedia.org/wiki/Polynomial_division
  [Euclid's algorithm]: http://en.wikipedia.org/wiki/Euclid%27s_algorithm_for_polynomials#Polynomials
  [square-free factorization]: http://en.wikipedia.org/wiki/Square-free_factorization
  []: http://asmeurersympy.files.wordpress.com/2010/06/gcd.png "gcd"
  [![][]]: http://asmeurersympy.files.wordpress.com/2010/06/gcd.png
  [Extended Euclidean Algorithm]: http://en.wikipedia.org/wiki/Extended_Euclidean_algorithm
  [resultant]: http://en.wikipedia.org/wiki/Resultant
  [Sylvester Matrix]: http://en.wikipedia.org/wiki/Sylvester_matrix
  [integration]: http://github.com/asmeurer/sympy/tree/integration
