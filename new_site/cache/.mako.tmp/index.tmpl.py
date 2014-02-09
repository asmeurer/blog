# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1391984309.848141
_enable_loop = True
_template_filename = '/Users/aaronmeurer/Documents/nikola/nikola/data/themes/base/templates/index.tmpl'
_template_uri = 'index.tmpl'
_source_encoding = 'utf-8'
_exports = ['content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 2
    ns = runtime.TemplateNamespace('helper', context._clean_inheritance_tokens(), templateuri='index_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'helper')] = ns

    # SOURCE LINE 3
    ns = runtime.TemplateNamespace('comments', context._clean_inheritance_tokens(), templateuri='comments_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'comments')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        date_format = context.get('date_format', UNDEFINED)
        index_teasers = context.get('index_teasers', UNDEFINED)
        posts = context.get('posts', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        helper = _mako_get_namespace(context, 'helper')
        comments = _mako_get_namespace(context, 'comments')
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer('\n')
        # SOURCE LINE 3
        __M_writer('\n')
        # SOURCE LINE 4
        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 29
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        date_format = context.get('date_format', UNDEFINED)
        index_teasers = context.get('index_teasers', UNDEFINED)
        posts = context.get('posts', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        helper = _mako_get_namespace(context, 'helper')
        comments = _mako_get_namespace(context, 'comments')
        __M_writer = context.writer()
        # SOURCE LINE 5
        __M_writer('\n')
        # SOURCE LINE 6
        for post in posts:
            # SOURCE LINE 7
            __M_writer('        <article class="postbox h-entry post-')
            __M_writer(str(post.meta('type')))
            __M_writer('">\n        <h1 class="p-name"><a href="')
            # SOURCE LINE 8
            __M_writer(str(post.permalink()))
            __M_writer('" class="u-url">')
            __M_writer(str(post.title()))
            __M_writer('</a>\n        <small>&nbsp;&nbsp;\n             ')
            # SOURCE LINE 10
            __M_writer(str(messages("Posted:")))
            __M_writer(' <time class="published dt-published" datetime="')
            __M_writer(str(post.date.isoformat()))
            __M_writer('">')
            __M_writer(str(post.formatted_date(date_format)))
            __M_writer('</time>\n        </small></h1>\n        <hr>\n')
            # SOURCE LINE 13
            if index_teasers:
                # SOURCE LINE 14
                __M_writer('        <div class="p-summary">\n        ')
                # SOURCE LINE 15
                __M_writer(str(post.text(teaser_only=True)))
                __M_writer('\n')
                # SOURCE LINE 16
            else:
                # SOURCE LINE 17
                __M_writer('        <div class="e-content">\n        ')
                # SOURCE LINE 18
                __M_writer(str(post.text(teaser_only=False)))
                __M_writer('\n')
            # SOURCE LINE 20
            __M_writer('        </div>\n')
            # SOURCE LINE 21
            if not post.meta('nocomments'):
                # SOURCE LINE 22
                __M_writer('            ')
                __M_writer(str(comments.comment_link(post.permalink(), post._base_path)))
                __M_writer('\n')
            # SOURCE LINE 24
            __M_writer('        </article>\n')
        # SOURCE LINE 26
        __M_writer('    ')
        __M_writer(str(helper.html_pager()))
        __M_writer('\n    ')
        # SOURCE LINE 27
        __M_writer(str(comments.comment_link_script()))
        __M_writer('\n\t')
        # SOURCE LINE 28
        __M_writer(str(helper.mathjax_script(posts)))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


