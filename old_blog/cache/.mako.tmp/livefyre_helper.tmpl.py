# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1391984309.789533
_enable_loop = True
_template_filename = '/Users/aaronmeurer/Documents/nikola/nikola/data/themes/base/templates/livefyre_helper.tmpl'
_template_uri = 'livefyre_helper.tmpl'
_source_encoding = 'utf-8'
_exports = ['comment_link', 'comment_form', 'comment_link_script']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 21
        __M_writer('\n\n')
        # SOURCE LINE 29
        __M_writer('\n\n\n')
        # SOURCE LINE 37
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_comment_link(context,link,identifier):
    __M_caller = context.caller_stack._push_frame()
    try:
        comment_system_id = context.get('comment_system_id', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 23
        __M_writer('\n    <p>\n    <a href="')
        # SOURCE LINE 25
        __M_writer(str(link))
        __M_writer('">\n    <span class="livefyre-commentcount" data-lf-site-id="')
        # SOURCE LINE 26
        __M_writer(str(comment_system_id))
        __M_writer('" data-lf-article-id="')
        __M_writer(str(identifier))
        __M_writer('">\n    0 Comments\n    </span></a>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_comment_form(context,url,title,identifier):
    __M_caller = context.caller_stack._push_frame()
    try:
        comment_system_id = context.get('comment_system_id', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer('\n<div id="livefyre-comments"></div>\n<script type="text/javascript" src="http://zor.livefyre.com/wjs/v3.0/javascripts/livefyre.js"></script>\n<script type="text/javascript">\n(function () {\n    var articleId = "')
        # SOURCE LINE 7
        __M_writer(str(identifier))
        __M_writer('";\n    fyre.conv.load({}, [{\n        el: \'livefyre-comments\',\n        network: "livefyre.com",\n        siteId: "')
        # SOURCE LINE 11
        __M_writer(str(comment_system_id))
        __M_writer('",\n        articleId: articleId,\n        signed: false,\n        collectionMeta: {\n            articleId: articleId,\n            url: fyre.conv.load.makeCollectionUrl(),\n        }\n    }], function() {});\n}());\n</script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_comment_link_script(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 32
        __M_writer('\n<script\n        type="text/javascript"\n        src="http://zor.livefyre.com/wjs/v1.0/javascripts/CommentCount.js">\n</script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


