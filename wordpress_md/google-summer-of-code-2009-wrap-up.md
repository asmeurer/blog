Title: Google Summer of Code 2009 Wrap Up
Date: 2009-09-07 06:49
Author: asmeurer
Category: Uncategorized
Slug: google-summer-of-code-2009-wrap-up

Sorry about the extreme delay with this. I of course have been busy with
classes.

Note that this will just be a summary of the summer, with my comments
looking back on it. If you want more details on each individual thing
that I implemented, look back on my previous blog posts.

Let me start from the beginning. Around late February to early March of
this year, I discovered the existence of Google Summer of Code. I knew
that I wanted to do some kind of work this summer, preferably an
internship, so it piqued my interest. At that time, the mentoring
organizations were still applying for GSoC 2009, so I could only look at
the ones from 2008. Most of them were either Linux things or Web things,
neither of which I had any experience in or am I much interested in. I
took a free course in Python at my University the previous semester, and
it was the programming language that I knew best at the time. I had
learned some Java in my first semester CS class (did I mention that this
was my first year at college?), and I hated it, and I was still learning
C for my second semester CS class. So I looked at what the Python
Foundation had to offer. I am a double major in math and computer
science, so I looked under the math/science heading. That's when I saw
SymPy.

I should not that I have been ahead in Math. It was my second semester,
and I was taking Discrete Mathematics, Ordinary Differential Equations,
Basic Concepts of Math, and Vector Analysis. So I looked for project
ideas on the SymPy page that related to what I knew. The only one that I
saw, other than core improvements, was to improve the ODE solving
capabilities. I got into contact with the community and looked at the
source, finding that it was only capable of solving 1st order linear
equations and some special cases of 2nd order linear homogeneous
equations with constant coefficients. I already at that point knew
several methods from my ODE course, and I knew much of what I would
learn.

**Application Period**  
The most difficult part of the Google Summer of Code, in my opinion, is
the application period. For starters, you have to do it while you are
still in classes, so you pretty much have to do it in your free time.
Also, if you have never applied for Google Summer of Code before, you do
not really know what a good application should look like. I have long
had my application available on the [SymPy Wiki][], and I will reference
it here a few times. First off, it was recommended to me by some of the
SymPy developers that I put as many potential things that I could do in
the summer in my application as I though I could do. I was still only
about half way through my ODEs course when I wrote the application, but
I had the syllabus so I knew the methods I would be learning at least by
name. So that is exactly what I did: I packed my application with every
possible thing that I knew we would be learning about in ODEs.

After I felt that I had a strong application, and Ondrej had proofread
it for me, I submitted it. There were actually two identical
applications, one for the Python Software Foundation, and one for
Portland State University. This is because SymPy was not accepted as a
mentoring organization directly, so they had to use those two
foundations as proxies. A requirement of acceptance is to submit a patch
that passes review. I decided to add a Bernoulli solver, because
Bernoulli can be solved in the general case much like the 1st order
linear ODE, which was already implemented.

After I applied, there was an acceptance period. I used that period to
become aquatinted with the SymPy community and code base. A good way to
do this is to try to fix [EasyToFix issues][]. I found [issue 694][],
which is to implement a bunch of tests from a paper by Michael Wester
for testing computer algebra systems. The tests cover every possible
thing that a full featured CAS could do, so it was a great way to learn
SymPy. The issue is still unfinished, so working on it is still a good
way to learn how to use SymPy.

Also, it was important to learn git, SymPy's version control system. The
learning curve it pretty steep if you have never used version control
system before, but once you can use it, it becomes a great tool at your
disposal.

**Acceptance**  
After being accepted, I toned down my work with SymPy to work on
finishing up my classes. My classes finished a few weeks before the
official start, so I used that period to get a jump start on my project.

**The GSoC Period**  
For the start of the period, I followed my timeline. I implemented 1st
order ODEs with homogeneous coefficients and 1st order exact ODEs. These
were both pretty simple to do, as I expected.

The next thing I wanted to do was separable. My goal at this point was
to get every relevant exercise from my textbook to work with my solvers.
One of the exercises from my [book][] (Pg. 56, No. 21) was \$latex
dy=e\^{x + y}dx\$. I soon discovered that it was impossible for SymPy to
separate \$latex e\^{x + y} \\rightarrow e\^{x}e\^{y}\$, because the
second would be automatically combined in the core. I also discovered
that `expand()`, which should have been the function to split that,
expanded using all possible methods indiscriminately. Part of my
`separatevars()` function that I was writing to separate variables in
expressions would be to split things like \$latex x + yx \\rightarrow
x(1 + y)\$ and \$latex 2 x y + x\^{2} + y\^{2} \\rightarrow (x +
y)\^{2}\$, but `expand()`  
as it was currently written would expand those.

So I spent a few weeks hacking on the core to make it not auto-combine
exponents. I came up with a rule that exponents would only auto-combine
if they had the same term minus the coefficient, the same rule that
`Add` uses to determine what terms should auto combined by addition. So
it would combine \$latex e\^{x}e\^{x} \\rightarrow e\^{2x}\$, but
\$latex e\^{x}e\^{y}\$ would be left alone. It turns out that some of
our algorithms, namely the Gruntz limit algorithm, relies on
auto-combining. We already had a function that could combine exponents,
`powsimp()`, but it also combined bases, as in \$latex x\^zy\^z
\\rightarrow (xy)\^z\$, so I had to split the behavior so that it could
act only as auto-combining once did (by the way, use
`powsimp(expr, combine='exp', deep=True)` to do this). Then, after some
help from Ondrej on pinpointing the exact location of the bugs, I just
applied the function there. The last thing I did here was to split the
behavior of expand, so that you could do `expand(x*(y + 1), mul=False)`
and it would leave it alone, but `expand(exp(x + y), mul=False)` would
return `exp(x)*exp(y)`. This split behavior turned out to be useful in
more than one place in my code.

This was the first non bug fix patch of mine that was pushed in to
SymPy, and at the time of this writing, it is the last major one in the
latest stable version. It took some major rebasing to get my convoluted
commit history ready for submission, and it was during this phase that I
git finally clicked for me, especial the `git rebase` command. This work
took a few weeks from my ODEs time, and it became clear that I would not
be doing every possible thing from my application. The reason that I
included so much in my application was that my project was non-atomic. I
could implement a little or a lot and still have a working useful
module.

If you look at my timeline on my application, you can see that the first
half is symbolic methods, and the second half is other methods, things
like series. It turns out that we didn't really learn much about systems
of ODEs in my course and we learned very little about numerical methods
(and it would take much more to know how to implement them). We did
learn series methods, but they were so annoying to do that I came to
hate them with a passion. So I decided to just focus on symbolic
methods, which were my favorite anyway. My goal was to implement as many
as I could.

After I finished up separable equations, I came up with an idea that I
did not have during the application period. `dsolve()` was becoming
cluttered fast with all of my solution methods. The way that it worked
was that it took an ODE and it tried to match methods one by one until
it found one that worked, which it then used. This had some drawbacks.
First, as I mentioned, the code was very cluttered. Second, the ODEs
methods would have to be applied in a predetermined order. There are
several ODEs that match more than one method. For example, \$latex 2xy +
(x\^2 + y\^2)\\frac{dy}{dx}=0\$ has coefficients that are both
homogeneous of order 2, and is also exact, so it can be solved by either
method. The two solvers return differently formatted solutions for each
one. A simpler example is that 1st order ODEs with homogeneous
coefficients can be solved in two different ways. My working solution
was to try them both and then apply some heuristics to return the
simplest one. But sometimes, one way would create an impossible integral
that would hand the integration engine. And it made debugging the two
solvers more difficult because I had to override my heuristic. This also
touches on the third point. Sometimes the solution to an ODE can only be
represented in the form of an unevaluatable integral. SymPy's
`integrate()` function is supposed to return an unevaluated `Integral`
class if it cannot do it, but all too often it will just hang forever.

The solution I came up with was to rewrite dsolve using a hints method.
I would create a new function called `classify_ode()` that would do all
of the ODE classification, removing it from the solving code. By
default, dsolve would still use a predetermined order of matching
methods. But you could override it by passing a "hint" to `dsolve` for
any matching method, and it would apply that method. There would also be
options to only return unevaluated integrals when applicable.

I ended up doing this and more (see the docstrings for `classify_ode()`
and `dsolve()` in the current git master branch), but before I could I
needed to clean up some things. I needed to rewrite all of `dsolve()`
and related functions. Before I started the program, there were some
special cases in dsolve for second order linear homogeneous ODEs with
constant coefficients and one very special case ODE for the expanded
form of \$latex \\frac{d\^2}{dx\^2}(xe\^{-y}) = 0\$.

So the first thing I did was implement a solver for the general
homogeneous linear with constant coefficients case. These are rather
simple to do: you just find the roots of the characteristic polynomial
built off of the coefficients, and then put the real parts of the roots
in front of the argument of an exponential and the imaginary parts in
front of the arguments of a sine and cosine (for example, \$latex 3 \\pm
2i\$ would give \$latex C1e\^{3x}\\sin{2x} + C2e\^{3x}\\cos{2x}\$. The
thing was, that if the imaginary part is 0, then you only have 1
arbitrary constant on the exponential, but if it is non-zero, you get 2,
one for each trig function. The rest falls out nicely if you plug 0 in
for \$latex b\$ into \$e\^{ax}(C1\\sin{bx} + C2\\cos{box})\$ because the
sine goes to 0 and the cosine becomes 1. But you would end up with
\$latex C1 + C2\$ instead of just \$latex C1\$ in that case. I had
already planned on doing arbitrary constant simplification as part of my
project, so I figured I would put this on hold and do that first. Then,
once that was done, the homogeneous case would be reduced to 1 case
instead of the usual 2 or 3.

My original plan was to make an arbitrary constant type that
automatically simplified itself. So, for example, if you entered
`C1 + 2 + x` with `C1` an arbitrary constant, it would reduce to just
`C1 + x`. I worked with Ondrej, including visiting him in Los Alamos,
and we build up a class that worked. The problem was that, in order to
have auto-simplification, I had to write the simplification directly
into the core. Neither of us liked this, so we worked a little bit on a
basic core that would allow auto-simplification to be written directly
in the classes instead of in the `Mul.flatten()` and `Add.flatten()`
methods. It turns out that my constant class isn't the only thing that
would benefit from this. Things like the order class (O(x)) and the
infinity class (oo) are auto-simplified in the core, and things could be
much cleaner if they happened in the classes themselves. Unfortunately,
modifying the core like this is not something that can happen overnight
or even in a few weeks. For one thing, it needed to wait until we had
the new assumptions system, which was another Google Summer of Code
project running parallel to my own. So we decided to shelf the idea.

I still wanted constant simplification, so I settled with writing a
function that could do it instead. There were some downsides to this.
Making the function as general as the classes might have been would have
been far too much work, so I settled on making it an internal-only
function that only worked on symbols named `C1`, `C2`, etc. Also, unlike
writing the simplification straight into `Mul.flatten()` which was as
simple as removing any terms that were not dependent on x, writing a
function that parsed an expression and simplified it was considerably
harder to write. I managed to churn out something that worked, and so I
was ready to finish up the solver I had started a few paragraphs ago.

After I finished that, I still needed to maintain the ability to solve
that special case ODE. Apparently, it is an ODE that you would get
somewhere in deriving something about relativity, because it was in the
relativity.py example file. I used Maple's excellent `odeanalyser()`
function (this is where I go the idea for my `classify_ode()`)to find a
simple general case ODE that it fit (Liouville ODE). After I finished
this, I was ready to start working on the hints engine.

It took me about a week to move all classification code into
`classify_ode()`, move all solvers into individual functions, separate
simplification code into yet other functions, and tie it all together in
`dsolve()`. In the end, the model worked very well. The modularization
allowed me to do some other things that I had not considered, such as
creating a special "best" hint that used some heuristics that I
originally developed for first order homogeneous which always has two
possible solutions to try to give the best formatted solution for any
ODE that has more than one possible solution method. It also made
debugging individual methods much easier, because I could just use the
built in hint calls in `dsolve()` instead of commenting out lines of
code in the source.

This was good, because there was one more method that I wanted to
implement. I wanted to be able to solve the inhomogeneous case of a nth
order linear ode with constant coefficients. This can be done in the
general case using the method of variation of parameters. It was quite
simple to set up variation of parameters up in the code. You only have
to set up a system of integrals using the Wronskian of the general
solutions. It would usually be a very poor choice of a method if you
were trying to solve an ODE by hand because taking the Wronskian and
computing n integrals is a lot of work. But for a CAS, the work is
already there. I just have to set up the integrals.

It soon became clear that even though, in theory, the method of
variation of parameters can solve any ODE of this type, in practice, it
does not always work so well in SymPy. This is because SymPy have very
poor simplification, especially trigonometric simplification, so
sometimes there would be a trigonometric Wronskian that would be
identically equal to some constant, but it could only simplify it to
some very large rational function of sines and cosines. When these were
passed to the integral engine, it would cause it to fail, because it
could not find the integral for such a seemingly complex expression.

In addition, taking Wronskians, simplifying them, and then taking n
integrals is a lot of work as I said, and even when SymPy could do it,
it took a long time. There is another method for solving these types of
equations called undetermined coefficients that does not require
integration. It only works on a class of ODEs where the right hand side
of the ODE is a simple combination of sines, cosines, exponentials, and
polynomials in x. It turns out that these kinds of functions are common
anyway, so most ODEs of this type that you would encounter could be
solved with this method. Unlike variation of parameters, undetermined
coefficients requires considerable setup, including checking for
different cases. This would be the method that you would want to use if
you had to solve the ODE by hand because, even with all the setup, it
only requires solving a system of linear equations vs. solving n
integrals with variation of parameters, but for a CAS, it is the setup
that matters, so this was a difficult prospect.

I spent the last couple of weeks writing up the necessary algorithms to
setup the required system of linear equations and handling the different
cases. After I finally worked out all of the bugs, I ran some profiling
against my variation of parameters solver. It turned out that for ODEs
that had trigonometric solutions (which take longer to simplify), my
undetermined coefficients solver was an order of magnitude faster than
the variation of parameters solver (and that is just for the ODEs that
the variation of parameters engine could even solve at all). For ODEs
that only had exponentials, it was still 2-4 times faster.

I finished off the summer by writing extensive documentation for all of
my solvers and functions. Hopefully someone who uses SymPy to solve ODEs
can learn something about ODE solving methods as well as how to use the
function I wrote when they read my documentation.

**Post-GSoC**  
I plan on continuing development with SymPy now that the Google Summer
of Code period is over. SymPy is an amazing project, mixing Python and
Computer Algebra, and I want to help it grow. I may even apply again in
a future year to implement some other thing in SymPy, or maybe apply as
a mentor for SymPy to help someone else improve it.

**Advice**  
What follows is some general advice for someone who wants to apply for
Google Summer of Code. Some of the advice pertains specifically to
SymPy, and some of it is general advice that I think would apply to any
project.

- Get involved early. As soon as you decide that you want to participate
in Google Summer of Code, start getting involved in the project. Get
into contact with them and discuss possible projects. If you are looking
before the participating organizations are announced, look at the
organizations from previous years. For some organizations, it will vary;
for others (like Python), it is almost given that they will be accepted
every year.

- Some projects (including SymPy) require you to send in a patch that
passes review to be accepted. This will give you a change to start
familiarizing yourself with the code base. If you are applying to SymPy,
the Wester example I mentioned above is a really good way to learn what
SymPy can do and how it works.

- Subscribe to the mailing list, and once you are comfortable with it,
participate. Also, it is a good idea to idle in IRC (SymPy is on
freenode at \#sympy). This will help you get to know the main
contributors for the project.

- For you application, see if the people in the project you are applying
for will review it. If they like your project idea, they will try to
help you write a good application so you can be accepted and you can
implement it. If they don't like your idea, then they will tell you and
you should change it, otherwise you will not be accepted, no matter how
well written your proposal is. I have my proposal on the wiki (see link
above). I am not saying that it is necessarily a very good proposal, but
it did get accepted. If you are applying to SymPy, Ondrej will proofread
your applications for you.

- If you are an IRC fan, there is also \#gsoc on freenode, where you can
ask all your GSoC related questions. Be warned that it does get pretty
noisy in the application period, especially right before the
applications are due and right before proposals are accepted.

- I cannot stress this one enough. If you have never worked with a
version control system before, it is perhaps more important to spend
your time learning it than it is to learn the code base for your
project. These things have a steep learning curve if you have never used
them before. Once you master them though, they can make your life much
easier. Also, the sooner you learn to use them well, the easier your
life will be later on down the road. I spent a good part of the last
week of GSoC cleaning up my commit history from the first half of the
summer when I bad very poor committing/log habits. If your project uses
git, such as SymPy does, you might look at [this][] tutorial. If it uses
something else, good luck. Seriously, git is the only good version
control system. See [this video][].

- Expect to spend only about half of the summer actually implementing
stuff. You may think that you are a good programmer and that your code
will not be so buggy that you will need to spend that much time fixing
bugs, and you may be right. But the fact is, you will be working on code
bases written by may programmers that are not so good. You will need to
fix several already existing bugs to make your code work, which means
that you will need to learn the code base well, learn how to read other
people's code, and how to fix bugs that you had no part in creating. You
will be glad if a bug is in your code because you will usually know
immediately what causes it and how to fix it. But if a bug is somewhere
else, you will need to find it, figure out why it happens, what is
supposed to happen, and how to fix it without breaking anything else.
This is also why it is important to be active in the developer
community.

- Good luck.

  [SymPy Wiki]: http://wiki.sympy.org/wiki/User:Asmeurer/GSoC2009_Application
  [EasyToFix issues]: http://code.google.com/p/sympy/issues/list?q=label:EasyToFix
  [issue 694]: http://code.google.com/p/sympy/issues/detail?id=694
  [book]: http://books.google.com.np/books?id=29utVed7QMIC&lpg=PA24&ots=uxLSUKt_3P&hl=en&pg=PA56#v=onepage&q=&f=false
  [this]: http://www-cs-students.stanford.edu/~blynn//gitmagic/
  [this video]: http://www.youtube.com/watch?v=4XpnKHJAok8
