# -*- coding: utf-8 -*-
__filename = 'c:\\cdb\\contact_elements_server_15.3.13\\cdb\\chrome\\login.html'
__tokens = {87: (u'load: landing_pages.html', 3, 29), 29: (u'${component_namespace}-html', 2, 13), 31: (u'component_namespace', 2, 15), 168: (u'landing_page.header', 5, 37), 168: (u'landing_page.header', 5, 37), 292: (u"message('branding_login_title')", 9, 24), 361: (u'${component_namespace}-body', 12, 13), 363: (u'component_namespace', 12, 15), 404: (u'container ${component_namespace}-container', 14, 12), 416: (u'component_namespace', 14, 24), 465: (u'${component_namespace}-loginbox', 15, 16), 467: (u'component_namespace', 15, 18), 619: (u'landing_page.language_select', 17, 41), 619: (u'landing_page.language_select', 17, 41), 701: (u'not is_logged_in', 18, 34), 752: (u'show_sso_failure', 19, 32), 789: (u'message_id', 19, 69), 806: (u" python: 'sso-message alert %s' % msg_typ", 19, 86), 887: (u"current_lang == 'de'", 20, 36), 1736: (u"current_lang != 'de'", 35, 36), 2506: (u'post_action', 49, 55), 2592: (u'query', 50, 72), 2679: (u'acr_values', 51, 77), 2773: (u'msg', 53, 36), 2797: (u'message_id', 53, 60), 2814: (u" python: 'alert %s' % msg_typ", 53, 77), 2886: (u'msg_title', 54, 39), 2910: (u'msg_title', 54, 63), 2971: (u'msg', 55, 39), 3126: (u"message('login_user_label')", 58, 57), 3278: (u'last_username', 59, 114), 3449: (u"message('login_password_label')", 63, 59), 3655: (u'show_mfa_fields', 66, 42), 3990: (u'message(login_mfa_label)', 72, 60), 4326: (u'remember_me', 78, 114), 4406: (u"message('login_remember')", 79, 66), 4494: (u'${component_namespace}-submit-box', 82, 28), 4496: (u'component_namespace', 82, 30), 4745: (u'btn cs-web-components-base-semantic-button-primary ${component_namespace}-submit', 86, 59), 4798: (u'component_namespace', 86, 112), 4849: (u"message('login_button')", 86, 163), 4921: (u'sso_enabled', 87, 46), 5125: (u"message('login_sso_divider')", 91, 47), 5330: (u"message('login_sso_button')", 93, 136), 5485: (u'landing_page.portalbox', 97, 45), 5485: (u'landing_page.portalbox', 97, 45), 5602: (u'is_logged_in', 100, 34), 5669: (u"${message('login_welcome')}", 101, 52), 5671: (u"message('login_welcome')", 101, 54), 5784: (u'modal hide fade ${component_namespace}-modal', 107, 28), 5802: (u'component_namespace', 107, 46), 6118: (u"message('login_info_title')", 110, 85), 6341: (u"message('login_info_button')", 116, 100)}

from sys import exc_info as _exc_info
from chameleon.py26 import lookup_attr as _lookup_attr

_static_427418456 = {u'aria-labelledby': u'msgs-modal-label', u'class': u'modal hide fade ${component_namespace}-modal', u'role': u'dialog', u'aria-hidden': u'true', u'id': u'msgs-modal', u'tabindex': u'-1', }
_static_427276776 = {u'class': u'checkbox', }
_static_426763936 = {u'class': u'${component_namespace}-body', }
_static_427364704 = {u'type': u'submit', u'id': u'login', u'value': u"message('login_button')", u'class': u'btn cs-web-components-base-semantic-button-primary ${component_namespace}-submit', }
_static_426674776 = {u'lang': u'en', }
_static_427156760 = {u'type': u'hidden', u'name': u'acr_values', u'value': u'acr_values', }
_static_426676008 = {u'src': u'/static/jscript/elink_login.js', }
_static_427276160 = {u'class': u'form-group field-wrapper password-wrapper', }
_static_427366328 = u'landing_page.portalbox'
_static_427071192 = u'landing_page.language_select'
_static_427389168 = {u'class': u'right', }
_static_427070184 = {u'src': u'/static/imgid/branding_web_portal_logo.svg', u'class': u'ce-logo', }
_static_427420528 = {u'class': u'modal-header', }
_static_426318256 = {}
_static_427336256 = {u'onclick': u'', u'for': u'remember', }
_static_427452400 = {u'class': u'icon-info-sign', }
_static_427158832 = {u'id': u'message_id', u'class': u"python: 'alert %s' % msg_type", }
_static_427390960 = {u'type': u'button', u'class': u'btn cs-web-components-base-semantic-button-primary login-sso', u'value': u"message('login_sso_button')", }
_static_426766008 = {u'class': u'${component_namespace}-loginbox', }
_static_427309208 = {u'checked': u'remember_me', u'type': u'checkbox', u'id': u'remember', u'value': u'remember', u'name': u'remember', }
_static_427366944 = {u'class': u'sso-divider', }
_static_427248496 = {u'class': u'mfa-extra-wrapper hide', }
_static_426673432 = {u'class': u'${component_namespace}-html', }
_static_427453744 = {u'class': u'modal-body', }
_static_427451616 = {u'id': u'msgs-modal-label', }
_static_427392640 = {u'id': u'login_message', u'class': u'logged-in', }
_static_426764944 = {u'class': u'container ${component_namespace}-container', }
_static_427338216 = {u'class': u'throbber-wrap', }
_static_427246648 = {u'type': u'password', u'id': u'login_passwd', u'name': u'password', u'class': u'form-control', }
_static_427367896 = {u'class': u'left', }
_static_427475688 = {u'class': u'modal-footer', }
_static_427339168 = {u'src': u'/static/images/throbber.svg', u'class': u'throbber', }
_static_427132464 = {u'action': u'post_action', u'method': u'POST', }
_static_427072088 = {u'id': u'message_id', u'class': u"python: 'sso-message alert %s' % msg_type", }
_static_426675616 = u'landing_page.header'
_static_427245864 = {u'for': u'login_passwd', }
_static_427134872 = {u'type': u'hidden', u'name': u'query', u'value': u'query', }
_static_427337152 = {u'class': u'${component_namespace}-submit-box', }
_static_427191208 = {u'class': u'form-group field-wrapper', }
_static_427157992 = {u'id': u'login_fieldset', }
_static_427249392 = {u'alt': u'', u'href': u'', u'id': u'mfa-img', u'title': u'', }
_static_427421368 = {u'data-dismiss': u'modal', u'type': u'button', u'class': u'close', u'aria-hidden': u'true', }
_static_427307248 = {u'type': u'text', u'id': u'login_mfacode', u'name': u'mfacode', u'class': u'form-control', }
_static_427214048 = {u'value': u'last_username', u'type': u'text', u'id': u'login_user', u'name': u'username', u'class': u'form-control', }
_static_427215728 = {u'class': u'form-group field-wrapper password-wrapper', }
_static_427476472 = {u'data-dismiss': u'modal', u'class': u'btn btn-primary', u'aria-hidden': u'true', }
_static_427213320 = {u'for': u'login_user', }
_static_427277672 = {u'for': u'login_mfacode', }
_static_427275488 = {u'id': u'mfa-base32', }

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
            __backup_landing_page_426672760 = get('landing_page', __marker)

            # <Value u'load: landing_pages.html' (3:29)> -> __value
            __token = 87
            __value = u' landing_pages.html'
            __value = __loader(__value)
            econtext['landing_page'] = __value

            # <Static value=<_ast.Dict object at 0x00000000196E8518> name=None at 196e84e0> -> __attrs_426674104
            __attrs_426674104 = _static_426673432

            # <html ... (2:0)
            # --------------------------------------------------------
            __append(u'<html')

            # <Builtin id='False' ctx=<_ast.Load object at 0x000000001938DEB8> at 19691978> -> __default_426673824
            __default_426673824 = False

            # <Interpolation value=<Substitution u'${component_namespace}-html' (2:13)> braces_required=True translation=False at 196e8668> -> __attr_class
            __token = 29
            __token = 31
            __attr_class = getitem('component_namespace')
            __attr_class = __quote(__attr_class, '"', '&quot;', None, False)
            __attr_class = ('%s%s' % ((__attr_class if (__attr_class is not None) else ''), u'-html', ))
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
            __append(u'\n')

            # <Static value=<_ast.Dict object at 0x00000000196E8A58> name=None at 196e8a20> -> __attrs_426675224
            __attrs_426675224 = _static_426674776

            # <head ... (4:0)
            # --------------------------------------------------------
            __append(u'<head')
            __append(u' lang="en"')
            __append(u'>')
            __append(u'\n    ')
            __backup_macroname_426735752 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x00000000196E8DA0> name=None at 196e8dd8> -> __value
            __value = _static_426675616
            econtext['macroname'] = __value

            # <Value u'landing_page.header' (5:37)> -> __macro
            __token = 168
            __macro = _lookup_attr(getitem('landing_page'), 'header')
            __token = 168
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_426735752 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_426735752
            __append(u'\n\n    ')

            # <Static value=<_ast.Dict object at 0x00000000196E8F28> name=None at 196e8ef0> -> __attrs_426762592
            __attrs_426762592 = _static_426676008

            # <script ... (7:4)
            # --------------------------------------------------------
            __append(u'<script')
            __append(u' src="/static/jscript/elink_login.js"')
            __append(u'>')
            __append(u'</script>')
            __append(u'\n\n    ')

            # <Static value=<_ast.Dict object at 0x00000000196919B0> name=None at 19691b00> -> __attrs_426763544
            __attrs_426763544 = _static_426318256

            # <title ... (9:4)
            # --------------------------------------------------------
            __append(u'<title>')
            __default_426763208 = '__default'

            # <Value u"message('branding_login_title')" (9:24)> -> __cache_426762816
            __token = 292
            __cache_426762816 = getitem('message')('branding_login_title')

            # <Identity expression=<Value u"message('branding_login_title')" (9:24)> value=<_ast.Str object at 0x00000000196FE2B0> at 196fe2e8> -> __condition
            __expression = __cache_426762816
            __value = '__default'
            __condition = (__expression is __value)
            if __condition:
                __append(u'Title')
            else:
                __content = __cache_426762816
                __content = __quote(__content, None, '\xad', None, None)
                if (__content is not None):
                    __append(__content)
            __append(u'</title>')
            __append(u'\n\n')
            __append(u'</head>')
            __append(u'\n')

            # <Static value=<_ast.Dict object at 0x00000000196FE6A0> name=None at 196fe668> -> __attrs_426764608
            __attrs_426764608 = _static_426763936

            # <body ... (12:0)
            # --------------------------------------------------------
            __append(u'<body')

            # <Builtin id='False' ctx=<_ast.Load object at 0x000000001938DEB8> at 19691978> -> __default_426764328
            __default_426764328 = False

            # <Interpolation value=<Substitution u'${component_namespace}-body' (12:13)> braces_required=True translation=False at 196fe7f0> -> __attr_class
            __token = 361
            __token = 363
            __attr_class = getitem('component_namespace')
            __attr_class = __quote(__attr_class, '"', '&quot;', None, False)
            __attr_class = ('%s%s' % ((__attr_class if (__attr_class is not None) else ''), u'-body', ))
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
            __append(u'\n\n')

            # <Static value=<_ast.Dict object at 0x00000000196FEA90> name=None at 196fea58> -> __attrs_426765616
            __attrs_426765616 = _static_426764944

            # <div ... (14:0)
            # --------------------------------------------------------
            __append(u'<div')

            # <Builtin id='False' ctx=<_ast.Load object at 0x000000001938DEB8> at 19691978> -> __default_426765336
            __default_426765336 = False

            # <Interpolation value=<Substitution u'container ${component_namespace}-container' (14:12)> braces_required=True translation=False at 196febe0> -> __attr_class
            __token = 404
            __token = 416
            __attr_class = getitem('component_namespace')
            __attr_class = __quote(__attr_class, '"', '&quot;', None, False)
            __attr_class = ('%s%s%s' % (u'container ', (__attr_class if (__attr_class is not None) else ''), u'-container', ))
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
            __append(u'\n    ')

            # <Static value=<_ast.Dict object at 0x00000000196FEEB8> name=None at 196fee80> -> __attrs_427069848
            __attrs_427069848 = _static_426766008

            # <div ... (15:4)
            # --------------------------------------------------------
            __append(u'<div')

            # <Builtin id='False' ctx=<_ast.Load object at 0x000000001938DEB8> at 19691978> -> __default_427069568
            __default_427069568 = False

            # <Interpolation value=<Substitution u'${component_namespace}-loginbox' (15:16)> braces_required=True translation=False at 19749048> -> __attr_class
            __token = 465
            __token = 467
            __attr_class = getitem('component_namespace')
            __attr_class = __quote(__attr_class, '"', '&quot;', None, False)
            __attr_class = ('%s%s' % ((__attr_class if (__attr_class is not None) else ''), u'-loginbox', ))
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

            # <Static value=<_ast.Dict object at 0x00000000197492E8> name=None at 19749320> -> __attrs_427070912
            __attrs_427070912 = _static_427070184

            # <img ... (16:8)
            # --------------------------------------------------------
            __append(u'<img')
            __append(u' class="ce-logo"')
            __append(u' src="/static/imgid/branding_web_portal_logo.svg"')
            __append(u'>')
            __append(u'\n        ')
            __backup_macroname_427054984 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x00000000197496D8> name=None at 19749710> -> __value
            __value = _static_427071192
            econtext['macroname'] = __value

            # <Value u'landing_page.language_select' (17:41)> -> __macro
            __token = 619
            __macro = _lookup_attr(getitem('landing_page'), 'language_select')
            __token = 619
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_427054984 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_427054984
            __append(u'\n        ')

            # <Value u'not is_logged_in' (18:34)> -> __condition
            __token = 701
            __condition = not getitem('is_logged_in')
            if __condition:
                __append(u'\n            ')

                # <Value u'show_sso_failure' (19:32)> -> __condition
                __token = 752
                __condition = getitem('show_sso_failure')
                if __condition:

                    # <Static value=<_ast.Dict object at 0x0000000019749A58> name=None at 19749a90> -> __attrs_427073096
                    __attrs_427073096 = _static_427072088

                    # <div ... (19:12)
                    # --------------------------------------------------------
                    __append(u'<div')

                    # <Builtin id='False' ctx=<_ast.Load object at 0x000000001938DEB8> at 19691978> -> __default_427072592
                    __default_427072592 = False

                    # <Substitution u'message_id' (19:69)> -> __attr_id
                    __token = 789
                    __attr_id = getitem('message_id')
                    __attr_id = __quote(__attr_id, '"', '&quot;', None, False)
                    if (__attr_id is not None):
                        __append((u' id="%s"' % __attr_id))

                    # <Builtin id='False' ctx=<_ast.Load object at 0x000000001938DEB8> at 19691978> -> __default_427072816
                    __default_427072816 = False

                    # <Substitution u"python: 'sso-message alert %s' % msg_type" (19:86)> -> __attr_class
                    __token = 806
                    __attr_class = ('sso-message alert %s' % getitem('msg_type'))
                    __attr_class = __quote(__attr_class, '"', '&quot;', None, False)
                    if (__attr_class is not None):
                        __append((u' class="%s"' % __attr_class))
                    __append(u'>')
                    __append(u'\n                ')

                    # <Value u"current_lang == 'de'" (20:36)> -> __condition
                    __token = 887
                    __condition = (getitem('current_lang') == 'de')
                    if __condition:

                        # <Static value=<_ast.Dict object at 0x00000000196919B0> name=None at 19691b00> -> __attrs_427102616
                        __attrs_427102616 = _static_426318256

                        # <div ... (20:16)
                        # --------------------------------------------------------
                        __append(u'<div>')
                        __append(u'\n                    ')

                        # <Static value=<_ast.Dict object at 0x00000000196919B0> name=None at 19691b00> -> __attrs_427103400
                        __attrs_427103400 = _static_426318256

                        # <p ... (21:20)
                        # --------------------------------------------------------
                        __append(u'<p>')
                        __append(u'Das Starten der Sitzung mit Single Sign-On (SSO) ist fehlgeschlagen.')
                        __append(u'</p>')
                        __append(u'\n                    ')

                        # <Static value=<_ast.Dict object at 0x00000000196919B0> name=None at 19691b00> -> __attrs_427103904
                        __attrs_427103904 = _static_426318256

                        # <p ... (22:20)
                        # --------------------------------------------------------
                        __append(u'<p>')
                        __append(u'Pr\xfcfen Sie bitte folgende Ursachen:')
                        __append(u'</p>')
                        __append(u'\n                    ')

                        # <Static value=<_ast.Dict object at 0x00000000196919B0> name=None at 19691b00> -> __attrs_427104408
                        __attrs_427104408 = _static_426318256

                        # <ul ... (23:20)
                        # --------------------------------------------------------
                        __append(u'<ul>')
                        __append(u'\n                        ')

                        # <Static value=<_ast.Dict object at 0x00000000196919B0> name=None at 19691b00> -> __attrs_427105024
                        __attrs_427105024 = _static_426318256

                        # <li ... (24:24)
                        # --------------------------------------------------------
                        __append(u'<li>')
                        __append(u'Falls Ihre Windows-Sitzung lange aktiv war, sperren\n                            Sie Ihre Windows-Sitzung und entsperren Sie sie\n                            danach. Dadurch werden die Anmeldedaten Ihrer\n                            Sitzung aktualisiert\n                        ')
                        __append(u'</li>')
                        __append(u'\n                        ')

                        # <Static value=<_ast.Dict object at 0x00000000196919B0> name=None at 19691b00> -> __attrs_427105584
                        __attrs_427105584 = _static_426318256

                        # <li ... (29:24)
                        # --------------------------------------------------------
                        __append(u'<li>')
                        __append(u'Stellen Sie sicher, dass die Uhrzeit Ihres Computers\n                            korrekt eingestellt ist. Eine Abweichung von 5 Minuten\n                            f\xfchrt bereits zu Fehlern.\n                        ')
                        __append(u'</li>')
                        __append(u'\n                    ')
                        __append(u'</ul>')
                        __append(u'\n                ')
                        __append(u'</div>')
                    __append(u'\n                ')

                    # <Value u"current_lang != 'de'" (35:36)> -> __condition
                    __token = 1736
                    __condition = (getitem('current_lang') != 'de')
                    if __condition:

                        # <Static value=<_ast.Dict object at 0x00000000196919B0> name=None at 19691b00> -> __attrs_427106032
                        __attrs_427106032 = _static_426318256

                        # <div ... (35:16)
                        # --------------------------------------------------------
                        __append(u'<div>')
                        __append(u'\n                    ')

                        # <Static value=<_ast.Dict object at 0x00000000196919B0> name=None at 19691b00> -> __attrs_427131344
                        __attrs_427131344 = _static_426318256

                        # <p ... (36:20)
                        # --------------------------------------------------------
                        __append(u'<p>')
                        __append(u'Establishing your session using Single Sign-On (SSO) failed.')
                        __append(u'</p>')
                        __append(u'\n                    ')

                        # <Static value=<_ast.Dict object at 0x00000000196919B0> name=None at 19691b00> -> __attrs_427131848
                        __attrs_427131848 = _static_426318256

                        # <p ... (37:20)
                        # --------------------------------------------------------
                        __append(u'<p>')
                        __append(u'Please check these possible causes:')
                        __append(u'</p>')
                        __append(u'\n                    ')

                        # <Static value=<_ast.Dict object at 0x00000000196919B0> name=None at 19691b00> -> __attrs_427132352
                        __attrs_427132352 = _static_426318256

                        # <ul ... (38:20)
                        # --------------------------------------------------------
                        __append(u'<ul>')
                        __append(u'\n                        ')

                        # <Static value=<_ast.Dict object at 0x00000000196919B0> name=None at 19691b00> -> __attrs_427132912
                        __attrs_427132912 = _static_426318256

                        # <li ... (39:24)
                        # --------------------------------------------------------
                        __append(u'<li>')
                        __append(u'If your Windows session has been active for a while,\n                            try locking and unlocking your Windows session.\n                            This should refresh the credentials for your session.\n                        ')
                        __append(u'</li>')
                        __append(u'\n                        ')

                        # <Static value=<_ast.Dict object at 0x00000000196919B0> name=None at 19691b00> -> __attrs_427133472
                        __attrs_427133472 = _static_426318256

                        # <li ... (43:24)
                        # --------------------------------------------------------
                        __append(u'<li>')
                        __append(u'Check if your system time is accurate. A difference\n                            of 5 minutes can already cause failures.\n                        ')
                        __append(u'</li>')
                        __append(u'\n                    ')
                        __append(u'</ul>')
                        __append(u'\n                ')
                        __append(u'</div>')
                    __append(u'\n            ')
                    __append(u'</div>')
                __append(u'\n            ')

                # <Static value=<_ast.Dict object at 0x0000000019758630> name=None at 19758b00> -> __attrs_427134536
                __attrs_427134536 = _static_427132464

                # <form ... (49:12)
                # --------------------------------------------------------
                __append(u'<form')
                __append(u' method="POST"')

                # <Builtin id='False' ctx=<_ast.Load object at 0x000000001938DEB8> at 19691978> -> __default_427134256
                __default_427134256 = False

                # <Substitution u'post_action' (49:55)> -> __attr_action
                __token = 2506
                __attr_action = getitem('post_action')
                __attr_action = __quote(__attr_action, '"', '&quot;', None, False)
                if (__attr_action is not None):
                    __append((u' action="%s"' % __attr_action))
                __append(u'>')
                __append(u'\n                ')

                # <Static value=<_ast.Dict object at 0x0000000019758F98> name=None at 19758fd0> -> __attrs_427156480
                __attrs_427156480 = _static_427134872

                # <input ... (50:16)
                # --------------------------------------------------------
                __append(u'<input')
                __append(u' type="hidden"')
                __append(u' name="query"')

                # <Builtin id='False' ctx=<_ast.Load object at 0x000000001938DEB8> at 19691978> -> __default_427156256
                __default_427156256 = False

                # <Substitution u'query' (50:72)> -> __attr_value
                __token = 2592
                __attr_value = getitem('query')
                __attr_value = __quote(__attr_value, '"', '&quot;', None, False)
                if (__attr_value is not None):
                    __append((u' value="%s"' % __attr_value))
                __append(u' />')
                __append(u'\n                ')

                # <Static value=<_ast.Dict object at 0x000000001975E518> name=None at 1975e588> -> __attrs_427157768
                __attrs_427157768 = _static_427156760

                # <input ... (51:16)
                # --------------------------------------------------------
                __append(u'<input')
                __append(u' type="hidden"')
                __append(u' name="acr_values"')

                # <Builtin id='False' ctx=<_ast.Load object at 0x000000001938DEB8> at 19691978> -> __default_427157544
                __default_427157544 = False

                # <Substitution u'acr_values' (51:77)> -> __attr_value
                __token = 2679
                __attr_value = getitem('acr_values')
                __attr_value = __quote(__attr_value, '"', '&quot;', None, False)
                if (__attr_value is not None):
                    __append((u' value="%s"' % __attr_value))
                __append(u' />')
                __append(u'\n            ')

                # <Static value=<_ast.Dict object at 0x000000001975E9E8> name=None at 1975e9b0> -> __attrs_427158496
                __attrs_427158496 = _static_427157992

                # <fieldset ... (52:12)
                # --------------------------------------------------------
                __append(u'<fieldset')
                __append(u' id="login_fieldset"')
                __append(u'>')
                __append(u'\n                ')

                # <Value u'msg' (53:36)> -> __condition
                __token = 2773
                __condition = getitem('msg')
                if __condition:

                    # <Static value=<_ast.Dict object at 0x000000001975ED30> name=None at 1975ed68> -> __attrs_427188576
                    __attrs_427188576 = _static_427158832

                    # <div ... (53:16)
                    # --------------------------------------------------------
                    __append(u'<div')

                    # <Builtin id='False' ctx=<_ast.Load object at 0x000000001938DEB8> at 19691978> -> __default_427159336
                    __default_427159336 = False

                    # <Substitution u'message_id' (53:60)> -> __attr_id
                    __token = 2797
                    __attr_id = getitem('message_id')
                    __attr_id = __quote(__attr_id, '"', '&quot;', None, False)
                    if (__attr_id is not None):
                        __append((u' id="%s"' % __attr_id))

                    # <Builtin id='False' ctx=<_ast.Load object at 0x000000001938DEB8> at 19691978> -> __default_427188296
                    __default_427188296 = False

                    # <Substitution u"python: 'alert %s' % msg_type" (53:77)> -> __attr_class
                    __token = 2814
                    __attr_class = ('alert %s' % getitem('msg_type'))
                    __attr_class = __quote(__attr_class, '"', '&quot;', None, False)
                    if (__attr_class is not None):
                        __append((u' class="%s"' % __attr_class))
                    __append(u'>')
                    __append(u'\n                    ')

                    # <Value u'msg_title' (54:39)> -> __condition
                    __token = 2886
                    __condition = getitem('msg_title')
                    if __condition:

                        # <Static value=<_ast.Dict object at 0x00000000196919B0> name=None at 19691b00> -> __attrs_427189752
                        __attrs_427189752 = _static_426318256

                        # <h4 ... (54:20)
                        # --------------------------------------------------------
                        __append(u'<h4>')
                        __default_427189416 = '__default'

                        # <Value u'msg_title' (54:63)> -> __cache_427189024
                        __token = 2910
                        __cache_427189024 = getitem('msg_title')

                        # <Identity expression=<Value u'msg_title' (54:63)> value=<_ast.Str object at 0x0000000019766390> at 197663c8> -> __condition
                        __expression = __cache_427189024
                        __value = '__default'
                        __condition = (__expression is __value)
                        if __condition:
                            __append(u'Title')
                        else:
                            __content = __cache_427189024
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append(u'</h4>')
                    __append(u'\n                    ')

                    # <Static value=<_ast.Dict object at 0x00000000196919B0> name=None at 19691b00> -> __attrs_427190872
                    __attrs_427190872 = _static_426318256

                    # <span ... (55:20)
                    # --------------------------------------------------------
                    __append(u'<span>')
                    __default_427190536 = '__default'

                    # <Value u'msg' (55:39)> -> __cache_427190088
                    __token = 2971
                    __cache_427190088 = getitem('msg')

                    # <Identity expression=<Value u'msg' (55:39)> value=<_ast.Str object at 0x00000000197667F0> at 19766828> -> __condition
                    __expression = __cache_427190088
                    __value = '__default'
                    __condition = (__expression is __value)
                    if __condition:
                        __append(u'Message')
                    else:
                        __content = __cache_427190088
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append(u'</span>')
                    __append(u'\n                ')
                    __append(u'</div>')
                __append(u'\n                ')

                # <Static value=<_ast.Dict object at 0x0000000019766BA8> name=None at 19766b70> -> __attrs_427191712
                __attrs_427191712 = _static_427191208

                # <div ... (57:16)
                # --------------------------------------------------------
                __append(u'<div')
                __append(u' class="form-group field-wrapper"')
                __append(u'>')
                __append(u'\n                    ')

                # <Static value=<_ast.Dict object at 0x000000001976C208> name=None at 1976c1d0> -> __attrs_427213768
                __attrs_427213768 = _static_427213320

                # <label ... (58:20)
                # --------------------------------------------------------
                __append(u'<label')
                __append(u' for="login_user"')
                __append(u'>')
                __default_427213096 = '__default'

                # <Value u"message('login_user_label')" (58:57)> -> __cache_427192104
                __token = 3126
                __cache_427192104 = getitem('message')('login_user_label')

                # <Identity expression=<Value u"message('login_user_label')" (58:57)> value=<_ast.Str object at 0x0000000019766FD0> at 1976c048> -> __condition
                __expression = __cache_427192104
                __value = '__default'
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_427192104
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append(u'</label>')
                __append(u'\n                    ')

                # <Static value=<_ast.Dict object at 0x000000001976C4E0> name=None at 1976c470> -> __attrs_427215504
                __attrs_427215504 = _static_427214048

                # <input ... (59:20)
                # --------------------------------------------------------
                __append(u'<input')
                __append(u' type="text"')
                __append(u' id="login_user"')
                __append(u' class="form-control"')
                __append(u' name="username"')

                # <Builtin id='False' ctx=<_ast.Load object at 0x000000001938DEB8> at 19691978> -> __default_427215280
                __default_427215280 = False

                # <Substitution u'last_username' (59:114)> -> __attr_value
                __token = 3278
                __attr_value = getitem('last_username')
                __attr_value = __quote(__attr_value, '"', '&quot;', None, False)
                if (__attr_value is not None):
                    __append((u' value="%s"' % __attr_value))
                __append(u'>')
                __append(u'\n                ')
                __append(u'</div>')
                __append(u'\n\n                ')

                # <Static value=<_ast.Dict object at 0x000000001976CB70> name=None at 1976c4a8> -> __attrs_427216232
                __attrs_427216232 = _static_427215728

                # <div ... (62:16)
                # --------------------------------------------------------
                __append(u'<div')
                __append(u' class="form-group field-wrapper password-wrapper"')
                __append(u'>')
                __append(u'\n                    ')

                # <Static value=<_ast.Dict object at 0x0000000019774128> name=None at 197740f0> -> __attrs_427246368
                __attrs_427246368 = _static_427245864

                # <label ... (63:20)
                # --------------------------------------------------------
                __append(u'<label')
                __append(u' for="login_passwd"')
                __append(u'>')
                __default_427245696 = '__default'

                # <Value u"message('login_password_label')" (63:59)> -> __cache_427216568
                __token = 3449
                __cache_427216568 = getitem('message')('login_password_label')

                # <Identity expression=<Value u"message('login_password_label')" (63:59)> value=<_ast.Str object at 0x000000001976CF28> at 1976cf60> -> __condition
                __expression = __cache_427216568
                __value = '__default'
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_427216568
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append(u'</label>')
                __append(u'\n                    ')

                # <Static value=<_ast.Dict object at 0x0000000019774438> name=None at 197744a8> -> __attrs_427247768
                __attrs_427247768 = _static_427246648

                # <input ... (64:20)
                # --------------------------------------------------------
                __append(u'<input')
                __append(u' type="password"')
                __append(u' id="login_passwd"')
                __append(u' class="form-control"')
                __append(u' name="password"')
                __append(u'>')
                __append(u'\n                ')
                __append(u'</div>')
                __append(u'\n                ')

                # <Value u'show_mfa_fields' (66:42)> -> __condition
                __token = 3655
                __condition = getitem('show_mfa_fields')
                if __condition:
                    __append(u'\n                ')

                    # <Static value=<_ast.Dict object at 0x0000000019774B70> name=None at 19774b38> -> __attrs_427249000
                    __attrs_427249000 = _static_427248496

                    # <div ... (67:16)
                    # --------------------------------------------------------
                    __append(u'<div')
                    __append(u' class="mfa-extra-wrapper hide"')
                    __append(u'>')
                    __append(u'\n                    ')

                    # <Static value=<_ast.Dict object at 0x0000000019774EF0> name=None at 19774eb8> -> __attrs_427275152
                    __attrs_427275152 = _static_427249392

                    # <img ... (68:20)
                    # --------------------------------------------------------
                    __append(u'<img')
                    __append(u' id="mfa-img"')
                    __append(u' href=""')
                    __append(u' alt=""')
                    __append(u' title=""')
                    __append(u' />')
                    __append(u'\n                    ')

                    # <Static value=<_ast.Dict object at 0x000000001977B4E0> name=None at 1977b4a8> -> __attrs_427275936
                    __attrs_427275936 = _static_427275488

                    # <p ... (69:20)
                    # --------------------------------------------------------
                    __append(u'<p')
                    __append(u' id="mfa-base32"')
                    __append(u'>')
                    __append(u'</p>')
                    __append(u'\n                ')
                    __append(u'</div>')
                    __append(u'\n                ')

                    # <Static value=<_ast.Dict object at 0x000000001977B780> name=None at 1977b470> -> __attrs_427276664
                    __attrs_427276664 = _static_427276160

                    # <div ... (71:16)
                    # --------------------------------------------------------
                    __append(u'<div')
                    __append(u' class="form-group field-wrapper password-wrapper"')
                    __append(u'>')
                    __append(u'\n                    ')

                    # <Static value=<_ast.Dict object at 0x000000001977BD68> name=None at 1977bd30> -> __attrs_427278176
                    __attrs_427278176 = _static_427277672

                    # <label ... (72:20)
                    # --------------------------------------------------------
                    __append(u'<label')
                    __append(u' for="login_mfacode"')
                    __append(u'>')
                    __default_427277504 = '__default'

                    # <Value u'message(login_mfa_label)' (72:60)> -> __cache_427277056
                    __token = 3990
                    __cache_427277056 = getitem('message')(getitem('login_mfa_label'))

                    # <Identity expression=<Value u'message(login_mfa_label)' (72:60)> value=<_ast.Str object at 0x000000001977BBA8> at 1977bbe0> -> __condition
                    __expression = __cache_427277056
                    __value = '__default'
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_427277056
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append(u'</label>')
                    __append(u'\n                    ')

                    # <Static value=<_ast.Dict object at 0x00000000197830F0> name=None at 19783128> -> __attrs_427308312
                    __attrs_427308312 = _static_427307248

                    # <input ... (73:20)
                    # --------------------------------------------------------
                    __append(u'<input')
                    __append(u' type="text"')
                    __append(u' id="login_mfacode"')
                    __append(u' class="form-control"')
                    __append(u' name="mfacode"')
                    __append(u'>')
                    __append(u'\n                ')
                    __append(u'</div>')
                    __append(u'\n                ')
                __append(u'\n\n                ')

                # <Static value=<_ast.Dict object at 0x000000001977B9E8> name=None at 19774a20> -> __attrs_427308816
                __attrs_427308816 = _static_427276776

                # <div ... (77:16)
                # --------------------------------------------------------
                __append(u'<div')
                __append(u' class="checkbox"')
                __append(u'>')
                __append(u'\n                    ')

                # <Static value=<_ast.Dict object at 0x0000000019783898> name=None at 19783860> -> __attrs_427310664
                __attrs_427310664 = _static_427309208

                # <input ... (78:20)
                # --------------------------------------------------------
                __append(u'<input')
                __append(u' type="checkbox"')
                __append(u' id="remember"')
                __append(u' name="remember"')
                __append(u' value="remember"')

                # <Builtin id='False' ctx=<_ast.Load object at 0x000000001938DEB8> at 19691978> -> __default_427310440
                __default_427310440 = False

                # <Substitution u'remember_me' (78:114)> -> __attr_checked
                __token = 4326
                __attr_checked = getitem('remember_me')
                __attr_checked = __quote(__attr_checked, '"', '&quot;', None, False)
                if (__attr_checked is not None):
                    __append((u' checked="%s"' % __attr_checked))
                __append(u'>')
                __append(u'\n                    ')

                # <Static value=<_ast.Dict object at 0x000000001978A240> name=None at 1978a208> -> __attrs_427336928
                __attrs_427336928 = _static_427336256

                # <label ... (79:20)
                # --------------------------------------------------------
                __append(u'<label')
                __append(u' for="remember"')
                __append(u' onclick=""')
                __append(u'>')
                __default_427336032 = '__default'

                # <Value u"message('login_remember')" (79:66)> -> __cache_427310832
                __token = 4406
                __cache_427310832 = getitem('message')('login_remember')

                # <Identity expression=<Value u"message('login_remember')" (79:66)> value=<_ast.Str object at 0x000000001978A048> at 1978a080> -> __condition
                __expression = __cache_427310832
                __value = '__default'
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_427310832
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append(u'</label>')
                __append(u'\n                ')
                __append(u'</div>')
                __append(u'\n\n                ')

                # <Static value=<_ast.Dict object at 0x000000001978A5C0> name=None at 19783780> -> __attrs_427337824
                __attrs_427337824 = _static_427337152

                # <div ... (82:16)
                # --------------------------------------------------------
                __append(u'<div')

                # <Builtin id='False' ctx=<_ast.Load object at 0x000000001938DEB8> at 19691978> -> __default_427337544
                __default_427337544 = False

                # <Interpolation value=<Substitution u'${component_namespace}-submit-box' (82:28)> braces_required=True translation=False at 1978a710> -> __attr_class
                __token = 4494
                __token = 4496
                __attr_class = getitem('component_namespace')
                __attr_class = __quote(__attr_class, '"', '&quot;', None, False)
                __attr_class = ('%s%s' % ((__attr_class if (__attr_class is not None) else ''), u'-submit-box', ))
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

                # <Static value=<_ast.Dict object at 0x000000001978A9E8> name=None at 1978a9b0> -> __attrs_427338720
                __attrs_427338720 = _static_427338216

                # <div ... (83:20)
                # --------------------------------------------------------
                __append(u'<div')
                __append(u' class="throbber-wrap"')
                __append(u'>')
                __append(u'\n                        ')

                # <Static value=<_ast.Dict object at 0x000000001978ADA0> name=None at 1978acf8> -> __attrs_427364480
                __attrs_427364480 = _static_427339168

                # <img ... (84:24)
                # --------------------------------------------------------
                __append(u'<img')
                __append(u' class="throbber"')
                __append(u' src="/static/images/throbber.svg"')
                __append(u'>')
                __append(u'\n                    ')
                __append(u'</div>')
                __append(u'\n                    ')

                # <Static value=<_ast.Dict object at 0x0000000019791160> name=None at 19791198> -> __attrs_427366160
                __attrs_427366160 = _static_427364704

                # <input ... (86:20)
                # --------------------------------------------------------
                __append(u'<input')
                __append(u' type="submit"')
                __append(u' id="login"')

                # <Builtin id='False' ctx=<_ast.Load object at 0x000000001938DEB8> at 19691978> -> __default_427365712
                __default_427365712 = False

                # <Interpolation value=<Substitution u'btn cs-web-components-base-semantic-button-primary ${component_namespace}-submit' (86:59)> braces_required=True translation=False at 19791518> -> __attr_class
                __token = 4745
                __token = 4798
                __attr_class = getitem('component_namespace')
                __attr_class = __quote(__attr_class, '"', '&quot;', None, False)
                __attr_class = ('%s%s%s' % (u'btn cs-web-components-base-semantic-button-primary ', (__attr_class if (__attr_class is not None) else ''), u'-submit', ))
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

                # <Builtin id='False' ctx=<_ast.Load object at 0x000000001938DEB8> at 19691978> -> __default_427365936
                __default_427365936 = False

                # <Substitution u"message('login_button')" (86:163)> -> __attr_value
                __token = 4849
                __attr_value = getitem('message')('login_button')
                __attr_value = __quote(__attr_value, '"', '&quot;', None, False)
                if (__attr_value is not None):
                    __append((u' value="%s"' % __attr_value))
                __append(u'>')
                __append(u'\n                    ')

                # <Value u'sso_enabled' (87:46)> -> __condition
                __token = 4921
                __condition = getitem('sso_enabled')
                if __condition:
                    __append(u'\n                        ')

                    # <Static value=<_ast.Dict object at 0x0000000019791A20> name=None at 197919b0> -> __attrs_427367448
                    __attrs_427367448 = _static_427366944

                    # <div ... (88:24)
                    # --------------------------------------------------------
                    __append(u'<div')
                    __append(u' class="sso-divider"')
                    __append(u'>')
                    __append(u'\n                            ')

                    # <Static value=<_ast.Dict object at 0x0000000019791DD8> name=None at 19791da0> -> __attrs_427368288
                    __attrs_427368288 = _static_427367896

                    # <hr ... (89:28)
                    # --------------------------------------------------------
                    __append(u'<hr')
                    __append(u' class="left"')
                    __append(u'>')
                    __append(u'\n                            ')

                    # <Static value=<_ast.Dict object at 0x00000000197970F0> name=None at 197970b8> -> __attrs_427389560
                    __attrs_427389560 = _static_427389168

                    # <hr ... (90:28)
                    # --------------------------------------------------------
                    __append(u'<hr')
                    __append(u' class="right"')
                    __append(u'>')
                    __append(u'\n                            ')

                    # <Static value=<_ast.Dict object at 0x00000000196919B0> name=None at 19691b00> -> __attrs_427390512
                    __attrs_427390512 = _static_426318256

                    # <span ... (91:28)
                    # --------------------------------------------------------
                    __append(u'<span>')
                    __default_427390176 = '__default'

                    # <Value u"message('login_sso_divider')" (91:47)> -> __cache_427389784
                    __token = 5125
                    __cache_427389784 = getitem('message')('login_sso_divider')

                    # <Identity expression=<Value u"message('login_sso_divider')" (91:47)> value=<_ast.Str object at 0x00000000197973C8> at 19797400> -> __condition
                    __expression = __cache_427389784
                    __value = '__default'
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_427389784
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append(u'</span>')
                    __append(u'\n                        ')
                    __append(u'</div>')
                    __append(u'\n                        ')

                    # <Static value=<_ast.Dict object at 0x00000000197977F0> name=None at 19797748> -> __attrs_427392080
                    __attrs_427392080 = _static_427390960

                    # <input ... (93:24)
                    # --------------------------------------------------------
                    __append(u'<input')
                    __append(u' type="button"')
                    __append(u' class="btn cs-web-components-base-semantic-button-primary login-sso"')

                    # <Builtin id='False' ctx=<_ast.Load object at 0x000000001938DEB8> at 19691978> -> __default_427391856
                    __default_427391856 = False

                    # <Substitution u"message('login_sso_button')" (93:136)> -> __attr_value
                    __token = 5330
                    __attr_value = getitem('message')('login_sso_button')
                    __attr_value = __quote(__attr_value, '"', '&quot;', None, False)
                    if (__attr_value is not None):
                        __append((u' value="%s"' % __attr_value))
                    __append(u'>')
                    __append(u'\n                    ')
                __append(u'\n                ')
                __append(u'</div>')
                __append(u'\n            ')
                __append(u'</fieldset>')
                __append(u'\n            ')
                __backup_macroname_427163976 = get('macroname', __marker)

                # <Static value=<_ast.Str object at 0x00000000197917B8> name=None at 197917f0> -> __value
                __value = _static_427366328
                econtext['macroname'] = __value

                # <Value u'landing_page.portalbox' (97:45)> -> __macro
                __token = 5485
                __macro = _lookup_attr(getitem('landing_page'), 'portalbox')
                __token = 5485
                __m = __macro.include
                __m(__stream, econtext.copy(), rcontext, __i18n_domain)
                econtext.update(rcontext)
                if (__backup_macroname_427163976 is __marker):
                    del econtext['macroname']
                else:
                    econtext['macroname'] = __backup_macroname_427163976
                __append(u'\n            ')
                __append(u'</form>')
                __append(u'\n        ')
            __append(u'\n        ')

            # <Value u'is_logged_in' (100:34)> -> __condition
            __token = 5602
            __condition = getitem('is_logged_in')
            if __condition:
                __append(u'\n            ')

                # <Static value=<_ast.Dict object at 0x0000000019797E80> name=None at 19797eb8> -> __attrs_427418064
                __attrs_427418064 = _static_427392640

                # <p ... (101:12)
                # --------------------------------------------------------
                __append(u'<p')
                __append(u' id="login_message"')
                __append(u' class="logged-in"')
                __append(u'>')

                # <Interpolation value=<Substitution u"${message('login_welcome')}" (101:52)> braces_required=True translation=False at 1979e2b0> -> __content_98550888
                __token = 5669
                __token = 5671
                __content_98550888 = getitem('message')('login_welcome')
                __content_98550888 = __quote(__content_98550888, '\x00', '&#0;', None, False)
                __content_98550888 = __content_98550888
                if (__content_98550888 is None):
                    pass
                else:
                    if (__content_98550888 is False):
                        __content_98550888 = None
                    else:
                        __tt = type(__content_98550888)
                        if ((__tt is int) or (__tt is float) or (__tt is long)):
                            __content_98550888 = unicode(__content_98550888)
                        else:
                            if (__tt is str):
                                __content_98550888 = decode(__content_98550888)
                            else:
                                if (__tt is not unicode):
                                    try:
                                        __content_98550888 = __content_98550888.__html__
                                    except get('AttributeError', AttributeError):
                                        __converted = convert(__content_98550888)
                                        __content_98550888 = (unicode(__content_98550888) if (__content_98550888 is __converted) else __converted)
                                    else:
                                        __content_98550888 = __content_98550888()
                if (__content_98550888 is not None):
                    __append(__content_98550888)
                __append(u'</p>')
                __append(u'\n        ')
            __append(u'\n    ')
            __append(u'</div>')
            __append(u'\n')
            __append(u'</div>')
            __append(u'\n\n')
            __append(u'<!-- Modal -->')
            __append(u'\n')

            # <Static value=<_ast.Dict object at 0x000000001979E358> name=None at 1979e2e8> -> __attrs_427420192
            __attrs_427420192 = _static_427418456

            # <div ... (107:0)
            # --------------------------------------------------------
            __append(u'<div')
            __append(u' id="msgs-modal"')

            # <Builtin id='False' ctx=<_ast.Load object at 0x000000001938DEB8> at 19691978> -> __default_427419464
            __default_427419464 = False

            # <Interpolation value=<Substitution u'modal hide fade ${component_namespace}-modal' (107:28)> braces_required=True translation=False at 1979e710> -> __attr_class
            __token = 5784
            __token = 5802
            __attr_class = getitem('component_namespace')
            __attr_class = __quote(__attr_class, '"', '&quot;', None, False)
            __attr_class = ('%s%s%s' % (u'modal hide fade ', (__attr_class if (__attr_class is not None) else ''), u'-modal', ))
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
            __append(u' tabindex="-1"')
            __append(u' role="dialog"')
            __append(u' aria-labelledby="msgs-modal-label"')
            __append(u' aria-hidden="true"')
            __append(u'>')
            __append(u'\n  ')

            # <Static value=<_ast.Dict object at 0x000000001979EB70> name=None at 1979eb38> -> __attrs_427421032
            __attrs_427421032 = _static_427420528

            # <div ... (108:2)
            # --------------------------------------------------------
            __append(u'<div')
            __append(u' class="modal-header"')
            __append(u'>')
            __append(u'\n    ')

            # <Static value=<_ast.Dict object at 0x000000001979EEB8> name=None at 1979ee80> -> __attrs_427451280
            __attrs_427451280 = _static_427421368

            # <button ... (109:4)
            # --------------------------------------------------------
            __append(u'<button')
            __append(u' type="button"')
            __append(u' class="close"')
            __append(u' data-dismiss="modal"')
            __append(u' aria-hidden="true"')
            __append(u'>')
            __append(u'\xd7')
            __append(u'</button>')
            __append(u'\n    ')

            # <Static value=<_ast.Dict object at 0x00000000197A64E0> name=None at 197a64a8> -> __attrs_427452120
            __attrs_427452120 = _static_427451616

            # <h3 ... (110:4)
            # --------------------------------------------------------
            __append(u'<h3')
            __append(u' id="msgs-modal-label"')
            __append(u'>')

            # <Static value=<_ast.Dict object at 0x00000000197A67F0> name=None at 197a67b8> -> __attrs_427452904
            __attrs_427452904 = _static_427452400

            # <i ... (110:30)
            # --------------------------------------------------------
            __append(u'<i')
            __append(u' class="icon-info-sign"')
            __append(u'>')
            __append(u'</i>')
            __append(u' ')
            __default_427453632 = '__default'

            # <Value u"message('login_info_title')" (110:85)> -> __cache_427453184
            __token = 6118
            __cache_427453184 = getitem('message')('login_info_title')

            # <Identity expression=<Value u"message('login_info_title')" (110:85)> value=<_ast.Str object at 0x00000000197A6BA8> at 197a6be0> -> __condition
            __expression = __cache_427453184
            __value = '__default'
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_427453184
                __content = __quote(__content, None, '\xad', None, None)
                if (__content is not None):
                    __append(__content)
            __append(u'</h3>')
            __append(u'\n  ')
            __append(u'</div>')
            __append(u'\n  ')

            # <Static value=<_ast.Dict object at 0x00000000197A6D30> name=None at 197a6d68> -> __attrs_427454360
            __attrs_427454360 = _static_427453744

            # <div ... (112:2)
            # --------------------------------------------------------
            __append(u'<div')
            __append(u' class="modal-body"')
            __append(u'>')
            __append(u'\n    ')

            # <Static value=<_ast.Dict object at 0x00000000196919B0> name=None at 19691b00> -> __attrs_427475408
            __attrs_427475408 = _static_426318256

            # <p ... (113:4)
            # --------------------------------------------------------
            __append(u'<p>')
            __append(u'</p>')
            __append(u'\n  ')
            __append(u'</div>')
            __append(u'\n  ')

            # <Static value=<_ast.Dict object at 0x00000000197AC2E8> name=None at 197ac2b0> -> __attrs_427476192
            __attrs_427476192 = _static_427475688

            # <div ... (115:2)
            # --------------------------------------------------------
            __append(u'<div')
            __append(u' class="modal-footer"')
            __append(u'>')
            __append(u'\n    ')

            # <Static value=<_ast.Dict object at 0x00000000197AC5F8> name=None at 197ac630> -> __attrs_427477480
            __attrs_427477480 = _static_427476472

            # <button ... (116:4)
            # --------------------------------------------------------
            __append(u'<button')
            __append(u' class="btn btn-primary"')
            __append(u' data-dismiss="modal"')
            __append(u' aria-hidden="true"')
            __append(u'>')
            __default_427478096 = '__default'

            # <Value u"message('login_info_button')" (116:100)> -> __cache_427477704
            __token = 6341
            __cache_427477704 = getitem('message')('login_info_button')

            # <Identity expression=<Value u"message('login_info_button')" (116:100)> value=<_ast.Str object at 0x00000000197ACB38> at 197acb70> -> __condition
            __expression = __cache_427477704
            __value = '__default'
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_427477704
                __content = __quote(__content, None, '\xad', None, None)
                if (__content is not None):
                    __append(__content)
            __append(u'</button>')
            __append(u'\n  ')
            __append(u'</div>')
            __append(u'\n')
            __append(u'</div>')
            __append(u'\n\n\n')
            __append(u'</body>')
            __append(u'\n')
            __append(u'</html>')
            if (__backup_landing_page_426672760 is __marker):
                del econtext['landing_page']
            else:
                econtext['landing_page'] = __backup_landing_page_426672760
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }