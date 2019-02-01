# -*- coding: utf-8 -*-
__filename = u'c:\\cdb\\contact_elements_server_15.3.13\\cdb\\chrome\\documentation\\layout.html'
__tokens = {42: (u" title = lang._l('branding_doc_portal_title') ", 4, 12), 116: (u'title + page_title | title', 5, 25), 1434: (u'categories', 24, 34), 1455: (u'.docapp-category-box.${category.name} {\n            background-color: ${category.color};\n        }\n        .docapp-category-box.${category.name} .box-icon,\n        .docapp-navbar-main ul.navbar-category li a.${category.name} .icon {\n            background-image: url("${category.icon}");\n        }', 25, 8), 1478: (u'category.name', 25, 31), 1527: (u'category.color', 26, 32), 1585: (u'category.name', 28, 31), 1665: (u'category.name', 29, 54), 1725: (u'category.icon', 30, 37), 1821: (u"'catbar' if catbar else False", 35, 28), 2564: (u'${approot}/${lang.iso}/', 48, 33), 2566: (u'approot', 48, 35), 2577: (u'lang.iso', 48, 46), 2623: (u"${lang._l('branding_doc_portal_title')}", 49, 34), 2625: (u"lang._l('branding_doc_portal_title')", 49, 36), 3211: (u'lang.title()', 60, 47), 3442: (u'languages', 64, 53), 3507: (u"'active' if router.is_current('overview', {'lang_iso': language.iso}) else ''", 65, 54), 3683: (u"router.link_to(None, {'lang_iso': language.iso}, keep_query=True)", 67, 61), 3798: (u'language.title()', 68, 48), 4005: (u'searchbar', 73, 60), 4064: (u'load: searchbar.html', 74, 47), 4064: (u'load: searchbar.html', 74, 47), 4224: (u'catbar', 77, 78), 4277: (u'categories', 78, 44), 4311: (u"'active' if\n                            router.is_current('overview.category', {'cat_name': cat.name}) else ''", 78, 78), 4512: (u"router.link_to('overview.category', {'cat_name': cat.name})", 81, 57), 4578: (u' cat.nam', 81, 123), 4665: (u'cat.title', 82, 75), 4852: (u' classes = ["main-container"] ', 90, 12), 4897: (u' if sidebar: classes.append("has-sidebar") ', 91, 12), 4955: (u'\n        try: classes.append(page_name)\n        except: pass ', 92, 12), 5031: (u' class_names = " ".join(classes) ', 95, 12), 5098: (u'class_names', 96, 31), 5140: (u'sidebar', 97, 28), 5332: (u'sidebar', 100, 28), 5760: (u"&copy; ${year}\n                    ${lang._l('branding_company_name')}", 110, 40), 5769: (u'year', 110, 49), 5797: (u"lang._l('branding_company_name')", 111, 22), 5930: (u'highlight', 116, 34), 5954: (u'var hlText = "${highlight}".replace(/[\\-\\[\\]\\/\\{\\}\\(\\)\\*\\+\\?\\\\\\^\\$\\|]/g, "");\n            if(hlText.length>1){\n                $(".docapp-content").highlight(hlText);\n            }', 117, 12), 5970: (u'highlight', 117, 28), 6169: (u'$(\'#search\').typeahead({\n            highlight: true,\n            minLength: 2\n        }, {\n            name: \'search-ac\',\n            limit: 8,\n            source: function (query, process, asyncProcess) {\n                $.ajax({\n                    type: \'json\',\n                    url:\n                            "${router.link_to(\'overview.search_ac\', None, False)}",\n                    data: { q: query },\n                    type: \'GET\',\n                    success: function(data) {\n                        return asyncProcess(data);\n                    }\n                });\n            }\n        });', 123, 8), 6491: (u"router.link_to('overview.search_ac', None, False)", 133, 31)}

from sys import exc_info as _exc_info
from chameleon.py26 import lookup_attr as _lookup_attr

_static_548967088 = {u'class': u'sidebar-expand-btn', }
_static_549634680 = u'load: searchbar.html'
_static_535398832 = {u'content': u'user-scalable=yes, width=device-width, initial-scale=1', u'name': u'viewport', }
_static_549566952 = {u'href': u'/static/imgid/branding_web_app_icon.png', u'rel': u'apple-touch-icon', }
_static_549548216 = {u'class': u"'catbar' if catbar else False", }
_static_549668960 = {u'class': u'copyright', }
_static_550364328 = {u'src': u'/static/jscript/doc/app.js', }
_static_549550400 = {u'class': u'docapp-navbar-main', }
_static_447069488 = {u'content': u'text/html; charset=UTF-8', u'http-equiv': u'Content-Type', }
_static_549550680 = {u'class': u'container-fluid', }
_static_550542080 = {u'class': u'sr-only', }
_static_550344968 = {u'class': u'navbar-brand', }
_static_550542472 = {u'class': u'icon-bar', }
_static_550348672 = {u'class': u'caret', }
_static_447068816 = {u'content': u'IE=edge', u'http-equiv': u'X-UA-Compatible', }
_static_551113280 = {u'class': u'class_names', }
_static_550349568 = {u'class': u'dropdown-menu dropdown-menu-right', }
_static_428309248 = {}
_static_549564488 = {u'href': u'/static/imgid/branding_web_favicon.ico', u'rel': u'shortcut icon', }
_static_549637032 = {u'class': u'navbar-form', }
_static_550343960 = {u'class': u'icon-bar', }
_static_549551800 = {u'class': u'navbar-header', }
_static_550346936 = {u'class': u'glyphicon glyphicon-globe', }
_static_549637256 = {u'href': u"router.link_to(None, {'lang_iso': language.iso}, keep_query=True)", }
_static_550342896 = {u'class': u'icon-bar', }
_static_549566728 = {u'href': u'/static/imgid/branding_web_favicon.ico', u'rel': u'icon', }
_static_550889736 = {u'class': u'btn-group navbar-btn navbar-right', }
_static_549549952 = {u'class': u'navbar navbar-default navbar-fixed-top', }
_static_548799768 = {u'src': u'/static/jscript/doc/bootstrap.min.js', }
_static_551115408 = {u'data-offset-top': u'0', u'class': u'sidebar-container', u'data-offset-bottom': u'50', u'data-spy': u'affix', }
_static_548825856 = {u'href': u'/static/images/doc/css/bootstrap-theme.min.css', u'type': u'text/css', u'rel': u'stylesheet', }
_static_549568184 = {u'href': u'/static/images/doc/css/bootstrap.min.css', u'type': u'text/css', u'rel': u'stylesheet', }
_static_549667504 = {u'class': u'footer', }
_static_550345864 = {u'href': u'${approot}/${lang.iso}/', u'title': u"${lang._l('branding_doc_portal_title')}", }
_static_549667056 = {u'class': u'col-xs-12', }
_static_548969776 = {u'class': u'row', }
_static_550350688 = {u'class': u"'active' if router.is_current('overview', {'lang_iso': language.iso}) else ''", }
_static_548826360 = {u'href': u'/static/images/doc/css/app.css', u'type': u'text/css', u'rel': u'stylesheet', }
_static_548800608 = {u'src': u'/static/jscript/doc/jquery.highlight-5.js', }
_static_550887496 = {u'role': u'navigation', u'class': u'collapse navbar-collapse', u'id': u'navbar-collapse-1', }
_static_535397992 = {u'content': u'yes', u'name': u'apple-mobile-web-app-capable', }
_static_550881152 = {u'class': u"'active' if\n                            router.is_current('overview.category', {'cat_name': cat.name}) else ''", }
_static_548801392 = {u'src': u'/static/jscript/doc/typeahead.jquery.js', }
_static_549635912 = {u'class': u'nav navbar-nav navbar-category', }
_static_548967816 = {u'class': u'glyphicon glyphicon-list', }
_static_535399448 = {u'content': u"default-src 'self' ; script-src 'self' 'unsafe-inline' ; style-src 'self' 'unsafe-inline' ; ", u'http-equiv': u'Content-Security-Policy', }
_static_550882440 = {u'class': u'icon', }
_static_550540904 = {u'data-toggle': u'collapse', u'type': u'button', u'class': u'navbar-toggle collapsed', u'aria-expanded': u'false', u'data-target': u'#navbar-collapse-1', }
_static_548969048 = {u'class': u'content-container docapp-content container-fluid', }
_static_550880480 = {u'href': u"router.link_to('overview.category', {'cat_name': cat.name})", u'class': u'cat.name', }
_static_548798704 = {u'src': u'/static/jscript/doc/jquery-2.2.1.min.js', }
_static_550890128 = {u'data-toggle': u'dropdown', u'aria-haspopup': u'true', u'class': u'btn btn-default dropdown-toggle', u'aria-expanded': u'false', }

import re
import functools
from itertools import chain as __chain
from sys import exc_clear as __exc_clear
__marker = object()
g_re_amp = re.compile('&(?!([A-Za-z]+|#[0-9]+);)')
g_re_needs_escape = re.compile('[&<>\\"\\\']').search
__re_whitespace = functools.partial(re.compile('\\s+').sub, ' ')

def initialize(__loader, macros, nothing, template):

    def render(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
        __append = __stream.append
        __re_amp = g_re_amp
        __token = None
        __re_needs_escape = g_re_needs_escape

        def __convert(target):
            if (target is None):
                return
            __tt = type(target)
            if ((__tt is int) or (__tt is float) or (__tt is long)):
                target = unicode(target)
            else:
                if (__tt is str):
                    target = decode(target)
                else:
                    if (__tt is not unicode):
                        try:
                            target = target.__html__
                        except AttributeError:
                            __converted = convert(target)
                            target = (unicode(target) if (target is __converted) else __converted)
                        else:
                            target = target()
            return target

        def __quote(target, quote, quote_entity, default, default_marker):
            if (target is None):
                return
            if (target is default_marker):
                return default
            __tt = type(target)
            if ((__tt is int) or (__tt is float) or (__tt is long)):
                target = unicode(target)
            else:
                if (__tt is str):
                    target = decode(target)
                else:
                    if (__tt is not unicode):
                        try:
                            target = target.__html__
                        except:
                            __converted = convert(target)
                            target = (unicode(target) if (target is __converted) else __converted)
                        else:
                            return target()
                if (target is not None):
                    try:
                        escape = (__re_needs_escape(target) is not None)
                    except TypeError:
                        pass
                    else:
                        if escape:
                            if ('&' in target):
                                target = target.replace('&', '&amp;')
                            if ('<' in target):
                                target = target.replace('<', '&lt;')
                            if ('>' in target):
                                target = target.replace('>', '&gt;')
                            if ((quote is not None) and (quote in target)):
                                target = target.replace(quote, quote_entity)
            return target
        decode = econtext['__decode']
        convert = econtext['__convert']
        translate = econtext['__translate']
        try:
            __slot_sidebar = econtext[u'__slot_sidebar'].pop()
        except:
            __slot_sidebar = None

        try:
            __slot_content = econtext[u'__slot_content'].pop()
        except:
            __slot_content = None

        try:
            getitem = econtext.__getitem__
            get = econtext.get
            __append(u'<!DOCTYPE html>')
            __append(u'\n')

            # <Static value=<_ast.Dict object at 0x0000000019877B00> name=None at 19877c50> -> __attrs_429392840
            __attrs_429392840 = _static_428309248

            # <html ... (2:0)
            # --------------------------------------------------------
            __append(u'<html>')
            __append(u'\n')

            # <Static value=<_ast.Dict object at 0x0000000019877B00> name=None at 19877c50> -> __attrs_447067752
            __attrs_447067752 = _static_428309248

            # <head ... (3:0)
            # --------------------------------------------------------
            __append(u'<head>')
            __append(u'\n    ')
            __token = 42
            econtext['title'] = getitem('lang')._l('branding_doc_portal_title')
            __append(u'\n    ')

            # <Static value=<_ast.Dict object at 0x0000000019877B00> name=None at 19877c50> -> __attrs_447069824
            __attrs_447069824 = _static_428309248

            # <title ... (5:4)
            # --------------------------------------------------------
            __append(u'<title>')
            __default_447069376 = '__default'

            # <Value u'title + page_title | title' (5:25)> -> __cache_447067528
            __token = 116
            try:
                __cache_447067528 = (getitem('title') + getitem('page_title'))
            except (NameError, ValueError, AttributeError, LookupError, TypeError, ):
                __cache_447067528 = getitem('title')
                __exc_clear()


            # <Identity expression=<Value u'title + page_title | title' (5:25)> value=<_ast.Str object at 0x000000001AA5B4A8> at 1aa5b470> -> __condition
            __expression = __cache_447067528
            __value = '__default'
            __condition = (__expression is __value)
            if __condition:
                __append(u'Dokumentations Portal')
            else:
                __content = __cache_447067528
                __content = __quote(__content, None, '\xad', None, None)
                if (__content is not None):
                    __append(__content)
            __append(u'</title>')
            __append(u'\n    ')

            # <Static value=<_ast.Dict object at 0x000000001AA5BD30> name=None at 1aa5be10> -> __attrs_447068536
            __attrs_447068536 = _static_447069488

            # <meta ... (6:4)
            # --------------------------------------------------------
            __append(u'<meta')
            __append(u' http-equiv="Content-Type"')
            __append(u' content="text/html; charset=UTF-8"')
            __append(u'>')
            __append(u'\n    ')

            # <Static value=<_ast.Dict object at 0x000000001AA5BA90> name=None at 1aa5b940> -> __attrs_535397488
            __attrs_535397488 = _static_447068816

            # <meta ... (7:4)
            # --------------------------------------------------------
            __append(u'<meta')
            __append(u' http-equiv="X-UA-Compatible"')
            __append(u' content="IE=edge"')
            __append(u'>')
            __append(u'\n    ')

            # <Static value=<_ast.Dict object at 0x000000001FE98668> name=None at 1fe98630> -> __attrs_535398160
            __attrs_535398160 = _static_535397992

            # <meta ... (8:4)
            # --------------------------------------------------------
            __append(u'<meta')
            __append(u' name="apple-mobile-web-app-capable"')
            __append(u' content="yes"')
            __append(u' />')
            __append(u'\n    ')

            # <Static value=<_ast.Dict object at 0x000000001FE989B0> name=None at 1fe98978> -> __attrs_535399056
            __attrs_535399056 = _static_535398832

            # <meta ... (9:4)
            # --------------------------------------------------------
            __append(u'<meta')
            __append(u' name="viewport"')
            __append(u' content="user-scalable=yes, width=device-width, initial-scale=1"')
            __append(u' >')
            __append(u'\n    ')

            # <Static value=<_ast.Dict object at 0x000000001FE98C18> name=None at 1fe98dd8> -> __attrs_549565160
            __attrs_549565160 = _static_535399448

            # <meta ... (10:4)
            # --------------------------------------------------------
            __append(u'<meta')
            __append(u' http-equiv="Content-Security-Policy"')
            __append(u' content="default-src \'self\' ; script-src \'self\' \'unsafe-inline\' ; style-src \'self\' \'unsafe-inline\' ; "')
            __append(u'>')
            __append(u'\n\n    ')

            # <Static value=<_ast.Dict object at 0x0000000020C1B048> name=None at 20c1b128> -> __attrs_549565496
            __attrs_549565496 = _static_549564488

            # <link ... (12:4)
            # --------------------------------------------------------
            __append(u'<link')
            __append(u' rel="shortcut icon"')
            __append(u' href="/static/imgid/branding_web_favicon.ico"')
            __append(u'>')
            __append(u'\n    ')

            # <Static value=<_ast.Dict object at 0x0000000020C1B908> name=None at 20c1b8d0> -> __attrs_549566112
            __attrs_549566112 = _static_549566728

            # <link ... (13:4)
            # --------------------------------------------------------
            __append(u'<link')
            __append(u' rel="icon"')
            __append(u' href="/static/imgid/branding_web_favicon.ico"')
            __append(u'>')
            __append(u'\n    ')

            # <Static value=<_ast.Dict object at 0x0000000020C1B9E8> name=None at 20c1b7f0> -> __attrs_549567960
            __attrs_549567960 = _static_549566952

            # <link ... (14:4)
            # --------------------------------------------------------
            __append(u'<link')
            __append(u' rel="apple-touch-icon"')
            __append(u' href="/static/imgid/branding_web_app_icon.png"')
            __append(u'>')
            __append(u'\n\n    ')

            # <Static value=<_ast.Dict object at 0x0000000020C1BEB8> name=None at 20c1bf28> -> __attrs_548825184
            __attrs_548825184 = _static_549568184

            # <link ... (16:4)
            # --------------------------------------------------------
            __append(u'<link')
            __append(u' href="/static/images/doc/css/bootstrap.min.css"')
            __append(u' rel="stylesheet"')
            __append(u' type="text/css"')
            __append(u' />')
            __append(u'\n    ')

            # <Static value=<_ast.Dict object at 0x0000000020B66B00> name=None at 20b669b0> -> __attrs_548825576
            __attrs_548825576 = _static_548825856

            # <link ... (17:4)
            # --------------------------------------------------------
            __append(u'<link')
            __append(u' href="/static/images/doc/css/bootstrap-theme.min.css"')
            __append(u' rel="stylesheet"')
            __append(u' type="text/css"')
            __append(u' />')
            __append(u'\n    ')

            # <Static value=<_ast.Dict object at 0x0000000020B66CF8> name=None at 20b66978> -> __attrs_548798648
            __attrs_548798648 = _static_548826360

            # <link ... (18:4)
            # --------------------------------------------------------
            __append(u'<link')
            __append(u' href="/static/images/doc/css/app.css"')
            __append(u' rel="stylesheet"')
            __append(u' type="text/css"')
            __append(u' />')
            __append(u'\n    ')

            # <Static value=<_ast.Dict object at 0x0000000020B600F0> name=None at 20b601d0> -> __attrs_548799488
            __attrs_548799488 = _static_548798704

            # <script ... (19:4)
            # --------------------------------------------------------
            __append(u'<script')
            __append(u' src="/static/jscript/doc/jquery-2.2.1.min.js"')
            __append(u'>')
            __append(u'</script>')
            __append(u'\n    ')

            # <Static value=<_ast.Dict object at 0x0000000020B60518> name=None at 20b604e0> -> __attrs_548800440
            __attrs_548800440 = _static_548799768

            # <script ... (20:4)
            # --------------------------------------------------------
            __append(u'<script')
            __append(u' src="/static/jscript/doc/bootstrap.min.js"')
            __append(u'>')
            __append(u'</script>')
            __append(u'\n    ')

            # <Static value=<_ast.Dict object at 0x0000000020B60860> name=None at 20b60898> -> __attrs_548801168
            __attrs_548801168 = _static_548800608

            # <script ... (21:4)
            # --------------------------------------------------------
            __append(u'<script')
            __append(u' src="/static/jscript/doc/jquery.highlight-5.js"')
            __append(u'>')
            __append(u'</script>')
            __append(u'\n    ')

            # <Static value=<_ast.Dict object at 0x0000000020B60B70> name=None at 20b60b38> -> __attrs_548802456
            __attrs_548802456 = _static_548801392

            # <script ... (22:4)
            # --------------------------------------------------------
            __append(u'<script')
            __append(u' src="/static/jscript/doc/typeahead.jquery.js"')
            __append(u'>')
            __append(u'</script>')
            __append(u'\n    ')

            # <Static value=<_ast.Dict object at 0x0000000019877B00> name=None at 19877c50> -> __attrs_548802232
            __attrs_548802232 = _static_428309248

            # <style ... (23:4)
            # --------------------------------------------------------
            __append(u'<style>')
            __append(u'\n        ')
            __backup_category_548685696 = get('category', __marker)

            # <Value u'categories' (24:34)> -> __iterator
            __token = 1434
            __iterator = getitem('categories')
            (__iterator, ____index_549548608, ) = getitem('repeat')(u'category', __iterator)
            econtext['category'] = None
            for __item in __iterator:
                econtext['category'] = __item

                # <Interpolation value=<Substitution u'\n        .docapp-category-box.${category.name} {\n            background-color: ${category.color};\n        }\n        .docapp-category-box.${category.name} .box-icon,\n        .docapp-navbar-main ul.navbar-category li a.${category.name} .icon {\n            background-image: url("${category.icon}");\n        }\n        ' (24:46)> braces_required=True translation=False at 20c171d0> -> __content_100582504
                __token = 1455
                __token = 1478
                __content_100582504 = _lookup_attr(getitem('category'), 'name')
                __content_100582504 = __quote(__content_100582504, '\x00', '&#0;', None, False)
                __token = 1527
                __content_100582504_1525 = _lookup_attr(getitem('category'), 'color')
                __content_100582504_1525 = __quote(__content_100582504_1525, '\x00', '&#0;', None, False)
                __token = 1585
                __content_100582504_1583 = _lookup_attr(getitem('category'), 'name')
                __content_100582504_1583 = __quote(__content_100582504_1583, '\x00', '&#0;', None, False)
                __token = 1665
                __content_100582504_1663 = _lookup_attr(getitem('category'), 'name')
                __content_100582504_1663 = __quote(__content_100582504_1663, '\x00', '&#0;', None, False)
                __token = 1725
                __content_100582504_1723 = _lookup_attr(getitem('category'), 'icon')
                __content_100582504_1723 = __quote(__content_100582504_1723, '\x00', '&#0;', None, False)
                __content_100582504 = ('%s%s%s%s%s%s%s%s%s%s%s' % (u'\n        .docapp-category-box.', (__content_100582504 if (__content_100582504 is not None) else ''), u' {\n            background-color: ', (__content_100582504_1525 if (__content_100582504_1525 is not None) else ''), u';\n        }\n        .docapp-category-box.', (__content_100582504_1583 if (__content_100582504_1583 is not None) else ''), u' .box-icon,\n        .docapp-navbar-main ul.navbar-category li a.', (__content_100582504_1663 if (__content_100582504_1663 is not None) else ''), u' .icon {\n            background-image: url("', (__content_100582504_1723 if (__content_100582504_1723 is not None) else ''), u'");\n        }\n        ', ))
                if (__content_100582504 is None):
                    pass
                else:
                    if (__content_100582504 is False):
                        __content_100582504 = None
                    else:
                        __tt = type(__content_100582504)
                        if ((__tt is int) or (__tt is float) or (__tt is long)):
                            __content_100582504 = unicode(__content_100582504)
                        else:
                            if (__tt is str):
                                __content_100582504 = decode(__content_100582504)
                            else:
                                if (__tt is not unicode):
                                    try:
                                        __content_100582504 = __content_100582504.__html__
                                    except get('AttributeError', AttributeError):
                                        __converted = convert(__content_100582504)
                                        __content_100582504 = (unicode(__content_100582504) if (__content_100582504 is __converted) else __converted)
                                    else:
                                        __content_100582504 = __content_100582504()
                if (__content_100582504 is not None):
                    __append(__content_100582504)
                ____index_549548608 -= 1
                if (____index_549548608 > 0):
                    __append('')
            if (__backup_category_548685696 is __marker):
                del econtext['category']
            else:
                econtext['category'] = __backup_category_548685696
            __append(u'\n    ')
            __append(u'</style>')
            __append(u'\n')
            __append(u'</head>')
            __append(u'\n')

            # <Static value=<_ast.Dict object at 0x0000000020C170B8> name=None at 20c17128> -> __attrs_549548944
            __attrs_549548944 = _static_549548216

            # <body ... (35:0)
            # --------------------------------------------------------
            __append(u'<body')

            # <Builtin id='False' ctx=<_ast.Load object at 0x000000001964B048> at 20acd898> -> __default_549548888
            __default_549548888 = False

            # <Substitution u"'catbar' if catbar else False" (35:28)> -> __attr_class
            __token = 1821
            __attr_class = ('catbar' if getitem('catbar') else False)
            __attr_class = __quote(__attr_class, '"', '&quot;', None, False)
            if (__attr_class is not None):
                __append((u' class="%s"' % __attr_class))
            __append(u'>')
            __append(u'\n    ')

            # <Static value=<_ast.Dict object at 0x0000000020C17940> name=None at 20c17978> -> __attrs_549550120
            __attrs_549550120 = _static_549550400

            # <div ... (36:4)
            # --------------------------------------------------------
            __append(u'<div')
            __append(u' class="docapp-navbar-main"')
            __append(u'>')
            __append(u'\n        ')

            # <Static value=<_ast.Dict object at 0x0000000020C17780> name=None at 20c17c18> -> __attrs_549549280
            __attrs_549549280 = _static_549549952

            # <nav ... (37:8)
            # --------------------------------------------------------
            __append(u'<nav')
            __append(u' class="navbar navbar-default navbar-fixed-top"')
            __append(u'>')
            __append(u'\n            ')

            # <Static value=<_ast.Dict object at 0x0000000020C17A58> name=None at 20c17be0> -> __attrs_549551576
            __attrs_549551576 = _static_549550680

            # <div ... (38:12)
            # --------------------------------------------------------
            __append(u'<div')
            __append(u' class="container-fluid"')
            __append(u'>')
            __append(u'\n                ')

            # <Static value=<_ast.Dict object at 0x0000000020C17EB8> name=None at 20c17f28> -> __attrs_550539560
            __attrs_550539560 = _static_549551800

            # <div ... (39:16)
            # --------------------------------------------------------
            __append(u'<div')
            __append(u' class="navbar-header"')
            __append(u'>')
            __append(u'\n                    ')

            # <Static value=<_ast.Dict object at 0x0000000020D09668> name=None at 20d095f8> -> __attrs_550541576
            __attrs_550541576 = _static_550540904

            # <button ... (40:20)
            # --------------------------------------------------------
            __append(u'<button')
            __append(u' type="button"')
            __append(u' class="navbar-toggle collapsed"')
            __append(u' data-toggle="collapse"')
            __append(u'\n                            data-target="#navbar-collapse-1"')
            __append(u' aria-expanded="false"')
            __append(u'>')
            __append(u'\n                        ')

            # <Static value=<_ast.Dict object at 0x0000000020D09B00> name=None at 20d09ac8> -> __attrs_550541968
            __attrs_550541968 = _static_550542080

            # <span ... (42:24)
            # --------------------------------------------------------
            __append(u'<span')
            __append(u' class="sr-only"')
            __append(u'>')
            __append(u'Toggle navigation')
            __append(u'</span>')
            __append(u'\n                        ')

            # <Static value=<_ast.Dict object at 0x0000000020D09C88> name=None at 20d09eb8> -> __attrs_550543200
            __attrs_550543200 = _static_550542472

            # <span ... (43:24)
            # --------------------------------------------------------
            __append(u'<span')
            __append(u' class="icon-bar"')
            __append(u'>')
            __append(u'</span>')
            __append(u'\n                        ')

            # <Static value=<_ast.Dict object at 0x0000000020CD90F0> name=None at 20cd90b8> -> __attrs_550343456
            __attrs_550343456 = _static_550342896

            # <span ... (44:24)
            # --------------------------------------------------------
            __append(u'<span')
            __append(u' class="icon-bar"')
            __append(u'>')
            __append(u'</span>')
            __append(u'\n                        ')

            # <Static value=<_ast.Dict object at 0x0000000020CD9518> name=None at 20cd94e0> -> __attrs_550344408
            __attrs_550344408 = _static_550343960

            # <span ... (45:24)
            # --------------------------------------------------------
            __append(u'<span')
            __append(u' class="icon-bar"')
            __append(u'>')
            __append(u'</span>')
            __append(u'\n                    ')
            __append(u'</button>')
            __append(u'\n                    ')

            # <Static value=<_ast.Dict object at 0x0000000020CD9908> name=None at 20cd98d0> -> __attrs_550345696
            __attrs_550345696 = _static_550344968

            # <div ... (47:20)
            # --------------------------------------------------------
            __append(u'<div')
            __append(u' class="navbar-brand"')
            __append(u'>')
            __append(u'\n                        ')

            # <Static value=<_ast.Dict object at 0x0000000020CD9C88> name=None at 20cd9ac8> -> __attrs_550344184
            __attrs_550344184 = _static_550345864

            # <a ... (48:24)
            # --------------------------------------------------------
            __append(u'<a')

            # <Builtin id='False' ctx=<_ast.Load object at 0x000000001964B048> at 20acd898> -> __default_550346480
            __default_550346480 = False

            # <Interpolation value=<Substitution u'${approot}/${lang.iso}/' (48:33)> braces_required=True translation=False at 20cd9eb8> -> __attr_href
            __token = 2564
            __token = 2566
            __attr_href = getitem('approot')
            __attr_href = __quote(__attr_href, '"', '&quot;', None, False)
            __token = 2577
            __attr_href_2575 = _lookup_attr(getitem('lang'), 'iso')
            __attr_href_2575 = __quote(__attr_href_2575, '"', '&quot;', None, False)
            __attr_href = ('%s%s%s%s' % ((__attr_href if (__attr_href is not None) else ''), u'/', (__attr_href_2575 if (__attr_href_2575 is not None) else ''), u'/', ))
            if (__attr_href is None):
                pass
            else:
                if (__attr_href is False):
                    __attr_href = None
                else:
                    __tt = type(__attr_href)
                    if ((__tt is int) or (__tt is float) or (__tt is long)):
                        __attr_href = unicode(__attr_href)
                    else:
                        if (__tt is str):
                            __attr_href = decode(__attr_href)
                        else:
                            if (__tt is not unicode):
                                try:
                                    __attr_href = __attr_href.__html__
                                except get('AttributeError', AttributeError):
                                    __converted = convert(__attr_href)
                                    __attr_href = (unicode(__attr_href) if (__attr_href is __converted) else __converted)
                                else:
                                    __attr_href = __attr_href()
            if (__attr_href is not None):
                __append((u' href="%s"' % __attr_href))

            # <Builtin id='False' ctx=<_ast.Load object at 0x000000001964B048> at 20acd898> -> __default_550346144
            __default_550346144 = False

            # <Interpolation value=<Substitution u"${lang._l('branding_doc_portal_title')}" (49:34)> braces_required=True translation=False at 20cd9d68> -> __attr_title
            __token = 2623
            __token = 2625
            __attr_title = _lookup_attr(getitem('lang'), '_l')('branding_doc_portal_title')
            __attr_title = __quote(__attr_title, '"', '&quot;', None, False)
            __attr_title = __attr_title
            if (__attr_title is None):
                pass
            else:
                if (__attr_title is False):
                    __attr_title = None
                else:
                    __tt = type(__attr_title)
                    if ((__tt is int) or (__tt is float) or (__tt is long)):
                        __attr_title = unicode(__attr_title)
                    else:
                        if (__tt is str):
                            __attr_title = decode(__attr_title)
                        else:
                            if (__tt is not unicode):
                                try:
                                    __attr_title = __attr_title.__html__
                                except get('AttributeError', AttributeError):
                                    __converted = convert(__attr_title)
                                    __attr_title = (unicode(__attr_title) if (__attr_title is __converted) else __converted)
                                else:
                                    __attr_title = __attr_title()
            if (__attr_title is not None):
                __append((u'\n                           title="%s"' % __attr_title))
            __append(u'>')
            __append(u'\n                        ')
            __append(u'</a>')
            __append(u'\n                    ')
            __append(u'</div>')
            __append(u'\n                ')
            __append(u'</div>')
            __append(u'\n\n                ')

            # <Static value=<_ast.Dict object at 0x0000000020D5E048> name=None at 20d5e0b8> -> __attrs_550890688
            __attrs_550890688 = _static_550887496

            # <div ... (54:16)
            # --------------------------------------------------------
            __append(u'<div')
            __append(u' class="collapse navbar-collapse"')
            __append(u' role="navigation"')
            __append(u'\n                 id="navbar-collapse-1"')
            __append(u'>')
            __append(u'\n                    ')

            # <Static value=<_ast.Dict object at 0x0000000020D5E908> name=None at 20d5e780> -> __attrs_550890352
            __attrs_550890352 = _static_550889736

            # <div ... (56:20)
            # --------------------------------------------------------
            __append(u'<div')
            __append(u' class="btn-group navbar-btn navbar-right"')
            __append(u'>')
            __append(u'\n                        ')

            # <Static value=<_ast.Dict object at 0x0000000020D5EA90> name=None at 20d5eda0> -> __attrs_550888560
            __attrs_550888560 = _static_550890128

            # <a ... (57:24)
            # --------------------------------------------------------
            __append(u'<a')
            __append(u' class="btn btn-default dropdown-toggle"')
            __append(u' data-toggle="dropdown"')
            __append(u'\n                            aria-haspopup="true"')
            __append(u' aria-expanded="false"')
            __append(u'>')
            __append(u'\n                            ')

            # <Static value=<_ast.Dict object at 0x0000000020CDA0B8> name=None at 20cda080> -> __attrs_550347776
            __attrs_550347776 = _static_550346936

            # <span ... (59:28)
            # --------------------------------------------------------
            __append(u'<span')
            __append(u' class="glyphicon glyphicon-globe"')
            __append(u'>')
            __append(u'</span>')
            __append(u'\n                            ')

            # <Static value=<_ast.Dict object at 0x0000000019877B00> name=None at 19877c50> -> __attrs_550348616
            __attrs_550348616 = _static_428309248

            # <span ... (60:28)
            # --------------------------------------------------------
            __append(u'<span>')
            __default_550348336 = '__default'

            # <Value u'lang.title()' (60:47)> -> __cache_550347608
            __token = 3211
            __cache_550347608 = _lookup_attr(getitem('lang'), 'title')()

            # <Identity expression=<Value u'lang.title()' (60:47)> value=<_ast.Str object at 0x0000000020CDA240> at 20cda4e0> -> __condition
            __expression = __cache_550347608
            __value = '__default'
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_550347608
                __content = __quote(__content, None, '\xad', None, None)
                if (__content is not None):
                    __append(__content)
            __append(u'</span>')
            __append(u'\n                            ')

            # <Static value=<_ast.Dict object at 0x0000000020CDA780> name=None at 20cdaa20> -> __attrs_550350184
            __attrs_550350184 = _static_550348672

            # <span ... (61:28)
            # --------------------------------------------------------
            __append(u'<span')
            __append(u' class="caret"')
            __append(u'>')
            __append(u'</span>')
            __append(u'\n                        ')
            __append(u'</a>')
            __append(u'\n                        ')

            # <Static value=<_ast.Dict object at 0x0000000020CDAB00> name=None at 20cdac18> -> __attrs_550350408
            __attrs_550350408 = _static_550349568

            # <ul ... (63:24)
            # --------------------------------------------------------
            __append(u'<ul')
            __append(u' class="dropdown-menu dropdown-menu-right"')
            __append(u'>')
            __append(u'\n                            ')
            __backup_language_548685472 = get('language', __marker)

            # <Value u'languages' (64:53)> -> __iterator
            __token = 3442
            __iterator = getitem('languages')
            (__iterator, ____index_549635296, ) = getitem('repeat')(u'language', __iterator)
            econtext['language'] = None
            for __item in __iterator:
                econtext['language'] = __item

                # <Static value=<_ast.Dict object at 0x0000000020CDAF60> name=None at 20cdaf28> -> __attrs_549634568
                __attrs_549634568 = _static_550350688

                # <li ... (64:28)
                # --------------------------------------------------------
                __append(u'<li')

                # <Builtin id='False' ctx=<_ast.Load object at 0x000000001964B048> at 20acd898> -> __default_549634176
                __default_549634176 = False

                # <Substitution u"'active' if router.is_current('overview', {'lang_iso': language.iso}) else ''" (65:54)> -> __attr_class
                __token = 3507
                __attr_class = ('active' if _lookup_attr(getitem('router'), 'is_current')('overview', {'lang_iso': _lookup_attr(getitem('language'), 'iso'), }) else '')
                __attr_class = __quote(__attr_class, '"', '&quot;', None, False)
                if (__attr_class is not None):
                    __append((u' class="%s"' % __attr_class))
                __append(u'>')
                __append(u'\n                                ')

                # <Static value=<_ast.Dict object at 0x0000000020C2CC88> name=None at 20c2c588> -> __attrs_549636864
                __attrs_549636864 = _static_549637256

                # <a ... (66:32)
                # --------------------------------------------------------
                __append(u'<a')

                # <Builtin id='False' ctx=<_ast.Load object at 0x000000001964B048> at 20acd898> -> __default_549637312
                __default_549637312 = False

                # <Substitution u"router.link_to(None, {'lang_iso': language.iso}, keep_query=True)" (67:61)> -> __attr_href
                __token = 3683
                __attr_href = _lookup_attr(getitem('router'), 'link_to')(None, {'lang_iso': _lookup_attr(getitem('language'), 'iso'), }, keep_query=True)
                __attr_href = __quote(__attr_href, '"', '&quot;', None, False)
                if (__attr_href is not None):
                    __append((u' href="%s"' % __attr_href))
                __append(u'\n                                >')
                __default_549635688 = '__default'

                # <Value u'language.title()' (68:48)> -> __cache_549634960
                __token = 3798
                __cache_549634960 = _lookup_attr(getitem('language'), 'title')()

                # <Identity expression=<Value u'language.title()' (68:48)> value=<_ast.Str object at 0x0000000020C2C400> at 20c2c550> -> __condition
                __expression = __cache_549634960
                __value = '__default'
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_549634960
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append(u'</a>')
                __append(u'\n                            ')
                __append(u'</li>')
                ____index_549635296 -= 1
                if (____index_549635296 > 0):
                    __append('\n                            ')
            if (__backup_language_548685472 is __marker):
                del econtext['language']
            else:
                econtext['language'] = __backup_language_548685472
            __append(u'\n                        ')
            __append(u'</ul>')
            __append(u'\n                    ')
            __append(u'</div>')
            __append(u'\n                    ')

            # <Value u'searchbar' (73:60)> -> __condition
            __token = 4005
            __condition = getitem('searchbar')
            if __condition:

                # <Static value=<_ast.Dict object at 0x0000000020C2CBA8> name=None at 20c2cb70> -> __attrs_549637984
                __attrs_549637984 = _static_549637032

                # <div ... (73:20)
                # --------------------------------------------------------
                __append(u'<div')
                __append(u' class="navbar-form"')
                __append(u'>')
                __append(u'\n                        ')
                __backup_macroname_555359240 = get('macroname', __marker)

                # <Static value=<_ast.Str object at 0x0000000020C2C278> name=None at 20c2c898> -> __value
                __value = _static_549634680
                econtext['macroname'] = __value

                # <Value u'load: searchbar.html' (74:47)> -> __macro
                __token = 4064
                __macro = u' searchbar.html'
                __macro = __loader(__macro)
                __token = 4064
                __m = __macro.include
                __m(__stream, econtext.copy(), rcontext, __i18n_domain)
                econtext.update(rcontext)
                if (__backup_macroname_555359240 is __marker):
                    del econtext['macroname']
                else:
                    econtext['macroname'] = __backup_macroname_555359240
                __append(u'\n                    ')
                __append(u'</div>')
            __append(u'\n                    ')

            # <Value u'catbar' (77:78)> -> __condition
            __token = 4224
            __condition = getitem('catbar')
            if __condition:

                # <Static value=<_ast.Dict object at 0x0000000020C2C748> name=None at 20c2c7f0> -> __attrs_550879976
                __attrs_550879976 = _static_549635912

                # <ul ... (77:20)
                # --------------------------------------------------------
                __append(u'<ul')
                __append(u' class="nav navbar-nav navbar-category"')
                __append(u'>')
                __append(u'\n                        ')
                __backup_cat_548707856 = get('cat', __marker)

                # <Value u'categories' (78:44)> -> __iterator
                __token = 4277
                __iterator = getitem('categories')
                (__iterator, ____index_550881488, ) = getitem('repeat')(u'cat', __iterator)
                econtext['cat'] = None
                for __item in __iterator:
                    econtext['cat'] = __item

                    # <Static value=<_ast.Dict object at 0x0000000020D5C780> name=None at 20d5c710> -> __attrs_550880760
                    __attrs_550880760 = _static_550881152

                    # <li ... (78:24)
                    # --------------------------------------------------------
                    __append(u'<li')

                    # <Builtin id='False' ctx=<_ast.Load object at 0x000000001964B048> at 20acd898> -> __default_550880088
                    __default_550880088 = False

                    # <Substitution u"'active' if\n                            router.is_current('overview.category', {'cat_name': cat.name}) else ''" (78:78)> -> __attr_class
                    __token = 4311
                    __attr_class = ('active' if _lookup_attr(getitem('router'), 'is_current')('overview.category', {'cat_name': _lookup_attr(getitem('cat'), 'name'), }) else '')
                    __attr_class = __quote(__attr_class, '"', '&quot;', None, False)
                    if (__attr_class is not None):
                        __append((u' class="%s"' % __attr_class))
                    __append(u'>')
                    __append(u'\n                            ')

                    # <Static value=<_ast.Dict object at 0x0000000020D5C4E0> name=None at 20d5c080> -> __attrs_550882608
                    __attrs_550882608 = _static_550880480

                    # <a ... (80:28)
                    # --------------------------------------------------------
                    __append(u'<a')

                    # <Builtin id='False' ctx=<_ast.Load object at 0x000000001964B048> at 20acd898> -> __default_550879752
                    __default_550879752 = False

                    # <Substitution u"router.link_to('overview.category', {'cat_name': cat.name})" (81:57)> -> __attr_href
                    __token = 4512
                    __attr_href = _lookup_attr(getitem('router'), 'link_to')('overview.category', {'cat_name': _lookup_attr(getitem('cat'), 'name'), })
                    __attr_href = __quote(__attr_href, '"', '&quot;', None, False)
                    if (__attr_href is not None):
                        __append((u' href="%s"' % __attr_href))

                    # <Builtin id='False' ctx=<_ast.Load object at 0x000000001964B048> at 20acd898> -> __default_550882776
                    __default_550882776 = False

                    # <Substitution u'cat.name' (81:123)> -> __attr_class
                    __token = 4578
                    __attr_class = _lookup_attr(getitem('cat'), 'name')
                    __attr_class = __quote(__attr_class, '"', '&quot;', None, False)
                    if (__attr_class is not None):
                        __append((u' class="%s"' % __attr_class))
                    __append(u'>')
                    __append(u'\n                                ')

                    # <Static value=<_ast.Dict object at 0x0000000020D5CC88> name=None at 20d5ccc0> -> __attrs_550880200
                    __attrs_550880200 = _static_550882440

                    # <div ... (82:32)
                    # --------------------------------------------------------
                    __append(u'<div')
                    __append(u' class="icon"')
                    __append(u'>')
                    __append(u'</div>')

                    # <Static value=<_ast.Dict object at 0x0000000019877B00> name=None at 19877c50> -> __attrs_551113504
                    __attrs_551113504 = _static_428309248

                    # <span ... (82:56)
                    # --------------------------------------------------------
                    __append(u'<span>')
                    __default_551113000 = '__default'

                    # <Value u'cat.title' (82:75)> -> __cache_551115688
                    __token = 4665
                    __cache_551115688 = _lookup_attr(getitem('cat'), 'title')

                    # <Identity expression=<Value u'cat.title' (82:75)> value=<_ast.Str object at 0x0000000020D95048> at 20d95080> -> __condition
                    __expression = __cache_551115688
                    __value = '__default'
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_551115688
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append(u'</span>')
                    __append(u'\n                           ')
                    __append(u'</a>')
                    __append(u'\n                        ')
                    __append(u'</li>')
                    ____index_550881488 -= 1
                    if (____index_550881488 > 0):
                        __append('\n                        ')
                if (__backup_cat_548707856 is __marker):
                    del econtext['cat']
                else:
                    econtext['cat'] = __backup_cat_548707856
                __append(u'\n                    ')
                __append(u'</ul>')
            __append(u'\n                ')
            __append(u'</div>')
            __append(u'\n            ')
            __append(u'</div>')
            __append(u'\n        ')
            __append(u'</nav>')
            __append(u'\n    ')
            __append(u'</div>')
            __append(u'\n    ')
            __token = 4852
            econtext['classes'] = ['main-container', ]
            __append(u'\n    ')
            __token = 4897
            if getitem('sidebar'):
                getitem('classes').append('has-sidebar')
            __append(u'\n    ')
            __token = 4955
            try:
                getitem('classes').append(getitem('page_name'))
            except:
                pass

            __append(u'\n    ')
            __token = 5031
            econtext['class_names'] = ' '.join(getitem('classes'))
            __append(u'\n    ')

            # <Static value=<_ast.Dict object at 0x0000000020D95240> name=None at 20d956a0> -> __attrs_551114792
            __attrs_551114792 = _static_551113280

            # <div ... (96:4)
            # --------------------------------------------------------
            __append(u'<div')

            # <Builtin id='False' ctx=<_ast.Load object at 0x000000001964B048> at 20acd898> -> __default_551115072
            __default_551115072 = False

            # <Substitution u'class_names' (96:31)> -> __attr_class
            __token = 5098
            __attr_class = getitem('class_names')
            __attr_class = __quote(__attr_class, '"', '&quot;', None, False)
            if (__attr_class is not None):
                __append((u' class="%s"' % __attr_class))
            __append(u'>')
            __append(u'\n        ')

            # <Value u'sidebar' (97:28)> -> __condition
            __token = 5140
            __condition = getitem('sidebar')
            if __condition:

                # <Static value=<_ast.Dict object at 0x0000000020D95A90> name=None at 20d95978> -> __attrs_551115800
                __attrs_551115800 = _static_551115408

                # <div ... (97:8)
                # --------------------------------------------------------
                __append(u'<div')
                __append(u' class="sidebar-container"')
                __append(u' data-spy="affix"')
                __append(u' data-offset-top="0"')
                __append(u' data-offset-bottom="50"')
                __append(u'>')
                __append(u'\n            ')
                if (__slot_sidebar is None):

                    # <Static value=<_ast.Dict object at 0x0000000019877B00> name=None at 19877c50> -> __attrs_548966584
                    __attrs_548966584 = _static_428309248

                    # <div ... (98:12)
                    # --------------------------------------------------------
                    __append(u'<div>')
                    __append(u'</div>')
                else:
                    __slot_sidebar(__stream, econtext.copy(), rcontext)
                __append(u'\n        ')
                __append(u'</div>')
            __append(u'\n        ')

            # <Value u'sidebar' (100:28)> -> __condition
            __token = 5332
            __condition = getitem('sidebar')
            if __condition:

                # <Static value=<_ast.Dict object at 0x0000000020B892B0> name=None at 20b89208> -> __attrs_548967424
                __attrs_548967424 = _static_548967088

                # <div ... (100:8)
                # --------------------------------------------------------
                __append(u'<div')
                __append(u' class="sidebar-expand-btn"')
                __append(u'>')
                __append(u'\n            ')

                # <Static value=<_ast.Dict object at 0x0000000020B89588> name=None at 20b897f0> -> __attrs_548968600
                __attrs_548968600 = _static_548967816

                # <span ... (101:12)
                # --------------------------------------------------------
                __append(u'<span')
                __append(u' class="glyphicon glyphicon-list"')
                __append(u'>')
                __append(u'</span>')
                __append(u'\n        ')
                __append(u'</div>')
            __append(u'\n        ')

            # <Static value=<_ast.Dict object at 0x0000000020B89A58> name=None at 20b895f8> -> __attrs_548969104
            __attrs_548969104 = _static_548969048

            # <div ... (103:8)
            # --------------------------------------------------------
            __append(u'<div')
            __append(u' class="content-container docapp-content container-fluid"')
            __append(u'>')
            __append(u'\n            ')

            # <Static value=<_ast.Dict object at 0x0000000020B89D30> name=None at 20b89cf8> -> __attrs_548970448
            __attrs_548970448 = _static_548969776

            # <div ... (104:12)
            # --------------------------------------------------------
            __append(u'<div')
            __append(u' class="row"')
            __append(u'>')
            __append(u'\n                ')

            # <Static value=<_ast.Dict object at 0x0000000020C340F0> name=None at 20c34048> -> __attrs_549667392
            __attrs_549667392 = _static_549667056

            # <div ... (105:16)
            # --------------------------------------------------------
            __append(u'<div')
            __append(u' class="col-xs-12"')
            __append(u'>')
            __append(u'\n                    ')
            if (__slot_content is None):

                # <Static value=<_ast.Dict object at 0x0000000019877B00> name=None at 19877c50> -> __attrs_549668064
                __attrs_549668064 = _static_428309248

                # <div ... (106:20)
                # --------------------------------------------------------
                __append(u'<div>')
                __append(u'</div>')
            else:
                __slot_content(__stream, econtext.copy(), rcontext)
            __append(u'\n                ')
            __append(u'</div>')
            __append(u'\n            ')
            __append(u'</div>')
            __append(u'\n            ')

            # <Static value=<_ast.Dict object at 0x0000000020C342B0> name=None at 20c345f8> -> __attrs_549668848
            __attrs_549668848 = _static_549667504

            # <div ... (109:12)
            # --------------------------------------------------------
            __append(u'<div')
            __append(u' class="footer"')
            __append(u' >')
            __append(u'\n                ')

            # <Static value=<_ast.Dict object at 0x0000000020C34860> name=None at 20c34828> -> __attrs_549670248
            __attrs_549670248 = _static_549668960

            # <span ... (110:16)
            # --------------------------------------------------------
            __append(u'<span')
            __append(u' class="copyright"')
            __append(u'>')

            # <Interpolation value=<Substitution u"&copy; ${year}\n                    ${lang._l('branding_company_name')}" (110:40)> braces_required=True translation=False at 20c34c50> -> __content_100582504
            __token = 5760
            __token = 5769
            __content_100582504 = getitem('year')
            __content_100582504 = __quote(__content_100582504, '\x00', '&#0;', None, False)
            __token = 5797
            __content_100582504_5795 = _lookup_attr(getitem('lang'), '_l')('branding_company_name')
            __content_100582504_5795 = __quote(__content_100582504_5795, '\x00', '&#0;', None, False)
            __content_100582504 = ('%s%s%s%s' % (u'&copy; ', (__content_100582504 if (__content_100582504 is not None) else ''), u'\n                    ', (__content_100582504_5795 if (__content_100582504_5795 is not None) else ''), ))
            if (__content_100582504 is None):
                pass
            else:
                if (__content_100582504 is False):
                    __content_100582504 = None
                else:
                    __tt = type(__content_100582504)
                    if ((__tt is int) or (__tt is float) or (__tt is long)):
                        __content_100582504 = unicode(__content_100582504)
                    else:
                        if (__tt is str):
                            __content_100582504 = decode(__content_100582504)
                        else:
                            if (__tt is not unicode):
                                try:
                                    __content_100582504 = __content_100582504.__html__
                                except get('AttributeError', AttributeError):
                                    __converted = convert(__content_100582504)
                                    __content_100582504 = (unicode(__content_100582504) if (__content_100582504 is __converted) else __converted)
                                else:
                                    __content_100582504 = __content_100582504()
            if (__content_100582504 is not None):
                __append(__content_100582504)
            __append(u'</span>')
            __append(u'\n            ')
            __append(u'</div>')
            __append(u'\n        ')
            __append(u'</div>')
            __append(u'\n    ')
            __append(u'</div>')
            __append(u'\n    ')

            # <Static value=<_ast.Dict object at 0x0000000019877B00> name=None at 19877c50> -> __attrs_549670584
            __attrs_549670584 = _static_428309248

            # <script ... (115:4)
            # --------------------------------------------------------
            __append(u'<script>')
            __append(u'\n        ')

            # <Value u'highlight' (116:34)> -> __condition
            __token = 5930
            __condition = getitem('highlight')
            if __condition:

                # <Interpolation value=<Substitution u'\n            var hlText = "${highlight}".replace(/[\\-\\[\\]\\/\\{\\}\\(\\)\\*\\+\\?\\\\\\^\\$\\|]/g, "");\n            if(hlText.length>1){\n                $(".docapp-content").highlight(hlText);\n            }\n        ' (116:45)> braces_required=True translation=False at 20c34be0> -> __content_100582504
                __token = 5954
                __token = 5970
                __content_100582504 = getitem('highlight')
                __content_100582504 = __quote(__content_100582504, '\x00', '&#0;', None, False)
                __content_100582504 = ('%s%s%s' % (u'\n            var hlText = "', (__content_100582504 if (__content_100582504 is not None) else ''), u'".replace(/[\\-\\[\\]\\/\\{\\}\\(\\)\\*\\+\\?\\\\\\^\\$\\|]/g, "");\n            if(hlText.length>1){\n                $(".docapp-content").highlight(hlText);\n            }\n        ', ))
                if (__content_100582504 is None):
                    pass
                else:
                    if (__content_100582504 is False):
                        __content_100582504 = None
                    else:
                        __tt = type(__content_100582504)
                        if ((__tt is int) or (__tt is float) or (__tt is long)):
                            __content_100582504 = unicode(__content_100582504)
                        else:
                            if (__tt is str):
                                __content_100582504 = decode(__content_100582504)
                            else:
                                if (__tt is not unicode):
                                    try:
                                        __content_100582504 = __content_100582504.__html__
                                    except get('AttributeError', AttributeError):
                                        __converted = convert(__content_100582504)
                                        __content_100582504 = (unicode(__content_100582504) if (__content_100582504 is __converted) else __converted)
                                    else:
                                        __content_100582504 = __content_100582504()
                if (__content_100582504 is not None):
                    __append(__content_100582504)

            # <Interpolation value=<Substitution u'\n\n        $(\'#search\').typeahead({\n            highlight: true,\n            minLength: 2\n        }, {\n            name: \'search-ac\',\n            limit: 8,\n            source: function (query, process, asyncProcess) {\n                $.ajax({\n                    type: \'json\',\n                    url:\n                            "${router.link_to(\'overview.search_ac\', None, False)}",\n                    data: { q: query },\n                    type: \'GET\',\n                    success: function(data) {\n                        return asyncProcess(data);\n                    }\n                });\n            }\n        });\n    ' (121:24)> braces_required=True translation=False at 20c34f60> -> __content_100582504
            __token = 6169
            __token = 6491
            __content_100582504 = _lookup_attr(getitem('router'), 'link_to')('overview.search_ac', None, False)
            __content_100582504 = __quote(__content_100582504, '\x00', '&#0;', None, False)
            __content_100582504 = ('%s%s%s' % (u'\n\n        $(\'#search\').typeahead({\n            highlight: true,\n            minLength: 2\n        }, {\n            name: \'search-ac\',\n            limit: 8,\n            source: function (query, process, asyncProcess) {\n                $.ajax({\n                    type: \'json\',\n                    url:\n                            "', (__content_100582504 if (__content_100582504 is not None) else ''), u'",\n                    data: { q: query },\n                    type: \'GET\',\n                    success: function(data) {\n                        return asyncProcess(data);\n                    }\n                });\n            }\n        });\n    ', ))
            if (__content_100582504 is None):
                pass
            else:
                if (__content_100582504 is False):
                    __content_100582504 = None
                else:
                    __tt = type(__content_100582504)
                    if ((__tt is int) or (__tt is float) or (__tt is long)):
                        __content_100582504 = unicode(__content_100582504)
                    else:
                        if (__tt is str):
                            __content_100582504 = decode(__content_100582504)
                        else:
                            if (__tt is not unicode):
                                try:
                                    __content_100582504 = __content_100582504.__html__
                                except get('AttributeError', AttributeError):
                                    __converted = convert(__content_100582504)
                                    __content_100582504 = (unicode(__content_100582504) if (__content_100582504 is __converted) else __converted)
                                else:
                                    __content_100582504 = __content_100582504()
            if (__content_100582504 is not None):
                __append(__content_100582504)
            __append(u'</script>')
            __append(u'\n    ')

            # <Static value=<_ast.Dict object at 0x0000000020CDE4A8> name=None at 20cde748> -> __attrs_550363320
            __attrs_550363320 = _static_550364328

            # <script ... (143:4)
            # --------------------------------------------------------
            __append(u'<script')
            __append(u' src="/static/jscript/doc/app.js"')
            __append(u'>')
            __append(u'</script>')
            __append(u'\n')
            __append(u'</body>')
            __append(u'\n')
            __append(u'</html>')
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }