Title: git stash
Date: 2009-06-05 03:56
Author: asmeurer
Category: Uncategorized
Slug: git-stash

I've always wondered what the command is that lets you do stuff like
change branches and checkout to older states without commiting, since
git won't let you do anything if you haven't commited.

Well, I found the answer. It's `git stash`. I think I will be using this
a lot, considering how often my workflow gets interrupted. I wish I knew
about it before I started working on this exponentiation mess (more on
that later).

It is also nicer to test if my code breaks an old feature to stash
instead of testing in sympy 0.6.4 installed on my system.

UPDATE: No wonder I didn't find this earlier. `stash` isn't listed in
`git --help`.
