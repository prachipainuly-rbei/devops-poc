# -*- coding: utf-8 -*-
__filename = 'c:\\cdb\\contact_elements_server_15.3.13\\cdb\\chrome\\documentation\\category.html'
__tokens = {103: (u'category.title', 3, 25), 191: (u'category.books', 5, 34), 255: (u'item.name', 6, 35), 529: (u"router.link_to('overview.category.book',\n                        {'book_name': item.name, 'lang_iso': item.lang_iso})", 12, 24), 673: (u'${item.title}', 14, 24), 675: (u'item.title', 14, 26), 732: (u'not item.lang_iso == lang.iso', 15, 45), 863: (u"${lang._l('doc_book_different_language')}", 17, 35), 865: (u"lang._l('doc_book_different_language')", 17, 37), 935: (u'${item.lang_iso}', 18, 28), 937: (u'item.lang_iso', 18, 30), 1390: (u'item.teaser', 28, 61), 1577: (u'not category.books', 34, 32), 1614: (u"${lang._l('doc_category_is_empty')}", 35, 16), 1616: (u"lang._l('doc_category_is_empty')", 35, 18), 22: (u'load: layout.html', 1, 22), 22: (u'load: layout.html', 1, 22)}

from sys import exc_info as _exc_info
from chameleon.py26 import lookup_attr as _lookup_attr
from collections import deque as _deque

_static_548379280 = {u'class': u'teaser-text', }
_static_548638336 = u'load: layout.html'
_static_550365504 = {u'class': u'icon', }
_static_550366456 = {u'href': u"router.link_to('overview.category.book',\n                        {'book_name': item.name, 'lang_iso': item.lang_iso})", u'class': u'title', }
_static_428309248 = {}
_static_429393960 = {u'class': u'book-list', }
_static_548707464 = {u'class': u'teaser-block', }
_static_548377936 = {u'class': u'teaser-row', }
_static_548376648 = {u'class': u'teaser', }
_static_550365112 = {u'class': u'label label-primary cs-label', u'title': u"${lang._l('doc_book_different_language')}", }
_static_548707800 = {u'class': u'teaser-line', }
_static_548200232 = {u'class': u'book', u'id': u'item.name', }
_static_550366400 = {u'class': u'glyphicon glyphicon-book', }
_static_548376928 = {u'class': u'teaser-block', }
_static_548198776 = {u'class': u'title-line', }

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
            __backup_macroname_446448136 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x0000000020B38E80> name=None at 20b38b38> -> __value
            __value = _static_548638336
            econtext['macroname'] = __value

            def __fill_content(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getitem = econtext.__getitem__
                get = econtext.get

                # <Static value=<_ast.Dict object at 0x0000000019877B00> name=None at 19877c50> -> __attrs_548638616
                __attrs_548638616 = _static_428309248

                # <div ... (2:4)
                # --------------------------------------------------------
                __append(u'<div>')
                __append(u'\n        ')

                # <Static value=<_ast.Dict object at 0x0000000019877B00> name=None at 19877c50> -> __attrs_429393512
                __attrs_429393512 = _static_428309248

                # <h1 ... (3:8)
                # --------------------------------------------------------
                __append(u'<h1>')
                __default_429395696 = '__default'

                # <Value u'category.title' (3:25)> -> __cache_429392168
                __token = 103
                __cache_429392168 = _lookup_attr(getitem('category'), 'title')

                # <Identity expression=<Value u'category.title' (3:25)> value=<_ast.Str object at 0x0000000019980198> at 199806a0> -> __condition
                __expression = __cache_429392168
                __value = '__default'
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_429392168
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append(u'</h1>')
                __append(u'\n        ')

                # <Static value=<_ast.Dict object at 0x0000000019980828> name=None at 199805c0> -> __attrs_548196816
                __attrs_548196816 = _static_429393960

                # <div ... (4:8)
                # --------------------------------------------------------
                __append(u'<div')
                __append(u' class="book-list"')
                __append(u'>')
                __append(u'\n            ')
                __backup_item_548636264 = get('item', __marker)

                # <Value u'category.books' (5:34)> -> __iterator
                __token = 191
                __iterator = _lookup_attr(getitem('category'), 'books')
                (__iterator, ____index_548199952, ) = getitem('repeat')(u'item', __iterator)
                econtext['item'] = None
                for __item in __iterator:
                    econtext['item'] = __item

                    # <Static value=<_ast.Dict object at 0x0000000020ACDF28> name=None at 20acdf60> -> __attrs_548199616
                    __attrs_548199616 = _static_548200232

                    # <div ... (5:12)
                    # --------------------------------------------------------
                    __append(u'<div')
                    __append(u' class="book"')

                    # <Builtin id='False' ctx=<_ast.Load object at 0x000000001964B048> at 20b384a8> -> __default_548200176
                    __default_548200176 = False

                    # <Substitution u'item.name' (6:35)> -> __attr_id
                    __token = 255
                    __attr_id = _lookup_attr(getitem('item'), 'name')
                    __attr_id = __quote(__attr_id, '"', '&quot;', None, False)
                    if (__attr_id is not None):
                        __append((u' id="%s"' % __attr_id))
                    __append(u'>')
                    __append(u'\n                ')

                    # <Static value=<_ast.Dict object at 0x0000000020ACD978> name=None at 20acdfd0> -> __attrs_550364160
                    __attrs_550364160 = _static_548198776

                    # <div ... (7:16)
                    # --------------------------------------------------------
                    __append(u'<div')
                    __append(u' class="title-line"')
                    __append(u'>')
                    __append(u'\n                    ')

                    # <Static value=<_ast.Dict object at 0x0000000020CDE940> name=None at 20cde8d0> -> __attrs_550366288
                    __attrs_550366288 = _static_550365504

                    # <span ... (8:20)
                    # --------------------------------------------------------
                    __append(u'<span')
                    __append(u' class="icon"')
                    __append(u'>')
                    __append(u'\n                        ')

                    # <Static value=<_ast.Dict object at 0x0000000020CDECC0> name=None at 20cdedd8> -> __attrs_550367128
                    __attrs_550367128 = _static_550366400

                    # <span ... (9:24)
                    # --------------------------------------------------------
                    __append(u'<span')
                    __append(u' class="glyphicon glyphicon-book"')
                    __append(u'>')
                    __append(u'</span>')
                    __append(u'\n                    ')
                    __append(u'</span>')
                    __append(u'\n                    ')

                    # <Static value=<_ast.Dict object at 0x0000000020CDECF8> name=None at 20cde160> -> __attrs_550364384
                    __attrs_550364384 = _static_550366456

                    # <a ... (11:20)
                    # --------------------------------------------------------
                    __append(u'<a')
                    __append(u' class="title"')

                    # <Builtin id='False' ctx=<_ast.Load object at 0x000000001964B048> at 20b384a8> -> __default_550363992
                    __default_550363992 = False

                    # <Substitution u"router.link_to('overview.category.book',\n                        {'book_name': item.name, 'lang_iso': item.lang_iso})" (12:24)> -> __attr_href
                    __token = 529
                    __attr_href = _lookup_attr(getitem('router'), 'link_to')('overview.category.book', {'book_name': _lookup_attr(getitem('item'), 'name'), 'lang_iso': _lookup_attr(getitem('item'), 'lang_iso'), })
                    __attr_href = __quote(__attr_href, '"', '&quot;', None, False)
                    if (__attr_href is not None):
                        __append((u' href="%s"' % __attr_href))
                    __append(u'>')

                    # <Interpolation value=<Substitution u'\n                        ${item.title}\n                        ' (13:78)> braces_required=True translation=False at 20cde518> -> __content_100582504
                    __token = 673
                    __token = 675
                    __content_100582504 = _lookup_attr(getitem('item'), 'title')
                    __content_100582504 = __quote(__content_100582504, '\x00', '&#0;', None, False)
                    __content_100582504 = ('%s%s%s' % (u'\n                        ', (__content_100582504 if (__content_100582504 is not None) else ''), u'\n                        ', ))
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

                    # <Value u'not item.lang_iso == lang.iso' (15:45)> -> __condition
                    __token = 732
                    __condition = not (_lookup_attr(getitem('item'), 'lang_iso') == _lookup_attr(getitem('lang'), 'iso'))
                    if __condition:

                        # <Static value=<_ast.Dict object at 0x0000000020CDE7B8> name=None at 20cde2e8> -> __attrs_548705952
                        __attrs_548705952 = _static_550365112

                        # <span ... (15:24)
                        # --------------------------------------------------------
                        __append(u'<span')
                        __append(u'\n                            class="label label-primary cs-label"')

                        # <Builtin id='False' ctx=<_ast.Load object at 0x000000001964B048> at 20b384a8> -> __default_548707520
                        __default_548707520 = False

                        # <Interpolation value=<Substitution u"${lang._l('doc_book_different_language')}" (17:35)> braces_required=True translation=False at 20b49eb8> -> __attr_title
                        __token = 863
                        __token = 865
                        __attr_title = _lookup_attr(getitem('lang'), '_l')('doc_book_different_language')
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
                            __append((u'\n                            title="%s"' % __attr_title))
                        __append(u'>')

                        # <Interpolation value=<Substitution u'\n                            ${item.lang_iso}\n                        ' (17:78)> braces_required=True translation=False at 20b492b0> -> __content_100582504
                        __token = 935
                        __token = 937
                        __content_100582504 = _lookup_attr(getitem('item'), 'lang_iso')
                        __content_100582504 = __quote(__content_100582504, '\x00', '&#0;', None, False)
                        __content_100582504 = ('%s%s%s' % (u'\n                            ', (__content_100582504 if (__content_100582504 is not None) else ''), u'\n                        ', ))
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
                    __append(u'\n                    ')
                    __append(u'</a>')
                    __append(u'\n                ')
                    __append(u'</div>')
                    __append(u'\n                ')

                    # <Static value=<_ast.Dict object at 0x0000000020B49DD8> name=None at 20b49240> -> __attrs_548707128
                    __attrs_548707128 = _static_548707800

                    # <div ... (22:16)
                    # --------------------------------------------------------
                    __append(u'<div')
                    __append(u' class="teaser-line"')
                    __append(u'>')
                    __append(u'\n                    ')

                    # <Static value=<_ast.Dict object at 0x0000000020B49C88> name=None at 20b49400> -> __attrs_548705224
                    __attrs_548705224 = _static_548707464

                    # <div ... (23:20)
                    # --------------------------------------------------------
                    __append(u'<div')
                    __append(u' class="teaser-block"')
                    __append(u'>')
                    __append(u'</div>')
                    __append(u'\n                    ')

                    # <Static value=<_ast.Dict object at 0x0000000020AF9160> name=None at 20b498d0> -> __attrs_548377264
                    __attrs_548377264 = _static_548376928

                    # <div ... (24:20)
                    # --------------------------------------------------------
                    __append(u'<div')
                    __append(u' class="teaser-block"')
                    __append(u'>')
                    __append(u'\n                        ')

                    # <Static value=<_ast.Dict object at 0x0000000020AF9048> name=None at 20af9390> -> __attrs_548378216
                    __attrs_548378216 = _static_548376648

                    # <div ... (25:24)
                    # --------------------------------------------------------
                    __append(u'<div')
                    __append(u' class="teaser"')
                    __append(u'>')
                    __append(u'\n                            ')

                    # <Static value=<_ast.Dict object at 0x0000000020AF9550> name=None at 20af9400> -> __attrs_548378608
                    __attrs_548378608 = _static_548377936

                    # <div ... (26:28)
                    # --------------------------------------------------------
                    __append(u'<div')
                    __append(u' class="teaser-row"')
                    __append(u'>')
                    __append(u'\n                                ')

                    # <Static value=<_ast.Dict object at 0x0000000020AF9A90> name=None at 20af9f60> -> __attrs_548379728
                    __attrs_548379728 = _static_548379280

                    # <div ... (27:32)
                    # --------------------------------------------------------
                    __append(u'<div')
                    __append(u' class="teaser-text"')
                    __append(u'>')
                    __default_548380344 = '__default'

                    # <Value u'item.teaser' (28:61)> -> __cache_548378832
                    __token = 1390
                    __cache_548378832 = _lookup_attr(getitem('item'), 'teaser')

                    # <Identity expression=<Value u'item.teaser' (28:61)> value=<_ast.Str object at 0x0000000020AF9CC0> at 20af9cf8> -> __condition
                    __expression = __cache_548378832
                    __value = '__default'
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_548378832
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append(u'</div>')
                    __append(u'\n                            ')
                    __append(u'</div>')
                    __append(u'\n                        ')
                    __append(u'</div>')
                    __append(u'\n                    ')
                    __append(u'</div>')
                    __append(u'\n                ')
                    __append(u'</div>')
                    __append(u'\n            ')
                    __append(u'</div>')
                    ____index_548199952 -= 1
                    if (____index_548199952 > 0):
                        __append('\n            ')
                if (__backup_item_548636264 is __marker):
                    del econtext['item']
                else:
                    econtext['item'] = __backup_item_548636264
                __append(u'\n            ')

                # <Value u'not category.books' (34:32)> -> __condition
                __token = 1577
                __condition = not _lookup_attr(getitem('category'), 'books')
                if __condition:

                    # <Static value=<_ast.Dict object at 0x0000000019877B00> name=None at 19877c50> -> __attrs_548325976
                    __attrs_548325976 = _static_428309248

                    # <div ... (34:12)
                    # --------------------------------------------------------
                    __append(u'<div>')

                    # <Interpolation value=<Substitution u"\n                ${lang._l('doc_category_is_empty')}\n            " (34:52)> braces_required=True translation=False at 20aec630> -> __content_100582504
                    __token = 1614
                    __token = 1616
                    __content_100582504 = _lookup_attr(getitem('lang'), '_l')('doc_category_is_empty')
                    __content_100582504 = __quote(__content_100582504, '\x00', '&#0;', None, False)
                    __content_100582504 = ('%s%s%s' % (u'\n                ', (__content_100582504 if (__content_100582504 is not None) else ''), u'\n            ', ))
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
                    __append(u'</div>')
                __append(u'\n        ')
                __append(u'</div>')
                __append(u'\n    ')
                __append(u'</div>')
            _slots = econtext[u'__slot_content'] = _deque((__fill_content, ))

            # <Value u'load: layout.html' (1:22)> -> __macro
            __token = 22
            __macro = u' layout.html'
            __macro = __loader(__macro)
            __token = 22
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_446448136 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_446448136
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }