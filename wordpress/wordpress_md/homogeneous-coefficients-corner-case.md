Title: Homogeneous coefficients corner case
Date: 2009-08-10 17:30
Author: asmeurer
Category: Uncategorized
Slug: homogeneous-coefficients-corner-case

Before I started the program, I implemented Bernoulli equations. But the
general solution to Bernoulli equations involves raising something to
the power of \$latex \\frac{1}{1-n}\$, where n is the power of the
dependent term (see the [Wikipedia page][] for more info). This works
great, as I soon discovered, unless n == 1. Then you get something to
the power of \$latex \\infty\$. So I had to go in and remove the corner
case.

So you think that after that I would have been more careful after that
about checking that if general solution that divides by something I
would test to see if that something is not zero before returning it as a
solution.

Well, as I was just trying to implement some separable equation tests, I
was going through the exercises of my ode text as I usually do for
tests, and I came across \$latex xy' - y = 0\$. If you recall, this
equation also has coefficients that homogeneous of the same order (1).
From the general solution to homogeneous coefficients, you would plug it
into \$latex
\\int{\\frac{dx}{x}}=\\int{\\frac{-Q(1,u)du}{P(1,u)+uQ(1,u)}}+C\$ where
\$latex u = \\frac{y}{x}\$ or \$latex
\\int{\\frac{dy}{y}}=\\int{\\frac{-P(u,1)du}{uP(u,1)+Q(u,1)}}+C\$ where
\$latex u = \\frac{x}{y}\$ (here, P and Q are from the general form
\$latex P(x,y)dx+Q(x,y)dy=0\$). Well, it turns out that if you plug the
coefficients from my example into those equations, the denominator will
become 0 for each one. So I (obviously) need to check for that \$latex
P(1,u)+uQ(1,u)\$ and \$latex uP(u,1)+Q(u,1)\$ are not 0 before running
the homogeneous coefficients solver on a differential equation.

  [Wikipedia page]: http://en.wikipedia.org/wiki/Special:Search?search=bernoulli%20differential%20equation&go=Go
