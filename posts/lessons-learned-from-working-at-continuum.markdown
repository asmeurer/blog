Last Friday was my last day working at Continuum Analytics. I enjoyed my
time at the company, and wish success to it, but the time has come for me to
move on. Starting later this year, I will start working with
[Anthony Scopatz](https://twitter.com/scopatz) at his new lab
[ERGS](http://www.ergs.sc.edu/index.html) at the University of South
Carolina.

During my time at Continuum (over two years if you count a summer internship),
I primarily worked on the
[Anaconda distribution](https://www.continuum.io/downloads) and its open
source package manager, [conda](http://conda.pydata.org/).  I learned a lot of
lessons in that time, and I'd like to share some of them here.

In no particular order:

- Left to their own devices, people will make the minimal possible solution to
  packaging. They won't try to architect something. The result will be
  over-engineered, specific to their use-case, and lack reproducibility.

- The best way to ensure that some software has no bugs is for it to have many
  users.

- Be wary of the "software would be great if it weren't for all the users"
  mentality (cf. the previous point).

- Most people don't code defensively. If you are working on a project that
  requires extreme stability, be cautious of contributions from those outside
  the development team.

- Hostility towards Windows and Windows users doesn't help anyone. >50% of
  Anaconda downloads are on Windows.

- For a software updater, stability is the number one priority. If the updater
  breaks, how can a fix be deployed?

- Even if you configure your program to update itself every time it runs you
  will still get bug reports with arbitrarily old versions.

- Separating components into separate git repositories leads to a
  philosophical separation of concerns among the components.

- Everyone who isn't an active developer on the project will ignore this
  separation and open issues in the wrong repo.

- Open source is more about the open than the source. Develop things in the
  open, and you will create a community that respects you.[^*]

- Academics (often) don't know good software practices, nor good licensing
  practices.

- Neither do some large corporations.

- Avoid over-engineering things.

- Far fewer people than I would have thought understand how hard links work.[^**]

- Changelogs are useful.

- Semantic versioning is over-hyped.

- If you make something and release it, the first version should be 1.0 (not
  0.1 or 0.0.1).

- Getting a difficult package to compile is like hacking a computer. All it
  takes is time.

- It doesn't matter how open source friendly your business is, there will
  always be people who will be skeptical and point their fingers at the
  smallest proprietary components, fear monger, and overgeneralize unrelated
  issues into FUD. These people should generally be ignored.

- People always assume you have way more automation than you really do.

- The Python standard library is not a Zen garden. Some parts of it are
  completely broken, and if you need to rely on them, you'll have to rewrite
  them. `shutil.rmtree` on Windows is one example of this.

- Linux is strictly forwards compatible. Windows is strictly backwards
  compatible.

- On Linux, things tend to be very simple. On Windows, things tend to be very
  complicated.

- I can't decide about OS X. It lies somewhere in between.

- Nobody uses 32-bit Linux. Why do we even support that?

- People oversimplify the problem of solving for package dependencies in their
  heads.  No one realizes that it's meaningless to say something like "the
  dependencies of NumPy" (every build of every version of NumPy has its own
  set of dependencies, which may or may not be the same).

- Writing a set of rules and a solver to solve against those rules is
  relatively easy. Writing heuristics to tell users why those rules are
  unsolvable when they are is hard.

- Some of the smartest people I know, who otherwise make very rational and
  intelligent decisions, refuse to update to Python 3.

- As an introvert, the option of working from home is great for maintaining
  sanity.

- [Aeron chairs are awesome](http://blog.codinghorror.com/a-developers-second-most-important-asset/).

- If living in Austin doesn't turn you into a foodie you will at least gain a
  respect for them.

- Twitter, if used correctly, is a great way to interact with your users.

- Twitter is also a great place to learn new things. Follow
  [John Cook](https://twitter.com/JohnDCook) and
  [Bret Victor](https://twitter.com/worrydream).

- One of the best ways to make heavily shared content is to make it on git
  (at least if you're an expert).

- A good optimization algorithm avoids getting caught in local maxima by
  trying different parts of the search space that initially appear to be
  worse. The same approach should be taken in life.

And some things that I already knew, but were reiterated:

- Don't feed the trolls.

- Avoid object oriented programming when procedural programming will do just
  fine.

- SAT solvers solve NP-complete problems in general, but they can be very fast
  to solve common case problems.

[^*]: These are things that I already knew, but were reiterated.

[^**]: If you are one of those people, I have a small presentation that
       explains the difference [here](https://speakerdeck.com/asmeurer/hard-links-and-soft-links)
