Title: Update for this week
Date: 2010-06-04 18:45
Author: asmeurer
Category: Uncategorized
Slug: update-for-this-week

So I started writing up a blog post on how rational function integration
works, but Ondrej [wants a blog post][] every week by the end of I don't
think I would do it justice by rushing to finish it now (read: I'm to
lazy to do it). So instead, I'll just give a short post (if that's
possible for me) on what I have been doing this week.

I finished up writing doctests for the polynomials module for now (see
[issue 1949][]), so now this week I started looking at the integrator.
In particular, I went through each of the 40 issues with the
[Integration label][] and added them to a test file that I can monitor
throughout the summer to see my progress. It is the
test\_failing\_integrals.py file in my [Integration branch][], where all
my work will be going for the foreseeable future. So if you want to
follow my work, follow that branch. Here are some observations from
those issues:

- integrate() can't handle almost all algebraic integrals (functions
with square roots, etc.). It can handle the derivative of arcsin and
arcsinh because of special code in heurisch.py, but that's about it.
Before I can do any work on the Algebraic Risch Algorithm, I will need
to implement the transcendental algorithm, so I think my temporary
solution for this may be to add pattern matching heuristics for some of
the more common algebraic integrals (anyone know a good integral
table?).

- I figured out why integrate hangs forever with some integrals, such as
the one in [issue 1441][]. Here is, in a nutshell, how the Heuristic
Risch algorithm works: Take the integrand and split it into components.
For example, the components of x\*cos(x)\*sin(x)\*\*2 are [x, cos(x),
sin(x)]. Replace each of these components with a dummy variable, so if x
= x0, cos(x) = x1, and sin(x) = x2, then the integrand is
x0\*x1\*x2\*\*2. Also, compute the derivative of each component in terms
of the dummy variables. So the derivatives of [x0, x1, x2] are [1, -x2,
2\*x1\*x2]. Then, using these, perform some magic to create some
rational functions out of the component dummy variables. Then, create a
candidate integral with a bunch of unknowns [A1, A2, …], which will be
rational numbers, and a multinomial of the An's and the xn's that should
equal 0 if the candidate integral is correct. Then, because the xn's are
not 0, and there is also some algebraic independence, you have the the
An coefficients of each term must equal 0. So you get a system of linear
equations in the An's. You then solve these equations, and plug the
values of the An's into the candidate integral to give you the solution,
or, if the system is inconsistent, then if cannot find a solution,
possibly because there is no elementary one.

Well, that over simplifies a lot of things, but the point I want to make
is that the integral from issue 1441 creates a system of \~600 linear
equations in \~450 variables, and solving that equation is what causes
the integration to hang. Also, as Mateusz, my mentor and the one who
wrote the current integration implementation, pointed out, quite a bit
of time is spent in the heurisch algorithm doing expansion on large
Basic polynomials. When I say Basic polynomials, I mean that they are
SymPy expressions, instead of Poly instances. Using Poly should speed
things up quite a bit, so my next move will be to convert heurisch()
into using Poly wherever applicable.

- There were a few bugs in the rational integration, which I fixed in my
branch. The problem was in rational integrals with symbolic
coefficients. Because the new polys are able to create polynomials using
any expression as a generator, not just symbols, things like
Poly(sin(y)\*x, x) creates Poly(sin(y)\*x, x, domain='ZZ[sin(y)]'). But
using the polynomial ring or fraction field creates problems with some
things like division, whereas we really only want the domain to be EX
(expression domain) in this case. So this was not too difficult to fix,
and you can see the fix in my integration branch.

- Some integrals will require some good implementation of special
functions such as the hypergeometric function to work. Sometimes, you
don't want to know what the non-elementary integral looks like, but you
just want to calculate a definite integral. The solution here is to use
Meijer-G functions, which are on the list of things to possibly do at
the end of the summer if I have time.

- Another bug that I plan on fixing (I haven't done it yet, but I know
how to do it and it will be trivial), is this ([issue 1888][]):

In [18]: print integrate(f(x).diff(x)\*\*2, x)

2\*D(f(x), x)\*f(x)/3 - 2\*x\*D(f(x), x, x)\*f(x)/3 + x\*D(f(x),
x)\*\*2/3

The problem is in the step where it computes the derivative of the
components, it tries to compute the derivative of f(x).diff(x) in terms
of a dummy variable, but it reduces to 0 because diff(x2, x) == 0. Thus,
it treats f(x).diff(x) like something that has a 0 third derivative,
i.e., x\*\*2.

Well that's it. I knew I couldn't make a short blog post :). If you want
to help, I have three branches that need review ([1][], [2][issue 1949],
[3][]), and except for the last one, my work is based on top of the
other two, so none of my integration work can be pushed in until those
two reviewed positively.

  [wants a blog post]: http://groups.google.com/group/sympy/browse_thread/thread/7d7dceb34db45302
  [issue 1949]: http://code.google.com/p/sympy/issues/detail?id=1949
  [Integration label]: http://code.google.com/p/sympy/issues/list?q=label:Integration
  [Integration branch]: http://github.com/asmeurer/sympy/tree/integration
  [issue 1441]: http://code.google.com/p/sympy/issues/detail?id=1441
  [issue 1888]: http://code.google.com/p/sympy/issues/detail?id=1888
  [1]: http://code.google.com/p/sympy/issues/detail?id=1883
  [3]: http://code.google.com/p/sympy/issues/detail?id=1843
