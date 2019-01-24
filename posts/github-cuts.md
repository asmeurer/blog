GitHub recently announced its [paper cuts
initiative](https://blog.github.com/2018-08-28-announcing-paper-cuts/) to fix
minor issues that make things more difficult for GitHub users. As someone who
spends most of his day on [github.com](https://github.com), this initiative is
great, as these small cuts can quickly add up to a painful experience.

The initiative has already made some great fixes, such as [making the diff
markers
unselectable](https://blog.github.com/changelog/2018-07-31-unselectable-diff-markers/)
and
[hovercards](https://blog.github.com/changelog/2018-10-08-issue-and-pull-request-hovercards/).
Small changes like these are usually quite easy for GitHub to do, but they
make a huge difference to those of use who use GitHub every day.

I [recently asked](https://twitter.com/asmeurer/status/1034528642389266432)
how these cuts could be reported to GitHub for fixing, but got no response. So
I am writing this blog post.

To be very clear: I think that on the whole GitHub is great and they are doing
a great job. And it's still better than the alternatives (to put things in
perspective, I recently spent [half an
hour](https://twitter.com/asmeurer/status/1029158262069899266) trying to
figure out how to change my password in BitBucket, and GitLab can't even keep
me logged in between sessions). GitHub has and continues to revolutionize the
open source ecosystem, and is still the best place to host an open source
project.

But since GitHub did
[ask](https://blog.github.com/2018-08-28-announcing-paper-cuts/) what sorts of
changes they want to see, I'm providing a list. In this post I'm trying to
only ask about things that are small changes (though I realize many won't be
as easy to fix as they may appear from the outside, and I readily admit that I
am not a web developer).

These are just the things that have bothered me, personally. Other people use
GitHub differently and no doubt have their own pain points. For instance, I
have no suggestions about the project boards feature of GitHub because I don't
use it. If you are also a GitHub user and have your own pain points feel free
to use the comment box below (though I have no idea if GitHub will actually
see them).

If you work for GitHub and have any questions, feel free to comment below, or
[email me](mailto:asmeurer@gmail.com).

In no particular order:

## Issues

1. **Allow anyone to add labels to issues.** At the very least, allow the
   person who opened the issue to add labels.

2. The new issue transfer ability is great, but please **make it require only
   push access, not admin access.**

3. **Remove the automatic hiding of comments when there are too many.** I
   understand this is done for technical reasons, but it breaks
   Cmd-F/scrolling through the page to find comments. Often I go to an issue
   trying to find an old comment and can't because buried in the comments is a
   button I have to press to actually show the comment (it's even worse when
   you have to find and press the button multiple times).

4. **Better indication for cross-referenced pull requests.** I really don't
   know how to fix this, only that it is a problem. It happens all the time
   that a new contributor comes to a SymPy issue and asks if it has been
   worked on yet. They generally do not seem to notice the cross-referenced
   pull requests in the list.
   [Here](https://github.com/sympy/sympy/issues/14943) is an example of what
   I'm talking about.

5. **Indicate better if a cross-referenced pull request would close an
   issue.** Preferably with text, not just an icon.

6. **HTML pull request/issue templates.** I don't know if this counts as a
   "cut", as it isn't a simple fix. Right now, many projects use pull
   requests/new issue templates, but it is not very user friendly. The problem
   is that the whole thing is done in plain text, often with the template text
   as an HTML comment to prevent it from appearing in the final issue text.
   Even for me, I often find this quite difficult to read through, but for new
   contributors, we often find that they don't read it at all. Sure there's no
   way to force people to read, but if we could instead create a very simple
   HTML form for people to fill out, it would be much more friendly, even to
   experienced people like myself.

7. **Fix the back button in Chrome.** I don't know if this is something that
   GitHub can fix, and I also do not know how things work in other browsers. I
   use Chrome on macOS. Often, when I click the "back" button and it takes me
   back to an issue page, the contents of the page are out-of-date (the newest
   comments or commits do not appear). It's often even more out-of-date than
   it was when I left the page. I have to reload the page to get the latest
   content.

8. **Allow Markdown formatting in issue titles.**

9. **Show people's names next to comments as "Real Name (@username)".**

10. **Remember my selection for the "sort" setting in the issues list.** I'd
    love to have issues/pull requests sort by "most recently updated" by
    default, so that I don't miss updates to old issues/pull requests.

11. **Make advanced search filters more accessible.** They should autofill,
    similar to how Gmail or even GitLab search works (yes, please still all
    the good ideas from GitLab; they already stole all their good ideas from
    you).

12. **Tone down the reaction emojis.** Maybe this ship has sailed, but
    reaction emojis are way too unprofessional for some projects.

13. **Copy/paste text as Markdown.** For example, copying "**bold**" and
    pasting it into the comment box would paste `**bold**`. Another idea that
    you can steal from GitLab.

14. **Strike out #12345 issue links when the issue/PR is closed/merged**
    (like <strike>#12345</strike>).

## Pull requests

15. **Add a button that automatically merges a pull request as soon as all the
    CI checks pass.** Any additional commits pushed to the branch in the
    interim would cancel it, and it should also be cancellable by someone else
    with push access or the PR author.

16. **Add some way to disable the automatic hiding of large diffs.** This
    breaks Cmd-F on the page, and makes it harder to scroll through the pull
    request to find what you are looking for (typically the most important
    changes are the ones that are hidden!).

17. **Include all issue/PR authors in the authors search on the pull request
    list page.** Right now it only lists people with push access. But I
    generally can't remember people's GitHub usernames, and autofilling based
    on all authors would be very helpful.

18. **Better contextual guesses for issue autofilling (after typing `#`).**
    For instance, if an issue has already been referenced or cross-referenced,
    it should appear near the top of the list. We have almost [3000 open
    issues](https://github.com/sympy/sympy/issues) in SymPy, and the current
    issue numbers are 5-digits long, so referencing an issue purely by number
    is very error prone.

19. **Auto-update edited comments.** Context: SymPy uses a
    [bot](https://github.com/sympy/sympy-bot) that comments on every pull
    request, requiring a release notes entry to be added to the description.
    This works quite well, but to prevent the bot from spamming, we have it
    comment only once, and edit its comment on any further checks. However,
    these edits do not automatically update, so people have to manually reload
    the page to see them.

20. **Don't hide full commit messages by default in the commits view.** It
    would be better to encourage people to write good commit messages.

21. **Make issue cross-references in pull request titles work.** I'd rather
    people didn't put issue numbers in pull request titles but they do it
    anyway, so it would be nice if they actually worked as links.

22. **Allow me to comment on lines that aren't visible by default.** That is,
    lines that you have to click the "expand" icon above or below the line
    numbers to access. As an example, this can be useful to point out a line
    that should have been changed but wasn't.

23. **Copying code from a diff that includes lines that aren't visible by
    default includes an extra space to the left for those lines.** This is a
    straight up bug. Probably fixing the previous point would also fix this :)

24. **Make searches include text from the pull request diff.**

25. **When a diff indents a line color the whitespace to the left of the
    line.** (see
    [this](https://twitter.com/asmeurer/status/740611970714480640))

26. **Pull requests can show commits that are already in master.** For
    example, if someone makes pull request B based off of pull request A and
    then A gets merged, B will still show the commits from A. This has been a
    bug forever.

27. **Make the "jump to file or symbol" popdown collapsible.** Specifically
    what I mean is I want to be able to show just the files, without any
    symbols. For large pull requests, it is very difficult to use this popdown
    if there are hundreds of symbols. I typically want to just jump to a
    specific file.

28. **The status check on the favicon goes away when you switch to the diff
    tab.** Kudos to Marius Gedminas for [pointing this
    out](https://twitter.com/mgedmin/status/1058381090694553601).

29. **[Apparently](https://github.com/sympy/sympy/pull/15280#issuecomment-426795606)
    status checks that use the GitHub Apps API are forced to link into the
    checks tab.** The checks tab is useless if no information is actually
    published to it. It would be better if it could link straight to the
    external site, like is done with oauth integrations.

30. **Make it easier to copy someone's username from the pull request page.**
    I generally do this to `git remote add` them (using
    [hub](https://github.com/github/hub)). If I try to select their username
    from a comment, it's a link, which makes it hard to select. I generally
    copy it from the blue text at the top "*user* wants to merge *n* commits
    from `sympy:master` from `user:branch`. If it were easier to select "user"
    or "branch" from that box (say, by double clicking), that would be
    helpful.

31. **Change the "resolve conversation" UI.** I keep pressing it on accident
    because it's where I expect the "new comment" button to be.

## Reviews

I wrote a [whole
post](https://www.asmeurer.com/blog/posts/github-reviews-gripes/) about the
reviews feature when it came out. Not much has changed since then (actually,
it has gotten worse). In short, the feature doesn't work like I would like it
too, and I find the default behavior of deferred comments to be extremely
detrimental. If there were a way to completely disable reviews (for myself, I
don't care about other people using the feature), I would.

See my blog post for full details on why I think the reviews feature is broken
and actually makes things worse, not better than before. I've summarized a few
things that could change below.

32. **Make reviews non-deferred by default.** This is the biggest thing. If I
    had to pick only a single item on this page to be changed, it would be
    this. The issue is if I start a review and walk away from it, but forget
    to "finalize" it with a review status, the review is never actually seen
    by anyone. The simplest way to fix this would be to simply make partial
    reviews public.

33. **Make Cmd-Enter default to immediate comment.** Barring the above change,
    Cmd-Enter on a pull request line comment should default to immediate
    comment, not deferred (review) comment. The problem with the
    Cmd-Shift-Enter shortcut is that it is inconsistent: on a normal comment,
    it closes the pull request, and on a reply comment, it does nothing. I
    shouldn't have to check what "comment context" I am in to figure out what
    keyboard shortcut to use. The worst part is if you accidentally start a
    review, it's a pain in the ass to undo that and just post a normal
    comment. The simples way to fix this would be to swap the current meaning
    of Cmd-Enter and Cmd-Shift-Enter for line comments (and no, this wouldn't
    be a backwards incompatible change, it would be a regression fix;
    Cmd-Enter *used* to do the right thing).

34. **Allow reviewing your own pull request.** There's no reason to disallow
    this, and it would often be quite useful to, for instance, mark a work in
    progress PR as such with a "request changes" review. Obviously
    self-reviews would be excluded from any required reviews.

35. **Unhide the reviews box.** It should just be the same box as the comment
    box, unstead of buried on the diff tab (see my [blog
    post](https://www.asmeurer.com/blog/posts/github-reviews-gripes/)).

36. **Show review status in the pull request list as a red X or green check.**
    This would make it easier to see which pull requests have reviews.

37. **Allow new commits to invalidate reviews.** That way they work the same
    way as any other status check. (I see that this is now an option for
    required reviews, which is new since my original blog post, but it still
    doesn't affect the status as reported on the pull requests list).

38. **Allow requiring zero negative reviews to merge (but not necessarily any
    positive reviews)**. Requiring a positive review is pointless. The person
    merging can just add one real quick before they merge, but it is
    unnecessary extra work. On the other hand allowing people with push access
    to block a merge with a negative review would be very useful.

## Web editor

39. **The web editor seems to have a search function, but I can't get it to
    actually work.** Half the time Cmd-F pops open the browser search, which
    doesn't find text that isn't on screen. And when I press Cmd-G to actually
    do the search, it doesn't work (and there are no buttons to perform the
    search either).

40. **Add basic syntax testing in the web editor for common languages to catch
    basic mistakes.**

## Mobile site

41. **Please make the mobile site work with iOS 10.** I don't see any reason
    why simple things like buttons (like the merge button or the comment
    button) shouldn't work on a slightly older browser. No, I am not a web
    developer, but I do use my phone a lot and I've noticed that literally
    every other website works just fine on it.

42. **Add a way to disable the mobile site permanently.** For the most part,
    the mobile site is useless (see below). If you aren't going to put full
    development effort into it, allow me to disable it permanently so that
    every time I visit [github.com](https://github.com) on my phone it goes to
    the desktop site.

Seeing as how the site (mobile or not) is almost completely unusable on every
mobile device I own, it's hard to list other things here, but based on back
when it actually worked, these are some of the things that annoyed me the
most. Basically, I have found that virtually every time I go to GitHub to do
anything on mobile, I have to switch to desktop mode to actually do what I
want.

My apologies if any of these actually work now: as I said,
[github.com](https://github.com) doesn't actually work at all on my phone.

43. **Cannot search issues on mobile.**

44. **Cannot make a line comment that *isn't* a review on mobile.**

45. **Cannot view lines beyond the default diff in pull requests on mobile.**

46. **Show more than 2 lines of the README and 0 lines of the code by default
    on project pages.** Yes mobile screens are small but it's also not hard to
    scroll on them.

47. **Support Jupyter notebook rendering on mobile.**

## Files view

48. **GitHub needs a better default color theme for syntax highlighting.**
    Most of the colors are very similar to one another and hard to
    differentiate. Also things like strings are black, even though one of the
    most useful aspects of syntax highlighting generally is to indicate
    whether something is in a string or not.

49. **Add MathJax support to markdown files.** This would be amazingly useful
    for SymPy, as well as many scientific software projects. Right now if you
    want this you have to use a Jupyter notebook. MathJax support in
    issue/pull request comments would be awesome as well, though I'm not
    holding out for that.

50. **Add "display source" button for markdown, ReST, etc.** I mean the button
    that is already there for Jupyter notebooks. Right now you have to view
    markdown and ReST files "raw" or edit the file to see their source.

51. **Add a link to the pull request in the blame view.** Usually I want to
    find the pull request that produced a change, not just the commit.

## Wiki

52. **The wikis used to support LaTeX math with MathJax. It would be great if
    this were re-added.**

53. **The ability to set push permissions for the wiki separately from the
    repo it is attached to, or otherwise create an oauth token that can only
    push to the wiki would be useful.** Context: for SymPy, we use a
    [bot](https://github.com/sympy/sympy-bot) that automatically updates our
    [release notes](https://github.com/sympy/sympy/wiki/Release-Notes) on our
    wiki. It works quite well, but the only way it can push to the wiki is if
    we give it push access to the full repo.

## Notification emails

54. **Don't clobber special emails/email headers.** GitHub adds special emails
    like [author@noreply.github.com](mailto:author@noreply.github.com) and
    [mention@noreply.github.com](mailto:mention@noreply.github.com) to email
    notifications based on how the notification was triggered. This is useful,
    as I can create an email filter for
    [author@noreply.github.com](mailto:author@noreply.github.com) for
    notifications on issues and pull requests created by me. The bad news is,
    [mention@noreply.github.com](mailto:mention@noreply.github.com), which is
    added when I am @mentioned, clobbers
    [author@noreply.github.com](mailto:author@noreply.github.com), so that it
    doesn't appear anymore. In other words, as soon as someone @mentions me in
    one of my issues, I become *less* likely to see it, because it no longer
    gets my label (I get @mentioned on *a lot* of issues and don't have the
    ability to read all of my notification emails). Ditto for the
    `X-GitHub-Reason` email headers.

55. **Readd the "view issue" links in Gmail.** (I forgot what these are
    called). GitHub notification emails used to have these useful "view issue"
    buttons that showed up on the right in the email list in Gmail, but they
    were removed for some reason.

## API

56. **Make the requests in the API docs actually return what they show in the
    docs.** This means the [example
    repo](https://github.com/octocat/Hello-World/) should have actual example
    issues corresponding to what is shown in the docs.

57. **Allow giving deploy key access to just one branch.** That way I can have
    a deploy key for `gh-pages` and minimize the attack surface that the
    existence of that key produces. I think everyone would agree that more
    fine-grained permissions throughout the API would be nice, but this is one
    that would benefit me personally, specifically for my project
    [doctr](https://drdoctr.github.io/).

## GitHub Pages

GitHub pages is one of the best features of GitHub, and infact, this very blog
is hosted on it. Very few complaints here, because for the most part, it "just
works".


58. [**Moar themes.**](https://twitter.com/asmeurer/status/831962312122761216)
    Also it's awesome that you can use any GitHub repo as a theme now, but it
    turns out most random themes you find around GitHub don't actually work
    very well.

59. **The steps to add HTTPS to an existing GitHub pages custom domain are a
    bit confusing.**. This took us a while to figure out for
    [sympy.org](https://sympy.org). To get things to work, you have to trigger
    GitHub to issue a cert for the domain. But the UI to issue the cert is to
    paste the domain into the box. So if the domain is already there but it
    doesn't work, you have to re-enter it. Also if you want both www and the
    apex domain to be HTTPS you have to enter them both in the box to trigger
    GitHub to issue a cert. This is primarily a UX issue. See
    [https://github.com/sympy/sympy.github.com/issues/105#issuecomment-415899934](https://github.com/sympy/sympy.github.com/issues/105#issuecomment-415899934).

## Settings

60. **Automatically protected branches make the branch difficult to delete
    when you are done with it.** My use-case is to create a branch for the
    release, which I want to protect, but I also want to delete the branch
    once it is merged. I can protect the branch automatically pretty easily,
    but then I have to go and delete the protection rule when it's merged to
    delete it. There are several ways this could be fixed. For instance, you
    could add a rule to allow protected branches to be deleted if they are
    up-to-date with default branch.

61. **Add a way to disable the ability for non-admins to create new branches
    on a repo.** We want all of our pull requests to come from forks. Branches
    in the repo just create confusion, for instance, they appear whenever
    someone clones the repository.

62. **Related to the previous point, make pull request reverts come from
    forks.** Right now when someone uses the revert pull request button, it
    creates a new branch in the same repo, but it would be better if the
    branch were made in the person's fork.

63. **Allow me to enable branch protection by default for new repos.**

64. **Allow me to enable branch protection by default on new branches.** This
    is more important than the previous one because of the feature that lets
    people push to your branch on a pull request (which is a great feature by
    the way).

65. **Clicking a team name in the settings should default to the "members"
    tab.** I don't understand why GitHub has a non-open "discussions" feature,
    but I find it to be completely useless, and generally see such things as
    harmful for open source.

66. **Suggest people to add push access to.** I don't necessarily mean
    passively (though that could be interesting too), but I mean in the page
    to add someone, it would be nice if the popup suggested or indicated which
    people had contributed the project before, since just searching for a name
    searches all of GitHub, and I don't want to accidentally give access to
    the wrong person.

## Profiles

67. **Stop trying to make profile pages look "cute" with randomly highlighted
    pull requests.** GitHub should have learned by now that profile pages
    matter a lot (whether people want them to or not), and there can be
    unintended consequences to the things that are put on them.

68. **Explain what the axes actually mean in the new "activity overview".**
    I'm referring to
    [this](https://twitter.com/asmeurer/status/1033141923630874624) (it's
    still in beta and you have to manually enable it on your profile page).
    Personally I'm leaving the feature off because I don't like being
    metricized/gamified, but if you're going to have it, at least include some
    transparency.

## Releases

69. **Allow hiding the "source code (zip)" and "source code (tar.gz)" files in
    a release.** We upload our actual release files (generated by `setup.py`)
    to the GitHub release. We want people to download those, not snapshots of
    the repo.

## Miscellaneous

70. **The repository search function doesn't support partial matches.** This
    is annoying for [conda-forge](https://github.com/conda-forge/). For
    instance, if I [search for
    "png"](https://github.com/conda-forge/?utf8=%E2%9C%93&q=png&type=&language=)
    it doesn't show the
    [libpng-feedstock](https://github.com/conda-forge/libpng-feedstock) repo.

71. **Show commit history as a graph.** Like `git log --graph`. This would go
    a *long* way to helping new users understand git. When I first started
    with git, understanding the history as a graph was a major part of me
    finally grokking how it worked.

72. **Bring back the old "fork" UI.** The one that just had icons for all the
    repos, and the icons didn't go away or become harder to find if you
    already had a fork. Some of us use the "fork" button to go to our
    pre-existing forks, not just to perform a fork action. This was recently
    changed and now it's better than it was, but I still don't see why
    existing forks need to be harder to find, visually, than nonexisting ones.

73. **Provide a more official way to request fixes to these cuts.** I often
    ask on Twitter, but get no response. Preferably something public so that
    others could vote on them (but I understand if you don't want too much
    bikeshedding).
