# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1391984309.770063
_enable_loop = True
_template_filename = '/Users/aaronmeurer/Documents/nikola/nikola/data/themes/base/templates/disqus_helper.tmpl'
_template_uri = 'disqus_helper.tmpl'
_source_encoding = 'utf-8'
_exports = ['comment_link', 'html_disqus', 'html_disqus_link', 'html_disqus_script', 'comment_form', 'comment_link_script']


# SOURCE LINE 2

import json
translations = {
    'es': 'es_ES',
}


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 7
        __M_writer('\n\n')
        # SOURCE LINE 31
        __M_writer('\n\n')
        # SOURCE LINE 38
        __M_writer('\n\n\n')
        # SOURCE LINE 45
        __M_writer('\n\n')
        # SOURCE LINE 50
        __M_writer('\n\n')
        # SOURCE LINE 54
        __M_writer('\n\n')
        # SOURCE LINE 58
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_comment_link(context,link,identifier):
    __M_caller = context.caller_stack._push_frame()
    try:
        comment_system_id = context.get('comment_system_id', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 33
        __M_writer('\n    <p>\n')
        # SOURCE LINE 35
        if comment_system_id:
            # SOURCE LINE 36
            __M_writer('        <a href="')
            __M_writer(str(link))
            __M_writer('#disqus_thread" data-disqus-identifier="')
            __M_writer(str(identifier))
            __M_writer('">Comments</a>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_disqus(context,url,title,identifier):
    __M_caller = context.caller_stack._push_frame()
    try:
        def comment_form(url,title,identifier):
            return render_comment_form(context,url,title,identifier)
        __M_writer = context.writer()
        # SOURCE LINE 48
        __M_writer('\n    ')
        # SOURCE LINE 49
        __M_writer(str(comment_form(url, title, identifier)))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_disqus_link(context,link,identifier):
    __M_caller = context.caller_stack._push_frame()
    try:
        def comment_link(link,identifier):
            return render_comment_link(context,link,identifier)
        __M_writer = context.writer()
        # SOURCE LINE 52
        __M_writer('\n    ')
        # SOURCE LINE 53
        __M_writer(str(comment_link(link, identifier)))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_disqus_script(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        def comment_link_script():
            return render_comment_link_script(context)
        __M_writer = context.writer()
        # SOURCE LINE 56
        __M_writer('\n    ')
        # SOURCE LINE 57
        __M_writer(str(comment_link_script()))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_comment_form(context,url,title,identifier):
    __M_caller = context.caller_stack._push_frame()
    try:
        comment_system_id = context.get('comment_system_id', UNDEFINED)
        lang = context.get('lang', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 9
        __M_writer('\n')
        # SOURCE LINE 10
        if comment_system_id:
            # SOURCE LINE 11
            __M_writer('        <div id="disqus_thread"></div>\n        <script>\n        var disqus_shortname ="')
            # SOURCE LINE 13
            __M_writer(str(comment_system_id))
            __M_writer('",\n')
            # SOURCE LINE 14
            if url:
                # SOURCE LINE 15
                __M_writer('            disqus_url="')
                __M_writer(str(url))
                __M_writer('",\n')
            # SOURCE LINE 17
            __M_writer('        disqus_title=')
            __M_writer(str(json.dumps(title)))
            __M_writer(',\n        disqus_identifier="')
            # SOURCE LINE 18
            __M_writer(str(identifier))
            __M_writer('",\n        disqus_config = function () {\n            this.language = "')
            # SOURCE LINE 20
            __M_writer(str(translations.get(lang, lang)))
            __M_writer('";\n        };\n        (function() {\n            var dsq = document.createElement(\'script\'); dsq.async = true;\n            dsq.src = \'//\' + disqus_shortname + \'.disqus.com/embed.js\';\n            (document.getElementsByTagName(\'head\')[0] || document.getElementsByTagName(\'body\')[0]).appendChild(dsq);\n        })();\n    </script>\n    <noscript>Please enable JavaScript to view the <a href="http://disqus.com/?ref_noscript" rel="nofollow">comments powered by Disqus.</a></noscript>\n    <a href="http://disqus.com" class="dsq-brlink" rel="nofollow">Comments powered by <span class="logo-disqus">Disqus</span></a>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_comment_link_script(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        comment_system_id = context.get('comment_system_id', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 41
        __M_writer('\n')
        # SOURCE LINE 42
        if comment_system_id:
            # SOURCE LINE 43
            __M_writer('       <script>var disqus_shortname="')
            __M_writer(str(comment_system_id))
            __M_writer('";(function(){var a=document.createElement("script");a.async=true;a.src="//"+disqus_shortname+".disqus.com/count.js";(document.getElementsByTagName("head")[0]||document.getElementsByTagName("body")[0]).appendChild(a)}());</script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


