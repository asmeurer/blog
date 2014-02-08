Title: Advice for Future Prospective GSoC Students
Date: 2011-04-27 21:15
Author: asmeurer
Category: Uncategorized
Slug: advice-for-future-prospective-gsoc-students

So now that Google has [announced the results][] of Google Summer of
Code, I want to write down some general things that I noticed when
reviewing applications while they are still fresh in my mind.

Note that none of these things apply to any specific student who applied
to SymPy. Many of these things are things that I noticed that people did
right.

Most of this should apply to any organization, though some of them might
be SymPy specific, since that is the lens that I am viewing this
through. These aren't really in any particular order.

1.  **Fulfill all the requirements.** This is kind of a no brainer, and
    as it turns out, almost all students who applied to SymPy did indeed
    do this. For SymPy, this means that you should submit a patch by the
    deadline. Other organizations might have other requirements. If you
    don't fulfill the requirements, it doesn't matter how good your
    application is; you won't be eligible and hence won't be accepted.
2.  **Discuss your proposal on the mailing list.** A proposal submitted
    out of the blue has a poor chance of being accepted. First, we like
    to see that you will be involved in the community, and if you don't
    discuss the proposal at all, it shows badly. Second, it is very
    likely that we will not like something about your proposal, or will
    have questions (see the next point). If you don't discuss it at all,
    you are making a shot in the dark. Even if the proposal is good, it
    could be rejected simply because it's not something that we feel
    that we want. And you don't want to accidentally submit a proposal
    to do something that has already been implemented.
    <p>
    It's important to discuss it on the public mailing list, not just
    with a specific mentor. Even if that mentor is the expert on your
    project subject and would likely be the person to mentor you if you
    are accepted, you need to remember that all the mentors review the
    proposals and decide who to accept. Also, this year for SymPy, we
    are trying to put an emphasis on students doing things publicly with
    the whole community, instead of just with their mentors.
3.  **Ask the mentors for advice on your proposal, and then follow it.**
    Again, most students who applied to SymPy were good on this one too.
    We request that all students put their proposals on the GitHub wiki,
    so that the mentors can take a look at them and give advice. If you
    feel uncomfortable putting your application in a public place, send
    it to some mentors privately.
    <p>
    But the most important thing here is to actually follow any advice
    that the mentors give you. If they tell you that you should expand
    your timeline section, you should expand your timeline section. If
    they tell you you should discuss the implementation more, you should
    do that (see the next point). If you don't follow the advice, it
    looks to the mentor like you didn't listen to him, which doesn't
    make you appear like a good candidate for acceptance. Also, the
    things that they tell you to improve will tend to be the things that
    they will look at when reviewing your proposal.
4.  **Don't just discuss the theory.** I suspect that this may be more
    of a problem with SymPy than for other organizations, because SymPy
    is very math based, so many of the proposals to SymPy involve
    complex mathematics. One of the biggest issues I saw in proposals
    was that students discussed the theory of what they wanted to
    implement too much and not enough of the actual implementation. It's
    easy to do this, but discussing the implementation is actually more
    important than the theory of what you want to do.

    An easy way to do this is to give a "fake" example session showing
    how your code might work after it is completed. For example, if you
    were writing a proposal for a PDE solver, you might include
    something like

    [code language="py"]  
    \>\>\> u = Function('u')  
    \>\>\> \# Solve the Heat Equation in one dimension  
    \>\>\> pdesolve(u(x, t).diff(t) - c\*\*2\*u(x, t).diff(x, x), u(x),
    {u(x, 0):f(x), u(0, t):0, u(0, pi):0}, method='separation of
    variables')  
    2/pi\*Sum(Integral(f(x)\*sin(n\*x),
    x)\*sin(n\*x)\*exp(-n\*\*2\*c\*\*2\*t), (n, 1, oo))  
    \>\>\> \# Use Fourier Transforms to get d'Alembert's Solution to
    the Wave Equation  
    \>\>\> …  
    [/code]

    in your proposal. Just saying "I plan to implement solvers for PDEs
    using separation of variables and Fourier Transforms" tells us only
    what we already know, which is that you can solve PDEs using
    separation of variables and Fourier Transforms. What we don't know
    is how it will look. The above example shows how the PDE,
    initial/boundary conditions, and method are entered by the user, and
    how the output looks.

    <p>
    A more advanced thing that you can do is to give actual prototype
    code. This is not required, but it can show that you are dedicated
    enough to get a start, and can demonstrate how things will work for
    more complicated projects.

5.  **But theory is important too.** This might also be a problem more
    in SymPy, but maybe not. The mathematical backgrounds of SymPy
    developers ranges quite a bit. For example, I know a lot about the
    complicated Risch Algorithm for symbolic integration that the
    majority of people (even among SymPy developers) know hardly
    anything about, but I know basically nothing about quantum
    mechanics. So that more mentors can have a chance to even have a
    clue about what you are talking about when they are reviewing your
    proposal, you should try to explain things to a general audience, at
    least in the introduction of your proposal. It can also help to
    explain why your project would be useful, so that even if someone
    doesn't know what it is, they can see why it would be nice to have.
    This doesn't mean that you should sacrifice details by dumbing
    everything down. There's a pretty good chance that someone will
    understand what you are talking about in your specifics, but you
    should also explain things from the other end.
    <p>
    If you are implementing a specific algorithm, maybe you could give a
    brief overview of the algorithm. This will not only explain things
    to the mentors who might not know how it works, but also it shows
    that you know how it works too.
6.  **Be involved in the community.** We understand that students have
    classes during the application period, but the more you involve
    yourself in the community beyond the patch requirement (or whatever
    requirement some other org might have), the better your chances of
    being accepted. Every org has to take risks accepting students,
    because there is always the chance that they will fail. This is not
    good for anyone: the student doesn't get paid the full stipend and
    the organization looses not only the project that would have been
    implemented, but also the slot that they could have given to someone
    who wouldn't have failed. Involving yourself in the community early
    is the best way to show the community that you are a low risk for
    failure.
7.  **The proposal is the most important thing.** But don't assume that
    just because you are involved in the community that you will be
    accepted. The most important thing is the proposal. If you don't
    have a good proposal, we will not even consider the rest of your
    activity. So you should focus most of your energy on writing a high
    quality proposal. The quality of the patch and your involvement in
    the community are secondary considerations after the quality of the
    proposal. These might be used to narrow down the list of good
    proposals to fit the number of slots Google gives us and the number
    of mentors we have available, but the first phase is always to
    narrow down the list based on the quality of the proposals.
8.  **Use a consistant nickname, preferably one based on your real
    name.** This is something that I think most people do not realize.
    If your real name is John Smith, and your IRC nick, GitHub handle,
    Google Code handle, and GSoC link\_id are all jsmith, it makes it
    very easy for me to associate in my mind: "OK, that person who just
    submitted that patch is the same person I talked to on IRC last
    week, and I remember reading his proposal on google-melange.com."
    But if your real name is John Smith, your IRC nick is freebird, your
    GitHub handle is mr.nice, your Google Code handle is smithy, and
    your link\_id on google-melange.com is johnhsmith, I can have a very
    hard time associating your work in one place with your work in
    another (my apologies if those are anybodys' real nicknames; I just
    made them up to make the point here). Maybe you actually have been
    very active in the IRC channel, but it is hard for me to realize
    that based on your nick vs. your real name. This year for SymPy, we
    had 25 applications by 25 students. None of these students were
    members of the SymPy community a few months ago. It's very hard for
    the other mentors and I to keep track of which nicknames associate
    with which people, and in the end, we may mistakenly believe that
    you haven't done as much as you really have. Your best bet is to use
    one nickname everywhere, and to make it based on your real name, so
    that we can easily tell who it is even based on the nickname. If
    your name is common enough that no one permutation is guaranteed to
    be available everywhere, at least try to be consistent with your
    nickname, or just use different permutations of your real name based
    on what site you are on.

That's all I can think of for now. I kind of wish I had thought of two
more, so I could make it "Ten pieces of advice," but whatever. If any
SymPy mentors or mentors from other projects feel that something is
missing, I would love to hear about it in the comments.

  [announced the results]: http://asmeurersympy.wordpress.com/2011/04/27/accepted-gsoc-students-announced/
