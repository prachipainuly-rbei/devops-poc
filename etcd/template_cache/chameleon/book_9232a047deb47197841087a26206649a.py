# -*- coding: utf-8 -*-
__filename = 'c:\\cdb\\contact_elements_server_15.3.13\\cdb\\chrome\\documentation\\book.html'
__tokens = {8: (u' page_name = "book" ', 1, 8), 270: (u"page.name == 'index'", 6, 99), 234: (u'book.formats.keys()', 6, 63), 337: (u"router.link_to(\n                        'overview.category.book.format',\n                        {'format': book.formats[fmt], 'book_name': book.name})", 7, 44), 563: (u'Download as ${fmt}', 11, 24), 577: (u'fmt', 11, 38), 793: (u'page.content_type == 0', 18, 37), 740: (u'page.content()', 17, 41), 929: (u'page.content_type == 1', 21, 32), 876: (u'load: genindex.html', 20, 34), 876: (u'load: genindex.html', 20, 34), 1049: (u'page.content_type == 2', 23, 32), 994: (u'load: genmodules.html', 22, 34), 994: (u'load: genmodules.html', 22, 34), 1237: (u'page.prev_link[0]', 28, 56), 1333: (u"router.link_to('overview.category.book.page', {\n                                'page_name': page.prev_link[0]\n                            })", 30, 28), 1601: (u'page.prev_link[1]', 34, 57), 1730: (u'page.next_link[0]', 37, 52), 1826: (u"router.link_to('overview.category.book.page', {\n                                'page_name': page.next_link[0]\n                            })", 39, 28), 2027: (u'page.next_link[1]', 42, 57), 2375: (u'category.books', 52, 35), 2416: (u" is_active=router.is_current('overview.category.book',\n                  {'book_name': book.name, 'lang_iso': book.lang_iso}) ", 53, 24), 2569: (u' has_children = page.toc() and len(page.toc())>0 ', 55, 24), 2645: (u' class_name = "active" if is_active else "" ', 56, 24), 2716: (u' class_name += " has-children" if has_children else "" ', 57, 24), 2801: (u'${class_name}', 58, 27), 2803: (u'class_name', 58, 29), 2846: (u"${router.link_to('overview.category.book',\n                     {'book_name': book.name, 'lang_iso': book.lang_iso})}", 59, 29), 2848: (u"router.link_to('overview.category.book',\n                     {'book_name': book.name, 'lang_iso': book.lang_iso})", 59, 31), 3116: (u'not book.lang_iso == lang.iso', 63, 42), 3214: (u'${book.lang_iso}', 64, 67), 3216: (u'book.lang_iso', 64, 69), 3279: (u'book.title', 65, 41), 3468: (u'is_active', 69, 35), 3421: (u'page.toc()', 68, 47), 3508: (u' is_active = levelone.is_current(router, book) ', 70, 28), 3586: (u' has_children = len(levelone)>0 ', 71, 28), 3649: (u' class_name = "active" if is_active else "" ', 72, 28), 3724: (u' class_name += " has-children" if has_children else "" ', 73, 28), 3813: (u'${class_name} navitem', 74, 31), 3815: (u'class_name', 74, 33), 3870: (u"${router.link_to('overview.category.book.page',\n                         {'book_name': book.name, 'page_name': levelone.refuri,\n                          '#': levelone.anchor})}", 75, 33), 3872: (u"router.link_to('overview.category.book.page',\n                         {'book_name': book.name, 'page_name': levelone.refuri,\n                          '#': levelone.anchor})", 75, 35), 4087: (u'levelone.title', 78, 38), 4254: (u'is_active', 81, 36), 4208: (u'levelone', 80, 51), 4316: (u"'active navitem'\n                         if leveltwo.is_current(router, book) else 'navitem'", 82, 50), 4449: (u"${router.link_to(\n                             'overview.category.book.page', {'book_name': book.name,\n                             'page_name': leveltwo.refuri, '#': leveltwo.anchor})}", 84, 37), 4451: (u"router.link_to(\n                             'overview.category.book.page', {'book_name': book.name,\n                             'page_name': leveltwo.refuri, '#': leveltwo.anchor})", 84, 39), 4678: (u'leveltwo.title', 87, 42), 53: (u'load: layout.html', 2, 22), 53: (u'load: layout.html', 2, 22)}

from sys import exc_info as _exc_info
from chameleon.py26 import lookup_attr as _lookup_attr
from collections import deque as _deque

_static_554064696 = {u'class': u'label label-default', u'title': u'Language', }
_static_428309248 = {}
_static_548707464 = {u'href': u"router.link_to(\n                        'overview.category.book.format',\n                        {'format': book.formats[fmt], 'book_name': book.name})", u'class': u'btn btn-default', }
_static_548197880 = u'load: genindex.html'
_static_552798864 = {u'aria-hidden': u'true', }
_static_554061896 = {u'href': u"${router.link_to('overview.category.book',\n                     {'book_name': book.name, 'lang_iso': book.lang_iso})}", u'class': u'booklink', }
_static_548325752 = {u'class': u'nav nav-stacked', u'id': u'sidebar', }
_static_535397544 = {u'href': u"router.link_to('overview.category.book.page', {\n                                'page_name': page.next_link[0]\n                            })", }
_static_552798752 = {u'href': u"router.link_to('overview.category.book.page', {\n                                'page_name': page.prev_link[0]\n                            })", }
_static_548707912 = {u'class': u'page-content', }
_static_552866648 = {u'class': u'nav nav-stacked', }
_static_550363712 = {u'class': u'row', }
_static_552731088 = {u'href': u"${router.link_to('overview.category.book.page',\n                         {'book_name': book.name, 'page_name': levelone.refuri,\n                          '#': levelone.anchor})}", }
_static_552796848 = {u'class': u'previous', }
_static_429393008 = {u'class': u'pager', }
_static_548200176 = {u'class': u'bottom-nav', }
_static_548379112 = {u'class': u'format pull-right', }
_static_548200344 = u'load: genmodules.html'
_static_554907856 = {u'href': u"${router.link_to(\n                             'overview.category.book.page', {'book_name': book.name,\n                             'page_name': leveltwo.refuri, '#': leveltwo.anchor})}", }
_static_548325640 = {u'class': u'${class_name}', }
_static_535399560 = {u'aria-hidden': u'true', }
_static_552731648 = {u'class': u'nav nav-stacked', }
_static_548379672 = {u'class': u'col-xs-12', }
_static_552869112 = {u'class': u'${class_name} navitem', }
_static_548825520 = {u'class': u'next', }
_static_550363488 = u'load: layout.html'
_static_552734672 = {u'class': u"'active navitem'\n                         if leveltwo.is_current(router, book) else 'navitem'", }
_static_554065816 = {u'class': u'glyphicon glyphicon-book', }
_static_548324688 = {u'class': u'sidebar', }

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
            __token = 8
            econtext['page_name'] = 'book'
            __append(u'\n')
            __backup_macroname_553970696 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x0000000020CDE160> name=None at 20cde4e0> -> __value
            __value = _static_550363488
            econtext['macroname'] = __value

            def __fill_content(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getitem = econtext.__getitem__
                get = econtext.get

                # <Static value=<_ast.Dict object at 0x0000000019877B00> name=None at 19877c50> -> __attrs_550365560
                __attrs_550365560 = _static_428309248

                # <div ... (3:4)
                # --------------------------------------------------------
                __append(u'<div>')
                __append(u'\n        ')

                # <Static value=<_ast.Dict object at 0x0000000020CDE240> name=None at 20cde630> -> __attrs_548379728
                __attrs_548379728 = _static_550363712

                # <div ... (4:8)
                # --------------------------------------------------------
                __append(u'<div')
                __append(u' class="row"')
                __append(u'>')
                __append(u'\n            ')

                # <Static value=<_ast.Dict object at 0x0000000020AF9C18> name=None at 20af9fd0> -> __attrs_548378832
                __attrs_548378832 = _static_548379672

                # <div ... (5:12)
                # --------------------------------------------------------
                __append(u'<div')
                __append(u' class="col-xs-12"')
                __append(u'>')
                __append(u'\n                ')

                # <Value u"page.name == 'index'" (6:99)> -> __condition
                __token = 270
                __condition = (_lookup_attr(getitem('page'), 'name') == 'index')
                if __condition:
                    __backup_fmt_548704440 = get('fmt', __marker)

                    # <Value u'book.formats.keys()' (6:63)> -> __iterator
                    __token = 234
                    __iterator = _lookup_attr(_lookup_attr(getitem('book'), 'formats'), 'keys')()
                    (__iterator, ____index_548377040, ) = getitem('repeat')(u'fmt', __iterator)
                    econtext['fmt'] = None
                    for __item in __iterator:
                        econtext['fmt'] = __item

                        # <Static value=<_ast.Dict object at 0x0000000020AF99E8> name=None at 20af9710> -> __attrs_548376872
                        __attrs_548376872 = _static_548379112

                        # <div ... (6:16)
                        # --------------------------------------------------------
                        __append(u'<div')
                        __append(u' class="format pull-right"')
                        __append(u'>')
                        __append(u'\n                    ')

                        # <Static value=<_ast.Dict object at 0x0000000020B49C88> name=None at 20b49cf8> -> __attrs_548707520
                        __attrs_548707520 = _static_548707464

                        # <a ... (7:20)
                        # --------------------------------------------------------
                        __append(u'<a')
                        __append(u'\n                        class="btn btn-default"')

                        # <Builtin id='False' ctx=<_ast.Load object at 0x000000001964B048> at 20af9240> -> __default_548707968
                        __default_548707968 = False

                        # <Substitution u"router.link_to(\n                        'overview.category.book.format',\n                        {'format': book.formats[fmt], 'book_name': book.name})" (7:44)> -> __attr_href
                        __token = 337
                        __attr_href = _lookup_attr(getitem('router'), 'link_to')('overview.category.book.format', {'format': _lookup_attr(getitem('book'), 'formats')[getitem('fmt')], 'book_name': _lookup_attr(getitem('book'), 'name'), })
                        __attr_href = __quote(__attr_href, '"', '&quot;', None, False)
                        if (__attr_href is not None):
                            __append((u' href="%s"' % __attr_href))
                        __append(u'>')

                        # <Interpolation value=<Substitution u'\n                        Download as ${fmt}\n                    ' (10:48)> braces_required=True translation=False at 20b492b0> -> __content_100582504
                        __token = 563
                        __token = 577
                        __content_100582504 = getitem('fmt')
                        __content_100582504 = __quote(__content_100582504, '\x00', '&#0;', None, False)
                        __content_100582504 = ('%s%s%s' % (u'\n                        Download as ', (__content_100582504 if (__content_100582504 is not None) else ''), u'\n                    ', ))
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
                        __append(u'\n                ')
                        __append(u'</div>')
                        ____index_548377040 -= 1
                        if (____index_548377040 > 0):
                            __append('\n                ')
                    if (__backup_fmt_548704440 is __marker):
                        del econtext['fmt']
                    else:
                        econtext['fmt'] = __backup_fmt_548704440
                __append(u'\n            ')
                __append(u'</div>')
                __append(u'\n        ')
                __append(u'</div>')
                __append(u'\n        ')

                # <Static value=<_ast.Dict object at 0x0000000020B49E48> name=None at 20b49160> -> __attrs_548704328
                __attrs_548704328 = _static_548707912

                # <div ... (16:8)
                # --------------------------------------------------------
                __append(u'<div')
                __append(u' class="page-content"')
                __append(u'>')
                __append(u'\n            ')

                # <Value u'page.content_type == 0' (18:37)> -> __condition
                __token = 793
                __condition = (_lookup_attr(getitem('page'), 'content_type') == 0)
                if __condition:
                    __default_548706568 = '__default'

                    # <Value u'page.content()' (17:41)> -> __cache_548705280
                    __token = 740
                    __cache_548705280 = _lookup_attr(getitem('page'), 'content')()

                    # <Identity expression=<Value u'page.content()' (17:41)> value=<_ast.Str object at 0x0000000020B495F8> at 20b49198> -> __condition
                    __expression = __cache_548705280
                    __value = '__default'
                    __condition = (__expression is __value)
                    if __condition:
                        __append(u'\n            ')
                    else:
                        __content = __cache_548705280
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                __append(u'\n            ')

                # <Value u'page.content_type == 1' (21:32)> -> __condition
                __token = 929
                __condition = (_lookup_attr(getitem('page'), 'content_type') == 1)
                if __condition:
                    __backup_macroname_548984584 = get('macroname', __marker)

                    # <Static value=<_ast.Str object at 0x0000000020ACD5F8> name=None at 20acde10> -> __value
                    __value = _static_548197880
                    econtext['macroname'] = __value

                    # <Value u'load: genindex.html' (20:34)> -> __macro
                    __token = 876
                    __macro = u' genindex.html'
                    __macro = __loader(__macro)
                    __token = 876
                    __m = __macro.include
                    __m(__stream, econtext.copy(), rcontext, __i18n_domain)
                    econtext.update(rcontext)
                    if (__backup_macroname_548984584 is __marker):
                        del econtext['macroname']
                    else:
                        econtext['macroname'] = __backup_macroname_548984584
                __append(u'\n            ')

                # <Value u'page.content_type == 2' (23:32)> -> __condition
                __token = 1049
                __condition = (_lookup_attr(getitem('page'), 'content_type') == 2)
                if __condition:
                    __backup_macroname_551331208 = get('macroname', __marker)

                    # <Static value=<_ast.Str object at 0x0000000020ACDF98> name=None at 20acdba8> -> __value
                    __value = _static_548200344
                    econtext['macroname'] = __value

                    # <Value u'load: genmodules.html' (22:34)> -> __macro
                    __token = 994
                    __macro = u' genmodules.html'
                    __macro = __loader(__macro)
                    __token = 994
                    __m = __macro.include
                    __m(__stream, econtext.copy(), rcontext, __i18n_domain)
                    econtext.update(rcontext)
                    if (__backup_macroname_551331208 is __marker):
                        del econtext['macroname']
                    else:
                        econtext['macroname'] = __backup_macroname_551331208
                __append(u'\n        ')
                __append(u'</div>')
                __append(u'\n        ')

                # <Static value=<_ast.Dict object at 0x0000000020ACDEF0> name=None at 20acdb00> -> __attrs_548198552
                __attrs_548198552 = _static_548200176

                # <div ... (25:8)
                # --------------------------------------------------------
                __append(u'<div')
                __append(u' class="bottom-nav"')
                __append(u'>')
                __append(u'\n            ')

                # <Static value=<_ast.Dict object at 0x0000000019877B00> name=None at 19877c50> -> __attrs_429392672
                __attrs_429392672 = _static_428309248

                # <nav ... (26:12)
                # --------------------------------------------------------
                __append(u'<nav>')
                __append(u'\n                ')

                # <Static value=<_ast.Dict object at 0x0000000019980470> name=None at 199803c8> -> __attrs_429393400
                __attrs_429393400 = _static_429393008

                # <ul ... (27:16)
                # --------------------------------------------------------
                __append(u'<ul')
                __append(u' class="pager"')
                __append(u'>')
                __append(u'\n                    ')

                # <Value u'page.prev_link[0]' (28:56)> -> __condition
                __token = 1237
                __condition = _lookup_attr(getitem('page'), 'prev_link')[0]
                if __condition:

                    # <Static value=<_ast.Dict object at 0x0000000020F302B0> name=None at 20f30278> -> __attrs_552797184
                    __attrs_552797184 = _static_552796848

                    # <li ... (28:20)
                    # --------------------------------------------------------
                    __append(u'<li')
                    __append(u' class="previous"')
                    __append(u'>')
                    __append(u'\n                        ')

                    # <Static value=<_ast.Dict object at 0x0000000020F30A20> name=None at 20f30978> -> __attrs_552799592
                    __attrs_552799592 = _static_552798752

                    # <a ... (29:24)
                    # --------------------------------------------------------
                    __append(u'<a')

                    # <Builtin id='False' ctx=<_ast.Load object at 0x000000001964B048> at 20af9240> -> __default_552797240
                    __default_552797240 = False

                    # <Substitution u"router.link_to('overview.category.book.page', {\n                                'page_name': page.prev_link[0]\n                            })" (30:28)> -> __attr_href
                    __token = 1333
                    __attr_href = _lookup_attr(getitem('router'), 'link_to')('overview.category.book.page', {'page_name': _lookup_attr(getitem('page'), 'prev_link')[0], })
                    __attr_href = __quote(__attr_href, '"', '&quot;', None, False)
                    if (__attr_href is not None):
                        __append((u' href="%s"' % __attr_href))
                    __append(u'>')
                    __append(u'\n                            ')

                    # <Static value=<_ast.Dict object at 0x0000000020F30A90> name=None at 20f30ac8> -> __attrs_552798024
                    __attrs_552798024 = _static_552798864

                    # <span ... (33:28)
                    # --------------------------------------------------------
                    __append(u'<span')
                    __append(u' aria-hidden="true"')
                    __append(u'>')
                    __append(u'&larr;')
                    __append(u'</span>')
                    __append(u'\n                            ')

                    # <Static value=<_ast.Dict object at 0x0000000019877B00> name=None at 19877c50> -> __attrs_552799816
                    __attrs_552799816 = _static_428309248

                    # <span ... (34:28)
                    # --------------------------------------------------------
                    __append(u'<span>')
                    __default_552800152 = '__default'

                    # <Value u'page.prev_link[1]' (34:57)> -> __cache_552798416
                    __token = 1601
                    __cache_552798416 = _lookup_attr(getitem('page'), 'prev_link')[1]

                    # <Identity expression=<Value u'page.prev_link[1]' (34:57)> value=<_ast.Str object at 0x0000000020F307B8> at 20f30c88> -> __condition
                    __expression = __cache_552798416
                    __value = '__default'
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_552798416
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append(u'</span>')
                    __append(u'\n                        ')
                    __append(u'</a>')
                    __append(u'\n                    ')
                    __append(u'</li>')
                __append(u'\n                    ')

                # <Value u'page.next_link[0]' (37:52)> -> __condition
                __token = 1730
                __condition = _lookup_attr(getitem('page'), 'next_link')[0]
                if __condition:

                    # <Static value=<_ast.Dict object at 0x0000000020B669B0> name=None at 20b66860> -> __attrs_535398216
                    __attrs_535398216 = _static_548825520

                    # <li ... (37:20)
                    # --------------------------------------------------------
                    __append(u'<li')
                    __append(u' class="next"')
                    __append(u'>')
                    __append(u'\n                        ')

                    # <Static value=<_ast.Dict object at 0x000000001FE984A8> name=None at 1fe983c8> -> __attrs_535398832
                    __attrs_535398832 = _static_535397544

                    # <a ... (38:24)
                    # --------------------------------------------------------
                    __append(u'<a')

                    # <Builtin id='False' ctx=<_ast.Load object at 0x000000001964B048> at 20af9240> -> __default_535397152
                    __default_535397152 = False

                    # <Substitution u"router.link_to('overview.category.book.page', {\n                                'page_name': page.next_link[0]\n                            })" (39:28)> -> __attr_href
                    __token = 1826
                    __attr_href = _lookup_attr(getitem('router'), 'link_to')('overview.category.book.page', {'page_name': _lookup_attr(getitem('page'), 'next_link')[0], })
                    __attr_href = __quote(__attr_href, '"', '&quot;', None, False)
                    if (__attr_href is not None):
                        __append((u' href="%s"' % __attr_href))
                    __append(u'>')
                    __append(u'\n                            ')

                    # <Static value=<_ast.Dict object at 0x0000000019877B00> name=None at 19877c50> -> __attrs_535400232
                    __attrs_535400232 = _static_428309248

                    # <span ... (42:28)
                    # --------------------------------------------------------
                    __append(u'<span>')
                    __default_535399224 = '__default'

                    # <Value u'page.next_link[1]' (42:57)> -> __cache_535399896
                    __token = 2027
                    __cache_535399896 = _lookup_attr(getitem('page'), 'next_link')[1]

                    # <Identity expression=<Value u'page.next_link[1]' (42:57)> value=<_ast.Str object at 0x000000001FE984E0> at 1fe98d68> -> __condition
                    __expression = __cache_535399896
                    __value = '__default'
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_535399896
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append(u'</span>')
                    __append(u'\n                            ')

                    # <Static value=<_ast.Dict object at 0x000000001FE98C88> name=None at 1fe98f60> -> __attrs_535398944
                    __attrs_535398944 = _static_535399560

                    # <span ... (43:28)
                    # --------------------------------------------------------
                    __append(u'<span')
                    __append(u' aria-hidden="true"')
                    __append(u'>')
                    __append(u'&rarr;')
                    __append(u'</span>')
                    __append(u'\n                        ')
                    __append(u'</a>')
                    __append(u'\n                    ')
                    __append(u'</li>')
                __append(u'\n                ')
                __append(u'</ul>')
                __append(u'\n            ')
                __append(u'</nav>')
                __append(u'\n        ')
                __append(u'</div>')
                __append(u'\n    ')
                __append(u'</div>')
            _slots = econtext[u'__slot_content'] = _deque((__fill_content, ))

            def __fill_sidebar(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getitem = econtext.__getitem__
                get = econtext.get

                # <Static value=<_ast.Dict object at 0x0000000020AEC550> name=None at 1fe98518> -> __attrs_548324912
                __attrs_548324912 = _static_548324688

                # <div ... (50:4)
                # --------------------------------------------------------
                __append(u'<div')
                __append(u' class="sidebar"')
                __append(u'>')
                __append(u'\n        ')

                # <Static value=<_ast.Dict object at 0x0000000020AEC978> name=None at 20aec8d0> -> __attrs_548326256
                __attrs_548326256 = _static_548325752

                # <ul ... (51:8)
                # --------------------------------------------------------
                __append(u'<ul')
                __append(u' class="nav nav-stacked"')
                __append(u' id="sidebar"')
                __append(u'>')
                __append(u'\n            ')
                __backup_book_552877808 = get('book', __marker)

                # <Value u'category.books' (52:35)> -> __iterator
                __token = 2375
                __iterator = _lookup_attr(getitem('category'), 'books')
                (__iterator, ____index_548326984, ) = getitem('repeat')(u'book', __iterator)
                econtext['book'] = None
                for __item in __iterator:
                    econtext['book'] = __item
                    __append(u'\n                ')
                    __token = 2416
                    econtext['is_active'] = getitem('router').is_current('overview.category.book', {'book_name': getitem('book').name, 'lang_iso': getitem('book').lang_iso, })
                    __append(u'\n                ')
                    __token = 2569
                    econtext['has_children'] = (getitem('page').toc() and (len(getitem('page').toc()) > 0))
                    __append(u'\n                ')
                    __token = 2645
                    econtext['class_name'] = ('active' if getitem('is_active') else '')
                    __append(u'\n                ')
                    __token = 2716
                    econtext['class_name'] += (' has-children' if getitem('has_children') else '')
                    __append(u'\n                ')

                    # <Static value=<_ast.Dict object at 0x0000000020AEC908> name=None at 20aec2e8> -> __attrs_554063968
                    __attrs_554063968 = _static_548325640

                    # <li ... (58:16)
                    # --------------------------------------------------------
                    __append(u'<li')

                    # <Builtin id='False' ctx=<_ast.Load object at 0x000000001964B048> at 20af9240> -> __default_554064192
                    __default_554064192 = False

                    # <Interpolation value=<Substitution u'${class_name}' (58:27)> braces_required=True translation=False at 210656d8> -> __attr_class
                    __token = 2801
                    __token = 2803
                    __attr_class = getitem('class_name')
                    __attr_class = __quote(__attr_class, '"', '&quot;', None, False)
                    __attr_class = __attr_class
                    if (__attr_class is None):
                        pass
                    else:
                        if (__attr_class is False):
                            __attr_class = None
                        else:
                            __tt = type(__attr_class)
                            if ((__tt is int) or (__tt is float) or (__tt is long)):
                                __attr_class = unicode(__attr_class)
                            else:
                                if (__tt is str):
                                    __attr_class = decode(__attr_class)
                                else:
                                    if (__tt is not unicode):
                                        try:
                                            __attr_class = __attr_class.__html__
                                        except get('AttributeError', AttributeError):
                                            __converted = convert(__attr_class)
                                            __attr_class = (unicode(__attr_class) if (__attr_class is __converted) else __converted)
                                        else:
                                            __attr_class = __attr_class()
                    if (__attr_class is not None):
                        __append((u' class="%s"' % __attr_class))
                    __append(u'>')
                    __append(u'\n                    ')

                    # <Static value=<_ast.Dict object at 0x0000000021065048> name=None at 21065e10> -> __attrs_554062344
                    __attrs_554062344 = _static_554061896

                    # <a ... (59:20)
                    # --------------------------------------------------------
                    __append(u'<a')

                    # <Builtin id='False' ctx=<_ast.Load object at 0x000000001964B048> at 20af9240> -> __default_554065760
                    __default_554065760 = False

                    # <Interpolation value=<Substitution u"${router.link_to('overview.category.book',\n                     {'book_name': book.name, 'lang_iso': book.lang_iso})}" (59:29)> braces_required=True translation=False at 210656a0> -> __attr_href
                    __token = 2846
                    __token = 2848
                    __attr_href = _lookup_attr(getitem('router'), 'link_to')('overview.category.book', {'book_name': _lookup_attr(getitem('book'), 'name'), 'lang_iso': _lookup_attr(getitem('book'), 'lang_iso'), })
                    __attr_href = __quote(__attr_href, '"', '&quot;', None, False)
                    __attr_href = __attr_href
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
                    __append(u'\n                       class="booklink"')
                    __append(u'>')
                    __append(u'\n                     ')

                    # <Static value=<_ast.Dict object at 0x0000000021065F98> name=None at 21065518> -> __attrs_554065088
                    __attrs_554065088 = _static_554065816

                    # <span ... (62:21)
                    # --------------------------------------------------------
                    __append(u'<span')
                    __append(u' class="glyphicon glyphicon-book"')
                    __append(u'>')
                    __append(u'</span>')
                    __append(u'\n                     ')

                    # <Value u'not book.lang_iso == lang.iso' (63:42)> -> __condition
                    __token = 3116
                    __condition = not (_lookup_attr(getitem('book'), 'lang_iso') == _lookup_attr(getitem('lang'), 'iso'))
                    if __condition:

                        # <Static value=<_ast.Dict object at 0x0000000021065B38> name=None at 21065898> -> __attrs_554064136
                        __attrs_554064136 = _static_554064696

                        # <span ... (63:21)
                        # --------------------------------------------------------
                        __append(u'<span')
                        __append(u'\n                      class="label label-default"')
                        __append(u' title="Language"')
                        __append(u'>')

                        # <Interpolation value=<Substitution u'${book.lang_iso}' (64:67)> braces_required=True translation=False at 20f41d68> -> __content_100582504
                        __token = 3214
                        __token = 3216
                        __content_100582504 = _lookup_attr(getitem('book'), 'lang_iso')
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
                    __append(u'\n                     ')
                    __default_552867208 = '__default'

                    # <Value u'book.title' (65:41)> -> __cache_552869056
                    __token = 3279
                    __cache_552869056 = _lookup_attr(getitem('book'), 'title')

                    # <Identity expression=<Value u'book.title' (65:41)> value=<_ast.Str object at 0x0000000020F41438> at 20f41550> -> __condition
                    __expression = __cache_552869056
                    __value = '__default'
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_552869056
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append(u'\n                    ')
                    __append(u'</a>')
                    __append(u'\n                ')

                    # <Static value=<_ast.Dict object at 0x0000000020F41358> name=None at 20f41320> -> __attrs_552868272
                    __attrs_552868272 = _static_552866648

                    # <ul ... (67:16)
                    # --------------------------------------------------------
                    __append(u'<ul')
                    __append(u' class="nav nav-stacked"')
                    __append(u'>')
                    __append(u'\n                ')

                    # <Value u'is_active' (69:35)> -> __condition
                    __token = 3468
                    __condition = getitem('is_active')
                    if __condition:
                        __backup_levelone_552796512 = get('levelone', __marker)

                        # <Value u'page.toc()' (68:47)> -> __iterator
                        __token = 3421
                        __iterator = _lookup_attr(getitem('page'), 'toc')()
                        (__iterator, ____index_552867040, ) = getitem('repeat')(u'levelone', __iterator)
                        econtext['levelone'] = None
                        for __item in __iterator:
                            econtext['levelone'] = __item
                            __append(u'\n                    ')
                            __token = 3508
                            econtext['is_active'] = getitem('levelone').is_current(getitem('router'), getitem('book'))
                            __append(u'\n                    ')
                            __token = 3586
                            econtext['has_children'] = (len(getitem('levelone')) > 0)
                            __append(u'\n                    ')
                            __token = 3649
                            econtext['class_name'] = ('active' if getitem('is_active') else '')
                            __append(u'\n                    ')
                            __token = 3724
                            econtext['class_name'] += (' has-children' if getitem('has_children') else '')
                            __append(u'\n                    ')

                            # <Static value=<_ast.Dict object at 0x0000000020F41CF8> name=None at 20f41e10> -> __attrs_552868048
                            __attrs_552868048 = _static_552869112

                            # <li ... (74:20)
                            # --------------------------------------------------------
                            __append(u'<li')

                            # <Builtin id='False' ctx=<_ast.Load object at 0x000000001964B048> at 20af9240> -> __default_552869840
                            __default_552869840 = False

                            # <Interpolation value=<Substitution u'${class_name} navitem' (74:31)> braces_required=True translation=False at 20f41dd8> -> __attr_class
                            __token = 3813
                            __token = 3815
                            __attr_class = getitem('class_name')
                            __attr_class = __quote(__attr_class, '"', '&quot;', None, False)
                            __attr_class = ('%s%s' % ((__attr_class if (__attr_class is not None) else ''), u' navitem', ))
                            if (__attr_class is None):
                                pass
                            else:
                                if (__attr_class is False):
                                    __attr_class = None
                                else:
                                    __tt = type(__attr_class)
                                    if ((__tt is int) or (__tt is float) or (__tt is long)):
                                        __attr_class = unicode(__attr_class)
                                    else:
                                        if (__tt is str):
                                            __attr_class = decode(__attr_class)
                                        else:
                                            if (__tt is not unicode):
                                                try:
                                                    __attr_class = __attr_class.__html__
                                                except get('AttributeError', AttributeError):
                                                    __converted = convert(__attr_class)
                                                    __attr_class = (unicode(__attr_class) if (__attr_class is __converted) else __converted)
                                                else:
                                                    __attr_class = __attr_class()
                            if (__attr_class is not None):
                                __append((u' class="%s"' % __attr_class))
                            __append(u'>')
                            __append(u'\n                        ')

                            # <Static value=<_ast.Dict object at 0x0000000020F201D0> name=None at 20f20160> -> __attrs_552732096
                            __attrs_552732096 = _static_552731088

                            # <a ... (75:24)
                            # --------------------------------------------------------
                            __append(u'<a')

                            # <Builtin id='False' ctx=<_ast.Load object at 0x000000001964B048> at 20af9240> -> __default_552733216
                            __default_552733216 = False

                            # <Interpolation value=<Substitution u"${router.link_to('overview.category.book.page',\n                         {'book_name': book.name, 'page_name': levelone.refuri,\n                          '#': levelone.anchor})}" (75:33)> braces_required=True translation=False at 20f20630> -> __attr_href
                            __token = 3870
                            __token = 3872
                            __attr_href = _lookup_attr(getitem('router'), 'link_to')('overview.category.book.page', {'book_name': _lookup_attr(getitem('book'), 'name'), 'page_name': _lookup_attr(getitem('levelone'), 'refuri'), '#': _lookup_attr(getitem('levelone'), 'anchor'), })
                            __attr_href = __quote(__attr_href, '"', '&quot;', None, False)
                            __attr_href = __attr_href
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
                            __append(u'>')
                            __default_552730752 = '__default'

                            # <Value u'levelone.title' (78:38)> -> __cache_552869000
                            __token = 4087
                            __cache_552869000 = _lookup_attr(getitem('levelone'), 'title')

                            # <Identity expression=<Value u'levelone.title' (78:38)> value=<_ast.Str object at 0x0000000020F20470> at 20f202b0> -> __condition
                            __expression = __cache_552869000
                            __value = '__default'
                            __condition = (__expression is __value)
                            if __condition:
                                pass
                            else:
                                __content = __cache_552869000
                                __content = __quote(__content, None, '\xad', None, None)
                                if (__content is not None):
                                    __append(__content)
                            __append(u'</a>')
                            __append(u'\n                    ')

                            # <Static value=<_ast.Dict object at 0x0000000020F20400> name=None at 20f20908> -> __attrs_552731872
                            __attrs_552731872 = _static_552731648

                            # <ul ... (79:20)
                            # --------------------------------------------------------
                            __append(u'<ul')
                            __append(u' class="nav nav-stacked"')
                            __append(u'>')
                            __append(u'\n                    ')

                            # <Value u'is_active' (81:36)> -> __condition
                            __token = 4254
                            __condition = getitem('is_active')
                            if __condition:
                                __backup_leveltwo_551349048 = get('leveltwo', __marker)

                                # <Value u'levelone' (80:51)> -> __iterator
                                __token = 4208
                                __iterator = getitem('levelone')
                                (__iterator, ____index_552733552, ) = getitem('repeat')(u'leveltwo', __iterator)
                                econtext['leveltwo'] = None
                                for __item in __iterator:
                                    econtext['leveltwo'] = __item
                                    __append(u'\n                        ')

                                    # <Static value=<_ast.Dict object at 0x0000000020F20FD0> name=None at 20f20c50> -> __attrs_552733104
                                    __attrs_552733104 = _static_552734672

                                    # <li ... (82:24)
                                    # --------------------------------------------------------
                                    __append(u'<li')

                                    # <Builtin id='False' ctx=<_ast.Load object at 0x000000001964B048> at 20af9240> -> __default_552734392
                                    __default_552734392 = False

                                    # <Substitution u"'active navitem'\n                         if leveltwo.is_current(router, book) else 'navitem'" (82:50)> -> __attr_class
                                    __token = 4316
                                    __attr_class = ('active navitem' if _lookup_attr(getitem('leveltwo'), 'is_current')(getitem('router'), getitem('book')) else 'navitem')
                                    __attr_class = __quote(__attr_class, '"', '&quot;', None, False)
                                    if (__attr_class is not None):
                                        __append((u' class="%s"' % __attr_class))
                                    __append(u'>')
                                    __append(u'\n                            ')

                                    # <Static value=<_ast.Dict object at 0x00000000211338D0> name=None at 21133908> -> __attrs_554908920
                                    __attrs_554908920 = _static_554907856

                                    # <a ... (84:28)
                                    # --------------------------------------------------------
                                    __append(u'<a')

                                    # <Builtin id='False' ctx=<_ast.Load object at 0x000000001964B048> at 20af9240> -> __default_554905784
                                    __default_554905784 = False

                                    # <Interpolation value=<Substitution u"${router.link_to(\n                             'overview.category.book.page', {'book_name': book.name,\n                             'page_name': leveltwo.refuri, '#': leveltwo.anchor})}" (84:37)> braces_required=True translation=False at 21133438> -> __attr_href
                                    __token = 4449
                                    __token = 4451
                                    __attr_href = _lookup_attr(getitem('router'), 'link_to')('overview.category.book.page', {'book_name': _lookup_attr(getitem('book'), 'name'), 'page_name': _lookup_attr(getitem('leveltwo'), 'refuri'), '#': _lookup_attr(getitem('leveltwo'), 'anchor'), })
                                    __attr_href = __quote(__attr_href, '"', '&quot;', None, False)
                                    __attr_href = __attr_href
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
                                    __append(u'>')
                                    __default_554907968 = '__default'

                                    # <Value u'leveltwo.title' (87:42)> -> __cache_552732264
                                    __token = 4678
                                    __cache_552732264 = _lookup_attr(getitem('leveltwo'), 'title')

                                    # <Identity expression=<Value u'leveltwo.title' (87:42)> value=<_ast.Str object at 0x0000000021133CC0> at 21133ba8> -> __condition
                                    __expression = __cache_552732264
                                    __value = '__default'
                                    __condition = (__expression is __value)
                                    if __condition:
                                        pass
                                    else:
                                        __content = __cache_552732264
                                        __content = __quote(__content, None, '\xad', None, None)
                                        if (__content is not None):
                                            __append(__content)
                                    __append(u'</a>')
                                    __append(u'\n                        ')
                                    __append(u'</li>')
                                    __append(u'\n                    ')
                                    ____index_552733552 -= 1
                                    if (____index_552733552 > 0):
                                        __append('')
                                if (__backup_leveltwo_551349048 is __marker):
                                    del econtext['leveltwo']
                                else:
                                    econtext['leveltwo'] = __backup_leveltwo_551349048
                            __append(u'\n                ')
                            __append(u'</ul>')
                            __append(u'\n                ')
                            __append(u'</li>')
                            __append(u'\n                ')
                            ____index_552867040 -= 1
                            if (____index_552867040 > 0):
                                __append('')
                        if (__backup_levelone_552796512 is __marker):
                            del econtext['levelone']
                        else:
                            econtext['levelone'] = __backup_levelone_552796512
                    __append(u'\n                ')
                    __append(u'</ul>')
                    __append(u'\n                ')
                    __append(u'</li>')
                    __append(u'\n            ')
                    ____index_548326984 -= 1
                    if (____index_548326984 > 0):
                        __append('')
                if (__backup_book_552877808 is __marker):
                    del econtext['book']
                else:
                    econtext['book'] = __backup_book_552877808
                __append(u'\n        ')
                __append(u'</ul>')
                __append(u'\n    ')
                __append(u'</div>')
            _slots = econtext[u'__slot_sidebar'] = _deque((__fill_sidebar, ))

            # <Value u'load: layout.html' (2:22)> -> __macro
            __token = 53
            __macro = u' layout.html'
            __macro = __loader(__macro)
            __token = 53
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_553970696 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_553970696
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }