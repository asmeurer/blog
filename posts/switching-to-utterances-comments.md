I've ditched Disqus as the comment system on this blog. I am now using
[Utterances](https://utteranc.es/). Utterances is an open source comment
system that is backed by GitHub issues. Basically, every post has a
corresponding issue opened on GitHub, and the comments on the post are the
comments on the issue. Utterances automatically places the comments at the
bottom of the post. For example,
[here](https://github.com/asmeurer/blog/issues/18) is the issue corresponding
to this post.

I didn't like Disqus mostly because it serves ads and tracking. Even though I
had opted out from as much of it as I could in the Disqus settings, it still
loads tracking scripts on every page. I run [uBlock
Origin](https://github.com/gorhill/uBlock) always, and it's a bit hypocritical
if my own side has things that are blocked by it. In some cases I can't avoid
it (as far as I know), like when I embed a YouTube video, but it definitely
shouldn't be on every post.

Utterances is a very nice alternative. I has lots of advantages:

- Comments are not self-hosted. GitHub hosts them. Since you need a GitHub
  account to comment, this should make comment spam a non-issue.
- Comments support full Markdown.
- Users can edit their comments.
- I can edit and fully moderate all comments.
- Users log in with a federated system that proves their identity.
- Email subscription to posts.
- No ads or tracking.
- It's completely open source and free to use.

If you use [Nikola](https://getnikola.com/) like I do, it [natively supports
Utterances](https://getnikola.com/handbook.html#comments) (a feature which I
added).

## Exporting Disqus Comments

Some of my old posts had Disqus comments, which I wanted to preserve somehow.
Here is guide on how I did that, since it wasn't as straightforward as I would
have hoped.

The first step is to export your Disqus comments. It's very difficult to
actually find the place in the Disqus site where you do this, but I finally
found the [URL](https://disqus.com/admin/discussions/export/). The export takes
some time to complete (for me it took about half an hour). When it finished,
Disqus will email you an XML file with all your comments. Note that the file
contains all comments for all sites you have ever set up with Disqus. For me,
it also included all the comments on my old [Wordpress
blog](http://asmeurersympy.wordpress.com/), as well as posts for draft blog
posts that I never ended up publishing. It also contained all comments that
were marked as spam, so you will need to remember to filter those.

I decided that since I only have a handful of posts with Disqus comments, I
would just write a script to process them all and manually print them out,
which I will then manually enter in to the Utterances comment system for those
posts.

I wrote a script to process the comments, which you can find
[here](https://github.com/asmeurer/blog/blob/master/disqus-comments/export_disqus_comments.py).
Disqus does provides an [XML
schema](https://disqus.com/api/schemas/1.0/disqus.xsd) for the XML. I used a
library called [xsData](https://xsdata.readthedocs.io/en/latest/index.html),
which lets you take an XML scheme and generate Python dataclasses
corresponding to it, which make manipulating the parsed XML much easier than
the standard library xml library. The script outputs text like

```markdown
========== Comments from https://asmeurer.github.io/blog/posts/what-happens-when-you-mess-with-hashing-in-python/ ==========

These are the original comments on this post that were made when this blog used the [Disqus blog system](https://www.asmeurer.com/blog/posts/switching-to-utterances-comments/).

>**Comment from bjd2385 on 2016-08-28 12:33:12+00:00:**

><p>Very interesting post. I was just looking into hash functions (I've never formally learned what the topic entails), and since I'm most familiar with Python this post explained quite a bit, especially your early mathematical points.</p>

>**Comment from Mark Lawrence on 2016-10-03 20:26:54+00:00:**

><p>At what point does Python 3 force the override of __hash__ if you've defined __eq__?  E.g when would your</p><p>AlwaysEqual class fail?</p>

>**Replies:**

>>**Comment from asmeurer on 2016-10-03 20:38:13+00:00:**

>><p>That's a good catch. I originally wrote this post in Python 2. The example does indeed fail in Python 3. More specifically, if you override __eq__, Python 3 automatically sets __hash__ to None. I'll update the post to make this more clear.</p>

>**Comment from Erick Mendonça on 2017-07-30 03:23:55+00:00:**

><p>Great article! We must really pay attention to these details when implementing custom hashes.</p>

>**Comment from Ignacio on 2017-10-07 22:31:56+00:00:**

><p>Thanks a lot for this post! Clarified a lot of concepts.</p>
```

which I then manually copied to each post's Utterances page on GitHub.

Feel free to adapt [my
script](https://github.com/asmeurer/blog/blob/master/disqus-comments/export_disqus_comments.py)
if you find yourself in a similar situation.

## Utterances Comments

Feel free to use the comments on this page to play around with the commenting
system.

Note that to comment, there are two options. You can log in on this page,
which will let you type your comment in the box below. This requires giving
the Utterances bot access to your GitHub account. Alternately, if you don't
want to give a bot access, you can just go directly to the GitHub issue page
and comment there. I am currently in the process of figuring out how to add
some boilerplate to each page that makes this clear (see [this Utterances
issue](https://github.com/utterance/utterances/issues/355)). If anyone has any
suggestions on how to do this, let me know. For now, I am just going to
manually add a statement about this as the first comment on each post.
