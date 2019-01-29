# -*- coding: utf-8 -*-
__filename = 'c:\\cdb\\rbei\\site-packages\\cs.web-15.3.0.6-py2.7.egg\\cs\\web\\components\\base\\resources\\base.html'
__tokens = {43: (u'${widgets["document_title"]}', 4, 11), 45: (u'widgets["document_title"]', 4, 13), 182: (u'window.appSetup = JSON.parse(${structure: widgets["setup"]});\n        try { window.external.cdbEFEnableNotifyChanges(${widgets["enable_notify_changes"]|false}); } catch(e) {}', 7, 8), 213: (u'structure: widgets["setup"]', 7, 39), 224: (u'widgets["setup"]', 7, 50), 301: (u'widgets["enable_notify_changes"]|false', 8, 57), 411: (u"widgets['favicon']", 10, 40), 477: (u"widgets['additional_head']", 11, 43), 549: (u"widgets['includes']", 12, 41), 621: (u"'/static/' + widgets['global_styles']", 13, 48), 738: (u"widgets['body'] is None", 16, 26), 818: (u"widgets['body'] is not None", 17, 26), 870: (u"widgets['body']", 17, 78)}

from chameleon.utils import Markup as _Markup
from sys import exc_info as _exc_info

_static_214660320 = {u'href': u"'/static/' + widgets['global_styles']", u'charset': u'utf-8', u'type': u'text/css', u'rel': u'stylesheet', }
_static_214682648 = {}
_static_214693312 = {u'content': u'IE=edge', u'http-equiv': u'X-UA-Compatible', }
_static_214662336 = {u'id': u'application-root', }
_static_214694320 = {u'type': u'text/javascript', }

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
            __append(u'<!DOCTYPE html>')
            __append(u'\n')

            # <Static value=<_ast.Dict object at 0x000000000CCBCC18> name=None at ccbc0b8> -> __attrs_214691968
            __attrs_214691968 = _static_214682648

            # <html ... (2:0)
            # --------------------------------------------------------
            __append(u'<html>')
            __append(u'\n  ')

            # <Static value=<_ast.Dict object at 0x000000000CCBCC18> name=None at ccbc0b8> -> __attrs_214692472
            __attrs_214692472 = _static_214682648

            # <head ... (3:2)
            # --------------------------------------------------------
            __append(u'<head>')
            __append(u'\n    ')

            # <Static value=<_ast.Dict object at 0x000000000CCBCC18> name=None at ccbc0b8> -> __attrs_214692976
            __attrs_214692976 = _static_214682648

            # <title ... (4:4)
            # --------------------------------------------------------
            __append(u'<title>')

            # <Interpolation value=<Substitution u'${widgets["document_title"]}' (4:11)> braces_required=True translation=False at ccbf550> -> __content_70714392
            __token = 43
            __token = 45
            __content_70714392 = getitem('widgets')['document_title']
            __content_70714392 = __quote(__content_70714392, '\x00', '&#0;', None, False)
            __content_70714392 = __content_70714392
            if (__content_70714392 is None):
                pass
            else:
                if (__content_70714392 is False):
                    __content_70714392 = None
                else:
                    __tt = type(__content_70714392)
                    if ((__tt is int) or (__tt is float) or (__tt is long)):
                        __content_70714392 = unicode(__content_70714392)
                    else:
                        if (__tt is str):
                            __content_70714392 = decode(__content_70714392)
                        else:
                            if (__tt is not unicode):
                                try:
                                    __content_70714392 = __content_70714392.__html__
                                except get('AttributeError', AttributeError):
                                    __converted = convert(__content_70714392)
                                    __content_70714392 = (unicode(__content_70714392) if (__content_70714392 is __converted) else __converted)
                                else:
                                    __content_70714392 = __content_70714392()
            if (__content_70714392 is not None):
                __append(__content_70714392)
            __append(u'</title>')
            __append(u'\n    ')

            # <Static value=<_ast.Dict object at 0x000000000CCBF5C0> name=None at ccbf5f8> -> __attrs_214694040
            __attrs_214694040 = _static_214693312

            # <meta ... (5:4)
            # --------------------------------------------------------
            __append(u'<meta')
            __append(u' http-equiv="X-UA-Compatible"')
            __append(u' content="IE=edge"')
            __append(u'>')
            __append(u'\n    ')

            # <Static value=<_ast.Dict object at 0x000000000CCBF9B0> name=None at ccbf978> -> __attrs_214694824
            __attrs_214694824 = _static_214694320

            # <script ... (6:4)
            # --------------------------------------------------------
            __append(u'<script')
            __append(u' type="text/javascript"')
            __append(u'>')

            # <Interpolation value=<Substitution u'\n        window.appSetup = JSON.parse(${structure: widgets["setup"]});\n        try { window.external.cdbEFEnableNotifyChanges(${widgets["enable_notify_changes"]|false}); } catch(e) {}\n    ' (6:35)> braces_required=True translation=False at ccbfc88> -> __content_70714392
            __token = 182
            __token = 213
            __token = 224
            __content_70714392 = getitem('widgets')['setup']
            __content_70714392 = _Markup(__content_70714392)
            __content_70714392 = __quote(__content_70714392, '\x00', '&#0;', None, False)
            __token = 301
            try:
                __content_70714392_299 = getitem('widgets')['enable_notify_changes']
            except (NameError, ValueError, AttributeError, LookupError, TypeError, ):
                __content_70714392_299 = getitem('false')
                __exc_clear()

            __content_70714392_299 = __quote(__content_70714392_299, '\x00', '&#0;', None, False)
            __content_70714392 = ('%s%s%s%s%s' % (u'\n        window.appSetup = JSON.parse(', (__content_70714392 if (__content_70714392 is not None) else ''), u');\n        try { window.external.cdbEFEnableNotifyChanges(', (__content_70714392_299 if (__content_70714392_299 is not None) else ''), u'); } catch(e) {}\n    ', ))
            if (__content_70714392 is None):
                pass
            else:
                if (__content_70714392 is False):
                    __content_70714392 = None
                else:
                    __tt = type(__content_70714392)
                    if ((__tt is int) or (__tt is float) or (__tt is long)):
                        __content_70714392 = unicode(__content_70714392)
                    else:
                        if (__tt is str):
                            __content_70714392 = decode(__content_70714392)
                        else:
                            if (__tt is not unicode):
                                try:
                                    __content_70714392 = __content_70714392.__html__
                                except get('AttributeError', AttributeError):
                                    __converted = convert(__content_70714392)
                                    __content_70714392 = (unicode(__content_70714392) if (__content_70714392 is __converted) else __converted)
                                else:
                                    __content_70714392 = __content_70714392()
            if (__content_70714392 is not None):
                __append(__content_70714392)
            __append(u'</script>')
            __append(u'\n    ')
            __default_214695664 = '__default'

            # <Value u"widgets['favicon']" (10:40)> -> __cache_214695272
            __token = 411
            __cache_214695272 = getitem('widgets')['favicon']

            # <Identity expression=<Value u"widgets['favicon']" (10:40)> value=<_ast.Str object at 0x000000000CCBFDD8> at ccbfe10> -> __condition
            __expression = __cache_214695272
            __value = '__default'
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_214695272
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append(u'\n    ')
            __default_214659536 = '__default'

            # <Value u"widgets['additional_head']" (11:43)> -> __cache_214695888
            __token = 477
            __cache_214695888 = getitem('widgets')['additional_head']

            # <Identity expression=<Value u"widgets['additional_head']" (11:43)> value=<_ast.Str object at 0x000000000CCB70B8> at ccb70f0> -> __condition
            __expression = __cache_214695888
            __value = '__default'
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_214695888
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append(u'\n    ')
            __default_214660152 = '__default'

            # <Value u"widgets['includes']" (12:41)> -> __cache_214659760
            __token = 549
            __cache_214659760 = getitem('widgets')['includes']

            # <Identity expression=<Value u"widgets['includes']" (12:41)> value=<_ast.Str object at 0x000000000CCB7320> at ccb7358> -> __condition
            __expression = __cache_214659760
            __value = '__default'
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_214659760
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append(u'\n    ')

            # <Static value=<_ast.Dict object at 0x000000000CCB74E0> name=None at ccb74a8> -> __attrs_214661552
            __attrs_214661552 = _static_214660320

            # <link ... (13:4)
            # --------------------------------------------------------
            __append(u'<link')
            __append(u' rel="stylesheet"')
            __append(u' type="text/css"')
            __append(u' charset="utf-8"')

            # <Builtin id='False' ctx=<_ast.Load object at 0x000000000CC567B8> at cc8edd8> -> __default_214661328
            __default_214661328 = False

            # <Substitution u"'/static/' + widgets['global_styles']" (13:48)> -> __attr_href
            __token = 621
            __attr_href = ('/static/' + getitem('widgets')['global_styles'])
            __attr_href = __quote(__attr_href, '"', '&quot;', None, False)
            if (__attr_href is not None):
                __append((u' href="%s"' % __attr_href))
            __append(u'>')
            __append(u'\n  ')
            __append(u'</head>')
            __append(u'\n  ')

            # <Static value=<_ast.Dict object at 0x000000000CCBCC18> name=None at ccbc0b8> -> __attrs_214662000
            __attrs_214662000 = _static_214682648

            # <body ... (15:2)
            # --------------------------------------------------------
            __append(u'<body>')
            __append(u'\n      ')

            # <Value u"widgets['body'] is None" (16:26)> -> __condition
            __token = 738
            __condition = (getitem('widgets')['body'] is None)
            if __condition:

                # <Static value=<_ast.Dict object at 0x000000000CCB7CC0> name=None at ccb7c88> -> __attrs_214662840
                __attrs_214662840 = _static_214662336

                # <div ... (16:6)
                # --------------------------------------------------------
                __append(u'<div')
                __append(u' id="application-root"')
                __append(u'>')
                __append(u'</div>')
            __append(u'\n      ')

            # <Value u"widgets['body'] is not None" (17:26)> -> __condition
            __token = 818
            __condition = (getitem('widgets')['body'] is not None)
            if __condition:
                __default_214619024 = '__default'

                # <Value u"widgets['body']" (17:78)> -> __cache_214618632
                __token = 870
                __cache_214618632 = getitem('widgets')['body']

                # <Identity expression=<Value u"widgets['body']" (17:78)> value=<_ast.Str object at 0x000000000CCAD278> at ccad2b0> -> __condition
                __expression = __cache_214618632
                __value = '__default'
                __condition = (__expression is __value)
                if __condition:

                    # <Static value=<_ast.Dict object at 0x000000000CCBCC18> name=None at ccbc0b8> -> __attrs_214618520
                    __attrs_214618520 = _static_214682648

                    # <div ... (17:6)
                    # --------------------------------------------------------
                    __append(u'<div>')
                    __append(u'</div>')
                else:
                    __content = __cache_214618632
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
            __append(u'\n  ')
            __append(u'</body>')
            __append(u'\n')
            __append(u'</html>')
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }