Testing implicit solutions to ODEs
##################################
:date: 2009-08-12 21:27
:author: asmeurer
:category: Uncategorized
:slug: testing-implicit-solutions-to-odes

So, the hard deadline for GSoC it Monday, so this will probably be my
last post until then (I am very busy trying to finish up the ode module
by then). But this is one of those things that you just have to blog
about.

So I have this checksol function in test\_ode.py that attempts to check
it the solutions to odes are valid or not. It was a relic of the old ode
module. For that, it would just substitute the solution into the ode and
see if it simplified to 0. That is what it still does, if the solution
is solved for f(x) (the function for all of my ode tests). But if the
solution is implicit in f, either because solve() is not good enough to
solve it or because it cannot be solved, then that method obviously does
not work. So what I was trying to do is what my textbook suggested. Take
the derivative of the solution implicitly n times, where n is the order
of the ode, and see if that is equal to the ode. Basically, I was
subtracting the ode from it and seeing if it reduced to 0.

However, it wasn't really working at all for most of my implicit
solutions, even the really simple ones. I ended up XFAILing most of my
implicit checksol tests. I think every single `homogeneous
coefficients`_ had an implicit solution, and none of them were working
with checksol().

So I started to ask around on IRC to see if anyone had any better ideas
for testing these. Ondrej couldn't think of anything. Luke and Chris
worked on an example that I gave them, and it seemed to be that it
*wasn't* correct (which I didn't believe for a second, because the
solution was straight out of my text, and both homogeneous coefficients
integrals produced that same solution). It turns out that we were mixing
up $latex \\log{\\frac{y}{x}}$ and $latex \\log{\\frac{x}{y}}$ terms.
One of those appeared in the ode and the other appeared in the solution
(the ode was $latex y dx + x\\log{\\frac{y}{x}}dy - 2x dy = 0$ and the
solution is $latex \\frac{y}{1 + \\log{\\frac{x}{y}}}=C$, `number 9 from
my odes text, pg. 61`_.

So Chris had a novel idea. For 1st order odes, you can take the
derivative of the solution and solve for $latex \\frac{dy}{dx}$, which
will always be possible, because differentiation is a linear operator.
Then substitute that into the original ode, and it will reduce.

So we were talking about this on IRC later, and I had an epiphany as to
why my original method wasn't working. After trying it manually on an
ode, I found that I had to multiply through the solution's derivative by
$latex \\frac{x}{f(x)}$ to make it equal to the ode. Then, that reminded
me of an important solution method that I didn't have time to implement
this summer: integrating factors. I remember that my textbook had
`mentioned`_ that there is a theorem that states that every 1st order
ODE that is linear in the derivative has a unique integrating factor
that makes it exact. And I realized, the derivative of the solution will
be equal to the ODE if and only if the ODE is exact. I checked my exact
tests and verified my hunch. I had to XFAIL all of my implicit
homogeneous coefficients solutions, but all of my exact checksols were
working just fine.

So I refactored my checksol function to do this, and it now can check
almost every one of my failing checksols. The exceptions are some where
trigsimp() cannot simplify the solution to 0 (we have a poor trigsimp),
a second order solution (the above trick only works on 1st order odes, I
believe), and some other simplification problems.

The only down side to this new routine is that it is kind of slow
(because of the simplification). I am going to have to skip a test of
only 6 solutions because it takes 24 seconds to complete.

.. _homogeneous coefficients: http://asmeurersympy.wordpress.com/2009/05/31/first-order-differential-equations-with-homogeneous-coefficients/
.. _number 9 from my odes text, pg. 61: http://books.google.com.np/books?id=29utVed7QMIC&lpg=PA24&ots=uxLSUKt_3P&dq=testing%20implicit%20solutions%20to%20ode&hl=en&pg=PA61#v=onepage&q=&f=false
.. _mentioned: http://books.google.com.np/books?id=29utVed7QMIC&lpg=PA24&ots=uxLSUKt_3P&dq=testing%20implicit%20solutions%20to%20ode&hl=en&pg=PA83#v=onepage&q=&f=false
