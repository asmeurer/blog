Here are some things that I've worked on. Most of what I do is open source,
and most of my open source work is on my
[GitHub page](https://github.com/asmeurer).

# Main projects

- [SymPy](http://www.sympy.org/en/index.html), a
  [computer algebra system](https://en.wikipedia.org/wiki/Computer_algebra_system)
  in Python. My first foray into open source was with
  [Google Summer of Code](https://www.google-melange.com/) with SymPy in 2009.
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

- [Conda](http://conda.pydata.org/docs/), a package manager. I work primarily
  on conda for my day job at
  [Continuum Analytics](http://continuum.io/). Conda is the package manager
  included with [Anaconda](http://continuum.io/downloads), a free collection
  of open source packages for doing science, math, engineering, data
  analysis in Python.

  I gave a talk about conda at SciPy 2014. <iframe width="560" height="315"
  src="https://www.youtube.com/embed/UaIvrDWrIWM" frameborder="0"
  allowfullscreen></iframe>.

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

# Side stuff

Stuff I've done on my own. In no particular order.

## Good stuff

- [prefsync](https://github.com/asmeurer/prefsync), a little tool to help
  sync OS X plist files in a human-readable format.

- [dotfiles](https://github.com/asmeurer/dotfiles). All my dot files
  (configuration files) for various things. Mostly my emacs and bash
  configuration.

- A walkthrough of the
  [GitHub workflow](https://github.com/asmeurer/git-workflow) for contributing
  to open source projects.

- This [blog](https://github.com/asmeurer/blog).

- A
  [presentation](https://asmeurer.github.io/python3-presentation/slides.html)
  about why you should be using Python 3.

## Funny stuff

- Some interesting [spam](https://github.com/asmeurer/spam) I've received. The
  [deaththreat](https://github.com/asmeurer/spam/blob/master/deaththreat) one
  is pretty funny.

## Not so good stuff

- A [script](https://github.com/asmeurer/markov) to generate text from
  Hangouts chat using markov chains.

- [Miscellaneous Useful Scripts](https://github.com/asmeurer/Miscellaneous-Useful-Scripts),
  some miscellaneous useless scripts. Mostly crap from before I could
  program. The
  [folder cleanup](https://github.com/asmeurer/Miscellaneous-Useful-Scripts/blob/master/folder_cleanup.py)
  script is useful, though.
