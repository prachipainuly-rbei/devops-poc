# -*- coding: utf-8 -*-
__filename = u'c:\\cdb\\contact_elements_server_15.3.13\\cdb\\chrome\\documentation\\searchbar.html'
__tokens = {42: (u"${router.link_to('overview.search')}", 1, 42), 44: (u"router.link_to('overview.search')", 1, 44), 166: (u'${searchcat.name}', 2, 69), 168: (u'searchcat.name', 2, 71), 491: (u'${searchcat.title}', 7, 36), 493: (u'searchcat.title', 7, 38), 713: (u"${lang._l('doc_all_categories')}", 11, 61), 715: (u"lang._l('doc_all_categories')", 11, 63), 747: (u"${lang._l('doc_all_categories')}", 11, 95), 749: (u"lang._l('doc_all_categories')", 11, 97), 829: (u'categories', 12, 40), 883: (u'${cat.name}', 13, 41), 885: (u'cat.name', 13, 43), 911: (u'${cat.title}', 13, 69), 913: (u'cat.title', 13, 71), 966: (u'cat.title', 14, 41), 1105: (u'search_langs is not None', 18, 56), 1348: (u"${lang._l('doc_search_languages')}", 20, 43), 1350: (u"lang._l('doc_search_languages')", 20, 45), 1780: (u"'all' in search_langs", 27, 113), 1842: (u"${lang._l('doc_all_search_languages')}", 28, 36), 1844: (u"lang._l('doc_all_search_languages')", 28, 38), 2103: (u'languages', 33, 51), 2211: (u"'all' in search_langs", 35, 64), 2319: (u'${searchlang.iso}', 36, 84), 2321: (u'searchlang.iso', 36, 86), 2405: (u"searchlang.iso in search_langs or 'all' in search_langs", 37, 67), 2470: (u" 'all' in search_lang", 37, 132), 2533: (u'${searchlang.title(lang.iso)}', 38, 36), 2535: (u'searchlang.title(lang.iso)', 38, 38), 2817: (u"${lang._l('doc_search')}", 45, 32), 2819: (u"lang._l('doc_search')", 45, 34), 2850: (u'${query}', 45, 65), 2852: (u'query', 45, 67)}

from sys import exc_info as _exc_info
from chameleon.py26 import lookup_attr as _lookup_attr

_static_551115632 = {u'class': u'text', }
_static_428309248 = {}
_static_548326256 = {u'type': u'hidden', u'id': u'search-category', u'value': u'${searchcat.name}', u'name': u'category', }
_static_550366512 = {u'disabled': u"'all' in search_langs", u'checked': u"searchlang.iso in search_langs or 'all' in search_langs", u'type': u'checkbox', u'name': u'searchlang', u'value': u'${searchlang.iso}', }
_static_548745904 = {u'data-catname': u'all', u'data-cattitle': u"${lang._l('doc_all_categories')}", }
_static_548377992 = {u'class': u'input-group', }
_static_535399168 = {u'type': u'submit', u'class': u'btn btn-default', }
_static_548635536 = {u'class': u'text', }
_static_548636936 = {u'class': u'caret', }
_static_548378944 = {u'class': u'input-group-btn', }
_static_548196816 = {u'role': u'separator', u'class': u'divider', }
_static_548324632 = {u'action': u"${router.link_to('overview.search')}", u'id': u'searchform', u'class': u'search', u'method': u'get', }
_static_548637664 = {u'class': u'dropdown-menu', u'id': u'catDropdownMenu', }
_static_554428288 = {u'class': u'input-group-btn', }
_static_551114848 = {u'class': u'caret', }
_static_548379896 = {u'aria-expanded': u'false', u'class': u'btn btn-default dropdown-toggle', u'aria-haspopup': u'true', u'data-toggle': u'dropdown', u'type': u'button', u'id': u'catDropdown', }
_static_550365504 = {u'disabled': u"'all' in search_langs", }
_static_548704496 = {u'aria-expanded': u'false', u'class': u'btn btn-default dropdown-toggle', u'aria-haspopup': u'true', u'data-toggle': u'dropdown', u'type': u'button', u'id': u'searchlangDropdown', }
_static_548706344 = {u'class': u'input-group-btn', }
_static_535398552 = {u'class': u'glyphicon glyphicon-search', }
_static_429394856 = {u'checked': u"'all' in search_langs", u'type': u'checkbox', u'name': u'searchlang', u'value': u'all', }
_static_551115800 = {u'class': u'dropdown-menu', u'id': u'searchlangDropdownMenu', }
_static_548377208 = {u'class': u'form-group', }
_static_551115968 = {u'id': u'searchlangAll', }
_static_548684576 = {u'data-catname': u'${cat.name}', u'data-cattitle': u'${cat.title}', }
_static_554429128 = {u'name': u'q', u'type': u'text', u'value': u'${query}', u'id': u'search', u'placeholder': u"${lang._l('doc_search')}", u'class': u'form-control', }

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
            getitem = econtext.__getitem__
            get = econtext.get

            # <Static value=<_ast.Dict object at 0x0000000020AEC518> name=None at 20aec470> -> __attrs_548325976
            __attrs_548325976 = _static_548324632

            # <form ... (1:0)
            # --------------------------------------------------------
            __append(u'<form')
            __append(u' class="search"')
            __append(u' method="get"')

            # <Builtin id='False' ctx=<_ast.Load object at 0x000000001964B048> at 20b66e80> -> __default_548325472
            __default_548325472 = False

            # <Interpolation value=<Substitution u"${router.link_to('overview.search')}" (1:42)> braces_required=True translation=False at 20aec898> -> __attr_action
            __token = 42
            __token = 44
            __attr_action = _lookup_attr(getitem('router'), 'link_to')('overview.search')
            __attr_action = __quote(__attr_action, '"', '&quot;', None, False)
            __attr_action = __attr_action
            if (__attr_action is None):
                pass
            else:
                if (__attr_action is False):
                    __attr_action = None
                else:
                    __tt = type(__attr_action)
                    if ((__tt is int) or (__tt is float) or (__tt is long)):
                        __attr_action = unicode(__attr_action)
                    else:
                        if (__tt is str):
                            __attr_action = decode(__attr_action)
                        else:
                            if (__tt is not unicode):
                                try:
                                    __attr_action = __attr_action.__html__
                                except get('AttributeError', AttributeError):
                                    __converted = convert(__attr_action)
                                    __attr_action = (unicode(__attr_action) if (__attr_action is __converted) else __converted)
                                else:
                                    __attr_action = __attr_action()
            if (__attr_action is not None):
                __append((u' action="%s"' % __attr_action))
            __append(u' id="searchform"')
            __append(u'>')
            __append(u'\n    ')

            # <Static value=<_ast.Dict object at 0x0000000020AECB70> name=None at 20aecbe0> -> __attrs_548376928
            __attrs_548376928 = _static_548326256

            # <input ... (2:4)
            # --------------------------------------------------------
            __append(u'<input')
            __append(u' type="hidden"')
            __append(u' id="search-category"')
            __append(u' name="category"')

            # <Builtin id='False' ctx=<_ast.Load object at 0x000000001964B048> at 20b66e80> -> __default_548327320
            __default_548327320 = False

            # <Interpolation value=<Substitution u'${searchcat.name}' (2:69)> braces_required=True translation=False at 20aeceb8> -> __attr_value
            __token = 166
            __token = 168
            __attr_value = _lookup_attr(getitem('searchcat'), 'name')
            __attr_value = __quote(__attr_value, '"', '&quot;', None, False)
            __attr_value = __attr_value
            if (__attr_value is None):
                pass
            else:
                if (__attr_value is False):
                    __attr_value = None
                else:
                    __tt = type(__attr_value)
                    if ((__tt is int) or (__tt is float) or (__tt is long)):
                        __attr_value = unicode(__attr_value)
                    else:
                        if (__tt is str):
                            __attr_value = decode(__attr_value)
                        else:
                            if (__tt is not unicode):
                                try:
                                    __attr_value = __attr_value.__html__
                                except get('AttributeError', AttributeError):
                                    __converted = convert(__attr_value)
                                    __attr_value = (unicode(__attr_value) if (__attr_value is __converted) else __converted)
                                else:
                                    __attr_value = __attr_value()
            if (__attr_value is not None):
                __append((u' value="%s"' % __attr_value))
            __append(u' />')
            __append(u'\n    ')

            # <Static value=<_ast.Dict object at 0x0000000020AF9278> name=None at 20af9208> -> __attrs_548377712
            __attrs_548377712 = _static_548377208

            # <div ... (3:4)
            # --------------------------------------------------------
            __append(u'<div')
            __append(u' class="form-group"')
            __append(u'>')
            __append(u'\n        ')

            # <Static value=<_ast.Dict object at 0x0000000020AF9588> name=None at 20af95c0> -> __attrs_548378552
            __attrs_548378552 = _static_548377992

            # <div ... (4:8)
            # --------------------------------------------------------
            __append(u'<div')
            __append(u' class="input-group"')
            __append(u'>')
            __append(u'\n            ')

            # <Static value=<_ast.Dict object at 0x0000000020AF9940> name=None at 20af9908> -> __attrs_548379504
            __attrs_548379504 = _static_548378944

            # <div ... (5:12)
            # --------------------------------------------------------
            __append(u'<div')
            __append(u' class="input-group-btn"')
            __append(u'>')
            __append(u'\n                ')

            # <Static value=<_ast.Dict object at 0x0000000020AF9CF8> name=None at 20af9cc0> -> __attrs_548635592
            __attrs_548635592 = _static_548379896

            # <button ... (6:16)
            # --------------------------------------------------------
            __append(u'<button')
            __append(u' id="catDropdown"')
            __append(u' type="button"')
            __append(u' class="btn btn-default dropdown-toggle"')
            __append(u' data-toggle="dropdown"')
            __append(u' aria-haspopup="true"')
            __append(u' aria-expanded="false"')
            __append(u'>')
            __append(u'\n                 ')

            # <Static value=<_ast.Dict object at 0x0000000020B38390> name=None at 20b38588> -> __attrs_548636376
            __attrs_548636376 = _static_548635536

            # <span ... (7:17)
            # --------------------------------------------------------
            __append(u'<span')
            __append(u' class="text"')
            __append(u'>')

            # <Interpolation value=<Substitution u'${searchcat.title}' (7:36)> braces_required=True translation=False at 20b38828> -> __content_100582504
            __token = 491
            __token = 493
            __content_100582504 = _lookup_attr(getitem('searchcat'), 'title')
            __content_100582504 = __quote(__content_100582504, '\x00', '&#0;', None, False)
            __content_100582504 = __content_100582504
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
            __append(u'\n                 ')

            # <Static value=<_ast.Dict object at 0x0000000020B38908> name=None at 20b388d0> -> __attrs_548637328
            __attrs_548637328 = _static_548636936

            # <span ... (8:17)
            # --------------------------------------------------------
            __append(u'<span')
            __append(u' class="caret"')
            __append(u'>')
            __append(u'</span>')
            __append(u'\n                ')
            __append(u'</button>')
            __append(u'\n                ')

            # <Static value=<_ast.Dict object at 0x0000000020B38BE0> name=None at 20b38400> -> __attrs_548638224
            __attrs_548638224 = _static_548637664

            # <ul ... (10:16)
            # --------------------------------------------------------
            __append(u'<ul')
            __append(u' class="dropdown-menu"')
            __append(u' id="catDropdownMenu"')
            __append(u'>')
            __append(u'\n                    ')

            # <Static value=<_ast.Dict object at 0x0000000019877B00> name=None at 19877c50> -> __attrs_548745736
            __attrs_548745736 = _static_428309248

            # <li ... (11:20)
            # --------------------------------------------------------
            __append(u'<li>')

            # <Static value=<_ast.Dict object at 0x0000000020B532B0> name=None at 20b534a8> -> __attrs_548686256
            __attrs_548686256 = _static_548745904

            # <a ... (11:24)
            # --------------------------------------------------------
            __append(u'<a')
            __append(u' data-catname="all"')

            # <Builtin id='False' ctx=<_ast.Load object at 0x000000001964B048> at 20b66e80> -> __default_548684072
            __default_548684072 = False

            # <Interpolation value=<Substitution u"${lang._l('doc_all_categories')}" (11:61)> braces_required=True translation=False at 20b53438> -> __attr_data_cattitle
            __token = 713
            __token = 715
            __attr_data_cattitle = _lookup_attr(getitem('lang'), '_l')('doc_all_categories')
            __attr_data_cattitle = __quote(__attr_data_cattitle, '"', '&quot;', None, False)
            __attr_data_cattitle = __attr_data_cattitle
            if (__attr_data_cattitle is None):
                pass
            else:
                if (__attr_data_cattitle is False):
                    __attr_data_cattitle = None
                else:
                    __tt = type(__attr_data_cattitle)
                    if ((__tt is int) or (__tt is float) or (__tt is long)):
                        __attr_data_cattitle = unicode(__attr_data_cattitle)
                    else:
                        if (__tt is str):
                            __attr_data_cattitle = decode(__attr_data_cattitle)
                        else:
                            if (__tt is not unicode):
                                try:
                                    __attr_data_cattitle = __attr_data_cattitle.__html__
                                except get('AttributeError', AttributeError):
                                    __converted = convert(__attr_data_cattitle)
                                    __attr_data_cattitle = (unicode(__attr_data_cattitle) if (__attr_data_cattitle is __converted) else __converted)
                                else:
                                    __attr_data_cattitle = __attr_data_cattitle()
            if (__attr_data_cattitle is not None):
                __append((u' data-cattitle="%s"' % __attr_data_cattitle))
            __append(u'>')

            # <Interpolation value=<Substitution u"${lang._l('doc_all_categories')}" (11:95)> braces_required=True translation=False at 20b44518> -> __content_100582504
            __token = 747
            __token = 749
            __content_100582504 = _lookup_attr(getitem('lang'), '_l')('doc_all_categories')
            __content_100582504 = __quote(__content_100582504, '\x00', '&#0;', None, False)
            __content_100582504 = __content_100582504
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
            __append(u'</a>')
            __append(u'</li>')
            __append(u'\n                    ')
            __backup_cat_548378720 = get('cat', __marker)

            # <Value u'categories' (12:40)> -> __iterator
            __token = 829
            __iterator = getitem('categories')
            (__iterator, ____index_548686144, ) = getitem('repeat')(u'cat', __iterator)
            econtext['cat'] = None
            for __item in __iterator:
                econtext['cat'] = __item

                # <Static value=<_ast.Dict object at 0x0000000019877B00> name=None at 19877c50> -> __attrs_548684968
                __attrs_548684968 = _static_428309248

                # <li ... (12:20)
                # --------------------------------------------------------
                __append(u'<li>')
                __append(u'\n                        ')

                # <Static value=<_ast.Dict object at 0x0000000020B44320> name=None at 20b44470> -> __attrs_548705672
                __attrs_548705672 = _static_548684576

                # <a ... (13:24)
                # --------------------------------------------------------
                __append(u'<a')

                # <Builtin id='False' ctx=<_ast.Load object at 0x000000001964B048> at 20b66e80> -> __default_548686872
                __default_548686872 = False

                # <Interpolation value=<Substitution u'${cat.name}' (13:41)> braces_required=True translation=False at 20b44f98> -> __attr_data_catname
                __token = 883
                __token = 885
                __attr_data_catname = _lookup_attr(getitem('cat'), 'name')
                __attr_data_catname = __quote(__attr_data_catname, '"', '&quot;', None, False)
                __attr_data_catname = __attr_data_catname
                if (__attr_data_catname is None):
                    pass
                else:
                    if (__attr_data_catname is False):
                        __attr_data_catname = None
                    else:
                        __tt = type(__attr_data_catname)
                        if ((__tt is int) or (__tt is float) or (__tt is long)):
                            __attr_data_catname = unicode(__attr_data_catname)
                        else:
                            if (__tt is str):
                                __attr_data_catname = decode(__attr_data_catname)
                            else:
                                if (__tt is not unicode):
                                    try:
                                        __attr_data_catname = __attr_data_catname.__html__
                                    except get('AttributeError', AttributeError):
                                        __converted = convert(__attr_data_catname)
                                        __attr_data_catname = (unicode(__attr_data_catname) if (__attr_data_catname is __converted) else __converted)
                                    else:
                                        __attr_data_catname = __attr_data_catname()
                if (__attr_data_catname is not None):
                    __append((u' data-catname="%s"' % __attr_data_catname))

                # <Builtin id='False' ctx=<_ast.Load object at 0x000000001964B048> at 20b66e80> -> __default_548687264
                __default_548687264 = False

                # <Interpolation value=<Substitution u'${cat.title}' (13:69)> braces_required=True translation=False at 20b44d30> -> __attr_data_cattitle
                __token = 911
                __token = 913
                __attr_data_cattitle = _lookup_attr(getitem('cat'), 'title')
                __attr_data_cattitle = __quote(__attr_data_cattitle, '"', '&quot;', None, False)
                __attr_data_cattitle = __attr_data_cattitle
                if (__attr_data_cattitle is None):
                    pass
                else:
                    if (__attr_data_cattitle is False):
                        __attr_data_cattitle = None
                    else:
                        __tt = type(__attr_data_cattitle)
                        if ((__tt is int) or (__tt is float) or (__tt is long)):
                            __attr_data_cattitle = unicode(__attr_data_cattitle)
                        else:
                            if (__tt is str):
                                __attr_data_cattitle = decode(__attr_data_cattitle)
                            else:
                                if (__tt is not unicode):
                                    try:
                                        __attr_data_cattitle = __attr_data_cattitle.__html__
                                    except get('AttributeError', AttributeError):
                                        __converted = convert(__attr_data_cattitle)
                                        __attr_data_cattitle = (unicode(__attr_data_cattitle) if (__attr_data_cattitle is __converted) else __converted)
                                    else:
                                        __attr_data_cattitle = __attr_data_cattitle()
                if (__attr_data_cattitle is not None):
                    __append((u' data-cattitle="%s"' % __attr_data_cattitle))
                __append(u'>')
                __default_548684464 = '__default'

                # <Value u'cat.title' (14:41)> -> __cache_548686200
                __token = 966
                __cache_548686200 = _lookup_attr(getitem('cat'), 'title')

                # <Identity expression=<Value u'cat.title' (14:41)> value=<_ast.Str object at 0x0000000020B44710> at 20b440f0> -> __condition
                __expression = __cache_548686200
                __value = '__default'
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_548686200
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append(u'</a>')
                __append(u'\n                    ')
                __append(u'</li>')
                ____index_548686144 -= 1
                if (____index_548686144 > 0):
                    __append('\n                    ')
            if (__backup_cat_548378720 is __marker):
                del econtext['cat']
            else:
                econtext['cat'] = __backup_cat_548378720
            __append(u'\n                ')
            __append(u'</ul>')
            __append(u'\n            ')
            __append(u'</div>')
            __append(u'\n            ')

            # <Value u'search_langs is not None' (18:56)> -> __condition
            __token = 1105
            __condition = (getitem('search_langs') is not None)
            if __condition:

                # <Static value=<_ast.Dict object at 0x0000000020B49828> name=None at 20b49e80> -> __attrs_548705112
                __attrs_548705112 = _static_548706344

                # <div ... (18:12)
                # --------------------------------------------------------
                __append(u'<div')
                __append(u' class="input-group-btn"')
                __append(u'>')
                __append(u'\n                    ')

                # <Static value=<_ast.Dict object at 0x0000000020B490F0> name=None at 20b49dd8> -> __attrs_551113336
                __attrs_551113336 = _static_548704496

                # <button ... (19:20)
                # --------------------------------------------------------
                __append(u'<button')
                __append(u' id="searchlangDropdown"')
                __append(u' type="button"')
                __append(u' class="btn btn-default dropdown-toggle"')
                __append(u' data-toggle="dropdown"')
                __append(u' aria-haspopup="true"')
                __append(u' aria-expanded="false"')
                __append(u'>')
                __append(u'\n                        ')

                # <Static value=<_ast.Dict object at 0x0000000020D95B70> name=None at 20d951d0> -> __attrs_551113784
                __attrs_551113784 = _static_551115632

                # <span ... (20:24)
                # --------------------------------------------------------
                __append(u'<span')
                __append(u' class="text"')
                __append(u'>')

                # <Interpolation value=<Substitution u"${lang._l('doc_search_languages')}" (20:43)> braces_required=True translation=False at 20d95828> -> __content_100582504
                __token = 1348
                __token = 1350
                __content_100582504 = _lookup_attr(getitem('lang'), '_l')('doc_search_languages')
                __content_100582504 = __quote(__content_100582504, '\x00', '&#0;', None, False)
                __content_100582504 = __content_100582504
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
                __append(u'\n                        ')

                # <Static value=<_ast.Dict object at 0x0000000020D95860> name=None at 20d95748> -> __attrs_551114120
                __attrs_551114120 = _static_551114848

                # <span ... (21:24)
                # --------------------------------------------------------
                __append(u'<span')
                __append(u' class="caret"')
                __append(u'>')
                __append(u'</span>')
                __append(u'\n                    ')
                __append(u'</button>')
                __append(u'\n                    ')

                # <Static value=<_ast.Dict object at 0x0000000020D95C18> name=None at 20d959b0> -> __attrs_551116528
                __attrs_551116528 = _static_551115800

                # <ul ... (23:20)
                # --------------------------------------------------------
                __append(u'<ul')
                __append(u' class="dropdown-menu"')
                __append(u' id="searchlangDropdownMenu"')
                __append(u'>')
                __append(u'\n                        ')

                # <Static value=<_ast.Dict object at 0x0000000020D95CC0> name=None at 20d95e48> -> __attrs_429392728
                __attrs_429392728 = _static_551115968

                # <li ... (24:24)
                # --------------------------------------------------------
                __append(u'<li')
                __append(u' id="searchlangAll"')
                __append(u'>')
                __append(u'\n                            ')

                # <Static value=<_ast.Dict object at 0x0000000019877B00> name=None at 19877c50> -> __attrs_429394464
                __attrs_429394464 = _static_428309248

                # <a ... (25:28)
                # --------------------------------------------------------
                __append(u'<a>')
                __append(u'\n                                ')

                # <Static value=<_ast.Dict object at 0x0000000019877B00> name=None at 19877c50> -> __attrs_429395696
                __attrs_429395696 = _static_428309248

                # <label ... (26:32)
                # --------------------------------------------------------
                __append(u'<label>')
                __append(u'\n                                    ')

                # <Static value=<_ast.Dict object at 0x0000000019980BA8> name=None at 19980d68> -> __attrs_548200288
                __attrs_548200288 = _static_429394856

                # <input ... (27:36)
                # --------------------------------------------------------
                __append(u'<input')
                __append(u' type="checkbox"')
                __append(u' name="searchlang"')
                __append(u' value="all"')

                # <Builtin id='False' ctx=<_ast.Load object at 0x000000001964B048> at 20b66e80> -> __default_548199952
                __default_548199952 = False

                # <Substitution u"'all' in search_langs" (27:113)> -> __attr_checked
                __token = 1780
                __attr_checked = ('all' in getitem('search_langs'))
                __attr_checked = __quote(__attr_checked, '"', '&quot;', None, False)
                if (__attr_checked is not None):
                    __append((u' checked="%s"' % __attr_checked))
                __append(u' />')

                # <Interpolation value=<Substitution u"\n                                    ${lang._l('doc_all_search_languages')}\n                                " (27:138)> braces_required=True translation=False at 20acdeb8> -> __content_100582504
                __token = 1842
                __token = 1844
                __content_100582504 = _lookup_attr(getitem('lang'), '_l')('doc_all_search_languages')
                __content_100582504 = __quote(__content_100582504, '\x00', '&#0;', None, False)
                __content_100582504 = ('%s%s%s' % (u'\n                                    ', (__content_100582504 if (__content_100582504 is not None) else ''), u'\n                                ', ))
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
                __append(u'</label>')
                __append(u'\n                            ')
                __append(u'</a>')
                __append(u'\n                        ')
                __append(u'</li>')
                __append(u'\n                        ')

                # <Static value=<_ast.Dict object at 0x0000000020ACD1D0> name=None at 20acd400> -> __attrs_550364328
                __attrs_550364328 = _static_548196816

                # <li ... (32:24)
                # --------------------------------------------------------
                __append(u'<li')
                __append(u' role="separator"')
                __append(u' class="divider"')
                __append(u'>')
                __append(u'</li>')
                __append(u'\n                        ')
                __backup_searchlang_548379784 = get('searchlang', __marker)

                # <Value u'languages' (33:51)> -> __iterator
                __token = 2103
                __iterator = getitem('languages')
                (__iterator, ____index_550363880, ) = getitem('repeat')(u'searchlang', __iterator)
                econtext['searchlang'] = None
                for __item in __iterator:
                    econtext['searchlang'] = __item

                    # <Static value=<_ast.Dict object at 0x0000000019877B00> name=None at 19877c50> -> __attrs_550365224
                    __attrs_550365224 = _static_428309248

                    # <li ... (33:24)
                    # --------------------------------------------------------
                    __append(u'<li>')
                    __append(u'\n                            ')

                    # <Static value=<_ast.Dict object at 0x0000000019877B00> name=None at 19877c50> -> __attrs_550364272
                    __attrs_550364272 = _static_428309248

                    # <a ... (34:28)
                    # --------------------------------------------------------
                    __append(u'<a>')
                    __append(u'\n                                ')

                    # <Static value=<_ast.Dict object at 0x0000000020CDE940> name=None at 20cde8d0> -> __attrs_550366232
                    __attrs_550366232 = _static_550365504

                    # <label ... (35:32)
                    # --------------------------------------------------------
                    __append(u'<label')

                    # <Builtin id='False' ctx=<_ast.Load object at 0x000000001964B048> at 20b66e80> -> __default_550366288
                    __default_550366288 = False

                    # <Substitution u"'all' in search_langs" (35:64)> -> __attr_disabled
                    __token = 2211
                    __attr_disabled = ('all' in getitem('search_langs'))
                    __attr_disabled = __quote(__attr_disabled, '"', '&quot;', None, False)
                    if (__attr_disabled is not None):
                        __append((u' disabled="%s"' % __attr_disabled))
                    __append(u'>')
                    __append(u'\n                                    ')

                    # <Static value=<_ast.Dict object at 0x0000000020CDED30> name=None at 20cdea58> -> __attrs_554429744
                    __attrs_554429744 = _static_550366512

                    # <input ... (36:36)
                    # --------------------------------------------------------
                    __append(u'<input')
                    __append(u' type="checkbox"')
                    __append(u' name="searchlang"')

                    # <Builtin id='False' ctx=<_ast.Load object at 0x000000001964B048> at 20b66e80> -> __default_550365448
                    __default_550365448 = False

                    # <Interpolation value=<Substitution u'${searchlang.iso}' (36:84)> braces_required=True translation=False at 20cde390> -> __attr_value
                    __token = 2319
                    __token = 2321
                    __attr_value = _lookup_attr(getitem('searchlang'), 'iso')
                    __attr_value = __quote(__attr_value, '"', '&quot;', None, False)
                    __attr_value = __attr_value
                    if (__attr_value is None):
                        pass
                    else:
                        if (__attr_value is False):
                            __attr_value = None
                        else:
                            __tt = type(__attr_value)
                            if ((__tt is int) or (__tt is float) or (__tt is long)):
                                __attr_value = unicode(__attr_value)
                            else:
                                if (__tt is str):
                                    __attr_value = decode(__attr_value)
                                else:
                                    if (__tt is not unicode):
                                        try:
                                            __attr_value = __attr_value.__html__
                                        except get('AttributeError', AttributeError):
                                            __converted = convert(__attr_value)
                                            __attr_value = (unicode(__attr_value) if (__attr_value is __converted) else __converted)
                                        else:
                                            __attr_value = __attr_value()
                    if (__attr_value is not None):
                        __append((u' value="%s"' % __attr_value))

                    # <Builtin id='False' ctx=<_ast.Load object at 0x000000001964B048> at 20b66e80> -> __default_550364496
                    __default_550364496 = False

                    # <Substitution u"searchlang.iso in search_langs or 'all' in search_langs" (37:67)> -> __attr_checked
                    __token = 2405
                    __attr_checked = ((_lookup_attr(getitem('searchlang'), 'iso') in getitem('search_langs')) or ('all' in getitem('search_langs')))
                    __attr_checked = __quote(__attr_checked, '"', '&quot;', None, False)
                    if (__attr_checked is not None):
                        __append((u' checked="%s"' % __attr_checked))

                    # <Builtin id='False' ctx=<_ast.Load object at 0x000000001964B048> at 20b66e80> -> __default_554430416
                    __default_554430416 = False

                    # <Substitution u"'all' in search_langs" (37:132)> -> __attr_disabled
                    __token = 2470
                    __attr_disabled = ('all' in getitem('search_langs'))
                    __attr_disabled = __quote(__attr_disabled, '"', '&quot;', None, False)
                    if (__attr_disabled is not None):
                        __append((u' disabled="%s"' % __attr_disabled))
                    __append(u' />')

                    # <Interpolation value=<Substitution u'\n                                    ${searchlang.title(lang.iso)}\n                                ' (37:158)> braces_required=True translation=False at 210bed68> -> __content_100582504
                    __token = 2533
                    __token = 2535
                    __content_100582504 = _lookup_attr(getitem('searchlang'), 'title')(_lookup_attr(getitem('lang'), 'iso'))
                    __content_100582504 = __quote(__content_100582504, '\x00', '&#0;', None, False)
                    __content_100582504 = ('%s%s%s' % (u'\n                                    ', (__content_100582504 if (__content_100582504 is not None) else ''), u'\n                                ', ))
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
                    __append(u'</label>')
                    __append(u'\n                            ')
                    __append(u'</a>')
                    __append(u'\n                        ')
                    __append(u'</li>')
                    ____index_550363880 -= 1
                    if (____index_550363880 > 0):
                        __append('\n                        ')
                if (__backup_searchlang_548379784 is __marker):
                    del econtext['searchlang']
                else:
                    econtext['searchlang'] = __backup_searchlang_548379784
                __append(u'\n                    ')
                __append(u'</ul>')
                __append(u'\n            ')
                __append(u'</div>')
            __append(u'\n            ')

            # <Static value=<_ast.Dict object at 0x00000000210BEAC8> name=None at 210beb70> -> __attrs_554427728
            __attrs_554427728 = _static_554429128

            # <input ... (44:12)
            # --------------------------------------------------------
            __append(u'<input')
            __append(u' id="search"')
            __append(u' name="q"')
            __append(u' type="text"')
            __append(u' class="form-control"')

            # <Builtin id='False' ctx=<_ast.Load object at 0x000000001964B048> at 20b66e80> -> __default_554428456
            __default_554428456 = False

            # <Interpolation value=<Substitution u"${lang._l('doc_search')}" (45:32)> braces_required=True translation=False at 210be7f0> -> __attr_placeholder
            __token = 2817
            __token = 2819
            __attr_placeholder = _lookup_attr(getitem('lang'), '_l')('doc_search')
            __attr_placeholder = __quote(__attr_placeholder, '"', '&quot;', None, False)
            __attr_placeholder = __attr_placeholder
            if (__attr_placeholder is None):
                pass
            else:
                if (__attr_placeholder is False):
                    __attr_placeholder = None
                else:
                    __tt = type(__attr_placeholder)
                    if ((__tt is int) or (__tt is float) or (__tt is long)):
                        __attr_placeholder = unicode(__attr_placeholder)
                    else:
                        if (__tt is str):
                            __attr_placeholder = decode(__attr_placeholder)
                        else:
                            if (__tt is not unicode):
                                try:
                                    __attr_placeholder = __attr_placeholder.__html__
                                except get('AttributeError', AttributeError):
                                    __converted = convert(__attr_placeholder)
                                    __attr_placeholder = (unicode(__attr_placeholder) if (__attr_placeholder is __converted) else __converted)
                                else:
                                    __attr_placeholder = __attr_placeholder()
            if (__attr_placeholder is not None):
                __append((u'\n                   placeholder="%s"' % __attr_placeholder))

            # <Builtin id='False' ctx=<_ast.Load object at 0x000000001964B048> at 20b66e80> -> __default_554428736
            __default_554428736 = False

            # <Interpolation value=<Substitution u'${query}' (45:65)> braces_required=True translation=False at 210be908> -> __attr_value
            __token = 2850
            __token = 2852
            __attr_value = getitem('query')
            __attr_value = __quote(__attr_value, '"', '&quot;', None, False)
            __attr_value = __attr_value
            if (__attr_value is None):
                pass
            else:
                if (__attr_value is False):
                    __attr_value = None
                else:
                    __tt = type(__attr_value)
                    if ((__tt is int) or (__tt is float) or (__tt is long)):
                        __attr_value = unicode(__attr_value)
                    else:
                        if (__tt is str):
                            __attr_value = decode(__attr_value)
                        else:
                            if (__tt is not unicode):
                                try:
                                    __attr_value = __attr_value.__html__
                                except get('AttributeError', AttributeError):
                                    __converted = convert(__attr_value)
                                    __attr_value = (unicode(__attr_value) if (__attr_value is __converted) else __converted)
                                else:
                                    __attr_value = __attr_value()
            if (__attr_value is not None):
                __append((u' value="%s"' % __attr_value))
            __append(u'>')
            __append(u'\n            ')

            # <Static value=<_ast.Dict object at 0x00000000210BE780> name=None at 210be7b8> -> __attrs_554429184
            __attrs_554429184 = _static_554428288

            # <div ... (46:12)
            # --------------------------------------------------------
            __append(u'<div')
            __append(u' class="input-group-btn"')
            __append(u'>')
            __append(u'\n                ')

            # <Static value=<_ast.Dict object at 0x000000001FE98B00> name=None at 210bee48> -> __attrs_535397936
            __attrs_535397936 = _static_535399168

            # <button ... (47:16)
            # --------------------------------------------------------
            __append(u'<button')
            __append(u' class="btn btn-default"')
            __append(u' type="submit"')
            __append(u'>')
            __append(u'\n                    ')

            # <Static value=<_ast.Dict object at 0x000000001FE98898> name=None at 1fe987b8> -> __attrs_535398776
            __attrs_535398776 = _static_535398552

            # <span ... (48:20)
            # --------------------------------------------------------
            __append(u'<span')
            __append(u' class="glyphicon glyphicon-search"')
            __append(u'>')
            __append(u'</span>')
            __append(u'\n                ')
            __append(u'</button>')
            __append(u'\n            ')
            __append(u'</div>')
            __append(u'\n        ')
            __append(u'</div>')
            __append(u'\n    ')
            __append(u'</div>')
            __append(u'\n')
            __append(u'</form>')
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }