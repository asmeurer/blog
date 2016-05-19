About a month ago I tweeted this:

<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">Thought: get the maintainers of a bunch of big Python libraries to sign something saying that they WILL drop Python 2.7 support in 2020.</p>&mdash; Aaron Meurer (@asmeurer) <a href="https://twitter.com/asmeurer/status/712304912428875776">March 22, 2016</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

For those of you who don't know, Python 2.7 is
[slated](https://docs.python.org/devguide/#status-of-python-branches) to reach
end-of-life in 2020 (originally, it was slated to end in 2015, but it was
extended in 2014, due to the extraordinary difficulty of moving to a newer
version). "End-of-life" means absolutely no more support from the core Python
team, even for security updates.

I'm writing this post because I want to clarify why I think this should be
done, and to clear up some misconceptions, the primary one being that this
represents library developers being antagonistic against those who want or
have to use Python 2.

I'm writing this from my perspective as a library developer. I'm the lead
developer of [SymPy](http://www.sympy.org/), and I have sympathies for
developers of other libraries.[^sympy] I say this because my idea may seem a bit
in tension with "users" (even though I hate the "developer/user" distinction).

## Python 2

There are a few reasons why I think libraries should drop (and announce that
they will drop) Python 2 support by 2020 (actually earlier, say 2018 or 2019,
depending on how core the library is).

First, library developers have to be the leaders here. This is apparent from
the historical move to Python 3 up to this point. Consider the three (not
necessarily disjoint) classes of people: CPython core developers, library
developers, and users. The core developers were the first to move to Python 3,
since they were the ones who wrote it. They were also the ones who provided
the messaging around Python 3, which has varied over time. In my opinion, it
should have been and should be more forceful.[^core] Then you have the library
developers and the users. A chief difference here is that users are probably
going to be using only one version of Python. In order for them to switch that
version to Python 3, all the libraries that they use need to support it. This
took some time, since library developers saw little impetus to support Python
3 when no one was using it (Catch 22), and to worsen the situation, versions
of Python older than 2.6 made
[single codebase compatibility](https://asmeurersympy.wordpress.com/2013/08/22/python-3-single-codebase-vs-2to3/)
almost impossible.

Today, though, [almost all libraries](http://py3readiness.org/) support Python
3, and we're reaching a point where those that don't have
forks that do.

But it only happened *after* the library developers transitioned. I believe
libraries need to be the leaders in moving away from Python 2 as well. It's
important to do this for a few reasons:

- Python 2.7 support ends in 2020. That means all updates, including security
  updates. For all intents and purposes, Python 2.7 becomes an insecure
  language to use at that point in time.

- Supporting two major versions of Python is technical debt for every project
  that does it. While writing cross compatible code is
  [easier than ever](http://python-future.org/), it still remains true that
  you have to remember to add `__future__` imports to the top of every file,
  to import all relevant builtins from your compatibility file or library, and
  to run all your tests in both Python 2 and 3. Supporting both versions is a
  major cognitive burden to library developers, as they always have to be
  aware of important differences in the two languages. Developers on any
  library that does anything with strings will need to understand how things
  work in both Python 2 and 3, and the often obscure workarounds required for
  things to work in both (pop quiz: how do you write Unicode characters to a
  file in a Python 2/3 compatible way?).

- Some of Python 3's
  [new syntax features](https://asmeurer.github.io/python3-presentation/slides.html)
  (i.e., features that are impossible to use in Python 2) only matter for
  library developers. A great example of this is
  [keyword-only arguments](https://www.python.org/dev/peps/pep-3102/). From an
  API standpoint, almost every instance of keyword arguments should be
  implemented as keyword-only arguments. This avoids mistakes that come from
  the antipattern of passing keyword arguments without naming the keyword, and
  allows the argspec of the function to be expanded in the future without
  breaking API.[^swift]

The second reason I think library developers should agree to drop Python 2
support by 2020 is completely selfish. A response that I heard on that tweet
(as well as elsewhere), was that libraries should provide carrots, not sticks.
In other words, instead of forcing people off of Python 2, we should make them
want to come to Python 3. There are some issues with this argument. First,
Python 3 already has
[tons of carrots](https://asmeurer.github.io/python3-presentation/slides.html).
Honestly, not being terrible at Unicode ought to be a carrot in its own right.[^unicode]

If you don't deal with strings, or do but don't care about those silly
foreigners with weird accents in their names, there are other major carrots as
well. For SymPy, the fact that 1/2 gives 0 in Python 2 has historically been a
major source of frustration for new users. Imagine writing out `1/2*x +
x**(1/2)*y*z - 3*z**2` and wondering why half of what you wrote just
"disappeared" (granted, this was worse before we
[fixed the printers](https://asmeurersympy.wordpress.com/2011/08/18/sqrtx-now-prints-as-sqrtx/)).
While `integer/integer` not giving a rational number is a major
[gotcha](http://docs.sympy.org/latest/tutorial/gotchas.html#two-final-notes-and)
for SymPy, giving a float is infinitely better than giving what is effectively
the wrong answer. Don't use strings or integers?
[I've got more](https://asmeurer.github.io/python3-presentation/slides.html).

Frankly, if these "carrots" haven't convinced you yet, then I'll wager you're
not really the sort of person who is persuaded by carrots.

Second, some "carrots" are impossible unless they are implemented in
libraries. While some features can be implemented in 2/3 compatible code and
only work in Python 3 (such as `@` matrix multiplication), others, such as
keyword-only arguments, can only be implemented in code that does not support
Python 2. Supporting them in Python 2 would be a net deficit of technical debt
(one can imagine, for instance, trying to support keyword-only arguments
manually using `**kwargs`, or by using some monstrous meta-programming).

Third, as I said, I'm selfish. Python 3 *does* have carrots, and I want them.
As long as I have to support Python 2 in my code, I can't use keyword-only
arguments, or extended argument unpacking, or async/await, or any of the
dozens of features that can't be used in cross compatible code.

A counterargument might be that instead of blocking users of existing
libraries, developers should create new libraries which are Python 3-only and
make use of new exciting features of Python 3 there. I agree we should do
that, but existing libraries are good too. I don't see why developers should
throw out all of a well-developed library just so they can use some Python
features that they are excited about.

## Legacy Python

A lot of people have taken to calling Python 2
"[legacy Python](https://twitter.com/RipLegacyPython)". This phrase is often
used condescendingly and
[angers a lot of people](https://twitter.com/stephtdouglas/status/713433933040340993)
(and indeed, this blog post is the first time I've used it myself). However, I
think Python 2 really should be seen this way, as a "legacy" system. If you
want to use it, for whatever your reasons, that's fine, but just as you
shouldn't expect to get any of the newest features of Python, you shouldn't
expect to be able to use the newest versions of your libraries. Those
libraries that have a lot of development resources may choose to support older
Python 2-compatible versions with bug and/or security fixes. Python 2 itself
will be supported for these until 2020. Those without resources probably won't
(keep in mind that you're using open source libraries without paying for
them—the developers literally owe you nothing).

I get that some people have to use Python 2, for whatever reasons. But using
outdated software comes at a cost. Libraries have borne this technical debt
for the most part thus far, but they shouldn't be expected to bear it forever.
The debt will only increase, especially as the technical opportunity cost, if
you will, of not being able to use newer and shinier versions of Python 3
grows. The burden will have to shift at some point. Those with the financial
resources may choose to offload this debt to others,[^continuum] say, by
backporting features or bugfixes to older library versions that support Python
2 (or by helping to move code to Python 3).

I want to end by pointing out that if you are, for whatever reason, still
using Python 2, you may be worried that if libraries become Python 3-only and
start using Python 3 features, won't that break your code? The answer is no.
Assuming package maintainers mark the metadata on their packages correctly,
tools like pip and conda will not install non-Python 2 compatible versions
into Python 2.

If you haven't transitioned yet, and want to know more, a good place to start
is the [official docs](https://docs.python.org/3/howto/pyporting.html). I also
highly recommend using [conda](http://conda.pydata.org/docs/) environments, as
it will make it easy to separate your Python 2 code from your Python 3 code.

### Footnotes

[^sympy]: With that being said, the opinions here are entirely my own, and are
        don't necessarily represent those of other people, nor do they
        represent official SymPy policy (no decisions have been made by the
        community about this at this time).

[^core]: It often feels like core Python itself doesn't really want people to
        use Python 3. It's little things, like
        [docs links](https://docs.python.org/library/) that redirect to Python
        2, or [PEP 394](https://www.python.org/dev/peps/pep-0394/), which
        still says that the `python` should always point to Python 2.


[^swift]: In Swift, Apple's new language for iOS and OS X, function parameter
        names are effectively "keyword-only"
        [by default](https://developer.apple.com/library/ios/documentation/Swift/Conceptual/Swift_Programming_Language/Functions.html).

[^unicode]: As an example of this, in conda, if you use Python 2 in the root
        environment, then installing into a path with non-ASCII characters is
        unsupported. This is common on Windows, because Windows by default
        uses the user's full name as the username, and the default conda
        install path is in the user directory.

    This is unsupported except in Python 3, because to fix the issue,
    every single place in conda where a string appears would have to be
    changed to use a `unicode` string in Python 2. The basic issue is that
    things like `'π' + u'i'` raise `UnicodeDecodeError` in Python 2 (even
    though `'π' + 'i'`, `u'π' + 'i'`, and `u'π' + u'i'` all work fine).
    You can read a more in-depth description of the problem
    [here](https://github.com/sympy/sympy/pull/9692#issuecomment-126162173).
    Incidentally, this is also why you should never use `from __future__
    import unicode_literals` in Python 2, in my opinion.

    Even though I no longer work on conda, as far as I know, the
    [issue](https://github.com/conda/conda/issues/1180) remains unfixed.
    Of course, this whole thing works just fine if conda is run in Python
    3.


[^continuum]: If that legitimately interests you, I
        [hear Continuum](https://twitter.com/pwang/status/712780279211884546)
        may be able to help you.
