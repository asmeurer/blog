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

- [ndindex](https://quansight.github.io/ndindex/). ndindex is a new library
  that I have started as part of my work at
  [Quansight](https://www.quansight.com/), which can be used to represent and
  manipulate indices to NumPy arrays (e.g., slices).

# Side stuff

Stuff I've done on my own. In no particular order.

- [Doctr](https://drdoctr.github.io/doctr/). A tool for automatically
  deploying docs from Travis CI to GitHub pages
  ([Gil Forsyth](https://github.com/gforsyth/) also works on this).

- [removestar](https://www.asmeurer.com/removestar/). A tool to automatically
  replace `import *` with explicit imports in Python files.

- [Brown Water Python](https://www.asmeurer.com/brown-water-python/). Better
  documentation for Python's
  [tokenize](https://docs.python.org/3/library/tokenize.html) module (in the
  spirit of Thomas Kluyver's [Green Tree
  Snakes](https://greentreesnakes.readthedocs.io/en/latest/)).

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

- [Pyflakes](https://pypi.python.org/pypi/pyflakes), a linter for Python with
  a focus on logical errors only (no stylistic warnings). I use
  [flycheck-pyflakes](https://github.com/Wilfred/flycheck-pyflakes) in emacs
  to highlight errors in Python using pyflakes as I write. It's an essential
  tool for catching stupid mistakes early, and it doesn't bug about style, so
  the annoyance factor is minimal.

- [Jedi](http://jedi.jedidjah.ch/en/latest/), a completion library for
  Python. Jedi is pure magic. I use
  [emacs-jedi](https://tkf.github.io/emacs-jedi/latest/), but there are
  plugins for other editors as well.

- [Pyinstrument](https://github.com/joerick/pyinstrument), a statistical call
  stack profiler. The best way to speed profile Python code, although the
  standard library `profile` module and
  [line_profiler](https://pypi.python.org/pypi/line_profiler) are also good
  (and serve different purposes).

- [Prompt Toolkit](https://github.com/jonathanslenders/python-prompt-toolkit),
  a library for building interactive prompt-based terminal applications, such
  as shells and REPLs. I use this heavily in mypython (see above).

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
