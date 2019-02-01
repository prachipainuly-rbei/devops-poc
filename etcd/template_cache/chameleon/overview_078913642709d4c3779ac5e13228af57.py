# -*- coding: utf-8 -*-
__filename = 'c:\\cdb\\contact_elements_server_15.3.13\\cdb\\chrome\\documentation\\overview.html'
__tokens = {8: (u' page_name = "overview" ', 1, 8), 43: (u' page_title = "" ', 2, 8), 251: (u"lang._l('branding_doc_portal_title')", 7, 33), 401: (u"lang._l('doc_portal_welcome_text')", 9, 55), 650: (u'categories', 15, 85), 591: (u'docapp-category-box ${category.name}', 15, 26), 613: (u'category.name', 15, 48), 703: (u"router.link_to('overview.category', {'cat_name': category.name})", 16, 41), 825: (u'category.title', 17, 55), 962: (u'category.teaser', 19, 65), 85: (u'load: layout.html', 3, 22), 85: (u'load: layout.html', 3, 22)}

from sys import exc_info as _exc_info
from chameleon.py26 import lookup_attr as _lookup_attr
from collections import deque as _deque

_static_429392784 = {u'href': u"router.link_to('overview.category', {'cat_name': category.name})", u'class': u'docapp-category-box ${category.name}', }
_static_428309248 = {}
_static_447070104 = {u'class': u'lead', }
_static_535397824 = u'load: layout.html'
_static_535398776 = {u'class': u'row-fluid', }
_static_447068760 = {u'class': u'row-fluid', }
_static_535400288 = {u'class': u'span12 text-center', }
_static_548198944 = {u'class': u'box-icon', }
_static_548198048 = {u'class': u'box-head', }
_static_548825632 = {u'class': u'box-body', }
_static_429392168 = {u'class': u'box-container', }

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
            econtext['page_name'] = 'overview'
            __append(u'\n')
            __token = 43
            econtext['page_title'] = ''
            __append(u'\n')
            __backup_macroname_555371272 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x000000001FE985C0> name=None at 1fe985f8> -> __value
            __value = _static_535397824
            econtext['macroname'] = __value

            def __fill_content(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getitem = econtext.__getitem__
                get = econtext.get

                # <Static value=<_ast.Dict object at 0x0000000019877B00> name=None at 19877c50> -> __attrs_535398496
                __attrs_535398496 = _static_428309248

                # <div ... (4:4)
                # --------------------------------------------------------
                __append(u'<div>')
                __append(u'\n        ')

                # <Static value=<_ast.Dict object at 0x000000001FE98978> name=None at 1fe989b0> -> __attrs_535399952
                __attrs_535399952 = _static_535398776

                # <div ... (5:8)
                # --------------------------------------------------------
                __append(u'<div')
                __append(u' class="row-fluid"')
                __append(u'>')
                __append(u'\n            ')

                # <Static value=<_ast.Dict object at 0x000000001FE98F60> name=None at 1fe98ac8> -> __attrs_535399056
                __attrs_535399056 = _static_535400288

                # <div ... (6:12)
                # --------------------------------------------------------
                __append(u'<div')
                __append(u' class="span12 text-center"')
                __append(u'>')
                __append(u'\n                ')

                # <Static value=<_ast.Dict object at 0x0000000019877B00> name=None at 19877c50> -> __attrs_447067584
                __attrs_447067584 = _static_428309248

                # <h1 ... (7:16)
                # --------------------------------------------------------
                __append(u'<h1>')
                __default_447067360 = '__default'

                # <Value u"lang._l('branding_doc_portal_title')" (7:33)> -> __cache_443631264
                __token = 251
                __cache_443631264 = _lookup_attr(getitem('lang'), '_l')('branding_doc_portal_title')

                # <Identity expression=<Value u"lang._l('branding_doc_portal_title')" (7:33)> value=<_ast.Str object at 0x000000001AA5B470> at 1aa5b4a8> -> __condition
                __expression = __cache_443631264
                __value = '__default'
                __condition = (__expression is __value)
                if __condition:
                    __append(u'\n                    CONTACT Elements Documentation')
                else:
                    __content = __cache_443631264
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append(u'</h1>')
                __append(u'\n                ')

                # <Static value=<_ast.Dict object at 0x000000001AA5BF98> name=None at 1aa5bda0> -> __attrs_447069376
                __attrs_447069376 = _static_447070104

                # <p ... (9:16)
                # --------------------------------------------------------
                __append(u'<p')
                __append(u' class="lead"')
                __append(u'>')
                __default_447069712 = '__default'

                # <Value u"lang._l('doc_portal_welcome_text')" (9:55)> -> __cache_447069152
                __token = 401
                __cache_447069152 = _lookup_attr(getitem('lang'), '_l')('doc_portal_welcome_text')

                # <Identity expression=<Value u"lang._l('doc_portal_welcome_text')" (9:55)> value=<_ast.Str object at 0x000000001AA5BB38> at 1aa5bc18> -> __condition
                __expression = __cache_447069152
                __value = '__default'
                __condition = (__expression is __value)
                if __condition:
                    __append(u'\n                ')
                else:
                    __content = __cache_447069152
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append(u'</p>')
                __append(u'\n            ')
                __append(u'</div>')
                __append(u'\n        ')
                __append(u'</div>')
                __append(u'\n        ')

                # <Static value=<_ast.Dict object at 0x000000001AA5BA58> name=None at 1aa5b908> -> __attrs_447068088
                __attrs_447068088 = _static_447068760

                # <div ... (13:8)
                # --------------------------------------------------------
                __append(u'<div')
                __append(u' class="row-fluid"')
                __append(u'>')
                __append(u'\n            ')

                # <Static value=<_ast.Dict object at 0x0000000019980128> name=None at 19980518> -> __attrs_429392896
                __attrs_429392896 = _static_429392168

                # <div ... (14:12)
                # --------------------------------------------------------
                __append(u'<div')
                __append(u' class="box-container"')
                __append(u'>')
                __append(u'\n                ')
                __backup_category_440700152 = get('category', __marker)

                # <Value u'categories' (15:85)> -> __iterator
                __token = 650
                __iterator = getitem('categories')
                (__iterator, ____index_548197208, ) = getitem('repeat')(u'category', __iterator)
                econtext['category'] = None
                for __item in __iterator:
                    econtext['category'] = __item

                    # <Static value=<_ast.Dict object at 0x0000000019980390> name=None at 199802e8> -> __attrs_548196928
                    __attrs_548196928 = _static_429392784

                    # <a ... (15:16)
                    # --------------------------------------------------------
                    __append(u'<a')

                    # <Builtin id='False' ctx=<_ast.Load object at 0x000000001964B048> at 1fe98320> -> __default_429393512
                    __default_429393512 = False

                    # <Interpolation value=<Substitution u'docapp-category-box ${category.name}' (15:26)> braces_required=True translation=False at 19980e48> -> __attr_class
                    __token = 591
                    __token = 613
                    __attr_class = _lookup_attr(getitem('category'), 'name')
                    __attr_class = __quote(__attr_class, '"', '&quot;', None, False)
                    __attr_class = ('%s%s' % (u'docapp-category-box ', (__attr_class if (__attr_class is not None) else ''), ))
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

                    # <Builtin id='False' ctx=<_ast.Load object at 0x000000001964B048> at 1fe98320> -> __default_548196592
                    __default_548196592 = False

                    # <Substitution u"router.link_to('overview.category', {'cat_name': category.name})" (16:41)> -> __attr_href
                    __token = 703
                    __attr_href = _lookup_attr(getitem('router'), 'link_to')('overview.category', {'cat_name': _lookup_attr(getitem('category'), 'name'), })
                    __attr_href = __quote(__attr_href, '"', '&quot;', None, False)
                    if (__attr_href is not None):
                        __append((u' href="%s"' % __attr_href))
                    __append(u'>')
                    __append(u'\n                    ')

                    # <Static value=<_ast.Dict object at 0x0000000020ACD6A0> name=None at 20acd668> -> __attrs_548198496
                    __attrs_548198496 = _static_548198048

                    # <div ... (17:20)
                    # --------------------------------------------------------
                    __append(u'<div')
                    __append(u' class="box-head"')
                    __append(u'>')
                    __default_548197768 = '__default'

                    # <Value u'category.title' (17:55)> -> __cache_548197432
                    __token = 825
                    __cache_548197432 = _lookup_attr(getitem('category'), 'title')

                    # <Identity expression=<Value u'category.title' (17:55)> value=<_ast.Str object at 0x0000000020ACD4A8> at 20acd4e0> -> __condition
                    __expression = __cache_548197432
                    __value = '__default'
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_548197432
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append(u'</div>')
                    __append(u'\n                    ')

                    # <Static value=<_ast.Dict object at 0x0000000020ACDA20> name=None at 20acd208> -> __attrs_548824792
                    __attrs_548824792 = _static_548198944

                    # <div ... (18:20)
                    # --------------------------------------------------------
                    __append(u'<div')
                    __append(u' class="box-icon"')
                    __append(u'>')
                    __append(u'</div>')
                    __append(u'\n                    ')

                    # <Static value=<_ast.Dict object at 0x0000000020B66A20> name=None at 20b669e8> -> __attrs_548826080
                    __attrs_548826080 = _static_548825632

                    # <div ... (19:20)
                    # --------------------------------------------------------
                    __append(u'<div')
                    __append(u' class="box-body"')
                    __append(u'>')
                    __default_548825408 = '__default'

                    # <Value u'category.teaser' (19:65)> -> __cache_548824960
                    __token = 962
                    __cache_548824960 = _lookup_attr(getitem('category'), 'teaser')

                    # <Identity expression=<Value u'category.teaser' (19:65)> value=<_ast.Str object at 0x0000000020B66828> at 20b66860> -> __condition
                    __expression = __cache_548824960
                    __value = '__default'
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_548824960
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append(u'</div>')
                    __append(u'\n                ')
                    __append(u'</a>')
                    ____index_548197208 -= 1
                    if (____index_548197208 > 0):
                        __append('\n                ')
                if (__backup_category_440700152 is __marker):
                    del econtext['category']
                else:
                    econtext['category'] = __backup_category_440700152
                __append(u'\n            ')
                __append(u'</div>')
                __append(u'\n        ')
                __append(u'</div>')
                __append(u'\n    ')
                __append(u'</div>')
            _slots = econtext[u'__slot_content'] = _deque((__fill_content, ))

            # <Value u'load: layout.html' (3:22)> -> __macro
            __token = 85
            __macro = u' layout.html'
            __macro = __loader(__macro)
            __token = 85
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_555371272 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_555371272
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }