import sys
from collections import defaultdict
import textwrap

import disqus
from xsdata.formats.dataclass.parsers import XmlParser

def main():
    file = sys.argv[1]
    with open(file) as f:
        xml = f.read()

    comments = XmlParser().from_string(xml, disqus.Disqus)

    # "threads" are the pages. "posts" are the comments.
    threads = {t.id_attribute: t for t in comments.thread if
               # The export contains posts from my old Wordpress blog. It also
               # contains some draft posts that were never published, but we
               # don't need to worry about those because they don't have any
               # comments.
               t.link.startswith('https://asmeurer.github.io')}

    posts = defaultdict(dict)
    for p in comments.post:
        tid = p.thread.id
        if tid not in threads:
            # Old Wordpress comment
            continue
        if p.is_spam:
            continue
        posts[tid][p.id_attribute] = p

    child_posts = defaultdict(list)
    for tid in posts:
        for pid, p in posts[tid].items():
            if p.parent:
                child_posts[p.parent.id].append(p.id_attribute)

    def print_post(p, level=1):
        author = p.author
        pid = p.id_attribute
        print(textwrap.indent(f"""\
**Comment from {author.name} on {p.created_at.to_datetime()}:**

{p.message}
    """, '>'*level))

        if pid in child_posts:
            for child_id in child_posts[pid]:
                child = posts[tid][child_id]
                print(textwrap.indent("**Replies:**", '>'*level))
                print()
                print_post(child, level + 1)

    for tid in posts:
        t = threads[tid]
        print("========== Comments from", t.link, "==========")
        print()
        print("These are the original comments on this post that were made when this blog used the [Disqus blog system](https://www.asmeurer.com/blog/posts/switching-to-utterances-comments/).")
        print()
        for pid, p in posts[tid].items():
            if p.parent:
                continue
            print_post(p)


if __name__ == '__main__':
    main()
