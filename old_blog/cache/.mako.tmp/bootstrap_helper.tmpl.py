# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1391984309.613348
_enable_loop = True
_template_filename = '/Users/aaronmeurer/Documents/nikola/nikola/data/themes/bootstrap3/templates/bootstrap_helper.tmpl'
_template_uri = 'bootstrap_helper.tmpl'
_source_encoding = 'ascii'
_exports = ['html_translations', 'html_head', 'html_navigation_links', 'late_load_js']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer('\n')
        # SOURCE LINE 53
        __M_writer('\n\n')
        # SOURCE LINE 74
        __M_writer('\n\n\n')
        # SOURCE LINE 98
        __M_writer('\n\n\n')
        # SOURCE LINE 107
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_translations(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        lang = context.get('lang', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 101
        __M_writer('\n')
        # SOURCE LINE 102
        for langname in translations.keys():
            # SOURCE LINE 103
            if langname != lang:
                # SOURCE LINE 104
                __M_writer('            <li><a href="')
                __M_writer(str(_link("index", None, langname)))
                __M_writer('" rel="alternate" hreflang="')
                __M_writer(str(langname))
                __M_writer('">')
                __M_writer(str(messages("LANGUAGE", langname)))
                __M_writer('</a></li>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_head(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        use_cdn = context.get('use_cdn', UNDEFINED)
        description = context.get('description', UNDEFINED)
        has_custom_css = context.get('has_custom_css', UNDEFINED)
        title = context.get('title', UNDEFINED)
        use_bundles = context.get('use_bundles', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        len = context.get('len', UNDEFINED)
        rss_link = context.get('rss_link', UNDEFINED)
        permalink = context.get('permalink', UNDEFINED)
        blog_author = context.get('blog_author', UNDEFINED)
        abs_link = context.get('abs_link', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        striphtml = context.get('striphtml', UNDEFINED)
        blog_title = context.get('blog_title', UNDEFINED)
        mathjax_config = context.get('mathjax_config', UNDEFINED)
        favicons = context.get('favicons', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer('\n    <meta charset="utf-8">\n    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n')
        # SOURCE LINE 6
        if description:
            # SOURCE LINE 7
            __M_writer('    <meta name="description" content="')
            __M_writer(str(description))
            __M_writer('">\n')
        # SOURCE LINE 9
        __M_writer('    <meta name="author" content="')
        __M_writer(str(blog_author))
        __M_writer('">\n    <title>')
        # SOURCE LINE 10
        __M_writer(striphtml(str(title)))
        __M_writer(' | ')
        __M_writer(striphtml(str(blog_title)))
        __M_writer('</title>\n    ')
        # SOURCE LINE 11
        __M_writer(str(mathjax_config))
        __M_writer('\n')
        # SOURCE LINE 12
        if use_bundles:
            # SOURCE LINE 13
            if use_cdn:
                # SOURCE LINE 14
                __M_writer('            <link href="http://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css" rel="stylesheet">\n            <link href="/assets/css/all.css" rel="stylesheet" type="text/css">\n')
                # SOURCE LINE 16
            else:
                # SOURCE LINE 17
                __M_writer('            <link href="/assets/css/all-nocdn.css" rel="stylesheet" type="text/css">\n')
            # SOURCE LINE 19
        else:
            # SOURCE LINE 20
            if use_cdn:
                # SOURCE LINE 21
                __M_writer('            <link href="http://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css" rel="stylesheet">\n')
                # SOURCE LINE 22
            else:
                # SOURCE LINE 23
                __M_writer('            <link href="/assets/css/bootstrap.min.css" rel="stylesheet" type="text/css">\n')
            # SOURCE LINE 25
            __M_writer('        <link href="/assets/css/rst.css" rel="stylesheet" type="text/css">\n        <link href="/assets/css/code.css" rel="stylesheet" type="text/css">\n        <link href="/assets/css/colorbox.css" rel="stylesheet" type="text/css"/>\n        <link href="/assets/css/theme.css" rel="stylesheet" type="text/css"/>\n')
            # SOURCE LINE 29
            if has_custom_css:
                # SOURCE LINE 30
                __M_writer('            <link href="/assets/css/custom.css" rel="stylesheet" type="text/css">\n')
        # SOURCE LINE 33
        __M_writer('    <link rel="canonical" href="')
        __M_writer(str(abs_link(permalink)))
        __M_writer('">\n    <!--[if lt IE 9]>\n      <script src="http://html5shim.googlecode.com/svn/trunk/html5.js" type="text/javascript"></script>\n    <![endif]-->\n')
        # SOURCE LINE 37
        if rss_link:
            # SOURCE LINE 38
            __M_writer('        ')
            __M_writer(str(rss_link))
            __M_writer('\n')
            # SOURCE LINE 39
        else:
            # SOURCE LINE 40
            if len(translations) > 1:
                # SOURCE LINE 41
                for language in translations:
                    # SOURCE LINE 42
                    __M_writer('                <link rel="alternate" type="application/rss+xml" title="RSS (')
                    __M_writer(str(language))
                    __M_writer(')" href="')
                    __M_writer(str(_link('rss', None, language)))
                    __M_writer('">\n')
                # SOURCE LINE 44
            else:
                # SOURCE LINE 45
                __M_writer('            <link rel="alternate" type="application/rss+xml" title="RSS" href="')
                __M_writer(str(_link('rss', None)))
                __M_writer('">\n')
        # SOURCE LINE 48
        if favicons:
            # SOURCE LINE 49
            for name, file, size in favicons:
                # SOURCE LINE 50
                __M_writer('            <link rel="')
                __M_writer(str(name))
                __M_writer('" href="')
                __M_writer(str(file))
                __M_writer('" sizes="')
                __M_writer(str(size))
                __M_writer('"/>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_navigation_links(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        rel_link = context.get('rel_link', UNDEFINED)
        lang = context.get('lang', UNDEFINED)
        isinstance = context.get('isinstance', UNDEFINED)
        tuple = context.get('tuple', UNDEFINED)
        navigation_links = context.get('navigation_links', UNDEFINED)
        permalink = context.get('permalink', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 77
        __M_writer('\n')
        # SOURCE LINE 78
        for url, text in navigation_links[lang]:
            # SOURCE LINE 79
            if isinstance(url, tuple):
                # SOURCE LINE 80
                __M_writer('            <li class="dropdown"><a href="#" class="dropdown-toggle" data-toggle="dropdown">')
                __M_writer(str(text))
                __M_writer('<b class="caret"></b></a>\n            <ul class="dropdown-menu">\n')
                # SOURCE LINE 82
                for suburl, text in url:
                    # SOURCE LINE 83
                    if rel_link(permalink, suburl) == "#":
                        # SOURCE LINE 84
                        __M_writer('                    <li class="active"><a href="')
                        __M_writer(str(permalink))
                        __M_writer('">')
                        __M_writer(str(text))
                        __M_writer('</a>\n')
                        # SOURCE LINE 85
                    else:
                        # SOURCE LINE 86
                        __M_writer('                    <li><a href="')
                        __M_writer(str(suburl))
                        __M_writer('">')
                        __M_writer(str(text))
                        __M_writer('</a>\n')
                # SOURCE LINE 89
                __M_writer('            </ul>\n')
                # SOURCE LINE 90
            else:
                # SOURCE LINE 91
                if rel_link(permalink, url) == "#":
                    # SOURCE LINE 92
                    __M_writer('                <li class="active"><a href="')
                    __M_writer(str(permalink))
                    __M_writer('">')
                    __M_writer(str(text))
                    __M_writer('</a>\n')
                    # SOURCE LINE 93
                else:
                    # SOURCE LINE 94
                    __M_writer('                <li><a href="')
                    __M_writer(str(url))
                    __M_writer('">')
                    __M_writer(str(text))
                    __M_writer('</a>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_late_load_js(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        use_cdn = context.get('use_cdn', UNDEFINED)
        use_bundles = context.get('use_bundles', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 55
        __M_writer('\n')
        # SOURCE LINE 56
        if use_bundles:
            # SOURCE LINE 57
            if use_cdn:
                # SOURCE LINE 58
                __M_writer('            <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js" type="text/javascript"></script>\n            <script src="http://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>\n            <script src="/assets/js/all.js" type="text/javascript"></script>\n')
                # SOURCE LINE 61
            else:
                # SOURCE LINE 62
                __M_writer('            <script src="/assets/js/all-nocdn.js" type="text/javascript"></script>\n')
            # SOURCE LINE 64
        else:
            # SOURCE LINE 65
            if use_cdn:
                # SOURCE LINE 66
                __M_writer('            <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js" type="text/javascript"></script>\n            <script src="http://netdna.bootstrapcdn.com/bootstrap/3.0.0/js/bootstrap.min.js"></script>\n')
                # SOURCE LINE 68
            else:
                # SOURCE LINE 69
                __M_writer('            <script src="/assets/js/jquery-1.10.2.min.js" type="text/javascript"></script>\n            <script src="/assets/js/bootstrap.min.js" type="text/javascript"></script>\n')
            # SOURCE LINE 72
            __M_writer('        <script src="/assets/js/jquery.colorbox-min.js" type="text/javascript"></script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


