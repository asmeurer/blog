Today, David Beazley wrote a pretty controversial set of tweets:

<blockquote class="twitter-tweet" data-conversation="none" data-lang="en"><p lang="en" dir="ltr">At the bookstore. I&#39;ll admit I judge Python books by their tuple description. &quot;Read only list?&quot;  Back on the shelf.  Nope.</p>&mdash; David Beazley (@dabeaz) <a href="https://twitter.com/dabeaz/status/778634205395845120">September 21, 2016</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>
<blockquote class="twitter-tweet" data-conversation="none" data-lang="en"><p lang="en" dir="ltr">Usually there&#39;s a sentence nearby &quot;sometimes you need a read only list.&quot; No. No, I haven&#39;t. Not in 20 years. Not even once. Sorry.</p>&mdash; David Beazley (@dabeaz) <a href="https://twitter.com/dabeaz/status/778635637457088512">September 21, 2016</a></blockquote>
<script async src="//platform.twitter.com/widgets.js"
charset="utf-8"></script>
<blockquote class="twitter-tweet" data-conversation="none" data-lang="en"><p lang="en" dir="ltr">My main objection is that &quot;read only list&quot; is a lazy description lacking thought. A red flag for every other topic that might be covered.</p>&mdash; David Beazley (@dabeaz) <a href="https://twitter.com/dabeaz/status/778639979052498944">September 21, 2016</a></blockquote>
<script async src="//platform.twitter.com/widgets.js"
charset="utf-8"></script>

There are quite a few good responses to these tweets, both from David and from
others (and from yours truly), so I recommend reading them.

Now to start off, I want to say that I respect the hell out of David Beazley.
The guy literally [wrote the book](http://www.dabeaz.com/cookbook.html) on
Python, and he knows way more about Python than I ever well.

As you probably know, there are two "array" datatypes in Python, `list` and
`tuple`. The primary difference between the two is that lists are *mutable*,
that is you can change their entries and length after they are created, with
methods like `.append` or `+=`. Tuples, on the other hand, are *immutable*.
Once you create one, you cannot change it. This makes the implementation
simpler (and hence faster, although don't let anyone tell you you should use a
tuple just because it's faster). This, as
[Ned Batchelder](http://nedbatchelder.com/blog/201608/lists_vs_tuples.html)
points out, is the only technical difference between the two.

The the idea that particularly bugs me here is that tuples are primarily
useful as "record" datatypes.

<blockquote class="twitter-tweet" data-conversation="none" data-lang="en"><p lang="en" dir="ltr"><a href="https://twitter.com/AllenDowney">@AllenDowney</a> Better than &quot;read-only-list.&quot; ;-).   Mainly looking for the tuple-as-record description. That&#39;s often what&#39;s missing.</p>&mdash; David Beazley (@dabeaz) <a href="https://twitter.com/dabeaz/status/778685294593716224">September 21, 2016</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

Tuples are awesome for records. This is both by design—since they have a
fixed shape, the positions in a tuple can be "fixed" values, and by convention—if a
Python programmer sees parentheses instead of square brackets, he is more
likely to see it as such. The `namedtuple` object in the standard library
takes the record idea further by letting you actually name the fields:

``` python
>>> from collections import namedtuple
>>> person = namedtuple('Person', 'name, age')
>>> person('Aaron', 26)
Person(name='Aaron', age=26)
```

But is that really the *only* place you'd want to use a tuple over a list?
