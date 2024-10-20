Here are some things that I've worked on. Most of what I do is open source,
and most of my open source work is on my
[GitHub page](https://github.com/asmeurer). Everything I do is
[liberally licensed](http://copyfree.org/) (BSD or MIT) if possible.

# Main projects

- [Array API Standard](https://data-apis.org/array-api/latest/). I have been
  invoked in the Data APIs Consortium work on the Array API Standard. I have
  worked on the [standard itself](https://github.com/data-apis/array-api), the
  [array api test suite](https://github.com/data-apis/array-api-tests), the
  [array-api-compat](https://github.com/data-apis/array-api-compat) package,
  and the
  [`numpy.array_api`](https://numpy.org/devdocs/reference/array_api.html)
  minimal implementation. I have given a talk about the array API standard at
  [SciPy 2023](https://www.youtube.com/watch?v=16rB-fosAWw), with a
  [corresponding proceedings
  paper](https://conference.scipy.org/proceedings/scipy2023/aaron_meurer.html).

- [ndindex](https://quansight-labs.github.io/ndindex/). ndindex is a new library
  that I have started as part of my work at
  [Quansight](https://www.quansight.com/), which can be used to represent and
  manipulate indices to NumPy arrays (e.g., slices). I've also written a
  comprehensive [guide to NumPy
  indexing](https://quansight-labs.github.io/ndindex/indexing-guide/index.html)
  which lives in the ndindex documentation

- [Versioned HDF5](https://github.com/deshaw/versioned-hdf5) is a library I
  designed and wrote as part of my work at Quansight. It is an open source Python
  library that adds a versioned abstraction on top of HDF5 files.

- [SymPy](http://www.sympy.org/en/index.html), a [computer algebra
  system](https://en.wikipedia.org/wiki/Computer_algebra_system) in Python.
  I've been a contributor to SymPy since 2009 when I participated in [Google
  Summer of Code](https://summerofcode.withgoogle.com/) as a student, which
  was my introduction to open source.

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

# Presentations

I have given several presentations at conferences, most notably the [SciPy
conference](https://conference.scipy.org/). A selection of my presentations
include:

- **Python Array API Standard: Toward Array Interoperability in the Scientific
  Python Ecosystem** SciPy 2023.
  - [Video](https://www.youtube.com/watch?v=16rB-fosAWw)
  - [Slides](https://speakerdeck.com/asmeurer/python-array-api-standard-toward-array-interoperability-in-the-scientific-python-ecosystem)

- **SymPy Introductory Tutorial** SciPy 2023. Co-presented with Sangyub Lee.
  - [Video](https://www.youtube.com/watch?v=FZWevQ6Xz6U)
  - [Materials](https://github.com/sympy/scipy-2023-tutorial/)

- **SymPy Code generation** SciPy 2016.
  - [Video](https://www.youtube.com/watch?v=nmI-cDAUjdE)
  - [Slides](https://speakerdeck.com/asmeurer/sympy-code-generation)

- **Conda: A Cross Platform Package Manager for any Binary Distribution**
SciPy 2014.
  - [Video](https://www.youtube.com/watch?v=UaIvrDWrIWM)
  - [Slides](https://speakerdeck.com/asmeurer/conda-a-cross-platform-binary-package-manager-for-any-distribution)

# Open source projects that I use heavily and contribute to

(though some not as much as I would like)

- [NumPy](https://numpy.org/) is the core library for numerics in Python,
  which implements the standard array type and some common algorithms. I have
  contributed to NumPy, primarily as part of my work on the array API standard.

- [Array API standard](https://data-apis.org/array-api/latest/) is a standard
  specification for Python array APIs, such as NumPy, PyTorch, and other
  similar libraries. I have worked on this as part of my work at Quansight,
  including work on the official [test
  suite](https://github.com/data-apis/array-api-tests), the [compatibility
  layer](https://data-apis.org/array-api-compat/), and the NumPy
  implementation of the specification.

- [PuDB](http://mathema.tician.de/debug-python-in-style/), a curses-based
  debugger for Python. It has been an essential tool for debugging and
  understanding Python code. I wrote some
  [blog](https://asmeurersympy.wordpress.com/2010/06/04/pudb-a-better-python-debugger/)
  [posts](https://asmeurersympy.wordpress.com/2011/08/08/hacking-pudb-now-an-even-better-python-debugger/)
  in the past about it.

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
