So I've finally decided to move my blog from Wordpress to GitHub pages.  I
highly recommend it if you are technically skilled enough to do it. I was
getting pretty annoyed at Wordpress. It forces you to write your posts in
html (or else using their WYSIWYG editor), the wordpress.com is locked down,
so you can't add any Javascript, their math is stuck in the past rendering png
instead of using MathJax. The list goes on.

With GitHub pages, I can write my posts in Markdown, and I have full control
over everything. And there is no lock in. If I decide I don't like the
software that is generating the posts, I can easily move to something else,
since the post content itself is all Markdown (or the occasional rst or
IPython notebook if I want to do something that Markdown doesn't support).

Here's the guide on how to do it. First, you need to set up GitHub pages. This
is a bit confusing, because there are actually two kinds of GitHub pages, user
pages and project pages. User pages are if you have a repo named
`username.github.io` (or `.com`). The pages are served from the `master`
branch.

For project pages, you add a `gh-pages` branch to any one of your projects,
and GitHub hosts the content automatically at
`username.github.io/projectname`. I originally had my blog content at
`asmeurer.github.io`, but I didn't like that I had to do everything in master,
both the generated and original content. So instead I created a repo called
`blog`. I have my content in the `master` branch and the generated pages in
the `gh-pages` branch (more on this later). At my
[`asmeurer.github.com`](https://github.com/asmeurer/asmeurer.github.com) repo,
I just have for now a basic redirect to the blog. In the future, I may want to
put additional, non-blog content on the website, and it would go there (or in
a separate project repo with its own `gh-pages` branch).

# Nikola

I had initially planned on using
[Pelican](http://blog.getpelican.com/). However, I got stalled on the
Wordpress import. I like that Pelican is written in Python, but I was not too
keen on their abrasive
[license](https://github.com/getpelican/pelican/blob/master/LICENSE). Frankly,
I shouldn't say too many bad things about Pelican because I never really tried
that hard with it.

I have decided to try [Nikola](http://getnikola.com/) instead. It's also
written in Python. It has a very nice
[license](https://github.com/getnikola/nikola/blob/master/LICENSE.txt). I like
the philosophy of the [manual](http://getnikola.com/handbook.html):

> DON'T READ THIS MANUAL. IF YOU NEED TO READ IT I FAILED, JUST USE THE THING.

I've also discovered that the
[Nikola community](https://groups.google.com/forum/#!forum/nikola-discuss) is
*very* nice. And of course, even if Nikola ends up not being for me, it will
be easy to switch, because my actual content is just some Markdown files that
I own.

## Getting started

Getting started with Nikola is pretty easy. First, you need to install it. It
has a *ton* of dependencies (fortunately all Python, so it won't be that
hard). In addition to the ones in the requirements.txt, you should also
install `markdown` and `webassets`. While using `nikola`, it will tell you if
you don't have something installed that you should, so if you see that, just
install what it tells you to.  If you use `conda` and Mac OS X, I have
uploaded all the dependencies to my [Binstar](https://binstar.org/asmeurer/),
so you can just `conda install -c asmeurer nikola`.

Then you just run the commands from
http://getnikola.com/handbook.html#all-you-need-to-know.

One thing that doesn't tell you is that after you init the site, you should
walk through `conf.py` and change the settings to your liking.

Another trick not there is that you can add

```bash
eval "`nikola tabcompletion`"
```

to your Bash profile to get tab completion.
