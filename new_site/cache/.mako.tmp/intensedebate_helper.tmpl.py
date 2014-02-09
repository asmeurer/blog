# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1391984309.80014
_enable_loop = True
_template_filename = '/Users/aaronmeurer/Documents/nikola/nikola/data/themes/base/templates/intensedebate_helper.tmpl'
_template_uri = 'intensedebate_helper.tmpl'
_source_encoding = 'utf-8'
_exports = ['comment_link', 'comment_form', 'comment_link_script']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 11
        __M_writer('\n\n')
        # SOURCE LINE 22
        __M_writer('\n\n')
        # SOURCE LINE 25
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_comment_link(context,link,identifier):
    __M_caller = context.caller_stack._push_frame()
    try:
        comment_system_id = context.get('comment_system_id', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 13
        __M_writer('\n<a href="{link}" onclick="this.href=\'')
        # SOURCE LINE 14
        __M_writer(str(link))
        __M_writer('\'; this.target=\'_self\';"><span class=\'IDCommentsReplace\' style=\'display:none\'>')
        __M_writer(str(identifier))
        __M_writer("</span>\n<script>\nvar idcomments_acct = '")
        # SOURCE LINE 16
        __M_writer(str(comment_system_id))
        __M_writer('\';\nvar idcomments_post_id = "')
        # SOURCE LINE 17
        __M_writer(str(identifier))
        __M_writer('";\nvar idcomments_post_url = "')
        # SOURCE LINE 18
        __M_writer(str(link))
        __M_writer('";\n</script>\n<script type="text/javascript" src="http://www.intensedebate.com/js/genericLinkWrapperV2.js"></script>\n</a>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_comment_form(context,url,title,identifier):
    __M_caller = context.caller_stack._push_frame()
    try:
        comment_system_id = context.get('comment_system_id', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer("\n<script>\nvar idcomments_acct = '")
        # SOURCE LINE 4
        __M_writer(str(comment_system_id))
        __M_writer('\';\nvar idcomments_post_id = "')
        # SOURCE LINE 5
        __M_writer(str(identifier))
        __M_writer('";\nvar idcomments_post_url = "')
        # SOURCE LINE 6
        __M_writer(str(url))
        __M_writer('";\n</script>\n<span id="IDCommentsPostTitle" style="display:none"></span>\n<script type=\'text/javascript\' src=\'http://www.intensedebate.com/js/genericCommentWrapperV2.js\'></script>\n</script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_comment_link_script(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 24
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


