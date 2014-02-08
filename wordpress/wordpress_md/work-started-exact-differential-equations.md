Title: Work started -- Exact Differential Equations 
Date: 2009-05-16 04:47
Author: asmeurer
Category: Uncategorized
Slug: work-started-exact-differential-equations

I have decided to start working on my project, even though it is a week
early, since I am finished with school and have nothing better to do.  I
also like the idea of getting ahead.  I am pushing everything to
my [github account][].  So far, I have implemented [exact differential
equations][], which are cake (i.e., they took me about an hour to code
up).  These are equations of the type,![Exact Differential Equation
Form][]where![dP:dy=dQ:dx][].  If this condition holds, then there
exists a function![F(x,y)][], often called a 'potential function'
because of some applications of theses equations to physics, such
that![dF:dx=P][]and![dF:dy=Q][].  This is because mixed partials are
equal for continuous functions.  The solution will then just
be![F(x,y)=C1][].  The tricky part is finding the potential
function![F(x,y)][], but it turns out to be easier than you would think.
 Because of the fundamental theorem of calculus, the potential function
is just![Exact Differential Equation Solution][].  There is a
restriction where the rectangle
connecting![(x0,y0)][],![(x0,y)][],![(x,y0)][], and![(x,y)][]has to lie
entirely in the domain of ![P][] and![Q][], but if we let![x0=y0=0][],
then this is not really a problem for functions that SymPy will
encounter.  UPDATE: It turns out this is a problem if the equation has
singularities in it.  Fortunately, I was able to code up a workaround
that usually works.

So you can see that this is easy to implement in SymPy if you know the
above fact.  It turns out that most solution methods for ODEs are like
this.  They can be solved in the general case, although usually students
are only taught tricks because they are much easier to remember than
generally solved formulas.  For example, to solve an exact differential
equation, students are often taught to just integrate![P][]with respect
to![x][]and![Q][]with respect to![y][].  It is much simpler for a human
being to do that than the above integral, because the integral involves
evaluating limits and so on, but for a computer algebra system, the
above integral is a one-liner.

By the way, if you want to test my code, you should clone my github
repository and switch to the odes branch.  You can do this by typing
'git clone git://github.com/asmeurer/sympy.git' and then 'git checkout
odes' in a Terminal that is cd'd to the directory you want to clone to
(of course, you will need git installed first!).  Then type 'cd sympy'
and './bin/isympy', which will start SymPy.  Then from there, you can do
stuff like
'dsolve(sin(x)\*cos(f(x))+cos(x)\*sin(f(x))\*f(x).diff(x),f(x)' (this is
exact).  It's easy to generate an exact differential equation.  Just
start with a random function of x and y, then take the derivative of it
with respect to x and y each, and do a subs(y,f(x)) on each term (SymPy
wants functions for the dependent variable, so we have to use f(x)).
 Then do dsolve(\<the derivative with respect to x\>+\<the derivative
with respect to y\>\*f(x).diff(x),f(x)).  You should get your original
function equals an arbitrary constant C1.  By the way,
diff(\<function\>,x) will take the derivative of \<function\> with
respect to x.

Up next: Initial conditions, and then first order homogeneous
differential equations.

  [github account]: http://github.com/asmeurer/sympy/tree/odes
  [exact differential equations]: http://en.wikipedia.org/wiki/Exact_differential_equation
  [Exact Differential Equation Form]: http://asmeurersympy.files.wordpress.com/2009/05/exact-differential-equation-form.png
    "Exact Differential Equation Form"
  [dP:dy=dQ:dx]: http://asmeurersympy.files.wordpress.com/2009/05/dpdydqdx.png
    "dP:dy=dQ:dx"
  [F(x,y)]: http://asmeurersympy.files.wordpress.com/2009/05/fxy.png
    "F(x,y)"
  [dF:dx=P]: http://asmeurersympy.files.wordpress.com/2009/05/dfdxp.png
    "dF:dx=P"
  [dF:dy=Q]: http://asmeurersympy.files.wordpress.com/2009/05/dfdyq.png
    "dF:dy=Q"
  [F(x,y)=C1]: http://asmeurersympy.files.wordpress.com/2009/05/fxyc1.png
    "F(x,y)=C1"
  [Exact Differential Equation Solution]: http://asmeurersympy.files.wordpress.com/2009/05/exact-differential-equation-solution.png
    "Exact Differential Equation Solution"
  [(x0,y0)]: http://asmeurersympy.files.wordpress.com/2009/05/x0y0.png
    "(x0,y0)"
  [(x0,y)]: http://asmeurersympy.files.wordpress.com/2009/05/x0y.png
    "(x0,y)"
  [(x,y0)]: http://asmeurersympy.files.wordpress.com/2009/05/xy0.png
    "(x,y0)"
  [(x,y)]: http://asmeurersympy.files.wordpress.com/2009/05/xy.png
    "(x,y)"
  [P]: http://asmeurersympy.files.wordpress.com/2009/05/p.png "P"
  [Q]: http://asmeurersympy.files.wordpress.com/2009/05/q.png "Q"
  [x0=y0=0]: http://asmeurersympy.files.wordpress.com/2009/05/x0y00.png
    "x0=y0=0"
  [x]: http://asmeurersympy.files.wordpress.com/2009/05/x.png "x"
  [y]: http://asmeurersympy.files.wordpress.com/2009/05/y.png "y"
