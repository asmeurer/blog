How to permanently lose data with git (and then retrieve it again)
##################################################################
:date: 2009-06-22 05:16
:author: asmeurer
:category: Uncategorized
:slug: how-to-permanently-lose-data-with-git-and-then-retrieve-it-again

So I pushed some changes to github so Ondrej could help me debug the
nseries tests, when I noticed that the changes that I pushed had some
bad comments. So I decided to rebase. But git rebase -i told me that
there was already a rebase in progress. I figured that I must have done
it a long time ago and forgot to abort, so I ran git rebase --abort.

DON'T DO THAT.

I noticed my editor was telling me that an open file had changed. Then,
I noticed that ALL of my uncommited changes were gone! And, being
uncommited changes, git did not have them saved anywhere!

So now I started to panic. I had done a lot of work on dsolve that I
hadn't commited yet. Normally, I have hourly backups run by `Time
Machine`_, but I am on vacation and my backup drive is at home. So I
started to see if I could retrieve it somewhere. grep quickly told me
that it wasn't in the hidden git directory, but it was still in my .pyc
files. But a Google search told me that retrieving from that is not so
easy, if not impossible with Python 2.6. So then, I decided to see if
there was any lingering stuff in my virtual memory from my editor. So I
ran grep on my harddrive and waited.

While I was waiting, though, I noticed when I scrolled up in my command
history that my lost changes were in my Terminal. It turns out that I
had just run git commit --interactive and had used \* on my patches, so
it gave me everything!

So I copied my Terminal history and will work on putting everything back
tomorrow. It should be easy, assuming that git apply works for the
format that git gives in commit --interactive.

So the lessons are: Don't abort a rebase without commiting. Don't start
a rebase and then leave it there. Look in your Terminal history if you
loose stuff. And it might be a good idea to make manual backups if you
are away from your backup drive for a while.

This also highlights why it is important to try to recover data
immediately after realizing that it is gone. If I had closed my Terminal
session or filled it past the maximum number of lines, my data would be
gone. Even if it were in my virtual memory, that wouldn't last forever
either.

.. _Time Machine: http://www.apple.com/macosx/features/timemachine.html
