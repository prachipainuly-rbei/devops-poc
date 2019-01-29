# -*- coding: utf-8 -*-
__filename = u'c:\\cdb\\contact_elements_server_15.3.13\\cdb\\chrome\\landing_pages.html'
__tokens = {2704: (u'${component_namespace}-portalbox', 53, 16), 2706: (u'component_namespace', 53, 18), 2929: (u"message('branding_installer_portal_title')", 56, 117), 3099: (u"'/doc/' + current_lang", 59, 56), 3183: (u"message('branding_doc_portal_title')", 59, 140), 1496: (u"message('login_language')", 25, 158), 1594: (u"message('login_language')", 26, 70), 1624: (u" message('login_language'", 26, 100), 1813: (u'languages', 29, 40), 1860: (u'lang[1] != current_lang', 30, 35), 1935: (u'lang[1]', 31, 49), 2061: (u'lang[0]', 34, 48), 2197: (u'lang[1] == current_lang', 38, 35), 2272: (u'lang[1]', 39, 49), 2480: (u'lang[0]', 43, 52)}

from sys import exc_info as _exc_info

_static_429846936 = {u'src': u'/static/images/login_docs.svg', }
_static_426762704 = {u'content': u'IE=edge', u'http-equiv': u'X-UA-Compatible', }
_static_428644336 = {u'src': u'/static/images/cis-s-check.svg', u'alt': u'', }
_static_426763656 = {u'content': u'yes', u'name': u'apple-mobile-web-app-capable', }
_static_430089160 = {u'src': u'/static/jscript/language_select.js', u'type': u'text/javascript', }
_static_429653688 = {u'class': u'portal-item', }
_static_426674160 = {u'href': u'/static/imgid/branding_web_favicon.ico', u'rel': u'icon', }
_static_426318256 = {}
_static_429651560 = {u'class': u'${component_namespace}-portalbox', }
_static_428326864 = {u'class': u'caret', }
_static_426406464 = {u'src': u'/static/jscript/jquery3.min.js', u'type': u'text/javascript', }
_static_429821512 = {u'href': u"'/doc/' + current_lang", u'target': u'_blank', }
_static_426765784 = {u'href': u'/static/imgid/branding_web_favicon.ico', u'rel': u'shortcut icon', }
_static_428569936 = {u'class': u'dropdown-menu dropdown-menu-right', u'id': u'language-list', }
_static_427072928 = {u'content': u'text/html; charset=UTF-8', u'http-equiv': u'Content-Type', }
_static_426473344 = {u'href': u'/static/global-style.css', u'type': u'text/css', u'rel': u'stylesheet', }
_static_426674496 = {u'href': u'/static/imgid/branding_web_app_icon.png', u'rel': u'apple-touch-icon', }
_static_426407584 = {u'src': u'/static/jscript/jquery_login/js.cookie.js', }
_static_426675616 = {u'href': u'/static/images/less/cdb.fonts.css', u'type': u'text/css', u'rel': u'stylesheet', }
_static_430090168 = {u'src': u'/static/jscript/cdb.elink.js', u'type': u'text/javascript', }
_static_426408368 = {u'src': u'/static/jscript/bootstrap3.min.js', u'type': u'text/javascript', }
_static_428570888 = {u'href': u'#', u'data-lang': u'lang[1]', }
_static_430090672 = {u'class': u'cs-web-components-theme-static-language-box dropdown', }
_static_429821064 = {u'class': u'portal-item', }
_static_430092016 = {u'title': u"message('login_language')", u'aria-expanded': u'false', u'aria-haspopup': u'true', u'data-toggle': u'dropdown', u'type': u'button', u'class': u'btn btn-default dropdown-toggle', }
_static_429653408 = {u'class': u'portal-links', }
_static_426763768 = {u'content': u'user-scalable=yes, width=device-width, initial-scale=1', u'name': u'viewport', }
_static_428644728 = {u'href': u'#', u'data-lang': u'lang[1]', }
_static_426409376 = {u'src': u'/static/jscript/bootstrap.cdb.js', u'type': u'text/javascript', }
_static_429819216 = {u'src': u'/static/images/login_installers.svg', }
_static_429818208 = {u'href': u'/install', u'target': u'_blank', }
_static_428325240 = {u'src': u'/static/images/Globe.svg', u'alt': u"message('login_language')", u'title': u"message('login_language')", }

import re
import functools
from itertools import chain as __chain
from sys import exc_clear as __exc_clear
__marker = object()
g_re_amp = re.compile('&(?!([A-Za-z]+|#[0-9]+);)')
g_re_needs_escape = re.compile('[&<>\\"\\\']').search
__re_whitespace = functools.partial(re.compile('\\s+').sub, ' ')

def initialize(__loader, macros, nothing, template):

    def render_portalbox(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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
            __append(u'\n    ')

            # <Static value=<_ast.Dict object at 0x00000000199BF668> name=None at 199bf438> -> __attrs_429652008
            __attrs_429652008 = _static_429651560

            # <div ... (53:4)
            # --------------------------------------------------------
            __append(u'<div')

            # <Builtin id='False' ctx=<_ast.Load object at 0x000000001938DEB8> at 197496a0> -> __default_429651896
            __default_429651896 = False

            # <Interpolation value=<Substitution u'${component_namespace}-portalbox' (53:16)> braces_required=True translation=False at 199bf978> -> __attr_class
            __token = 2704
            __token = 2706
            __attr_class = getitem('component_namespace')
            __attr_class = __quote(__attr_class, '"', '&quot;', None, False)
            __attr_class = ('%s%s' % ((__attr_class if (__attr_class is not None) else ''), u'-portalbox', ))
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
            __append(u'\n        ')

            # <Static value=<_ast.Dict object at 0x00000000199BFDA0> name=None at 199bff28> -> __attrs_429653520
            __attrs_429653520 = _static_429653408

            # <div ... (54:8)
            # --------------------------------------------------------
            __append(u'<div')
            __append(u' class="portal-links"')
            __append(u'>')
            __append(u'\n            ')

            # <Static value=<_ast.Dict object at 0x00000000199BFEB8> name=None at 199bff98> -> __attrs_429652176
            __attrs_429652176 = _static_429653688

            # <div ... (55:12)
            # --------------------------------------------------------
            __append(u'<div')
            __append(u' class="portal-item"')
            __append(u'>')
            __append(u'\n                ')

            # <Static value=<_ast.Dict object at 0x00000000199E8160> name=None at 199e8048> -> __attrs_429818880
            __attrs_429818880 = _static_429818208

            # <a ... (56:16)
            # --------------------------------------------------------
            __append(u'<a')
            __append(u' href="/install"')
            __append(u' target="_blank"')
            __append(u'>')

            # <Static value=<_ast.Dict object at 0x00000000199E8550> name=None at 199e8588> -> __attrs_429819664
            __attrs_429819664 = _static_429819216

            # <img ... (56:51)
            # --------------------------------------------------------
            __append(u'<img')
            __append(u' src="/static/images/login_installers.svg"')
            __append(u'>')

            # <Static value=<_ast.Dict object at 0x00000000196919B0> name=None at 19691b00> -> __attrs_429820560
            __attrs_429820560 = _static_426318256

            # <span ... (56:98)
            # --------------------------------------------------------
            __append(u'<span >')
            __default_429820504 = '__default'

            # <Value u"message('branding_installer_portal_title')" (56:117)> -> __cache_429820280
            __token = 2929
            __cache_429820280 = getitem('message')('branding_installer_portal_title')

            # <Identity expression=<Value u"message('branding_installer_portal_title')" (56:117)> value=<_ast.Str object at 0x00000000199E8A20> at 199e8828> -> __condition
            __expression = __cache_429820280
            __value = '__default'
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_429820280
                __content = __quote(__content, None, '\xad', None, None)
                if (__content is not None):
                    __append(__content)
            __append(u'</span>')
            __append(u'</a>')
            __append(u'\n            ')
            __append(u'</div>')
            __append(u'\n            ')

            # <Static value=<_ast.Dict object at 0x00000000199E8C88> name=None at 199e8470> -> __attrs_429821176
            __attrs_429821176 = _static_429821064

            # <div ... (58:12)
            # --------------------------------------------------------
            __append(u'<div')
            __append(u' class="portal-item"')
            __append(u'>')
            __append(u'\n                ')

            # <Static value=<_ast.Dict object at 0x00000000199E8E48> name=None at 199e8f60> -> __attrs_429848672
            __attrs_429848672 = _static_429821512

            # <a ... (59:16)
            # --------------------------------------------------------
            __append(u'<a')
            __append(u' target="_blank"')

            # <Builtin id='False' ctx=<_ast.Load object at 0x000000001938DEB8> at 197496a0> -> __default_429849120
            __default_429849120 = False

            # <Substitution u"'/doc/' + current_lang" (59:56)> -> __attr_href
            __token = 3099
            __attr_href = ('/doc/' + getitem('current_lang'))
            __attr_href = __quote(__attr_href, '"', '&quot;', None, False)
            if (__attr_href is not None):
                __append((u' href="%s"' % __attr_href))
            __append(u'>')

            # <Static value=<_ast.Dict object at 0x00000000199EF198> name=None at 199ef710> -> __attrs_429847216
            __attrs_429847216 = _static_429846936

            # <img ... (59:80)
            # --------------------------------------------------------
            __append(u'<img')
            __append(u' src="/static/images/login_docs.svg"')
            __append(u'>')

            # <Static value=<_ast.Dict object at 0x00000000196919B0> name=None at 19691b00> -> __attrs_429848224
            __attrs_429848224 = _static_426318256

            # <span ... (59:121)
            # --------------------------------------------------------
            __append(u'<span>')
            __default_429847664 = '__default'

            # <Value u"message('branding_doc_portal_title')" (59:140)> -> __cache_429847440
            __token = 3183
            __cache_429847440 = getitem('message')('branding_doc_portal_title')

            # <Identity expression=<Value u"message('branding_doc_portal_title')" (59:140)> value=<_ast.Str object at 0x00000000199EF2E8> at 199ef550> -> __condition
            __expression = __cache_429847440
            __value = '__default'
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_429847440
                __content = __quote(__content, None, '\xad', None, None)
                if (__content is not None):
                    __append(__content)
            __append(u'</span>')
            __append(u'</a>')
            __append(u'\n            ')
            __append(u'</div>')
            __append(u'\n        ')
            __append(u'</div>')
            __append(u'\n    ')
            __append(u'</div>')
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise


    def render_header(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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
            __append(u'\n    ')

            # <Static value=<_ast.Dict object at 0x0000000019749DA0> name=None at 19749dd8> -> __attrs_426762480
            __attrs_426762480 = _static_427072928

            # <meta ... (2:4)
            # --------------------------------------------------------
            __append(u'<meta')
            __append(u' http-equiv="Content-Type"')
            __append(u' content="text/html; charset=UTF-8"')
            __append(u'>')
            __append(u'\n    ')

            # <Static value=<_ast.Dict object at 0x00000000196FE1D0> name=None at 196fe550> -> __attrs_426762984
            __attrs_426762984 = _static_426762704

            # <meta ... (3:4)
            # --------------------------------------------------------
            __append(u'<meta')
            __append(u' http-equiv="X-UA-Compatible"')
            __append(u' content="IE=edge"')
            __append(u'>')
            __append(u'\n    ')

            # <Static value=<_ast.Dict object at 0x00000000196FE588> name=None at 196fe978> -> __attrs_426764328
            __attrs_426764328 = _static_426763656

            # <meta ... (4:4)
            # --------------------------------------------------------
            __append(u'<meta')
            __append(u' name="apple-mobile-web-app-capable"')
            __append(u' content="yes"')
            __append(u' />')
            __append(u'\n    ')

            # <Static value=<_ast.Dict object at 0x00000000196FE5F8> name=None at 196fe9e8> -> __attrs_426765336
            __attrs_426765336 = _static_426763768

            # <meta ... (5:4)
            # --------------------------------------------------------
            __append(u'<meta')
            __append(u' name="viewport"')
            __append(u' content="user-scalable=yes, width=device-width, initial-scale=1"')
            __append(u' >')
            __append(u'\n\n    ')

            # <Static value=<_ast.Dict object at 0x00000000196FEDD8> name=None at 196fea20> -> __attrs_426673208
            __attrs_426673208 = _static_426765784

            # <link ... (7:4)
            # --------------------------------------------------------
            __append(u'<link')
            __append(u' rel="shortcut icon"')
            __append(u' href="/static/imgid/branding_web_favicon.ico"')
            __append(u'>')
            __append(u'\n    ')

            # <Static value=<_ast.Dict object at 0x00000000196E87F0> name=None at 196e88d0> -> __attrs_426673824
            __attrs_426673824 = _static_426674160

            # <link ... (8:4)
            # --------------------------------------------------------
            __append(u'<link')
            __append(u' rel="icon"')
            __append(u' href="/static/imgid/branding_web_favicon.ico"')
            __append(u'>')
            __append(u'\n    ')

            # <Static value=<_ast.Dict object at 0x00000000196E8940> name=None at 196e8470> -> __attrs_426675000
            __attrs_426675000 = _static_426674496

            # <link ... (9:4)
            # --------------------------------------------------------
            __append(u'<link')
            __append(u' rel="apple-touch-icon"')
            __append(u' href="/static/imgid/branding_web_app_icon.png"')
            __append(u'>')
            __append(u'\n\n    ')

            # <Static value=<_ast.Dict object at 0x00000000196E8DA0> name=None at 196e8e10> -> __attrs_426474184
            __attrs_426474184 = _static_426675616

            # <link ... (11:4)
            # --------------------------------------------------------
            __append(u'<link')
            __append(u' rel="stylesheet"')
            __append(u' href="/static/images/less/cdb.fonts.css"')
            __append(u' type="text/css"')
            __append(u'>')
            __append(u'\n    ')

            # <Static value=<_ast.Dict object at 0x00000000196B7780> name=None at 196b7e10> -> __attrs_426406128
            __attrs_426406128 = _static_426473344

            # <link ... (12:4)
            # --------------------------------------------------------
            __append(u'<link')
            __append(u' rel="stylesheet"')
            __append(u' href="/static/global-style.css"')
            __append(u' type="text/css"')
            __append(u'>')
            __append(u'\n\n    ')

            # <Static value=<_ast.Dict object at 0x00000000196A7240> name=None at 196a7208> -> __attrs_426407192
            __attrs_426407192 = _static_426406464

            # <script ... (14:4)
            # --------------------------------------------------------
            __append(u'<script')
            __append(u' src="/static/jscript/jquery3.min.js"')
            __append(u' type="text/javascript"')
            __append(u'>')
            __append(u'</script>')
            __append(u'\n    ')

            # <Static value=<_ast.Dict object at 0x00000000196A76A0> name=None at 196a74a8> -> __attrs_426408200
            __attrs_426408200 = _static_426407584

            # <script ... (15:4)
            # --------------------------------------------------------
            __append(u'<script')
            __append(u' src="/static/jscript/jquery_login/js.cookie.js"')
            __append(u'>')
            __append(u'</script>')
            __append(u'\n\n    ')

            # <Static value=<_ast.Dict object at 0x00000000196A79B0> name=None at 196a7940> -> __attrs_426409544
            __attrs_426409544 = _static_426408368

            # <script ... (17:4)
            # --------------------------------------------------------
            __append(u'<script')
            __append(u' src="/static/jscript/bootstrap3.min.js"')
            __append(u' type="text/javascript"')
            __append(u'>')
            __append(u'</script>')
            __append(u'\n    ')

            # <Static value=<_ast.Dict object at 0x00000000196A7DA0> name=None at 196a7d68> -> __attrs_430091008
            __attrs_430091008 = _static_426409376

            # <script ... (18:4)
            # --------------------------------------------------------
            __append(u'<script')
            __append(u' src="/static/jscript/bootstrap.cdb.js"')
            __append(u' type="text/javascript"')
            __append(u'>')
            __append(u'</script>')
            __append(u'\n    ')

            # <Static value=<_ast.Dict object at 0x0000000019A2A7B8> name=None at 19a2afd0> -> __attrs_430088936
            __attrs_430088936 = _static_430090168

            # <script ... (19:4)
            # --------------------------------------------------------
            __append(u'<script')
            __append(u' src="/static/jscript/cdb.elink.js"')
            __append(u' type="text/javascript"')
            __append(u'>')
            __append(u'</script>')
            __append(u'\n    ')

            # <Static value=<_ast.Dict object at 0x0000000019A2A3C8> name=None at 19a2a400> -> __attrs_430090112
            __attrs_430090112 = _static_430089160

            # <script ... (20:4)
            # --------------------------------------------------------
            __append(u'<script')
            __append(u' src="/static/jscript/language_select.js"')
            __append(u' type="text/javascript"')
            __append(u'>')
            __append(u'</script>')
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise


    def render_language_select(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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
            __append(u'\n    ')

            # <Static value=<_ast.Dict object at 0x0000000019A2A9B0> name=None at 19a2a940> -> __attrs_430091400
            __attrs_430091400 = _static_430090672

            # <div ... (24:4)
            # --------------------------------------------------------
            __append(u'<div')
            __append(u' class="cs-web-components-theme-static-language-box dropdown"')
            __append(u'>')
            __append(u'\n        ')

            # <Static value=<_ast.Dict object at 0x0000000019A2AEF0> name=None at 19a2add8> -> __attrs_428324456
            __attrs_428324456 = _static_430092016

            # <button ... (25:8)
            # --------------------------------------------------------
            __append(u'<button')
            __append(u' type="button"')
            __append(u' class="btn btn-default dropdown-toggle"')
            __append(u' data-toggle="dropdown"')
            __append(u' aria-haspopup="true"')
            __append(u' aria-expanded="false"')

            # <Builtin id='False' ctx=<_ast.Load object at 0x000000001938DEB8> at 197496a0> -> __default_428324232
            __default_428324232 = False

            # <Substitution u"message('login_language')" (25:158)> -> __attr_title
            __token = 1496
            __attr_title = getitem('message')('login_language')
            __attr_title = __quote(__attr_title, '"', '&quot;', None, False)
            if (__attr_title is not None):
                __append((u' title="%s"' % __attr_title))
            __append(u'>')
            __append(u'\n            ')

            # <Static value=<_ast.Dict object at 0x000000001987B978> name=None at 1987b6d8> -> __attrs_428325744
            __attrs_428325744 = _static_428325240

            # <img ... (26:12)
            # --------------------------------------------------------
            __append(u'<img')
            __append(u' src="/static/images/Globe.svg"')

            # <Builtin id='False' ctx=<_ast.Load object at 0x000000001938DEB8> at 197496a0> -> __default_428325856
            __default_428325856 = False

            # <Substitution u"message('login_language')" (26:70)> -> __attr_title
            __token = 1594
            __attr_title = getitem('message')('login_language')
            __attr_title = __quote(__attr_title, '"', '&quot;', None, False)
            if (__attr_title is not None):
                __append((u' title="%s"' % __attr_title))

            # <Builtin id='False' ctx=<_ast.Load object at 0x000000001938DEB8> at 197496a0> -> __default_428326584
            __default_428326584 = False

            # <Substitution u"message('login_language')" (26:100)> -> __attr_alt
            __token = 1624
            __attr_alt = getitem('message')('login_language')
            __attr_alt = __quote(__attr_alt, '"', '&quot;', None, False)
            if (__attr_alt is not None):
                __append((u' alt="%s"' % __attr_alt))
            __append(u'>')
            __append(u' ')

            # <Static value=<_ast.Dict object at 0x000000001987BFD0> name=None at 1987bc88> -> __attrs_428325296
            __attrs_428325296 = _static_428326864

            # <span ... (26:129)
            # --------------------------------------------------------
            __append(u'<span')
            __append(u' class="caret"')
            __append(u'>')
            __append(u'</span>')
            __append(u'\n        ')
            __append(u'</button>')
            __append(u'\n        ')

            # <Static value=<_ast.Dict object at 0x00000000198B7550> name=None at 198b7048> -> __attrs_428569544
            __attrs_428569544 = _static_428569936

            # <ul ... (28:8)
            # --------------------------------------------------------
            __append(u'<ul')
            __append(u' class="dropdown-menu dropdown-menu-right"')
            __append(u' id="language-list"')
            __append(u'>')
            __append(u'\n            ')
            __backup_lang_422396760 = get('lang', __marker)

            # <Value u'languages' (29:40)> -> __iterator
            __token = 1813
            __iterator = getitem('languages')
            (__iterator, ____index_428570216, ) = getitem('repeat')(u'lang', __iterator)
            econtext['lang'] = None
            for __item in __iterator:
                econtext['lang'] = __item
                __append(u'\n                ')

                # <Value u'lang[1] != current_lang' (30:35)> -> __condition
                __token = 1860
                __condition = (getitem('lang')[1] != getitem('current_lang'))
                if __condition:

                    # <Static value=<_ast.Dict object at 0x00000000196919B0> name=None at 19691b00> -> __attrs_428569992
                    __attrs_428569992 = _static_426318256

                    # <li ... (30:16)
                    # --------------------------------------------------------
                    __append(u'<li>')
                    __append(u'\n                    ')

                    # <Static value=<_ast.Dict object at 0x00000000198B7908> name=None at 198b7940> -> __attrs_428571784
                    __attrs_428571784 = _static_428570888

                    # <a ... (31:20)
                    # --------------------------------------------------------
                    __append(u'<a')
                    __append(u'\n                            href="#"')

                    # <Builtin id='False' ctx=<_ast.Load object at 0x000000001938DEB8> at 197496a0> -> __default_428572008
                    __default_428572008 = False

                    # <Substitution u'lang[1]' (31:49)> -> __attr_data_lang
                    __token = 1935
                    __attr_data_lang = getitem('lang')[1]
                    __attr_data_lang = __quote(__attr_data_lang, '"', '&quot;', None, False)
                    if (__attr_data_lang is not None):
                        __append((u' data-lang="%s"' % __attr_data_lang))
                    __append(u'>')
                    __append(u'\n                        ')

                    # <Static value=<_ast.Dict object at 0x00000000196919B0> name=None at 19691b00> -> __attrs_428572568
                    __attrs_428572568 = _static_426318256

                    # <span ... (33:24)
                    # --------------------------------------------------------
                    __append(u'<span>')
                    __append(u'\n                        ')
                    __default_428642936 = '__default'

                    # <Value u'lang[0]' (34:48)> -> __cache_428642488
                    __token = 2061
                    __cache_428642488 = getitem('lang')[0]

                    # <Identity expression=<Value u'lang[0]' (34:48)> value=<_ast.Str object at 0x0000000019477208> at 198c9160> -> __condition
                    __expression = __cache_428642488
                    __value = '__default'
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_428642488
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append(u'\n                        ')
                    __append(u'</span>')
                    __append(u'\n                    ')
                    __append(u'</a>')
                    __append(u'\n                ')
                    __append(u'</li>')
                __append(u'\n                ')

                # <Value u'lang[1] == current_lang' (38:35)> -> __condition
                __token = 2197
                __condition = (getitem('lang')[1] == getitem('current_lang'))
                if __condition:

                    # <Static value=<_ast.Dict object at 0x00000000196919B0> name=None at 19691b00> -> __attrs_428642768
                    __attrs_428642768 = _static_426318256

                    # <li ... (38:16)
                    # --------------------------------------------------------
                    __append(u'<li>')
                    __append(u'\n                    ')

                    # <Static value=<_ast.Dict object at 0x00000000198C9978> name=None at 198c9940> -> __attrs_428645904
                    __attrs_428645904 = _static_428644728

                    # <a ... (39:20)
                    # --------------------------------------------------------
                    __append(u'<a')
                    __append(u'\n                            href="#"')

                    # <Builtin id='False' ctx=<_ast.Load object at 0x000000001938DEB8> at 197496a0> -> __default_428643888
                    __default_428643888 = False

                    # <Substitution u'lang[1]' (39:49)> -> __attr_data_lang
                    __token = 2272
                    __attr_data_lang = getitem('lang')[1]
                    __attr_data_lang = __quote(__attr_data_lang, '"', '&quot;', None, False)
                    if (__attr_data_lang is not None):
                        __append((u' data-lang="%s"' % __attr_data_lang))
                    __append(u'>')
                    __append(u'\n                        ')

                    # <Static value=<_ast.Dict object at 0x00000000196919B0> name=None at 19691b00> -> __attrs_428646016
                    __attrs_428646016 = _static_426318256

                    # <span ... (41:24)
                    # --------------------------------------------------------
                    __append(u'<span>')
                    __append(u'\n                            ')

                    # <Static value=<_ast.Dict object at 0x00000000198C97F0> name=None at 198c9780> -> __attrs_429650552
                    __attrs_429650552 = _static_428644336

                    # <img ... (42:28)
                    # --------------------------------------------------------
                    __append(u'<img')
                    __append(u' src="/static/images/cis-s-check.svg"')
                    __append(u' alt=""')
                    __append(u'>')
                    __append(u'\n                            ')
                    __default_429651112 = '__default'

                    # <Value u'lang[0]' (43:52)> -> __cache_429650776
                    __token = 2480
                    __cache_429650776 = getitem('lang')[0]

                    # <Identity expression=<Value u'lang[0]' (43:52)> value=<_ast.Str object at 0x00000000199BF3C8> at 199bf400> -> __condition
                    __expression = __cache_429650776
                    __value = '__default'
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_429650776
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append(u'\n                        ')
                    __append(u'</span>')
                    __append(u'\n                    ')
                    __append(u'</a>')
                    __append(u'\n                ')
                    __append(u'</li>')
                __append(u'\n            ')
                ____index_428570216 -= 1
                if (____index_428570216 > 0):
                    __append('')
            if (__backup_lang_422396760 is __marker):
                del econtext['lang']
            else:
                econtext['lang'] = __backup_lang_422396760
            __append(u'\n        ')
            __append(u'</ul>')
            __append(u'\n    ')
            __append(u'</div>')
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise


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
            __token = None
            render_header(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            __append(u'\n\n')
            __token = None
            render_language_select(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            __append(u'\n\n')
            __token = None
            render_portalbox(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {u'render_portalbox': render_portalbox, u'render_header': render_header, u'render_language_select': render_language_select, 'render': render, }