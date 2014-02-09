# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1391984309.57512
_enable_loop = True
_template_filename = '/Users/aaronmeurer/Documents/nikola/nikola/data/themes/base/templates/base_helper.tmpl'
_template_uri = 'base_helper.tmpl'
_source_encoding = 'utf-8'
_exports = ['html_translations', 'html_navigation_links', 'html_social', 'html_sidebar_links', 'html_head', 'late_load_js']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 47
        __M_writer('\n\n')
        # SOURCE LINE 50
        __M_writer('\n\n')
        # SOURCE LINE 54
        __M_writer('\n\n<!--FIXME: remove in v7 -->\n')
        # SOURCE LINE 59
        __M_writer('\n\n')
        # SOURCE LINE 82
        __M_writer('\n\n\n')
        # SOURCE LINE 91
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
        # SOURCE LINE 85
        __M_writer('\n')
        # SOURCE LINE 86
        for langname in translations.keys():
            # SOURCE LINE 87
            if langname != lang:
                # SOURCE LINE 88
                __M_writer('            <a href="')
                __M_writer(str(_link("index", None, langname)))
                __M_writer('" rel="alternate" hreflang="')
                __M_writer(str(langname))
                __M_writer('">')
                __M_writer(str(messages("LANGUAGE", langname)))
                __M_writer('</a>\n')
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
        # SOURCE LINE 61
        __M_writer('\n')
        # SOURCE LINE 62
        for url, text in navigation_links[lang]:
            # SOURCE LINE 63
            if isinstance(url, tuple):
                # SOURCE LINE 64
                __M_writer('            <li> ')
                __M_writer(str(text))
                __M_writer('\n            <ul>\n')
                # SOURCE LINE 66
                for suburl, text in url:
                    # SOURCE LINE 67
                    if rel_link(permalink, suburl) == "#":
                        # SOURCE LINE 68
                        __M_writer('                    <li class="active"><a href="')
                        __M_writer(str(permalink))
                        __M_writer('">')
                        __M_writer(str(text))
                        __M_writer('</a>\n')
                        # SOURCE LINE 69
                    else:
                        # SOURCE LINE 70
                        __M_writer('                    <li><a href="')
                        __M_writer(str(suburl))
                        __M_writer('">')
                        __M_writer(str(text))
                        __M_writer('</a>\n')
                # SOURCE LINE 73
                __M_writer('            </ul>\n')
                # SOURCE LINE 74
            else:
                # SOURCE LINE 75
                if rel_link(permalink, url) == "#":
                    # SOURCE LINE 76
                    __M_writer('                <li class="active"><a href="')
                    __M_writer(str(permalink))
                    __M_writer('">')
                    __M_writer(str(text))
                    __M_writer('</a>\n')
                    # SOURCE LINE 77
                else:
                    # SOURCE LINE 78
                    __M_writer('                <li><a href="')
                    __M_writer(str(url))
                    __M_writer('">')
                    __M_writer(str(text))
                    __M_writer('</a>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_social(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        social_buttons_code = context.get('social_buttons_code', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 52
        __M_writer('\n    ')
        # SOURCE LINE 53
        __M_writer(str(social_buttons_code))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_sidebar_links(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        def html_navigation_links():
            return render_html_navigation_links(context)
        __M_writer = context.writer()
        # SOURCE LINE 57
        __M_writer('\n    ')
        # SOURCE LINE 58
        __M_writer(str(html_navigation_links()))
        __M_writer('\n')
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
        _link = context.get('_link', UNDEFINED)
        use_bundles = context.get('use_bundles', UNDEFINED)
        comment_system_id = context.get('comment_system_id', UNDEFINED)
        len = context.get('len', UNDEFINED)
        rss_link = context.get('rss_link', UNDEFINED)
        permalink = context.get('permalink', UNDEFINED)
        blog_author = context.get('blog_author', UNDEFINED)
        abs_link = context.get('abs_link', UNDEFINED)
        comment_system = context.get('comment_system', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        striphtml = context.get('striphtml', UNDEFINED)
        blog_title = context.get('blog_title', UNDEFINED)
        mathjax_config = context.get('mathjax_config', UNDEFINED)
        favicons = context.get('favicons', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer('\n    <meta charset="utf-8">\n')
        # SOURCE LINE 4
        if description:
            # SOURCE LINE 5
            __M_writer('    <meta name="description" content="')
            __M_writer(str(description))
            __M_writer('">\n')
        # SOURCE LINE 7
        __M_writer('    <meta name="author" content="')
        __M_writer(str(blog_author))
        __M_writer('">\n    <title>')
        # SOURCE LINE 8
        __M_writer(striphtml(str(title)))
        __M_writer(' | ')
        __M_writer(striphtml(str(blog_title)))
        __M_writer('</title>\n    ')
        # SOURCE LINE 9
        __M_writer(str(mathjax_config))
        __M_writer('\n')
        # SOURCE LINE 10
        if use_bundles:
            # SOURCE LINE 11
            if use_cdn:
                # SOURCE LINE 12
                __M_writer('            <link href="/assets/css/all.css" rel="stylesheet" type="text/css">\n')
                # SOURCE LINE 13
            else:
                # SOURCE LINE 14
                __M_writer('            <link href="/assets/css/all-nocdn.css" rel="stylesheet" type="text/css">\n')
            # SOURCE LINE 16
        else:
            # SOURCE LINE 17
            __M_writer('        <link href="/assets/css/rst.css" rel="stylesheet" type="text/css">\n        <link href="/assets/css/code.css" rel="stylesheet" type="text/css">\n        <link href="/assets/css/theme.css" rel="stylesheet" type="text/css"/>\n')
            # SOURCE LINE 20
            if has_custom_css:
                # SOURCE LINE 21
                __M_writer('            <link href="/assets/css/custom.css" rel="stylesheet" type="text/css">\n')
        # SOURCE LINE 24
        __M_writer('    <link rel="canonical" href="')
        __M_writer(str(abs_link(permalink)))
        __M_writer('">\n    <!--[if lt IE 9]>\n      <script src="http://html5shim.googlecode.com/svn/trunk/html5.js" type="text/javascript"></script>\n    <![endif]-->\n')
        # SOURCE LINE 28
        if rss_link:
            # SOURCE LINE 29
            __M_writer('        ')
            __M_writer(str(rss_link))
            __M_writer('\n')
            # SOURCE LINE 30
        else:
            # SOURCE LINE 31
            if len(translations) > 1:
                # SOURCE LINE 32
                for language in translations:
                    # SOURCE LINE 33
                    __M_writer('                <link rel="alternate" type="application/rss+xml" title="RSS (')
                    __M_writer(str(language))
                    __M_writer(')" href="')
                    __M_writer(str(_link('rss', None, language)))
                    __M_writer('">\n')
                # SOURCE LINE 35
            else:
                # SOURCE LINE 36
                __M_writer('            <link rel="alternate" type="application/rss+xml" title="RSS" href="')
                __M_writer(str(_link('rss', None)))
                __M_writer('">\n')
        # SOURCE LINE 39
        if favicons:
            # SOURCE LINE 40
            for name, file, size in favicons:
                # SOURCE LINE 41
                __M_writer('            <link rel="')
                __M_writer(str(name))
                __M_writer('" href="')
                __M_writer(str(file))
                __M_writer('" sizes="')
                __M_writer(str(size))
                __M_writer('"/>\n')
        # SOURCE LINE 44
        if comment_system == 'facebook':
            # SOURCE LINE 45
            __M_writer('        <meta property="fb:app_id" content="')
            __M_writer(str(comment_system_id))
            __M_writer('">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_late_load_js(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 49
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


