Title: The SciPy 2011 Conference
Date: 2011-07-17 16:32
Author: asmeurer
Category: Uncategorized
Slug: the-scipy-2011-conference

So this past week, I attended the SciPy 2011 conference in Austin, TX,
which was my first conference ever. Here are some highlights of the
conference for me:

-   I met a *ton* of cool people. This included meeting several people
    who I had previously known from mailing lists in person for the
    first time. I met the SymPy developers Mateusz Paprocki and Andy
    Terrel, and I also had already known or heard about people like
    Fernando Perez, Gael Varoquaux, and Robert Kern. There are a lot of
    people out there who are excited to be using Python for their
    research, which is a real refresher from my university, where
    everyone is using Matlab and Maple.
-   Mateusz and I gave a tutorial on SymPy. This was one of the four
    introductory track tutorials. This was a great experience to teach
    SymPy to people. You can see the [Sphinx document][] that we used,
    and there should eventually be a video posted at the [SciPy 2011
    website][].
-   In addition to our tutorial, I attended some of the other tutorials.
    I particularly enjoyed the NumPy tutorial. Having never used NumPy
    before, I now feel comfortable with the basics. I also attended Gael
    Varoquaux's tutorial on scikits.learn and Corran Webster's tutorial
    on Matplotlib, Traits, and Chaco. My only regret is that the
    advanced track and introductory track tutorials were held at the
    same time, so I could not attend half of them. I plan to watch the
    ones I missed online.
-   The general conference was excellent. Some of the talks that I
    particularly enjoyed were:
    -   The keynotes. I found Eric Jone's keynote particularly relevant
        as the leader of SymPy, as he talked about some of the good
        things to do and bad things to not do when leading a scientific
        project. I also enjoyed Perry Greenfield's talk about how the
        astronomy community moved from some old proprietary system to
        Python.
    -   Mateusz gave a talk on his [FEMhub online lab][], which a was
        very impressive system for using Python entirely in the web
        browser.
    -   By far the best talk of the entire conference was Fernando
        Perez's talk on the new IPython 0.11, which will be coming out
        in about a week or so. His demo of the new features such as the
        QT console and html notebook were very impressive. If you want
        to watch just one video from the conference, I would recommend
        that one.
    -   Mark Dewing gave a talk about a system he wrote using SymPy to
        do automated derivation of equations. The system is impressive,
        and contains some features that would be nice to backport to
        SymPy. He told me that he wants to do this, so follow the
        mailing list. You can see what he has so far on his
        [derivation\_modeling][] branch at GitHub.
    -   The lightning talks. These are very short talks at the end of
        the conference that are only five minutes long. In addition to
        many interesting talks, both Mateusz and I gave a lightning
        talk. Mateusz gave a talk on [SymPy Live][], which he recently
        improved to do things like give LaTeX output, and I gave a talk
        on my work with the Risch algorithm. I would also highly
        recommend watch this talk once they post the videos.
    -   Again, regrettably, I could not attend half of the talks because
        they were held at the same time. Fortunately, they filmed all of
        them, so I hope to watch them all online when they are posted
        (and I recommend that you do too).

-   The sprints were a great time for getting together and hacking
    together. I worked with Min Ragan-Kelley to make isympy work with
    the new IPython. Having fixed this, I now want to release 0.7.1 very
    soon, so I used some of the time during the sprints getting ready
    for that. We already have [preliminary release notes][], and my hope
    is to create a release candidate on Monday (tomorrow). I also
    finished up my [MathJax branch][] and finished reviewing and pushed
    in Tom's first GSoC pull request, which has a lot of really cool
    stuff relating to converting hypergeometric functions and Meijer
    G-functions into standard elementary functions. This will all be in
    the release.

    Also at the sprints, Mateusz worked on an extension for our Sphinx
    docs that puts a SymPy Live console right in the docs. You can then
    click on "evaluate" next to any of the code examples, and it will
    run it in SymPy live. And of course, you can then edit it and play
    around with it. He already had a working version of this by the end
    of the sprints (with a few bugs still), but I don't think he has
    pushed it to GitHub yet. I think this is going to be a landmark
    change for our documentation. SymPy Live runs on the App Engine, so
    this approach can be applied to any library that can run in pure
    Python 2.5, and I think a lot of such projects are going to be
    jealous this and want to start using it, because it's very
    impressive and useful.

    <p>
    We also had a couple of people from the conference come to our table
    and work on SymPy. These were people who were new to SymPy, and I
    think attended our tutorial. One of them, Emma Hogan, worked a
    little bit on improving our documentation, and has submitted a [pull
    request][].

-   Austin, TX is a nice city with lots of fun places to go, but it is
    also very humid, which is something I could barely stand (I am used
    to the same heat, but in Albuquerque it is dry heat). One
    interesting thing that some of us went and saw was the bats. The
    bridge over this lake in Austin has over a million bats living under
    it, and at night they all fly out to feed.

There's all kinds of fun and interesting stuff that happened that I did
not mention here. If you are interested in science and Python, I would
highly recommend attending a future SciPy conference.

  [Sphinx document]: http://mattpap.github.com/scipy-2011-tutorial/html/index.html
  [SciPy 2011 website]: http://conference.scipy.org/scipy2011/tutorials.php#mateusz
  [FEMhub online lab]: http://lab.femhub.org/
  [derivation\_modeling]: https://github.com/markdewing/sympy/tree/derivation_modeling
  [SymPy Live]: http://live.sympy.org/
  [preliminary release notes]: https://github.com/sympy/sympy/wiki/Release-Notes-for-0.7.1
  [MathJax branch]: https://github.com/sympy/sympy/pull/491
  [pull request]: https://github.com/sympy/sympy/pull/490
