# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1391984309.539001
_enable_loop = True
_template_filename = '/Users/aaronmeurer/Documents/nikola/nikola/data/themes/bootstrap3/templates/base.tmpl'
_template_uri = 'base.tmpl'
_source_encoding = 'utf-8'
_exports = ['sourcelink', 'content', 'belowtitle', 'extra_js', 'extra_head']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 2
    ns = runtime.TemplateNamespace('base', context._clean_inheritance_tokens(), templateuri='base_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'base')] = ns

    # SOURCE LINE 4
    ns = runtime.TemplateNamespace('notes', context._clean_inheritance_tokens(), templateuri='annotation_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'notes')] = ns

    # SOURCE LINE 3
    ns = runtime.TemplateNamespace('bootstrap', context._clean_inheritance_tokens(), templateuri='bootstrap_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'bootstrap')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'notes')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'bootstrap')._populate(_import_ns, ['*'])
        annotations = _import_ns.get('annotations', context.get('annotations', UNDEFINED))
        def sourcelink():
            return render_sourcelink(context._locals(__M_locals))
        search_form = _import_ns.get('search_form', context.get('search_form', UNDEFINED))
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        body_end = _import_ns.get('body_end', context.get('body_end', UNDEFINED))
        def belowtitle():
            return render_belowtitle(context._locals(__M_locals))
        lang = _import_ns.get('lang', context.get('lang', UNDEFINED))
        blog_title = _import_ns.get('blog_title', context.get('blog_title', UNDEFINED))
        def extra_js():
            return render_extra_js(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        notes = _mako_get_namespace(context, 'notes')
        bootstrap = _mako_get_namespace(context, 'bootstrap')
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        base = _mako_get_namespace(context, 'base')
        post = _import_ns.get('post', context.get('post', UNDEFINED))
        extra_head_data = _import_ns.get('extra_head_data', context.get('extra_head_data', UNDEFINED))
        hide_sourcelink = _import_ns.get('hide_sourcelink', context.get('hide_sourcelink', UNDEFINED))
        abs_link = _import_ns.get('abs_link', context.get('abs_link', UNDEFINED))
        translations = _import_ns.get('translations', context.get('translations', UNDEFINED))
        content_footer = _import_ns.get('content_footer', context.get('content_footer', UNDEFINED))
        comment_system = _import_ns.get('comment_system', context.get('comment_system', UNDEFINED))
        set_locale = _import_ns.get('set_locale', context.get('set_locale', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer('\n')
        # SOURCE LINE 3
        __M_writer('\n')
        # SOURCE LINE 4
        __M_writer('\n')
        # SOURCE LINE 5
        __M_writer(str(set_locale(lang)))
        __M_writer('\n<!DOCTYPE html>\n<html\n')
        # SOURCE LINE 8
        if comment_system == 'facebook':
            # SOURCE LINE 9
            __M_writer('xmlns:fb="http://ogp.me/ns/fb#"\n')
        # SOURCE LINE 11
        __M_writer('lang="')
        __M_writer(str(lang))
        __M_writer('">\n<head>\n    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n    ')
        # SOURCE LINE 14
        __M_writer(str(bootstrap.html_head()))
        __M_writer('\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        # SOURCE LINE 16
        __M_writer('\n')
        # SOURCE LINE 17
        if annotations and post and not post.meta('noannotations'):
            # SOURCE LINE 18
            __M_writer('        ')
            __M_writer(str(notes.css()))
            __M_writer('\n')
            # SOURCE LINE 19
        elif not annotations and post and post.meta('annotations'):
            # SOURCE LINE 20
            __M_writer('        ')
            __M_writer(str(notes.css()))
            __M_writer('\n')
        # SOURCE LINE 22
        __M_writer('    ')
        __M_writer(str(extra_head_data))
        __M_writer('\n</head>\n<body>\n<!-- Menubar -->\n\n<nav class="navbar navbar-inverse navbar-fixed-top" role="navigation">\n    <div class="navbar-header">\n        <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-ex1-collapse">\n          <span class="sr-only">Toggle navigation</span>\n          <span class="icon-bar"></span>\n          <span class="icon-bar"></span>\n          <span class="icon-bar"></span>\n        </button>\n        <a class="navbar-brand" href="')
        # SOURCE LINE 35
        __M_writer(str(abs_link('/')))
        __M_writer('">')
        __M_writer(str(blog_title))
        __M_writer('</a>\n    </div>\n    <div class="collapse navbar-collapse navbar-ex1-collapse">\n        <ul class="nav navbar-nav">\n            ')
        # SOURCE LINE 39
        __M_writer(str(bootstrap.html_navigation_links()))
        __M_writer('\n        </ul>\n')
        # SOURCE LINE 41
        if search_form:
            # SOURCE LINE 42
            __M_writer('            ')
            __M_writer(str(search_form))
            __M_writer('\n')
        # SOURCE LINE 44
        __M_writer('\n        <ul class="nav navbar-nav navbar-right">\n            ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'belowtitle'):
            context['self'].belowtitle(**pageargs)
        

        # SOURCE LINE 50
        __M_writer('\n')
        # SOURCE LINE 51
        if not hide_sourcelink:
            # SOURCE LINE 52
            __M_writer('                ')
            if 'parent' not in context._data or not hasattr(context._data['parent'], 'sourcelink'):
                context['self'].sourcelink(**pageargs)
            

            __M_writer('\n')
        # SOURCE LINE 54
        __M_writer('        </ul>\n    </div><!-- /.navbar-collapse -->\n</nav>\n\n<!-- End of Menubar -->\n\n<div class="container">\n    <div class="body-content">\n        <!--Body content-->\n        <div class="row">\n            ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 64
        __M_writer('\n        </div>\n        <!--End of body content-->\n\n        <footer>\n            ')
        # SOURCE LINE 69
        __M_writer(str(content_footer))
        __M_writer('\n        </footer>\n    </div>\n</div>\n\n')
        # SOURCE LINE 74
        __M_writer(str(bootstrap.late_load_js()))
        __M_writer('\n')
        # SOURCE LINE 75
        __M_writer(str(base.html_social()))
        __M_writer('\n    <script type="text/javascript">jQuery("a.image-reference").colorbox({rel:"gal",maxWidth:"100%",maxHeight:"100%",scalePhotos:true});</script>\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_js'):
            context['self'].extra_js(**pageargs)
        

        # SOURCE LINE 77
        __M_writer('\n')
        # SOURCE LINE 78
        if annotations and post and not post.meta('noannotations'):
            # SOURCE LINE 79
            __M_writer('        ')
            __M_writer(str(notes.code()))
            __M_writer('\n')
            # SOURCE LINE 80
        elif not annotations and post and post.meta('annotations'):
            # SOURCE LINE 81
            __M_writer('        ')
            __M_writer(str(notes.code()))
            __M_writer('\n')
        # SOURCE LINE 83
        __M_writer(str(body_end))
        __M_writer('\n</body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_sourcelink(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'notes')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'bootstrap')._populate(_import_ns, ['*'])
        def sourcelink():
            return render_sourcelink(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'notes')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'bootstrap')._populate(_import_ns, ['*'])
        def content():
            return render_content(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_belowtitle(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'notes')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'bootstrap')._populate(_import_ns, ['*'])
        def belowtitle():
            return render_belowtitle(context)
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        translations = _import_ns.get('translations', context.get('translations', UNDEFINED))
        bootstrap = _mako_get_namespace(context, 'bootstrap')
        __M_writer = context.writer()
        # SOURCE LINE 46
        __M_writer('\n')
        # SOURCE LINE 47
        if len(translations) > 1:
            # SOURCE LINE 48
            __M_writer('                <li>')
            __M_writer(str(bootstrap.html_translations()))
            __M_writer('</li>\n')
        # SOURCE LINE 50
        __M_writer('            ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_js(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'notes')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'bootstrap')._populate(_import_ns, ['*'])
        def extra_js():
            return render_extra_js(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'notes')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'bootstrap')._populate(_import_ns, ['*'])
        def extra_head():
            return render_extra_head(context)
        __M_writer = context.writer()
        # SOURCE LINE 15
        __M_writer('\n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


