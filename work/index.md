Here are some things that I've worked on. Most of what I do is open source,
and most of my open source work is on my
[GitHub page](https://github.com/asmeurer). Everything I do is
[liberally licensed](http://copyfree.org/) (BSD or MIT) if possible.

# Main projects

- [SymPy](http://www.sympy.org/en/index.html), a
  [computer algebra system](https://en.wikipedia.org/wiki/Computer_algebra_system)
  in Python. My first foray into open source was with
  [Google Summer of Code](https://summerofcode.withgoogle.com/) with SymPy in 2009.
  I've been an active contributor ever since, and am now the lead developer.

  I've touched most parts of SymPy, but the parts that I'm most proud of are
  the [ODE module](http://docs.sympy.org/latest/modules/solvers/ode.html) (my
  2009 GSoC project), the implementation of the
  [Risch integration algorithm](https://en.wikipedia.org/wiki/Risch_algorithm)
  (my 2010 GSoC project), improvements to the assumptions system (an ongoing
  project), and the
  [tutorial](http://docs.sympy.org/latest/tutorial/index.html).

  If you are interested in SymPy or have any questions about it, please email
  the [SymPy mailing list](https://groups.google.com/forum/#!forum/sympy).

- [ndindex](https://quansight-labs.github.io/ndindex/). ndindex is a new library
  that I have started as part of my work at
  [Quansight](https://www.quansight.com/), which can be used to represent and
  manipulate indices to NumPy arrays (e.g., slices).

# Side stuff

Stuff I've done on my own. In no particular order.

- [Brown Water Python](https://www.asmeurer.com/brown-water-python/). Better
  documentation for Python's
  [tokenize](https://docs.python.org/3/library/tokenize.html) module (in the
  spirit of Thomas Kluyver's [Green Tree
  Snakes](https://greentreesnakes.readthedocs.io/en/latest/)).

- [removestar](https://www.asmeurer.com/removestar/). A tool to automatically
  replace `import *` with explicit imports in Python files.

- [mypython](https://github.com/asmeurer/mypython). I wrote my own Python
  REPL.

- [catimg](https://github.com/asmeurer/catimg/). Shows an random image of a
  cat from Imgur inline in the iTerm2 terminal.

- [prefsync](https://github.com/asmeurer/prefsync), a little tool to help
  sync OS X plist files in a human-readable format.

- [dotfiles](https://github.com/asmeurer/dotfiles). All my dot files
  (configuration files) for various things. Mostly my emacs and bash
  configuration.

- A walkthrough of the
  [GitHub workflow](http://asmeurer.com/git-workflow) for contributing
  to open source projects.

- This [blog](https://github.com/asmeurer/blog).

- My [old blog](https://asmeurersympy.wordpress.com/). Contains posts from
  when I was a Google Summer of Code student, posts about when I moved to
  emacs, and other interesting things about Python and mathematics.

- A
  [presentation](https://asmeurer.github.io/python3-presentation/slides.html)
  about why you should be using Python 3.


# Open source projects that I use heavily and contribute to

(though some not as much as I would like)

- [PuDB](http://mathema.tician.de/debug-python-in-style/), a curses-based
  debugger for Python. It has been an essential tool for debugging and
  understanding Python code. I wrote some
  [blog](https://asmeurersympy.wordpress.com/2010/06/04/pudb-a-better-python-debugger/)
  [posts](https://asmeurersympy.wordpress.com/2011/08/08/hacking-pudb-now-an-even-better-python-debugger/)
  in the past about it.

- [Prompt Toolkit](https://github.com/jonathanslenders/python-prompt-toolkit),
  a library for building interactive prompt-based terminal applications, such
  as shells and REPLs. I use this heavily in mypython (see above).

- [NumPy](https://numpy.org/) is the core library for numerics in Python,
  which implements the standard array type and some common algorithms. I have
  contributed to NumPy, specifically the `numpy.array_api` module (see the
  next bullet).

- [Array API specification](https://data-apis.org/array-api/latest/) is a
  specification for Python array APIs, such as NumPy and other similar
  libraries. I have worked on this as part of my work at Quansight, including
  work on the official [test
  suite](https://github.com/data-apis/array-api-tests) as well as the [NumPy
  implementation of the
  specification](https://numpy.org/doc/stable/reference/array_api.html).

- [Numba](https://numba.pydata.org/). Numba is JIT compiler for Python that
  lets you write pure Python code that executes as fast as compiled code. I
  have contributed to Numba as part of my work at
  [Quansight](https://www.quansight.com/).

- [Conda](http://conda.pydata.org/docs/), a package manager. I worked on conda
  when I was at [Continuum Analytics](http://continuum.io/) (now called
  Anaconda). Conda is the package manager included with the [Anaconda
  distribution](https://www.anaconda.com/products/individual). I no longer
  work on conda, so if you have any questions about it, you should reach out
  to the support channels at Anaconda.

- [conda-forge](https://conda-forge.org/) is a free distribution of conda
  packages maintained by the community. While I am not involved in the
  conda-forge core development, I do help maintain several package
  [feedstocks](https://github.com/orgs/conda-forge/teams?query=%40asmeurer).
